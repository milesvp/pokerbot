# DemoTreeVQ.py
import psyco
psyco.full()

import pygame, random, sys, time, Numeric
import pygame.surfarray as surfarray
import TreeVQ

from Vector import Vector

CardWidth  = 45
CardHeight = 62

def checkEvents():
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

def cutCard(CardsArr, card):
  cardSurf = pygame.Surface((CardWidth+1, CardHeight+1))
  cardArr = surfarray.array3d(cardSurf)

  suite = card // 13
  card = card % 13
  x = card * CardWidth + 1
  y = suite * CardHeight + 1
  cardArr[::] = CardsArr[x:x+CardWidth+1,y:y+CardHeight+1]
  return cardArr

def printCardV(CardVect, screen, (xpos, ypos)):
  CardSurf = pygame.Surface((CardWidth+1, CardHeight+1))
  CardArr = surfarray.array3d(CardSurf)
  for x in xrange(CardWidth+1):
    for y in xrange(CardHeight+1):
      (R,G,B) = CardVect[x][y]
      CardArr[x,y] = [R,G,B]

  surfarray.blit_array(CardSurf, CardArr)
  screen.blit(CardSurf, [xpos, ypos])
  pygame.display.flip()

def printVQNodes(VQ, screen):
  NL = VQ.getNodeList()
  # print NL
  x = 0
  y = 0
  cnt = 0
  for i in NL:
    xoff = cnt  % 26
    yoff = cnt  // 26
    cnt += 1
    printCardV(i.TVal, screen, (xoff*CardWidth, yoff*CardHeight))

if __name__ == "__main__":

  pygame.init()

  CardsSurf = pygame.image.load("allcards.bmp")
  CardSurf = pygame.Surface((CardWidth+1, CardHeight+1))
  CardsArr  = surfarray.array3d(CardsSurf)
  (w, h) = CardsSurf.get_size()
  size = (w*2, h*2)
  screen  = pygame.display.set_mode(size, 0, 32)
  arr = surfarray.array3d(screen)
  # screen.blit(CardsSurf, [0,0])
  Cards = []
  CardVs = []
  CardList = range(52)

  for i in range(52):
    c = cutCard(CardsArr, i)
    Cards.append(c)
    CardVs.append(Vector(c.astype(Numeric.Float32).tolist()))
    # printCardV(CardVs[-1], screen, (200,200))

  VQN = TreeVQ.VQNode(None, None, CardVs[0])
  VQ = TreeVQ.TreeVQ(VQN)

  Counter = 0

  def getRandomCard():
    global Counter
    choice = random.randint(0,51)
    Counter = (Counter + 1) % 52
    surfarray.blit_array(CardSurf, Cards[choice])
    screen.blit(CardSurf, (w*2-(CardWidth+1),h*2-(CardHeight+1)))
    pygame.display.flip()
    checkEvents()
    return CardVs[choice]

  def passNotify():
    print "Pass complete"
    global VQ
    global screen
    printVQNodes(VQ, screen)
    pygame.image.save(screen, "LastCodeBook.png")

  def trainVQ(VQ):
    VQ.train(getRandomCard, passNotify, 129, 52*3)

  trainVQ(VQ)

  while 1:
    checkEvents()

