## if you have extra time add in a hp bar and links to what the robots look like
## a way you could do an hp bar is to take current hp divided by total hp and have that percentage of a bar displayed

import random
import time
p = 0

def damage_formula(self, enemy, move_name, move_damage, hit_rate, condition, atk_buff, def_buff, spd_buff, heal_buff):
  j = random.randint(0,100)
  if self.status == 'powered off':
    if self.name == player_robot:
      q = random.randint(1,100)
      global w
      try: w
      except NameError: w = 0
      if w >= q:
        self.status = 'none'
        print(f"{self.name} has powered on!")
        w = 0
      else:
        w += 25
        print(f"{self.name} is powered off and cannot move!")
    if self.name != player_robot:
      x = random.randint(1,100)
      global y
      try: y
      except NameError: y = 0
      if y >= x:
        self.status = 'none'
        print(f"{self.name} has powered on!")
        y = 0
      else:
        y += 25
        print(f"{self.name} is powered off and cannot move!")
  if self.status != 'powered off' and j < int(hit_rate):
    if self.status == 'shocked':
      k = random.randint(0,100)
      if k >= 50:
        print(f"{self.name} used {move_name}.")
        if move_damage != 0:
          enemy.hp -= int(self.attack) + int(move_damage) / int(enemy.defense)
        if condition != 'none':
          enemy.status = condition
          print(f"{enemy.name} is now {condition}.")
        if atk_buff != 0:
          self.attack += int(atk_buff)
          print(f"{self.name}'s attack increased!")
        if def_buff != 0:
          self.defense += int(def_buff)
          print(f"{self.name}'s defense increased!")
        if spd_buff != 0:
          self.speed += int(spd_buff)
          print(f"{self.name}'s speed increased!")
        if heal_buff != 0:
          if (heal_buff + self.hp) < self.total_hp:
            self.hp += int(heal_buff)
            print(f"{self.name}'s hp increased!")
          if self.hp == self.total_hp:
            print(f"{self.name}'s hp can't go any higher!")
          elif (heal_buff + self.hp) > self.total_hp:
            self.hp = self.total_hp
            print(f"{self.name}'s hp increased!")


      if k < 50:
        print(f"{self.name} is shocked and is unable to move!")
    else:
      print(f"{self.name} used {move_name}.")
      if move_damage != 0:
        enemy.hp -= int(self.attack) + int(move_damage) / int(enemy.defense)
      if condition != 'none':
        enemy.status = condition
        print(f"{enemy.name} is now {condition}.")
      if atk_buff != 0:
        self.attack += int(atk_buff)
        print(f"{self.name}'s attack increased!")
      if def_buff != 0:
        self.defense += int(def_buff)
        print(f"{self.name}'s defense increased!")
      if spd_buff != 0:
        self.speed += int(spd_buff)
        print(f"{self.name}'s speed increased!")
      if heal_buff != 0:
        if (heal_buff + self.hp) < self.total_hp:
          self.hp += int(heal_buff)
          print(f"{self.name}'s hp increased!")
        if self.hp == self.total_hp:
          print(f"{self.name}'s hp can't go any higher!")
        elif (heal_buff + self.hp) > self.total_hp:
          self.hp = self.total_hp
          print(f"{self.name}'s hp increased!")
  if self.status != 'powered off' and j > int(hit_rate):
    print(f"{self.name} used {move_name}.")
    print(f"{self.name}'s move has missed!")

class robot:
  """general class for fighting robots"""
  def __init__(self, name, typing, total_hp, hp, attack, defense, speed, status, move1, move2, move3, move4):
    self.name = name
    self.typing = typing
    self.total_hp = total_hp
    self.hp = hp
    self.attack = attack
    self.defense = defense
    self.speed = speed
    self.status = status
    self.move1 = move1
    self.move2 = move2
    self.move3 = move3
    self.move4 = move4

