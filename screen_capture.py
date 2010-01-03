import pywinauto
from pywinauto import findwindows
from pywinauto.application import Application
import PIL
from time import sleep

class Table(object):
  def __init__(self, table_name, game_type = "NL Hold'em", width = 640, height = 482):
    self.name = table_name
    self.game_type = game_type
    self.app = Application()

    self.app.connect_(title_re = self.name + '.* ' + self.game_type)

    self.table_handle = findwindows.find_window( title_re = self.name + '.* ' + self.game_type)
    self.chat_parent_handle = self.GetChatParentHandle()
    self.chat_handle = self.GetChatHandle()
    self.chat_text = []
    self.GetChatText()
    self.width = 640
    self.height = 482
    

    self.lines_processed = len(self.chat_text)
    self.table_cards = []

  def GetChatParentHandle(self):
    for handle in findwindows.find_windows(process = self.app.process):
      texts = self.app.window_(handle = handle).GetProperties()['Texts'][0]
      if (    ("UB" not in texts)
          and (self.name in texts)
          and ("NL" not in texts)):
        return handle

  def GetChatHandle(self):
    parent_win = self.app.window_(handle = self.chat_parent_handle)
    for child_win in parent_win.Children():
      props = child_win.GetProperties()
      if (    (props['IsVisible'])
          and (props['Class'] == 'RichEdit20A')
          and ('connected' in props['Texts'][0])):
        return child_win.handle  

  def GetChatText(self):
    self.chat_text = self.app.window_(handle = self.chat_handle).GetProperties()['Texts'][0].split('\r\n')

  def CaptureWindow(self, filename = 'd:/pokerbot/image.bmp'):
    image = self.app.window_(handle = self.table_handle).CaptureAsImage()
    image.save(filename)

  def TimedCapture(self, total_images, timed_interval, filename = 'd:/pokerbot/screens/image.bmp'):
    win = self.app.window_(handle = self.table_handle)
    for i in xrange(total_images):
      save_file = filename.rsplit('.',2)
      save_file = save_file[0] + str(i) + '.' + save_file[1]
      self.CaptureWindow(filename = save_file)
      sleep(timed_interval)

  def ProcessLines(self):
    self.GetChatText()
    while (self.lines_processed < len(self.chat_text)):
      self.ProcessLine(self.chat_text[self.lines_processed])
      self.lines_processed += 1


  def SetTableCards(self, line):
    if ( ('FLOP' in line)
       or('TURN' in line)
       or('RIVER' in line)):
      cards = line.rsplit('[',2)[1].rsplit(']',2)[0].split(' ')
      for card in cards:
        self.table_cards.append(card)
      self.CaptureWindow('d:/pokerbot/screen4/' + ''.join(self.table_cards) + '.bmp')
    elif 'HOLE CARDS' in line:
      self.table_cards = []
      print 'new hand'

  

  def ProcessLine(self, line):
    if 'DEALING' in line:
      self.SetTableCards(line)
    if 'SHOW DOWN' in line:
      pass

          

def CardCapture(table_name, total_captures):
    table_handle = GetTableHandle(table_name)
    for i in xrange(total_captures):
        text = GetChatText(table_name)


#CaptureWindow(GetTableHandle('Tonga'))
#print GetDealerChat('Tonga').split('\r\n',2)[0]
print 'done'
