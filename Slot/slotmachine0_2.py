# Source File Name: slotmachine0_2.py
# Author's Name: Aldrin Jerome Almacin
# Last Modified By: Aldrin Jerome Almacin
# Date Last Modified:
"""
  Program Description:  This program simulates a Casino-Style Slot Machine. It provides an GUI
                        for the user that is an image of a slot machine with Label and Button objects
                        created through the tkinter module
  Version: 0.2: Slot machine console game
"""

# import statements
import random
import pygame

def main():
  pygame.init()
  slot_machine = SlotMachine(500, 1000)
  slot_machine.start_game()

class SlotMachine:
  def __init__(self, starting_jackpot, starting_cash):
    self.POSSIBLE_BETS = "10, 20, 50, 100"
    self.icons = []
    self.__create_icons()
    self.JACKPOT_INCREASE_RATE = .15
    self.FRAME_RATE = 60

    self.starting_jackpot = starting_jackpot
    self.starting_cash = starting_cash

    self.set_initial_values()

  def set_initial_values(self):
    self.current_jackpot = self.starting_jackpot
    self.current_cash = self.starting_cash
    self.results = 3*[""]
    self.turns = 0
    self.bet = 10
    self.wins = 0
    self.loses = 0

  def __create_icons(self):
    self.icons.append(Icon("Blank", 0, 0, "sadface.png", bonus_win_rate = 2))
    self.icons.append(Icon("Grapes", 20, 2, "katipunero_hat.png"))
    self.icons.append(Icon("Banana", 30, 2, "bandana.png"))
    self.icons.append(Icon("Orange", 40, 3, "camesa_de_chino.png"))
    self.icons.append(Icon("Cherry", 100, 4, "banyal.png"))
    self.icons.append(Icon("Bar", 200, 5, "tsinelas.png"))
    self.icons.append(Icon("Bell", 300, 10, "arnis.png"))
    self.icons.append(Icon("Seven", 1000, 20, "seven.png", bonus_win_rate = 10))

  def start_game(self):
    # Assign the Display Variables
    background = pygame.image.load("./images/background.png")

    background_rect = background.get_rect()
    screen = pygame.display.set_mode(background.get_size())
    pygame.display.set_caption("Slot Machine")

    # Set the frame rate
    clock = pygame.time.Clock()

    # Start the game Loop
    continue_playing = True
    while (continue_playing):
      clock.tick(self.FRAME_RATE)

      # Events
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          continue_playing = False

      # Refresh the display
      screen.blit(background, background_rect)
      pygame.display.flip()

  def set_bet(self):
    bet_selected = -1
    while True:
      print("How much would you bet?")
      print(self.POSSIBLE_BETS)
      bet_selected = input(">>> ")
      if (bet_selected in self.POSSIBLE_BETS.split(", ")):
        break
      else:
        print("Invalid bet value!")
    self.bet = int(bet_selected)

  def spin(self):
    self.__pay()
    self.__increase_jackpot()

    for spin in range(3):
      spinned_result = random.randint(0, 100)

      if spinned_result in range(0, 40):
          self.results[spin] = self.icons[0].name
      elif spinned_result in range(40, 56):
          self.results[spin] = self.icons[1].name
      elif spinned_result in range(56, 70):
          self.results[spin] = self.icons[2].name
      elif spinned_result in range(70, 82):
          self.results[spin] = self.icons[3].name
      elif spinned_result in range(82, 89):
          self.results[spin] = self.icons[4].name
      elif spinned_result in range(89, 95):
          self.results[spin] = self.icons[5].name
      elif spinned_result in range(95, 99):
          self.results[spin] = self.icons[6].name
      elif spinned_result in range(99, 100):
          self.results[spin] = self.icons[7].name

    self.__check_results()

  def __pay(self):
    self.current_cash -= self.bet

  def __increase_jackpot(self):
    self.current_jackpot += (int(self.bet * self.JACKPOT_INCREASE_RATE))

  def __check_results(self):
    win = False
    for icon in self.icons:
      if self.results.count(icon.name) == 3:
        self.current_cash += self.bet * icon.win_rate_full
        win = True
      if self.results.count(icon.name) == 2:
        self.current_cash += self.bet * icon.win_rate_two
        win = True
    if self.results.count(self.icons[0].name) == 0 and not win:
      self.current_cash += self.bet * self.icons[0].bonus_win_rate
    if self.results.count(self.icons[7].name) == 1 and not win:
      self.current_cash += self.bet * self.icons[7].bonus_win_rate

    #TODO Jackpot

    print(self.results)
    print("Cash"),
    print(self.current_cash)
    print("Bet"),
    print(self.bet)

  def reset(self):
    self.set_initial_values()

class Icon:
  def __init__(self, name, win_rate_full, win_rate_two, icon_image, bonus_win_rate = 0):
    self.name = name
    self.win_rate_full = win_rate_full
    self.win_rate_two = win_rate_two
    self.bonus_win_rate = bonus_win_rate

  def get_win_rate_full(self):
    return self.win_rate_full

  def get_win_rate_two(self):
    return self.win_rate_two

  def get_bonus_win_rate(self):
    return self.bonus_win_rate

  def get_name(self):
    return self.name

  def get_image(self):
    return self.icon_image

if __name__ == "__main__": main()
