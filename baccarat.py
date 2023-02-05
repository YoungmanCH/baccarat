import random as r
import copy as c

chips = 0
bet = 0
chips_check = False
game_mode = None
user_role = False

def game_mode_config():
  print("Enter 's' to start or continue the game, or 'q' to end the game.")
  game_mode_check = False
  #Using global variable
  global game_mode

  while game_mode_check == False:
    game_mode = input()

    if game_mode == "s":
      print("Game start!!")
      break

    elif game_mode == "q":
      print("Game over")
      break

    else:
      print('Enter other characters')
      print("Enter 's' to start or continue the game, or 'q' to end the game.")

def charge():
  #Using global variable
  global chips
  if chips < 15:
    while chips_check == False:
      try:
        print("Charge chips! Minimum charge is $15.")
        chips += int(input())
      except ValueError as e0:
        print("Charge chips! Minimum charge is $15.")
      if chips >= 15:
        break
      else:
        print("Only single-byte numbers can be used.")
        print("Your total chips: $" + str(chips))
        print("Minimum charge is $15. Charge chips!")
        continue
    

def preparation():
  print("Your total chips: $" + str(chips))
  print("Choose Player or Banker or Tie.")
  print("Player is p. Banker is b. Tie is t.")
  role_check = False
  wager_check = False
  #Using global variable
  global user_role

  while role_check == False:
    choose = input()
    user_role
    if choose == "p":
      user_role = "Player"
      print(user_role)
      print("Place your bet! Minimum wager is $15.")
      break
    elif choose =="b":
      user_role = "Banker"
      print(user_role)
      print("Place your bet! Minimum wager is $15.")
      break
    elif choose == "t":
      user_role = "Tie"
      print(user_role)
      print("Place your bet! Minimum wager is $15.")
      break
    else:
      print("Enter other characters.")
      print("Choose Player or Banker or Tie.")
      print("Player is p. Banker is b. Tie is t.")
      continue

  while wager_check == False:
    #Using global variable
    global bet
    try:
      bet = int(input())
      if bet >= 15:
        break
      else:
        print("Minimum wager is $15. Place your bet!")
        continue
    except ValueError as e1:
      print("Only single-byte numbers can be used.")
      print("Minimum wager is $15. Place your bet!")


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
  player_result = []
  player_count_result = []
  c1 = 0

  while c1 != 2:
    n1 = r.randint(0, 12)
    n2 = r.randint(0, 7)
    n3 = r.randint(0, 3)

    try:
      player_result.append(cards[n3][n2][n1])
      del cards[n3][n2][n1]
      c1 += 1
    except IndexError as e2:
      continue

  print("Player's card")
  print(player_result[0], player_result[1])
  player_count_result = c.copy(player_result)
  banker_result = []
  banker_count_result = []
  c2 = 0

  while c2 != 2:
    n1 = r.randint(0, 12)
    n2 = r.randint(0, 7)
    n3 = r.randint(0, 3)

    try:
      banker_result.append(cards[n3][n2][n1])
      del cards[n3][n2][n1]
      c2 += 1
    except IndexError as e3:
      continue

  print("Banker's card")
  print(banker_result[0], banker_result[1])
  banker_count_result = c.copy(banker_result)
  first_judge = None
  judge = None
  player_sum = None
  banker_sum = None
  if player_result[0] == "J" or player_result[0] == "Q" or player_result[0] == "K":
    player_result[0] = "10"
  if player_result[1] == "J" or player_result[1] == "Q" or player_result[1] == "K":
    player_result[1] = "10"
  player_sum = int(player_result[0])+int(player_result[1])
  if player_sum >= 20:
    player_sum -= 20
  if player_sum >= 10:
    player_sum -= 10
  if player_sum == 8 or player_sum == 9:
    first_judge = "Natural"
    
  if banker_result[0] == "J" or banker_result[0] == "Q" or banker_result[0] == "K":
    banker_result[0] = "10"
  if banker_result[1] == "J" or banker_result[1] == "Q" or banker_result[1] == "K":
    banker_result[1] = "10"
  banker_sum = int(banker_result[0])+int(banker_result[1])
  if banker_sum >= 20:
    banker_sum -= 20
  if banker_sum >= 10:
    banker_sum -= 10
  if banker_sum == 8 or banker_sum == 9:
    first_judge = "Natural"

  if first_judge == "Natural":
    if player_sum > banker_sum:
      judge = "Player"
      print(judge + " is winner!")
    elif player_sum == banker_sum:
      judge = "Tie"
      print(judge)
    else:
      judge = "Banker"
      print(judge + " is winner!")

  elif (player_sum == 6 or player_sum == 7) and banker_sum == 7:
    print("Player is stand")
    print("Banker is stand")

    if player_sum > banker_sum:
      judge = "Player"
      print(judge + " is winner!")
    elif player_sum == banker_sum:
      judge = "Tie"
      print(judge)
    else:
      judge = "Banker"
      print(judge + " is winner!")

  elif player_sum == 6 or player_sum == 7:
    print("Player is stand")
    print("Next cards!")

    c4 = 0

    while c4 !=1:
      n1 = r.randint(0, 12)
      n2 = r.randint(0, 7)
      n3 = r.randint(0, 3)
      try:
        banker_result.append(cards[n3][n2][n1])
        banker_count_result.append(cards[n3][n2][n1])
        del cards[n3][n2][n1]
        c4 += 1
      except IndexError as e4:
        continue

    print("Banker's card")
    print(banker_count_result[0], banker_count_result[1], banker_count_result[2])

    if banker_result[2] == "J" or banker_result[2] == "Q" or banker_result[2] == "K":
      banker_result[2] = "10"
    banker_sum = int(banker_result[0])+int(banker_result[1])+int(banker_result[2])
    if banker_sum >= 30:
      banker_sum -= 30
    if banker_sum >= 20:
      banker_sum -= 20
    if banker_sum >= 10:
      banker_sum -= 10
    
    if player_sum > banker_sum:
      judge = "Player"
      print(judge + " is winner!")
    elif player_sum == banker_sum:
      judge = "Tie"
      print(judge)
    else:
      judge = "Banker"
      print(judge + " is winner!")

  elif banker_sum == 7:
    print("Banker is stand")
    print("Next cards!")
    c3 = 0

    while c3 !=1:
      n1 = r.randint(0, 12)
      n2 = r.randint(0, 7)
      n3 = r.randint(0, 3)
      try:
        player_result.append(cards[n3][n2][n1])
        player_count_result.append(cards[n3][n2][n1])
        del cards[n3][n2][n1]
        c3 += 1
      except IndexError as e3:
        continue

    print("Player's card")
    print(player_count_result[0], player_count_result[1], player_count_result[2])
    
    if player_result[2] == "J" or player_result[2] == "Q" or player_result[2] == "K":
      player_result[2] = "10"
    player_sum = int(player_result[0])+int(player_result[1])+int(player_result[2])
    if player_sum >= 30:
      player_sum -= 30
    if player_sum >= 20:
      player_sum -= 20
    if player_sum >= 10:
      player_sum -= 10

    if player_sum > banker_sum:
      judge = "Player"
      print(judge + " is winner!")
    elif player_sum == banker_sum:
      judge = "Tie"
      print(judge)
    else:
      judge = "Banker"
      print(judge + " is winner!")

  else:
    print("Next cards!")
    c3 = 0

    while c3 !=1:
      n1 = r.randint(0, 12)
      n2 = r.randint(0, 7)
      n3 = r.randint(0, 3)
      try:
        player_result.append(cards[n3][n2][n1])
        player_count_result.append(cards[n3][n2][n1])
        del cards[n3][n2][n1]
        c3 += 1
      except IndexError as e3:
        continue

    print("Player's card")
    print(player_count_result[0], player_count_result[1], player_count_result[2])

    if player_result[2] == "J" or player_result[2] == "Q" or player_result[2] == "K":
      player_result[2] = "10"
    player_sum = int(player_result[0])+int(player_result[1])+int(player_result[2])
    if player_sum >= 30:
      player_sum -= 30
    if player_sum >= 20:
      player_sum -= 20
    if player_sum >= 10:
      player_sum -= 10
    
    if player_sum == 8 and banker_sum == 3:
      judge = "Player"
      print(judge + " is winner")

    if (player_sum == 8 or player_sum == 9) and banker_sum <= 2 :
      c4 = 0

      while c4 !=1:
        n1 = r.randint(0, 12)
        n2 = r.randint(0, 7)
        n3 = r.randint(0, 3)
        try:
          banker_result.append(cards[n3][n2][n1])
          banker_count_result.append(cards[n3][n2][n1])
          del cards[n3][n2][n1]
          c4 += 1
        except IndexError as e4:
          continue

      print("Banker's card")
      print(banker_count_result[0], banker_count_result[1], banker_count_result[2])

    
      if banker_result[2] == "J" or banker_result[2] == "Q" or banker_result[2] == "K":
        banker_result[2] = "10"
      banker_sum = int(banker_result[0])+int(banker_result[1])+int(banker_result[2])
      if banker_sum >= 30:
        banker_sum -= 30
      if banker_sum >= 20:
        banker_sum -= 20
      if banker_sum >= 10:
        banker_sum -= 10
      
      if player_sum > banker_sum:
        judge = "Player"
        print(judge + " is winner!")
      elif player_sum == banker_sum:
        judge = "Tie"
        print(judge)
      else:
        judge = "Banker"
        print(judge + " is winner!")

    elif player_sum == 8 or player_sum == 9:
      judge = "Player"
      print(judge + " is winner!")

    elif (player_sum == 0 or player_sum == 1 or player_sum == 8 or player_sum == 9) and banker_sum == 4:
      if player_sum > banker_sum:
        judge = "Player"
        print(judge + " is winner!")
      elif player_sum == banker_sum:
        judge = "Tie"
        print(judge)
      else:
        judge = "Banker"
        print(judge + " is winner!")
    
    elif (player_sum == 0 or player_sum == 1 or player_sum == 2 or player_sum == 3 or  player_sum == 8 or  player_sum == 9) and banker_sum == 5:
      if player_sum > banker_sum:
        judge = "Player"
        print(judge + " is winner!")
      elif player_sum == banker_sum:
        judge = "Tie"
        print(judge)
      else:
        judge = "Banker"
        print(judge + " is winner!")

    elif (player_sum == 0 or player_sum == 1 or player_sum == 2 or player_sum == 3 or player_sum == 4 or player_sum == 5 or player_sum == 8 or player_sum == 9) and banker_sum == 6:
      if player_sum > banker_sum:
        judge = "Player"
        print(judge + " is winner!")
      elif player_sum == banker_sum:
        judge = "Tie"
        print(judge)
      else:
        judge = "Banker"
        print(judge + " is winner!")

    else:
      c4 = 0

      while c4 !=1:
        n1 = r.randint(0, 12)
        n2 = r.randint(0, 7)
        n3 = r.randint(0, 3)
        try:
          banker_result.append(cards[n3][n2][n1])
          banker_count_result.append(cards[n3][n2][n1])
          del cards[n3][n2][n1]
          c4 += 1
        except IndexError as e4:
          continue

      print("Banker's card")
      print(banker_count_result[0], banker_count_result[1], banker_count_result[2])

    
      if banker_result[2] == "J" or banker_result[2] == "Q" or banker_result[2] == "K":
        banker_result[2] = "10"
      banker_sum = int(banker_result[0])+int(banker_result[1])+int(banker_result[2])
      if banker_sum >= 30:
        banker_sum -= 30
      if banker_sum >= 20:
        banker_sum -= 20
      if banker_sum >= 10:
        banker_sum -= 10
      
      if player_sum > banker_sum:
        judge = "Player"
        print(judge + " is winner!")
      elif player_sum == banker_sum:
        judge = "Tie"
        print(judge)
      else:
        judge = "Banker"
        print(judge + " is winner!")

  print("result: " + str(player_sum), str(banker_sum))

  #Using global variable
  global chips
  if (user_role == judge and judge == "Player"):
    chips += bet
  elif (user_role == judge and judge == "Banker"):
    bet_commission = float(bet) * 0.95
    chips += bet_commission
  elif (user_role == judge and judge == "Tie"):
    bet_commission = bet * 9
    chips += bet_commission
  elif judge == "Tie":
    chips = chips
  else:
    chips -= bet
  print("Your chips is $" + str(chips))
  more_charge = None
  print("Do you charge tips? Yes is 'y'. No is 'n'.")
  more_charge = input()

  while True:
    if more_charge =='y': 
      while True:
        try:
          print("You can charge tips from $1")
          more_chips = int(input())
          while True:
            if more_chips >0:
              chips += more_chips
              break
            else:
              print("Only single-byte numbers can be used.")
              print("You can charge tips from $1")
              more_chips = int(input())
              continue
          break

        except ValueError as e5:
          print("Only single-byte numbers can be used.")
          print("Your total chips: $" + str(chips))
          continue
      break
    elif more_charge == 'n':
      break
    else:
      print("Enter other characters.")
      print("Do you charge tips? Yes is 'y'. No is 'n'.")
      continue

  game_mode_config()

game_mode_config()
while game_mode != 'q':
  charge()
  preparation()
  game()

#Metamaskと混ぜれば面白そう





