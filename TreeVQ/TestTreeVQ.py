# TestTreeVQ.py
import unittest
import TreeVQ
from Vector import Vector

class TestTreeVQ(unittest.TestCase):
  def testQuantise_oneElement(self):
    N1 = TreeVQ.VQNode(None, None, Vector([1,0,0,0]))
    t = TreeVQ.TreeVQ(N1)

    self.failUnlessEqual(t.quantise(Vector([0,0,0,0])), Vector([1,0,0,0]), "Quantiser did not return correct element")

  def testQuantise_threeElements(self):
    N3 = TreeVQ.VQNode(None, None, Vector([-1,0,0,0]))
    N2 = TreeVQ.VQNode(None, None, Vector([ 1,0,0,0]))
    N1 = TreeVQ.VQNode(N2  , N3  , Vector([ 0,0,0,0]))
    t = TreeVQ.TreeVQ(N1)

    self.failUnlessEqual(t.quantise(Vector([ 0.1,0,0,0])), Vector([ 1,0,0,0]), "Quantiser did not return correct element")
    self.failUnlessEqual(t.quantise(Vector([-0.1,0,0,0])), Vector([-1,0,0,0]), "Quantiser did not return correct element")

if __name__ == "__main__":
  unittest.main()
