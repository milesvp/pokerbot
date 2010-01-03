# DemoTreeVQ.py
import psyco
psyco.full()

import pygame, random, sys, time
import numpy.oldnumeric as Numeric
import pygame.surfarray as surfarray
import TreeVQ_arr as TreeVQ

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

def printCard(Card, screen, (xpos, ypos)):
  CardSurf = pygame.Surface((CardWidth+1, CardHeight+1))
  CardArr = Card.astype(Numeric.UnsignedInt8)

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
    printCard(i.TVal, screen, (xoff*CardWidth, yoff*CardHeight))

if __name__ == "__main__":

  pygame.init()

  CardsSurf = pygame.image.load("allcards.bmp")
  CardSurf = pygame.Surface((CardWidth+1, CardHeight+1))
  CardsArr  = surfarray.array3d(CardsSurf)
  (w, h) = CardsSurf.get_size()
  size = (w*2, h*3)
  screen  = pygame.display.set_mode(size, 0, 32)
  arr = surfarray.array3d(screen)
  # screen.blit(CardsSurf, [0,0])
  Cards = []
  CardList = range(52)

  for i in range(52):
    c = cutCard(CardsArr, i).copy()
    Cards.append(c.astype(Numeric.Float))

  VQN = TreeVQ.VQNode(None, None, Cards[1])
  VQ = TreeVQ.TreeVQ(VQN)

  Counter = 0

  def getRandomCard():
    global Counter
    choice = Counter
    Counter = (Counter + 1) % 52
    surfarray.blit_array(CardSurf, Cards[choice].astype(Numeric.UnsignedInt8))
    screen.blit(CardSurf, (w*2-(CardWidth+1),h*3-(CardHeight+1)))
    pygame.display.flip()
    checkEvents()
    return Cards[choice]

  def passNotify():
    print "Pass complete"
    global VQ
    global screen
    printVQNodes(VQ, screen)
    pygame.image.save(screen, "LastCodeBook.png")

  def trainVQ(VQ):
    VQ.train(getRandomCard, passNotify, 128, 52)

  trainVQ(VQ)

  print "DONE!"
  sys.exit(0)
  while 1:
    checkEvents()

