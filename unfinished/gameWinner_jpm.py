import timeit
 
# Game Winner

# wendy moves fiorst
# wendy is black

# player cannot take off a piece they lose

# i = color ("w" or "bob")

# consequtive and equal or more

# colors = "wwwbb"
#colors in an array
# pieces = list(colors)

#wendy goes first
# for piece in pieces 
  # if pieces[index+1] == "w": #if there are 
  #   pieces.pop(piece) else
  #   print("bob")
  # elif

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


# dictionary player (key) with values being a count ex {wendy : 4, Bob : 3 }
# whoever has the collections with the highest number 
#  wendy : [ [w,w,w,w,w,w,w], [w,w,w], [w,w,w, w] ]
# or wendy : [7, 3, 4] and -1 if [num] is greater than 3; if you cannot reduce by 1 then other person wins

# [0,1,2,3,4] +1
# [0,2,3,4] +1
# [0,3,4] +1 
# [0,4] endgame

def gameWinner(colors):
  pieces = list(colors)
  if len(pieces) < 3:
    return "bob" 
  
  count_hash = {}
  count_hash["w"] = 0
  count_hash["b"] = 0

  for p in range(1, len(pieces)):
      # if (p + 1 < len(pieces)): 
        # while p + 1 < len(pieces): 
      # while (p + 1 < len(pieces)) and pieces[p-1 ] == "w" and pieces[p+1] == "w": 
          while  (p + 1 < len(pieces)) and  pieces[p-1] == pieces[p] and pieces[p+1] == pieces[p]:
            if pieces[p] == "w":
              count_hash["w"] += 1
              pieces.pop(p) 
            else:
          # while (p + 1 < len(pieces)) and pieces[p-1 ] == "b" and pieces[p+1] == "b":      
              count_hash["b"] += 1
              pieces.pop(p) 
          # else:
          #   continue
  count_hash

  if count_hash["w"] > count_hash["b"]:
    return "wendy", list(count_hash.values()) 
  else:  
    return "bob", list(count_hash.values())

g1 = gameWinner("wwwbbw")
g2 = gameWinner("bbwwwwwbbbwbwbwwbbbbbwwbwwbbwbwwbwwbwwbbwwbwbwbbwbbwwbwbbwbbwwbwwbwbwbbwwwbwwbbwbbbbbwwwwwbwbwbwwbwbbbwbbbbwbwbwwbbwbwbbbwbwwwwwwbbwbwbwwwbwbwwwbbwwbwbbwwwbbbbwwbbbwbbbbwwwwwbbwwbbwwwwwwbwbbwwwbbbwbbwwwwwwbbwwbbwwwbbbbwwbbbbbbwwbbbbbwbwbwbwwbbbwbwbbwbbbbwwwwwbbwbwbbbbbwwbwwbwwwwbwwbbbbbbwbbbwwwwbwbbwbbbwwwwbwwwbbwwwbwwwbwbwbbbwbwwwbwwbwwwwbwbwwbwwwwwbwbwbwwbwbbbwbbwbwbwwbbbwwwbbbbwwwwwbbbbwwwwwbbbbwwwwbbwbbwbbwwwbwbbwbbwwbbbbbwbbwbwbwbwwwbwwwwwbwbwwbwbwbwbbwbbbbbbbwwbbwbbwwbwbbbbwbwwbbbwbwwbwbbwwwwwbwbwwbwbwwbbwwbbbwbwwwbbwwwwwbbbbbbbbwwbwwwwbbbbwwbbbbbbwwwbbbbbwbwbbbwwwwbbwwwbwwwwwwwbwbbbbwwwbwwwwbwbwwwbwwbwwwbwwbbbwbwbwwwbbbbwwwbbbwwbwbwwbwwbbbwbwbwwwbbwwbbwwbwbwbwwbwwwbwbwbwbbbwwbwbwbbwbwwwwbbbwbbbwwwwbwbbwbbwwwbwwwbbbbwbwbwwwwbbbwbwwbwbbwwwbbbwwbbbbwbwwbwbwwwwwbbwwbwwbwwbbbbwwbwwwbwwwwwwbbbbwbbbwbbwbwbwbbwbbbwwwbbbbbwbwwwwbbbwbwwbbwbwwbwwbwbbbwwbwwwbbbwbbwwwbbbbbwwbwwwbbwbbwbwwwbbwbwwwbwwbwwwwbbwwbbwwwwwbwwbbwwbwbwbbbwwbbwbbwwbbbwwbwbwbwbbwwwwwbbbwwwbbwbbwwwbwwwbwwbwwbbbbbwbbwwwwbb")
g3 = gameWinner("wwbbbwwwbbbbbwww")
g4 = gameWinner("wwwbbbbbbbbwww")
g5 = gameWinner("bbbwwwwwwwwbbb")
g6 = gameWinner("bbbwwwbbwww")

