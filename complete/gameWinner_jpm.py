import timeit
# Game Winner
# 2 player game where each player must remove one of their pieces; player with most pieced removed wins
# piece can be removed if the piece before + after are also their pieces,
# if all 3 do not match, piece cannot be removed
# game ends when both players cannot move a piece 
# wendy moves first # return the name of the winner (i.e. "wendy" or "bob")

# colors = "wwwbb" #data passed in as a string. data is either a "w" or "b", no white spaces or special characters 
# split colors in an array
  # pieces = list(colors)

#wendy goes first
# for piece in pieces 
  # if piece == "w" and pieces[piece-1] == "w" and  pieces[piece+1] == "w": 3 conditions
  # wendy gets a point  
  # pieces.pop(piece) 

# dont actually need hash, simple counter works!
# whoever has the collections with the highest number 

def gameWinner(colors):
  if len(colors) < 3:
    return "bob" 
  
  pieces = list(colors)
  wendy = 0 
  bob = 0

  for p in range(1, len(pieces)):
    while  (p + 1 < len(pieces)) and  pieces[p-1] == pieces[p] and pieces[p+1] == pieces[p]:
      if pieces[p] == "w":
        wendy += 1
        pieces.pop(p) 
      else:
        bob += 1
        pieces.pop(p) 
  wendy, bob

  if wendy > bob:
    return "wendy"
  else:
    return "bob"

g1 = gameWinner("wwwbbw")
g2 = gameWinner("bbwwwwwbbbwbwbwwbbbbbwwbwwbbwbwwbwwbwwbbwwbwbwbbwbbwwbwbbwbbwwbwwbwbwbbwwwbwwbbwbbbbbwwwwwbwbwbwwbwbbbwbbbbwbwbwwbbwbwbbbwbwwwwwwbbwbwbwwwbwbwwwbbwwbwbbwwwbbbbwwbbbwbbbbwwwwwbbwwbbwwwwwwbwbbwwwbbbwbbwwwwwwbbwwbbwwwbbbbwwbbbbbbwwbbbbbwbwbwbwwbbbwbwbbwbbbbwwwwwbbwbwbbbbbwwbwwbwwwwbwwbbbbbbwbbbwwwwbwbbwbbbwwwwbwwwbbwwwbwwwbwbwbbbwbwwwbwwbwwwwbwbwwbwwwwwbwbwbwwbwbbbwbbwbwbwwbbbwwwbbbbwwwwwbbbbwwwwwbbbbwwwwbbwbbwbbwwwbwbbwbbwwbbbbbwbbwbwbwbwwwbwwwwwbwbwwbwbwbwbbwbbbbbbbwwbbwbbwwbwbbbbwbwwbbbwbwwbwbbwwwwwbwbwwbwbwwbbwwbbbwbwwwbbwwwwwbbbbbbbbwwbwwwwbbbbwwbbbbbbwwwbbbbbwbwbbbwwwwbbwwwbwwwwwwwbwbbbbwwwbwwwwbwbwwwbwwbwwwbwwbbbwbwbwwwbbbbwwwbbbwwbwbwwbwwbbbwbwbwwwbbwwbbwwbwbwbwwbwwwbwbwbwbbbwwbwbwbbwbwwwwbbbwbbbwwwwbwbbwbbwwwbwwwbbbbwbwbwwwwbbbwbwwbwbbwwwbbbwwbbbbwbwwbwbwwwwwbbwwbwwbwwbbbbwwbwwwbwwwwwwbbbbwbbbwbbwbwbwbbwbbbwwwbbbbbwbwwwwbbbwbwwbbwbwwbwwbwbbbwwbwwwbbbwbbwwwbbbbbwwbwwwbbwbbwbwwwbbwbwwwbwwbwwwwbbwwbbwwwwwbwwbbwwbwbwbbbwwbbwbbwwbbbwwbwbwbwbbwwwwwbbbwwwbbwbbwwwbwwwbwwbwwbbbbbwbbwwwwbb")
g3 = gameWinner("wwbbbwwwbbbbbwwwwwwbbbbww")
g4 = gameWinner("wwwbbbbbbbbwww")
g5 = gameWinner("bbbwwwwwwwwbbb")
g6 = gameWinner("bbbwwwbbwww")
g7 = gameWinner("ww")

print(g1) #wendy 1 -0
print(g2) #wendy 124 - 112
print(g3) #bob 6 - 5
print(g4) #bob 6 - 2
print(g5) #wendy 2 - 1
print(g6) #wendy
print(g7) #bob

print(timeit.timeit("gameWinner('wwbbbwwwbbbbbwwwwwwbbbbww')", number=10000, setup="from __main__ import gameWinner")) 
  #0.04208370800188277 - 0.048996624995197635
