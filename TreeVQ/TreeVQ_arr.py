# TreeVQ class

# Implements a Tree vector quantiser
# Copyright (c) 2006 Ray Heasman
from Vector import Vector
import Numeric

class VQNode(object):
  """Implements a single node in the VW tree"""
  def __init__(self, L = None, R = None, Vect = None):
    self.L = L
    self.R = R
    self.TVal = Vect # The "Test Val" ie. Value tested against

    self.VList = []

  def saveInfo(self, V):
    """Keep account for later training"""
    if (self.L == None) and (self.R == None):
      self.VList.append(V)

  def sum(self, L):
    sum = L[0].copy()
    for i in xrange(1, len(L)):
      sum += L[i]

    return sum

  def aveN(self, L, N):
    """Average the first N elements of L"""
    print "N = %s, len(L) = %d" % (N, len(L))
    if N == 0:
      return self.TVal

    return self.sum(L[:N])/(N*1.0)

  def processInfo(self):
    """Process the list of test vectors we have accumulated"""
    NumVals = len(self.VList)
    if NumVals > 0:
      LLen = NumVals*1.0
      LLen1 = NumVals//2
      LLen2 = NumVals-LLen1

      TValL = self.aveN(self.VList, LLen1)
      TValR = self.aveN(self.VList[LLen1:], LLen2)
      self.TVal  = (TValL + TValR)/2.0
      self.TValL = TValL
      self.TValR = TValR
    else:
      self.TValL = self.TVal
      self.TValR = self.TVal

    self.VList = []

class TreeVQ(object):
  def __init__(self, Root):
    self.Root = Root
    self.Leaves = 1

  def distance(self, a, b):
    diff = (a - b)**2
    return Numeric.sqrt(Numeric.sum(Numeric.sum(Numeric.sum(diff))))

  def search(self, V, CurrNode = None):
    """Return the node containing the quantised version of V"""
    if CurrNode == None:
      return self.search(V, self.Root)

    if (CurrNode.L == None) and (CurrNode.R == None):
      return CurrNode

    if (CurrNode.L != None) and (CurrNode.R != None):
      LErr = self.distance(V, CurrNode.L.TVal)
      RErr = self.distance(V, CurrNode.R.TVal)

      if LErr < RErr:
        return self.search(V, CurrNode.L)
      else:
        return self.search(V, CurrNode.R)

  def quantise(self, V):
    """Return the quantised version of V"""
    return self.search(V, self.Root).TVal

  def quantiseAndTrack(self, V):
    """Quantise as normal, but store bookkeeping data so we can train the VQ"""
    Best = self.search(V, self.Root)
    Best.saveInfo(V)
    return Best.TVal

  def _getNodeList(self, NodeList, Curr):
    NodeList.append(Curr)
    if Curr.L != None:
      self._getNodeList(NodeList, Curr.L)
    if Curr.R != None:
      self._getNodeList(NodeList, Curr.R)

  def getNodeList(self):
    NList = []
    self._getNodeList(NList, self.Root)
    return NList

  def updateLeaves(self, CurrNode, AddLeaves):
    if (CurrNode.L == None) and (CurrNode.R == None):
      # This is a leaf
      CurrNode.processInfo()
      if AddLeaves:
        CurrNode.L = VQNode(None, None, CurrNode.TValL)
        CurrNode.R = VQNode(None, None, CurrNode.TValR)
        self.Leaves += 1
      return

    if CurrNode.L != None:
      self.updateLeaves(CurrNode.L, AddLeaves)

    if CurrNode.R != None:
      self.updateLeaves(CurrNode.R, AddLeaves)

  def train(self, trainVectCB, notifyCB, MaxEntries, ItemsPerPass):
    """Train the VQ until we have MaxEntries codebook entries

    This is not the most memory efficient way to do things, but it's
    probably okay for now.

    trainVectCB  : A function that will called and that must return one test vector
    MaxEntries   : The maximum number of leaves in the codebook
    ItemsPerPass : The number of test vectors used to train on before each doubling of the codebook.
    """
    while self.Leaves < MaxEntries:
      # Train current leaves
      for j in xrange(5):
        for i in xrange(ItemsPerPass):
          self.quantiseAndTrack(trainVectCB())
        # Save results
        self.updateLeaves(self.Root, False)
        notifyCB()

      for i in xrange(ItemsPerPass):
        self.quantiseAndTrack(trainVectCB())
      # Add some new leaves
      self.updateLeaves(self.Root, True)
      notifyCB()

    for j in xrange(5):
      for i in xrange(ItemsPerPass):
        self.quantiseAndTrack(trainVectCB())
      # Save results
      self.updateLeaves(self.Root, False)
      notifyCB()

