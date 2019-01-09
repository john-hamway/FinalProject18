import random

## fighters have increased attack
## speedsters always go first
## defenders have increased defense
## specials can make the opponent poisoned (so they take x damage per turn)
## right now the idea is that typing shouldn't have any effect (so dont write if typing = whatever), instead typings just indicate which bots have higher stats in a certain area

## you need to create an introduction stating what the game is and listing the stats of the bots that the player has to choose from
## players will control only one bot (not a team) but after successful battle your bot will increase in level by 1, when it reaches a certain point it will evolve and all of its stats will increase

## create a plan for the different rooms that the player will go through on paper ----done this class
## there might be a problem with the damage function if a robot's defense is greater than the possible damage that another robot can do
## fried circuit is burn
class robot:
  """general class for fighting robots"""
  def __init__(self, name, typing, health, attack, defense, speed, status):
    self.name = name
    self.health = health
    self.attack = attack
    self.defense = defense
    self.typing = typing
    self.status = status

    def attack(self, enemy, move_damage, hit_rate):
        if self.status = shocked:
            hit_rate -= 10
        x = random.randint(0,100)
        move_hit = True
        if x < hit_rate:
            move_hit = False
            if self.status = shocked
                print("You're shocked. Your move missed.")
            else:
                print("Your move missed.")
        if move_hit != False:
            actual_damage = (move_damage + self.attack) / enemy.defense
def active(robot):
    if robot.health > 0:
        return True
    if robot.health <= 0:
        robot.health = 0
        return False

def battle(player1, player2):
    condition1, condition2 = True, True
    while condition1 and condition2:
        while not active(robot1):
            print(f"{robot1.name}, 'is out of battle. Choose another pokemon")
            robot1 = eval(input())
        robot2 = random.choice(player2.robot)
        while not active(robot2):
            robot2 = random.choice(player2.robot)
        print(player1.name, 'chose', robot1.name, '\n', player2.name, 'chose', robot2.name)
        while active(robot1) and active(robot2):
            pokemon1.attack(robot2)
            if active(robot2):
                robot2.attack(robot1)
            print(robot1.name, 1.hp)
            print(robot2.name, pokemon2.hp)
        print (player1.robot[0].name, player1.robot[0].health) #here its returning the original hp
        print (player2.robot[0].name, player2.robot[0].health) #here its returning the current hp, as it should
        if not any(active(robot) for robot in player1.robot):
            condition1 = False
        if not any(active(robot) for robot in player2.robot):
            condition2 = False