print(g1) #wendy
print(g2) #wendy
print(g3) #bob
print(g4) #bob
print(g5) #wendy
print(g6) #wendy

print(timeit.timeit("gameWinner('bbbwwwwwwbbb')", number=10000, setup="from __main__ import gameWinner"))
print(timeit.timeit("gameWinner('bbwwwwwbbbwbwbwwbbbbbwwbwwbbwbwwbwwbwwbbwwbwbwbbwbbwwbwbbwbbwwbwwbwbwbbwwwbwwbbwbbbbbwwwwwbwbwbwwbwbbbwbbbbwbwbwwbbwbwbbbwbwwwwwwbbwbwbwwwbwbwwwbbwwbwbbwwwbbbbwwbbbwbbbbwwwwwbbwwbbwwwwwwbwbbwwwbbbwbbwwwwwwbbwwbbwwwbbbbwwbbbbbbwwbbbbbwbwbwbwwbbbwbwbbwbbbbwwwwwbbwbwbbbbbwwbwwbwwwwbwwbbbbbbwbbbwwwwbwbbwbbbwwwwbwwwbbwwwbwwwbwbwbbbwbwwwbwwbwwwwbwbwwbwwwwwbwbwbwwbwbbbwbbwbwbwwbbbwwwbbbbwwwwwbbbbwwwwwbbbbwwwwbbwbbwbbwwwbwbbwbbwwbbbbbwbbwbwbwbwwwbwwwwwbwbwwbwbwbwbbwbbbbbbbwwbbwbbwwbwbbbbwbwwbbbwbwwbwbbwwwwwbwbwwbwbwwbbwwbbbwbwwwbbwwwwwbbbbbbbbwwbwwwwbbbbwwbbbbbbwwwbbbbbwbwbbbwwwwbbwwwbwwwwwwwbwbbbbwwwbwwwwbwbwwwbwwbwwwbwwbbbwbwbwwwbbbbwwwbbbwwbwbwwbwwbbbwbwbwwwbbwwbbwwbwbwbwwbwwwbwbwbwbbbwwbwbwbbwbwwwwbbbwbbbwwwwbwbbwbbwwwbwwwbbbbwbwbwwwwbbbwbwwbwbbwwwbbbwwbbbbwbwwbwbwwwwwbbwwbwwbwwbbbbwwbwwwbwwwwwwbbbbwbbbwbbwbwbwbbwbbbwwwbbbbbwbwwwwbbbwbwwbbwbwwbwwbwbbbwwbwwwbbbwbbwwwbbbbbwwbwwwbbwbbwbwwwbbwbwwwbwwbwwwwbbwwbbwwwwwbwwbbwwbwbwbbbwwbbwbbwwbbbwwbwbwbwbbwwwwwbbbwwwbbwbbwwwbwwwbwwbwwbbbbbwbbwwwwbb')", number=10000, setup="from __main__ import gameWinner"))