def player_select(self):
  r = 0
  while r == 0:
    select_a_move = input(f"Please select a move. Your avaliable moves are {self.move1}, {self.move2}, {self.move3}, and {self.move4}. Chose one by entering 1, 2, 3, or 4.\n")
    print('')
    global player_move
    if select_a_move == '1':
      player_move = self.move1
      r = 1
    if select_a_move == '2':
      player_move = self.move2
      r = 1
    if select_a_move == '3':
      player_move = self.move3
      r = 1
    if select_a_move == '4':
      player_move = self.move4
      r = 1
    if '1' not in select_a_move and '2' not in select_a_move and '3' not in select_a_move and '4' not in select_a_move:
      print("That is not a valid input.")

def player_attack(self, enemy, player_move):
  if player_move == 'bash':
    damage_formula(self, enemy, 'bash', 50, 90, 'none', 0, 0, 0, 0)
  if player_move == 'shock':
    damage_formula(self, enemy, 'shock', 0, 75, 'shocked', 0, 0, 0, 0)
  if player_move == 'burn':
    damage_formula(self, enemy, 'burn', 0, 75, 'burned', 0, 0, 0, 0)
  if player_move == 'off-button':
    damage_formula(self, enemy, 'off-button', 0, 60, 'powered off', 0, 0, 0, 0)
  if player_move == 'bump':
    damage_formula(self, enemy, 'bump', 50, 80, 'none', 0, 0, 0, 0)
  if player_move == 'dent':
    damage_formula(self, enemy, 'dent', 60, 85, 'none', 0, 0, 0, 0)
  if player_move == 'harden':
    damage_formula(self, enemy, 'harden', 0, 90, 'none', 0, 10, 0, 0)
  if player_move == 'power-up':
    damage_formula(self, enemy, 'power-up', 0, 90, 'none', 10, 0, 0, 0)
  if player_move == 'shift-gear':
    damage_formula(self, enemy, 'shift-gear', 0, 90, 'none', 0, 0, 10, 0)
  if player_move == 'overclock':
    damage_formula(self, enemy, 'overclock', 0, 90, 'none', 10, 10, 10, 0)
  if player_move == 'heal':
    damage_formula(self, enemy, 'heal', 0, 90, 'none', 0, 0, 0, 25)

#if you want to add more moves add them here above in the player section and below in the computer section
# self, enemy, move_name, move_damage, hit_rate, condition, atk_buff, def_buff, spd_buff, heal_buff

def computer_attack(self, enemy):
  y = random.randint(0,3)
  if y == 0:
    computer_move = self.move1
  if y == 1:
    computer_move = self.move2
  if y == 2:
    computer_move = self.move3
  if y == 3:
    computer_move = self.move4
  if computer_move == 'bash':
    damage_formula(self, enemy, 'bash', 50, 90, 'none', 0, 0, 0, 0)
  if computer_move == 'shock':
    damage_formula(self, enemy, 'shock', 0, 75, 'shocked', 0, 0, 0, 0)
  if computer_move == 'burn':
    damage_formula(self, enemy, 'burn', 0, 75, 'burned', 0, 0, 0, 0)
  if computer_move == 'off-button':
    damage_formula(self, enemy, 'off-button', 0, 60, 'powered off', 0, 0, 0, 0)
  if computer_move == 'bump':
    damage_formula(self, enemy, 'bump', 35, 80, 'none', 0, 0, 0, 0)
  if computer_move == 'dent':
    damage_formula(self, enemy, 'dent', 60, 85, 'none', 0, 0, 0, 0)
  if computer_move == 'harden':
    damage_formula(self, enemy, 'harden', 0, 90, 'none', 0, 10, 0, 0)
  if computer_move == 'power-up':
    damage_formula(self, enemy, 'power-up', 0, 90, 'none', 10, 0, 0, 0)
  if computer_move == 'shift-gear':
    damage_formula(self, enemy, 'shift-gear', 0, 90, 'none', 0, 0, 10, 0)
  if computer_move == 'overclock':
    damage_formula(self, enemy, 'overclock', 0, 90, 'none', 10, 10, 10, 0)
  if computer_move == 'heal':
    damage_formula(self, enemy, 'heal', 0, 90, 'none', 0, 0, 0, 25)

