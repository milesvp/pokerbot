# TreeVQ class

# Implements a Tree vector quantiser
class VQNode(object):
  """Implements a single node in the VW tree"""
  def __init__(self, L = None, R = None, Vect = None):
    self.L = L
    self.R = R
    self.Vect = Vect

class TreeVQ(object):
  def __init__(self):
    self.Root = VQNode()

  def quantise(self, V, CurrNode = None):
    """Return the quantised version of V"""
    if CurrNode == None:
      return self.quantise(V, self.Root)

    if (L == None) and (R == None):
      return CurrNode.Vect

    if (L != None) and (R != None):
      CErr = (V - ThisNode.Vect).mag
      LErr = (V - ThisNode.L.Vect).mag
      RErr = (V - ThisNode.R.Vect).mag

      if (CErr <= LErr) and (CErr <= RErr):
        return CurrNode.Vect

      if LErr < RErr:
        return self.quantise(V, ThisNode.L)
      else:
        return self.quantise(V, ThisNode.R)

