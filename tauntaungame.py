import random
import time

print('''Hoth Survival GAME:
As a warrior in the Rebel Army, you have destroyed a hanger full of Galactic
Fighters and then stole a Tauntaun to escape across the vast frozen tundra to
freedom. The Empire is chasing you down to kill you! Survive your ice desert trek
and outsmart them all!''')
time.sleep(2)
km_traveled = 0
hunger = 0
Tauntaun_tiredness = 0
enemy_distance = -20
chocolate_bars = 3
#added player dead for unique(ish) game end screens
playerdead = False
done = False
while not done:
  #setting variables for rng events
  tt_exhaust = random.randrange(1, 4)
  empire_movement = random.randrange(7, 15)
  full = random.randrange(10, 21)
  moderate = random.randrange(5, 13)
  print("Kilometers traveled:", km_traveled)
  print("Chocolate bars in food pack:", chocolate_bars)
  print("The Empire army is", km_traveled - enemy_distance, "kilometers behind you.")
  time.sleep(2)
  #added .lower so i dont have to put 8 billion or's
  choice = input('''A: Eat a chocolate bar from your food pack.
B. Ahead moderate speed.
C. Ahead full speed.
D. Stop and rest.
Q. Quit
Choice: ''').lower()
  if choice == "a":
    if chocolate_bars > 0:
      hunger = 0
      chocolate_bars -= 1
      print("You consumed a chocolate bar.")
      time.sleep(2)
    else:
      print("Error, you have no chocolate bars")
  elif choice == "b":
    km_traveled += moderate
    hunger += 1
    Tauntaun_tiredness += 1
    enemy_distance += empire_movement
    print("You and your Tauntaun moved at a moderate speed.")
    time.sleep(2)
    #best way i can think of the generate a NEW number everytime.
    #i like to imagine the print(campchance) is like a d20 roll
    campchance = random.randrange(1, 21)
    print(campchance)
  elif choice == "c":
    km_traveled += full
    hunger += 1
    Tauntaun_tiredness += tt_exhaust
    enemy_distance += empire_movement
    print("You and your Tauntaun moved at full speed.")
    time.sleep(2)
    campchance = random.randrange(1, 21)
    print(campchance)
  elif choice == "d":
    Tauntaun_tiredness = 0
    enemy_distance += empire_movement
    print("You and your Tauntaun rested. This makes your Tauntaun happy.")
    time.sleep(2)
  elif choice == "q":
    print("You quit the game.")
    time.sleep(2)
    exit()
  if hunger > 4:
    print("You are hungry.")
    time.sleep(2)
  if hunger > 6:
    print("Your decision to ignore your hunger has cost you your life.")
    time.sleep(2)
    print("Game Over.")
    done = True
    playerdead = True
  if Tauntaun_tiredness > 5:
    print("Your Tauntaun is getting tired")
    time.sleep(2)
  if Tauntaun_tiredness > 8:
    print("Your Tauntaun has died of exhaustion. You starve shortly after.")
    time.sleep(2)
    print("Game Over.")
    done = True
    playerdead = True
  if km_traveled - enemy_distance < 15:
    print("The Empire army are getting close...")
    time.sleep(2)
  if enemy_distance > km_traveled:
    print("The Empire army have caught up to you. You are captured")
    time.sleep(2)
    print("Game Over.")
    done = True
    playerdead = True
    #using >= so the player can win at 200 and not just 201+
  if km_traveled >= 200:
    print("You have escaped the Empire army!")
    time.sleep(2)
    print("You win!")
    done = True
  if campchance == 20:
    print("You found a rebel campsite!")
    time.sleep(2)
    print("You refilled on chocolate bars and rested with your Tauntaun.")
    chocolate_bars = 3
    Tauntaun_tiredness = 0
    hunger = 0
    time.sleep(2)
if playerdead == True:
  print("You should try again! You'll escape the Empire army next time!")
  time.sleep(2)
  exit()
if playerdead == False:
  print("Congrats on the win! Thanks for playing!")
  time.sleep(2)
  exit()