def active(robot):
  if robot.hp > 0:
    return True
  if robot.hp <= 0:
    robot.hp = 0
    return False

def battle(player_robot, computer_robot):
  print(f"{computer_robot.name} has challenged you. They are a {computer_robot.typing} type.\n")
  while active(player_robot) and active(computer_robot):
    player_select(player_robot)
    if player_robot.speed > computer_robot.speed:
        player_attack(player_robot, computer_robot, player_move)
        if active(computer_robot):
          computer_attack(computer_robot, player_robot)
    if player_robot.speed == computer_robot.speed:
      z = random.randint(0,100)
      if z >= 50:
        player_attack(player_robot, computer_robot, player_move)
        if active(computer_robot):
          computer_attack(computer_robot, player_robot)
      if z < 50:
        computer_attack(computer_robot, player_robot)
        if active(player_robot):
          player_attack(player_robot, computer_robot, player_move)
    if player_robot.speed < computer_robot.speed:
      computer_attack(computer_robot, player_robot)
      if active(player_robot):
        player_attack(player_robot, computer_robot, player_move)
    if player_robot.status == 'burned':
      player_robot.hp -= 10
      print(f"{player_robot.name} has lost 10hp due to burn damage!")
    if computer_robot.status == 'burned':
      computer_robot.hp -= 10
      print(f"{computer_robot.name} has lost 10hp due to burn damage!")
    if player_robot.hp < 0:
      player_robot.hp = 0
    if computer_robot.hp < 0:
      computer_robot.hp = 0
    player_robot.hp = round(player_robot.hp)
    computer_robot.hp = round(computer_robot.hp)
    time.sleep(1)
    print(f"\nYour robot has {player_robot.hp} out of {player_robot.total_hp} hp remaining.")
    print(f"The foe has {computer_robot.hp} out of {computer_robot.total_hp} hp remaining.")
    if player_robot.status != 'none':
      print(f"Your robot is {player_robot.status}.")
    if computer_robot.status != 'none':
      print(f"The enemy robot is {computer_robot.status}.")
    print('')
  if not active(player_robot):
    print(f"{player_robot.name} has fainted. You lost.")
  if not active(computer_robot):
    print(f"{computer_robot.name} has fainted. You win.")

