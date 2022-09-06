import numpy as np
board = np.zeros((3, 3)).astype(int)
def check_win():
  if any (np.sum(board, 1)==3) or any(np.sum(board, 0)==3) or sum(np.diag(board))==3 or sum(np.diag(board[::-1]))==3:
    return True
    if any (np.sum(board, 1)==-3) or any(np.sum(board, 0)==-3) or sum(np.diag(board))==-3 or sum(np.diag(board[::-1]))==-3:
      return False
    return True
def play_turn():
  x = int(input(f"what is player {turn}'s x position?"))
  y = int(input(f"what is player {turn}'s y position?"))
  try:
    if board[y, x]==0:
      board[y, x]=turn
    else:
        play_turn()
  except IndexError:
      play_turn()
turn = 1
move = 9
while move >0:
  print (board)
  play_turn()
  if check_win():
    print (f"player [Ture] has won!")
    break
  turn = turn*-1
  move = move -1
