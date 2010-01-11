def sortrank(a,b):
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
  if a[:-1] == '10':
    return 1
  if b[:-1] == '10':
    return -1
  if a[:-1] > b[:-1]:
    return 1
  if a[:-1] < b[:-1]:
    return -1

def sortsuits(a,b):
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
