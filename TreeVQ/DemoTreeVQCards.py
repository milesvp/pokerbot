#demo tree for individual cards
import psyco
psyco.full()

import glob
import pygame, random, sys, time
import numpy.oldnumeric as Numeric
import pygame.surfarray as surfarray
import TreeVQ_arr as TreeVQ

def getCardSize(path = '..\\cards\\*.bmp'):
  for imagename in glob.iglob(path):
    return pygame.image.load(imagename).get_size()

def checkEvents():
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

def printCard(Card, screen, (xpos, ypos)):
  CardSurf = pygame.Surface((CardWidth, CardHeight))
  CardArr = Card.astype(Numeric.UnsignedInt8)

  surfarray.blit_array(CardSurf, CardArr)
  screen.blit(CardSurf, [xpos, ypos])
  pygame.display.flip()

def printVQNodes(VQ, screen, card_size):
  (CardWidth, CardHeight) = card_size
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

def getCards(path = '..\\cards\\*.bmp'):
  cards = {}
  for imagename in glob.iglob(path):
    cardname = imagename.split('\\')[-1].split('.')[0]
    card_surf = pygame.image.load(imagename)
    cardArr = surfarray.array3d(card_surf)
    cards[cardname] = cardArr.astype(Numeric.Float)
  return cards

def cardsToArray(cards):
  Cards = []
  sorted_keys = 
  for key in cards.keys.sort():
    Cards.append(cards[key])
  return Cards

CardWidth, CardHeight = getCardSize()

if __name__ == "__main__":

  pygame.init()

  Cards = getCards()
  CardSurf = pygame.Surface((CardWidth, CardHeight))
  size = (1224,800)
  w, h = size
  screen  = pygame.display.set_mode(size, 0, 32)
  arr = surfarray.array3d(screen)

  Cards = cardsToArray(Cards)


  VQN = TreeVQ.VQNode(None, None, Cards[1])
  VQ = TreeVQ.TreeVQ(VQN)

  Counter = 0

  def getRandomCard():
    global Counter
    choice = Counter
    Counter = (Counter + 1) % 52
    surfarray.blit_array(CardSurf, Cards[choice].astype(Numeric.UnsignedInt8))
    screen.blit(CardSurf, (w-(CardWidth),h-(CardHeight)))
    pygame.display.flip()
    checkEvents()
    return Cards[choice]

  def passNotify():
    print "Pass complete"
    global VQ
    global screen
    printVQNodes(VQ, screen, (CardWidth, CardHeight))
    pygame.image.save(screen, "LastCodeBook.png")

  def trainVQ(VQ):
    VQ.train(getRandomCard, passNotify, 128, 52)

  trainVQ(VQ)

  print "DONE!"
  sys.exit(0)
  while 1:
    checkEvents()
