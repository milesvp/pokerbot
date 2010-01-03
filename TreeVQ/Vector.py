class Vector(object):
  """A class to implement the Vector type to be used in VMUs"""
  def __init__(self, Vect):
    """Create the vector, initialised from the list 'Vect'"""
    if isinstance(Vect, list):
      if isinstance(Vect[0], (int, float, long, complex)):
        self.Value = Vect
        return

    res = []
    for i in Vect:
      if isinstance(i, (int, float, long, complex)):
        res.append(i)
      else:
        res.append(Vector(i))

      self.Value = res

  def __repr__(self):
    return "Vector(%s)" % repr(self.Value)

  def __add__(self, V2):
    res = []
    for i in xrange(0, len(self.Value)):
      res.append(self.Value[i]+V2.Value[i])
    return Vector(res)

  def __sub__(self, V2):
    res = []
    for i in xrange(0, len(self.Value)):
      res.append(self.Value[i]-V2.Value[i])
    return Vector(res)

  def __mul__(self, V2):
    """Dot product for vectors, magnitude multiply for scalars"""
    if isinstance(V2, Vector):
      res = 0
      for i in xrange(0, len(self.Value)):
        res += self.Value[i]*V2.Value[i]
      return res
    else:
      res = []
      for i in xrange(0, len(self.Value)):
        res.append(self.Value[i]*V2)
      return Vector(res)

  __rmul__ = __mul__

  def __div__(self, V2):

    res = []
    for i in xrange(0, len(self.Value)):
      res.append(self.Value[i]/float(V2))
    return Vector(res)

  def __magnitude(self):
    res = 0
    for i in xrange(0, len(self.Value)):
      res += self.Value[i]*self.Value[i]
    return pow(res, 0.5)

  mag = property(__magnitude)

  def __eq__(self, other):
    Equal = True
    for i in xrange(0, len(self.Value)):
      Equal = Equal and (self.Value[i] == other.Value[i])
    return Equal

  def __ne__(self, other):
    return not self.__eq__(other)

  def __nonzero__(self):
    Zero = True
    for i in xrange(0, len(self.Value)):
      Zero = Zero and (self.Value[i] == 0)

    return not Zero

  def __getitem__(self, index):
    return self.Value[index]

  def __setitem__(self, index, item):
    self.Value[index] = item
