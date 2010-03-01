def SortRank(a,b):
  """takes 2 cards (Rank,Suit), and
     returns 1 if first is higher,
     returns -1 if second is higher,
     returns 0 if tied"""
  if a[:-1] == b[:-1]:
    return 0
  if a[:-1] == 'A':
    return 1
  if b[:-1] == 'A':
    return -1
  if a[:-1] == 'K':
    return 1
  if b[:-1] == 'K':
    return -1
  if a[:-1] == 'Q':
    return 1
  if b[:-1] == 'Q':
    return -1
  if a[:-1] == 'J':
    return 1
  if b[:-1] == 'J':
    return -1
  if a[:-1] == 'T':
    return 1
  if b[:-1] == 'T':
    return -1
  if a[:-1] > b[:-1]:
    return 1
  if a[:-1] < b[:-1]:
    return -1

def SortSuit(a,b):
  """Suits don't really have values, this is just to prettify things.
     Also sorts by rank if tied.
     takes 2 cards (Rank,Suit),
     returns 1 if first is higher,
     returns -1 if second is higher"""
  if a[-1] == b[-1]:
    return sortrank(a,b)
  if a[-1] == 'h':
    return 1
  if b[-1] == 'h':
    return -1
  if a[-1] == 'c':
    return -1
  if b[-1] == 'c':
    return 1
  if a[-1] == 's':
    return 1
  if b[-1] == 's':
    return -1
  if a[-1] == 'd':
    return 1
  if b[-1] == 'd':
    return -1