print(timeit.timeit("gameWinner('bbwwwwwbbbwbwbwwbbbbbwwbwwbbwbwwbwwbwwbbwwbwbwbbwbbwwbwbbwbbwwbwwbwbwbbwwwbwwbbwbbbbbwwwwwbwbwbwwbwbbbwbbbbwbwbwwbbwbwbbbwbwwwwwwbbwbwbwwwbwbwwwbbwwbwbbwwwbbbbwwbbbwbbbbwwwwwbbwwbbwwwwwwbwbbwwwbbbwbbwwwwwwbbwwbbwwwbbbbwwbbbbbbwwbbbbbwbwbwbwwbbbwbwbbwbbbbwwwwwbbwbwbbbbbwwbwwbwwwwbwwbbbbbbwbbbwwwwbwbbwbbbwwwwbwwwbbwwwbwwwbwbwbbbwbwwwbwwbwwwwbwbwwbwwwwwbwbwbwwbwbbbwbbwbwbwwbbbwwwbbbbwwwwwbbbbwwwwwbbbbwwwwbbwbbwbbwwwbwbbwbbwwbbbbbwbbwbwbwbwwwbwwwwwbwbwwbwbwbwbbwbbbbbbbwwbbwbbwwbwbbbbwbwwbbbwbwwbwbbwwwwwbwbwwbwbwwbbwwbbbwbwwwbbwwwwwbbbbbbbbwwbwwwwbbbbwwbbbbbbwwwbbbbbwbwbbbwwwwbbwwwbwwwwwwwbwbbbbwwwbwwwwbwbwwwbwwbwwwbwwbbbwbwbwwwbbbbwwwbbbwwbwbwwbwwbbbwbwbwwwbbwwbbwwbwbwbwwbwwwbwbwbwbbbwwbwbwbbwbwwwwbbbwbbbwwwwbwbbwbbwwwbwwwbbbbwbwbwwwwbbbwbwwbwbbwwwbbbwwbbbbwbwwbwbwwwwwbbwwbwwbwwbbbbwwbwwwbwwwwwwbbbbwbbbwbbwbwbwbbwbbbwwwbbbbbwbwwwwbbbwbwwbbwbwwbwwbwbbbwwbwwwbbbwbbwwwbbbbbwwbwwwbbwbbwbwwwbbwbwwwbwwbwwwwbbwwbbwwwwwbwwbbwwbwbwbbbwwbbwbbwwbbbwwbwbwbwbbwwwwwbbbwwwbbwbbwwwbwwwbwwbwwbbbbbwbbwwwwbb')", number=10000, setup="from __main__ import gameWinner"))
  #1.875502000002598 - 2.560829375004687







#original code (submitted in test):
# def gameWinner(colors):
#     pieces = list(colors)
    
#     if len(pieces) < 3:
#         return "bob" 
    
#     turn = "wendy" # wendy goes first (reset to bob)
    
#     for p in range(1, len(pieces) - 2):
#         if turn == "wendy": 
#             if pieces[p-1 ] == "w" and  pieces[p+1] == "w":
#                 turn = "bob" 
#                 pieces.pop(p) 
#             else:
#                 return "bob" #wins
            
#         elif turn == "bob": 
#             if pieces[p-1 ] == "b" and  pieces[p+1] == "b":
#                 turn = "wendy"
#                 pieces.pop(p)
#             else:
#                 return "wendy"


# g1 = gameWinner("wwwbbw")
# g2 = gameWinner("bbwwwwwbbbwbwbwwbbbbbwwbwwbbwbwwbwwbwwbbwwbwbwbbwbbwwbwbbwbbwwbwwbwbwbbwwwbwwbbwbbbbbwwwwwbwbwbwwbwbbbwbbbbwbwbwwbbwbwbbbwbwwwwwwbbwbwbwwwbwbwwwbbwwbwbbwwwbbbbwwbbbwbbbbwwwwwbbwwbbwwwwwwbwbbwwwbbbwbbwwwwwwbbwwbbwwwbbbbwwbbbbbbwwbbbbbwbwbwbwwbbbwbwbbwbbbbwwwwwbbwbwbbbbbwwbwwbwwwwbwwbbbbbbwbbbwwwwbwbbwbbbwwwwbwwwbbwwwbwwwbwbwbbbwbwwwbwwbwwwwbwbwwbwwwwwbwbwbwwbwbbbwbbwbwbwwbbbwwwbbbbwwwwwbbbbwwwwwbbbbwwwwbbwbbwbbwwwbwbbwbbwwbbbbbwbbwbwbwbwwwbwwwwwbwbwwbwbwbwbbwbbbbbbbwwbbwbbwwbwbbbbwbwwbbbwbwwbwbbwwwwwbwbwwbwbwwbbwwbbbwbwwwbbwwwwwbbbbbbbbwwbwwwwbbbbwwbbbbbbwwwbbbbbwbwbbbwwwwbbwwwbwwwwwwwbwbbbbwwwbwwwwbwbwwwbwwbwwwbwwbbbwbwbwwwbbbbwwwbbbwwbwbwwbwwbbbwbwbwwwbbwwbbwwbwbwbwwbwwwbwbwbwbbbwwbwbwbbwbwwwwbbbwbbbwwwwbwbbwbbwwwbwwwbbbbwbwbwwwwbbbwbwwbwbbwwwbbbwwbbbbwbwwbwbwwwwwbbwwbwwbwwbbbbwwbwwwbwwwwwwbbbbwbbbwbbwbwbwbbwbbbwwwbbbbbwbwwwwbbbwbwwbbwbwwbwwbwbbbwwbwwwbbbwbbwwwbbbbbwwbwwwbbwbbwbwwwbbwbwwwbwwbwwwwbbwwbbwwwwwbwwbbwwbwbwbbbwwbbwbbwwbbbwwbwbwbwbbwwwwwbbbwwwbbwbbwwwbwwwbwwbwwbbbbbwbbwwwwbb")
# g3 = gameWinner("wwbbbwwwbbbbbwww") #bob
# g4 = gameWinner("wwwbbbbbbbbwww")

# print(g1)
# print(g2) #
# print(g3)
# print(g4)


