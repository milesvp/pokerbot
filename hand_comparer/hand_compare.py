
def GetCardValue(card):
  if card[0] == 'A':
    return 14
  if card[0] == 'K':
    return 13
  if card[0] == 'Q':
    return 12
  if card[0] == 'J':
    return 11
  if card[0] == 'T':
    return 10
  return int(card[0])

def PrepareHand(hand):
  """takes a hand, and retuns a prepared hand,
     ([singles],[doubles],[trips],[quads],spades,hearts,diamonds,clubs)"""
  prepared_hand = {}
  #                          0  A 2 3 4 5 6 7 8 9 T J Q K A
  prepared_hand['s']     = ['-',0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  prepared_hand['h']     = ['-',0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  prepared_hand['d']     = ['-',0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  prepared_hand['c']     = ['-',0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  for card in hand:
    rank = GetCardValue(card)
    prepared_hand[card[1]][rank] += 1  #prepared_hand[suit][rank]
    if rank == 14:
      prepared_hand[card[1]][1] += 1   #prepared_hand[suit][1] Ace having two possible values, 1 being it's low value
  return prepared_hand

def HandClass(prepared_hand):
  """takes a prepared_hand, and returns the best hand class
     Straight Flush 9
     Quads          8
     Full House     7
     Flush          6
     Straight       5
     Trips          4
     Two Pair       3
     Pair           2
     High Card      1
     """
  #              0  A 2 3 4 5 6 7 8 9 T J Q K A
  rank_count = ['-',0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  flush        = False
  straight     = False
  straight_flush = False
  
  for suit in prepared_hand:
    flush_count          = 0
    straight_flush_count = 0
    
    if prepared_hand[suit][1] > 0:
      rank_count[1]        += 1
      straight_flush_count = 1

    for rank in xrange(2, 15): # 2card == 2, Acecard == 14
      if prepared_hand[suit][rank] == 0:
        straight_flush_count = 0
      else:
        straight_flush_count += 1
        flush_count   += 1
        rank_count[rank] += 1
        
      if straight_flush_count >= 5:
        straight_flush = True
      if flush_count == 5:
        flush = True

  straight_count = 0
  quad_count     = 0
  trip_count     = 0
  pair_count     = 0
  
  if rank_count[1] > 0:
    straight_count = 1

  for rank in xrange(2,15):
    if rank_count[rank] == 4:
      quad_count += 1
    if rank_count[rank] == 3:
      trip_count += 1
    if rank_count[rank] == 2:
      pair_count += 1
    if rank_count[rank] == 0:
      straight_count = 0
    else:
      straight_count += 1
    if straight_count == 5:
      straight = True

  print rank_count
  print trip_count
  if straight_flush:
    return 9
  if quad_count > 0:
    return 8 #quads
  if (trip_count > 1) or (trip_count and pair_count):
    return 7 #full house
  if flush:
    return 6
  if straight:
    return 5
  if trip_count == 1:
    return 4
  if pair_count > 1:
    return 3
  if pair_count == 1:
    return 2
  return 1
  

def CompareHands(hand_a, hand,b):
  """takes 2 hands (2 list of cards)
     returns 1 if first is higher,
     returns -1 if second is greater,
     returns 0 if tied"""
  pass   

a = ['As','Jd','Th','Qs','Kd']
foo = PrepareHand(a)
print HandClass(foo)

a = ['As','Js','Ts','Qs','Ks']
foo = PrepareHand(a)
print HandClass(foo)

a = ['Ad','Jd','Td','Qs','Kd','9d']
foo = PrepareHand(a)
print HandClass(foo)

a = ['As','Jd','Th','Qs','Kd','Kh','Ks']
foo = PrepareHand(a)
print HandClass(foo)

a = ['As','Jd','Qh','Qs','Kd','Kh','Ks']
foo = PrepareHand(a)
print HandClass(foo)
