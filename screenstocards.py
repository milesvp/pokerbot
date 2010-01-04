import Image
import glob


card_positions = ((219,161,259,217),
                  (260,161,300,217),
                  (302,161,342,217),
                  (343,161,383,217),
                  (385,161,425,217),)

background_color = (25,25,25)

def GetCardImage(imagename, card_box):
  image = Image.open(imagename)
  return image.crop(card_box)
  

def GetCardNames(imagename):
  cards = []
  cards_name = imagename.split('\\')[-1].split('.')[0]
  print cards_name
  card = ''
  for character in cards_name:
    if (   character is 'c'   #club
        or character is 'd'   #diamond
        or character is 'h'   #heart
        or character is 's'): #spade
      cards.append(card + character)
      card = ''
    else:
      card += character
  return cards

def GetCards(imagename):
  card_names = GetCardNames(imagename)
  for num, card in enumerate(card_names):
    print num, ': ', card
    image = GetCardImage(imagename, card_positions[num])
    image.putpixel((0,image.size[1]-1),background_color)
    image.putpixel((0,image.size[1]-2),background_color)
    image.putpixel((1,image.size[1]-1),background_color)
    image.putpixel((image.size[0]-1,image.size[1]-1),background_color)
    image.putpixel((image.size[0]-1,image.size[1]-2),background_color)
    image.putpixel((image.size[0]-2,image.size[1]-1),background_color)
    image.save('d:/pokerbot/cards/' + card + '.bmp')

def GetAllCards(path):  #path with wildcards
  for imagename in glob.iglob(path):
    GetCards(imagename)