game_continue = 0
while game_continue == 0:
  ## below i hashed out the timers to make the code easier to test, hash them back in before release
  print('Hello! This game is called Fighting Robots. It is a text-based Pokemon-style fighting game. Please pick a bot. You will be fighting with this bot for the duration of the game.\n')
  #time.sleep(4)
  print("'Striker' is a fighter, meaning that he has increased attack.")
  #time.sleep(2)
  print("'Big Boy' is a defender, meaning that he has increased defense.")
  #time.sleep(2)
  print("'Speedy' is a speedster, meaning that he has increased speed and almost always goes first, except against other speedsters.\n")
  #time.sleep(2)
  r = 0
  while r == 0:
    player_choice = input("Please input the name of the bot you'd like to play with.\n")
    if player_choice.lower() == 'striker':
      player_robot = robot('Striker', 'fighter', 95, 95, 50, 30, 40, 'none', 'heal', 'dent', 'power-up', 'burn')
      r = 1
    if player_choice.lower() == 'big boy':
      player_robot = robot('Big Boy', 'defender', 120, 120, 30, 50, 35, 'none', 'bash', 'dent', 'harden', 'off-button')
      r = 1
    if player_choice.lower() == 'speedy':
      player_robot = robot('Speedy', 'speedster', 80, 80, 40, 30, 100, 'none', 'heal', 'dent', 'shift-gear', 'shock')
      r = 1
    if 'big boy' not in player_choice.lower() and 'speedy' not in player_choice.lower() and 'striker' not in player_choice.lower():
      print("That is not a valid input.\n")

  print(f"\nGood choice! {player_robot.name} is now yours. Your first challenger is Bottweiler. Good luck!\n")

  bottweiler = robot('Bottweiler', 'fighter', 60, 60, 20, 15, 15, 'none', 'bump', 'bump', 'shock', 'shock')
  battle(player_robot, bottweiler)
  if bottweiler.hp == 0:
    print(f"\nGood job winning that last battle. Know that {player_robot.name} will be healed inbetween each battle.")
    player_robot.hp = player_robot.total_hp
  if player_robot.hp == 0:
    print("Man, you didn't beat the tutorial bot...")
    print("Honestly I'd say it's harder to lose against Bottweiler than to win against him.")
    print("If you want to have another chance, restart and try again.")
    if player_robot.name == 'Speedy':
      print('Speedy is a little difficult to use, try picking another robot next game.')
    game_continue = 1

  ## add in some timers here to make the pacing a bit better
  print("To win the game, you will need to beat 4 bots in a row (including Bottweiler) and then the final boss.")
  print("Note: something interesting might happen before the final boss battle...\n")
  print("Three challengers remain.\n")
  print("Your next challenger is Excalibot. Good luck!")

  excalibot = robot('Excalibot', 'speedster', 80, 80, 30, 35, 70, 'none', 'bash', 'burn', 'shift-gear', 'dent')
  battle(player_robot, excalibot)

  if excalibot.hp == 0:
    print(f"\nGood job winning that last battle. Excalibot was a little tougher.")
    player_robot.hp = player_robot.total_hp
  if player_robot.hp == 0:
    print("Eh, good try. Excalibot is considerable more difficult than Bottweiler.")
    game_continue = 1

  print("Two challengers remain.\n")
  print("Your next challenger is Iron Ingbot.")

  ingbot = robot('Iron Ingbot', 'defender', 110, 110, 25, 45, 25, 'none')
  battle(player_robot, ingbot)

  if ingbot.hp == 0:
    print(f"\nGood job winning that last battle. Iron Ingbot was even stronger.")
    player_robot.hp = player_robot.total_hp
  if player_robot.hp == 0:
    print("Good try. Iron Ingbot was hard. You can always restart and try again.")
    game_continue = 1

  print("One challenger remains.\n")
  print("Your next challenger is Robosapien.")

  robosapien = robot('Robosapien', 'fighter', 110, 110, 40, 30, 30, 'none')
  battle(player_robot, robosapien)

  if robosapien.hp == 0:
    print(f"\nGood job winning that last battle. Robosapien was the last challenger.")
    player_robot.hp = player_robot.total_hp
  if player_robot.hp == 0:
    print("Good try. Robosapien was the hardest challenger so far. You can always restart and try again.")
    game_continue = 1

  print(f"\nWhat's this? {player_robot.name} is evolving!")
  if player_robot.name == 'Striker':
    print("\nStriker has evolved into Heavy Hitter!")
    player_robot = robot('Heavy Hitter', 'fighter', 150, 150, 50, 40, 35, 'none', 'overclock', 'burn', )
  if player_robot.name == 'Big Boy':
    print("\nBig Boy has evolved into Biggest Boy!")
    player_robot = robot('Biggest Boy', 'defender', 200, 200, 40, 50, 30, 'none', 'overclock', 'off-button', )
  if player_robot.name == 'Speedy':
    print("\nSpeedy has evolved into Fasty!")
    player_robot = robot('Fasty', 'speedster', 120, 120, 35, 35, 200, 'none', 'overclock', 'shock', )

  print("Since the final boss is a little more difficult than the bots you've faced so far, you will have 3 tries to beat them before the game restarts.")
  print("\nThe final boss approaches...")

  final_boss_continue = 3
  game_win = 0
  while final_boss_continue >= 1:
    count_botula = robot('Count Botula', 'boss', 200, 200, 45, 45, 120, 'none', 'overclock')
    battle(player_robot, count_botula)

    if count_botula.hp == 0:
      final_boss_continue == 0
      game_win = 1
    if player_robot.hp == 0:
      print("Aww, tough luck. This bot may take a couple tries.")
      final_boss_continue -= 1

  if game_win == 1:
    print("\nCongratulations! You win.")
  if game_win == 0:
    game_continue = 1






