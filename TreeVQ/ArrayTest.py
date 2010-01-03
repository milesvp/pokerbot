# Used to figure out how arrays work so we can use them in TreeVQ

import Numeric, pygame

cardSurf = pygame.Surface((3, 2))
a1 = pygame.surfarray.array3d(cardSurf)
a2 = pygame.surfarray.array3d(cardSurf)

a1 = a1 + 1
a2 = a2 + [1,2,3]

a3 = (a2 - a1)**2
print "a1: \n%s" % a1
print "a2: \n%s" % a2
print "a3: \n%s" % a3
print "test: \n%s" % Numeric.sum(Numeric.sum(Numeric.sum(a3)))

