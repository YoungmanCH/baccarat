import random as r

def preparation():
  print("Choose Player or Banker or Tie.")
  print("Player is p. Banker is b. Tie is t.")
  role_check = False
  wager_check = False

  while role_check == False:
    choose = input()
    if choose == "p":
      print("Player")
      print("Place your bet! Minimum wager is $15.")
      break
    elif choose =="b":
      print("Banker")
      print("Place your bet! Minimum wager is $15.")
      break
    elif choose == "t":
      print("Tie")
      print("Place your bet! Minimum wager is $15.")
      break
    else:
      print("Enter other characters.")
      print("Choose Player or Banker or Tie.")
      print("Player is p. Banker is b. Tie is t.")
      continue

  while wager_check == False:
    try:
      bet = int(input())
    except ValueError as e1:
      print("Minimum wager is $15. Place your bet!")

    if bet >= 15:
      break
    else:
      print("Only single-byte numbers can be used.")
      print("Minimum wager is $15. Place your bet!")
      continue

#ここでは、バカラが1デッキ52枚の8デッキ使用、且つ1ゲーム毎にシャッフルされるものとする。
def game():

  Diamond1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  Diamond2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  Diamond3 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  Diamond4 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  Diamond5 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  Diamond6 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  Diamond7 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  Diamond8 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  Diamond = [Diamond1, Diamond2, Diamond3, Diamond4, Diamond5, Diamond6, Diamond7, Diamond8]
  Spade1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  Spade2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  Spade3 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  Spade4 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  Spade5 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  Spade6 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  Spade7 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  Spade8 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  Spade = [Spade1, Spade2, Spade3, Spade4, Spade5, Spade6, Spade7, Spade8]
  Heart1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  Heart2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  Heart3 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  Heart4 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  Heart5 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  Heart6 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  Heart7 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  Heart8 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  Heart = [Heart1, Heart2, Heart3, Heart4, Heart5, Heart6, Heart7, Heart8]
  Club1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  Club2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  Club3 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  Club4 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  Club5 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  Club6 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  Club7 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  Club8 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  Club = [Club1, Club2, Club3, Club4, Club5, Club6, Club7, Club8]
  cards = [Diamond, Spade, Heart, Club]
  player_first_result = []
  c1 = 0

  while c1 != 2:
    n1 = r.randint(0, 12)
    n2 = r.randint(0, 7)
    n3 = r.randint(0, 3)

    try:
      player_first_result.append(cards[n3][n2][n1])
      del cards[n3][n2][n1]
      c1 += 1
    except IndexError as e2:
      continue

  print("Player's card")
  print(player_first_result[0], player_first_result[1])

  banker_first_result = []
  c2 = 0

  while c2 != 2:
    n1 = r.randint(0, 12)
    n2 = r.randint(0, 7)
    n3 = r.randint(0, 3)

    try:
      banker_first_result.append(cards[n3][n2][n1])
      del cards[n3][n2][n1]
      c2 += 1
    except IndexError as e3:
      continue

  print("Banker's card")
  print(banker_first_result[0], banker_first_result[1])
  first_judge = None
  player_first_sum = None
  banker_first_sum = None

  if player_first_result[0] == "J" or player_first_result[0] == "Q" or player_first_result[0] == "K":
    player_first_result[0] = "10"
  if player_first_result[1] == "J" or player_first_result[1] == "Q" or player_first_result[1] == "K":
    player_first_result[1] = "10"
  player_first_sum = int(player_first_result[0])+int(player_first_result[1])
  if player_first_sum >= 10:
    player_first_sum -= 10
  if player_first_sum == 8 or player_first_sum == 9:
    first_judge = "Natural"
    
  if banker_first_result[0] == "J" or banker_first_result[0] == "Q" or banker_first_result[0] == "K":
    banker_first_result[0] = "10"
  if banker_first_result[1] == "J" or banker_first_result[1] == "Q" or banker_first_result[1] == "K":
    banker_first_result[1] = "10"
  banker_first_sum = int(banker_first_result[0])+int(banker_first_result[1])
  if banker_first_sum >= 10:
    banker_first_sum -= 10
  if banker_first_sum == 8 or banker_first_sum == 9:
    first_judge = "Natural"

  if first_judge == "Natural":
    if player_first_sum > banker_first_sum:
      print("Player is winner!")
    elif player_first_sum == banker_first_result:
      print("Tie")
    else:
      print("Banker is winner!")
  else:
    print("Next cards!")

# preparation()
game()





