import random
import sys
import os
import time


def p_map():      
  print_map = (  "\033[35m   Position for example:A1,B1,A2,C2,E7,C8,....\n"
                 "\033[36m           Type 'EXIT' to exit\n"
                 " \n"
                 "      \033[33mA B C   D E F   G H I\n"
                  "   1 |\033[31m" + str(mapp[0][0]) + "\033[39m \033[32m" + str(mapp[0][1]) + " " + str(mapp[0][2]) +"\033[33m | \033[32m" + str(mapp[0][3]) + " " + str(mapp[0][4]) + " " + str(mapp[0][5]) + "\033[33m | \033[31m" + str(mapp[0][6]) + "\033[39m \033[32m" + str(mapp[0][7]) + " " + str(mapp[0][8]) + "\033[33m | \n"
                  "   2 |\033[32m" + str(mapp[1][0]) + " \033[31m" + str(mapp[1][1]) + "\033[32m " + str(mapp[1][2]) +"\033[33m | \033[32m" + str(mapp[1][3]) + " " + str(mapp[1][4]) + " " + str(mapp[1][5]) + "\033[33m | \033[32m" + str(mapp[1][6]) + " " + str(mapp[1][7]) + " " + str(mapp[1][8]) + "\033[33m | \n"
                  "   3 |\033[32m" + str(mapp[2][0]) + " " + str(mapp[2][1]) + " " + str(mapp[2][2]) +"\033[33m | \033[31m" + str(mapp[2][3]) + "\033[39m \033[32m" + str(mapp[2][4]) + " " + str(mapp[2][5]) + "\033[33m | \033[32m" + str(mapp[2][6]) + " " + str(mapp[2][7]) + " " + str(mapp[2][8]) + "\033[33m | \n"
                  "     |------+-------+-------|\n"
                  "   4 |\033[32m" + str(mapp[3][0]) + " \033[31m" + str(mapp[3][1]) + "\033[39m \033[32m" + str(mapp[3][2]) +"\033[33m | \033[32m" + str(mapp[3][3]) + " " + str(mapp[3][4]) + " " + str(mapp[3][5]) + "\033[33m | \033[32m" + str(mapp[3][6]) + " \033[31m" + str(mapp[3][7]) + "\033[39m \033[32m" + str(mapp[3][8]) + "\033[33m | \n"
                  "   5 |\033[32m" + str(mapp[4][0]) + " " + str(mapp[4][1]) + " " + str(mapp[4][2]) +"\033[33m | \033[32m" + str(mapp[4][3]) + " \033[31m" + str(mapp[4][4]) + "\033[39m \033[32m" + str(mapp[4][5]) + "\033[33m | \033[31m" + str(mapp[4][6]) + "\033[39m \033[32m" + str(mapp[4][7]) + " " + str(mapp[4][8]) + "\033[33m | \n"
                  "   6 |\033[32m" + str(mapp[5][0]) + " " + str(mapp[5][1]) + " " + str(mapp[5][2]) +"\033[33m | \033[32m" + str(mapp[5][3]) + " \033[31m" + str(mapp[5][4]) + "\033[32m " + str(mapp[5][5]) + "\033[33m | \033[32m" + str(mapp[5][6]) + " " + str(mapp[5][7]) + " " + str(mapp[5][8]) + "\033[33m | \n"
                  "     |------+-------+-------|\n"
                  "   7 |\033[32m" + str(mapp[6][0]) + " " + str(mapp[6][1]) + " " + str(mapp[6][2]) +"\033[33m | \033[31m" + str(mapp[6][3]) + "\033[32m " + str(mapp[6][4]) + " \033[31m" + str(mapp[6][5]) + "\033[33m | \033[32m" + str(mapp[6][6]) + " \033[31m" + str(mapp[6][7]) + "\033[32m " + str(mapp[6][8]) + "\033[33m | \n"
                  "   8 |\033[31m" + str(mapp[7][0]) + "\033[32m " + str(mapp[7][1]) + " " + str(mapp[7][2]) +"\033[33m | \033[31m" + str(mapp[7][3]) + "\033[32m " + str(mapp[7][4]) + " " + str(mapp[7][5]) + "\033[33m | \033[32m" + str(mapp[7][6]) + " " + str(mapp[7][7]) + " " + str(mapp[7][8]) + "\033[33m | \n"
                  "   9 |\033[31m" + str(mapp[8][0]) + "\033[32m " + str(mapp[8][1]) + " \033[31m" + str(mapp[8][2]) +"\033[33m | \033[32m" + str(mapp[8][3]) + " " + str(mapp[8][4]) + " " + str(mapp[8][5]) + "\033[33m | \033[32m" + str(mapp[8][6]) + " " + str(mapp[8][7]) + " " + str(mapp[8][8]) + "\033[33m |\033[39m \n")
  print(print_map)


def p_full_map():
  print_full_map = (   "     \033[31m A B C   D E F   G H I\n"
                      "   1 |" + str(full_map[0][0]) + " " + str(full_map[0][1]) + " " + str(full_map[0][2]) +" | " + str(full_map[0][3]) + " " + str(full_map[0][4]) + " " + str(full_map[0][5]) + " | " + str(full_map[0][6]) + " " + str(full_map[0][7]) + " " + str(full_map[0][8]) + " | \n"
                      "   2 |" + str(full_map[1][0]) + " " + str(full_map[1][1]) + " " + str(full_map[1][2]) +" | " + str(full_map[1][3]) + " " + str(full_map[1][4]) + " " + str(full_map[1][5]) + " | " + str(full_map[1][6]) + " " + str(full_map[1][7]) + " " + str(full_map[1][8]) + " | \n"
                      "   3 |" + str(full_map[2][0]) + " " + str(full_map[2][1]) + " " + str(full_map[2][2]) +" | " + str(full_map[2][3]) + " " + str(full_map[2][4]) + " " + str(full_map[2][5]) + " | " + str(full_map[2][6]) + " " + str(full_map[2][7]) + " " + str(full_map[2][8]) + " | \n"
                      "     |------+-------+-------|\n"
                      "   4 |" + str(full_map[3][0]) + " " + str(full_map[3][1]) + " " + str(full_map[3][2]) +" | " + str(full_map[3][3]) + " " + str(full_map[3][4]) + " " + str(full_map[3][5]) + " | " + str(full_map[3][6]) + " " + str(full_map[3][7]) + " " + str(full_map[3][8]) + " | \n"
                      "   5 |" + str(full_map[4][0]) + " " + str(full_map[4][1]) + " " + str(full_map[4][2]) +" | " + str(full_map[4][3]) + " " + str(full_map[4][4]) + " " + str(full_map[4][5]) + " | " + str(full_map[4][6]) + " " + str(full_map[4][7]) + " " + str(full_map[4][8]) + " | \n"
                      "   6 |" + str(full_map[5][0]) + " " + str(full_map[5][1]) + " " + str(full_map[5][2]) +" | " + str(full_map[5][3]) + " " + str(full_map[5][4]) + " " + str(full_map[5][5]) + " | " + str(full_map[5][6]) + " " + str(full_map[5][7]) + " " + str(full_map[5][8]) + " | \n"
                      "     |------+-------+-------|\n"
                      "   7 |" + str(full_map[6][0]) + " " + str(full_map[6][1]) + " " + str(full_map[6][2]) +" | " + str(full_map[6][3]) + " " + str(full_map[6][4]) + " " + str(full_map[6][5]) + " | " + str(full_map[6][6]) + " " + str(full_map[6][7]) + " " + str(full_map[6][8]) + " | \n"
                      "   8 |" + str(full_map[7][0]) + " " + str(full_map[7][1]) + " " + str(full_map[7][2]) +" | " + str(full_map[7][3]) + " " + str(full_map[7][4]) + " " + str(full_map[7][5]) + " | " + str(full_map[7][6]) + " " + str(full_map[7][7]) + " " + str(full_map[7][8]) + " | \n"
                      "   9 |" + str(full_map[8][0]) + " " + str(full_map[8][1]) + " " + str(full_map[8][2]) +" | " + str(full_map[8][3]) + " " + str(full_map[8][4]) + " " + str(full_map[8][5]) + " | " + str(full_map[8][6]) + " " + str(full_map[8][7]) + " " + str(full_map[8][8]) + " |\033[31m \n")
  print(print_full_map)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#empty_numbers_list
mapp = [[4,0,0,0,0,0,8,0,0],
       [0,3,0,0,0,0,0,0,0],
       [0,0,0,7,0,0,0,0,0],
       [0,2,0,0,0,0,0,6,0],
       [0,0,0,0,8,0,4,0,0],
       [0,0,0,0,1,0,0,0,0],
       [0,0,0,6,0,3,0,7,0],
       [5,0,0,2,0,0,0,0,0],
       [1,0,4,0,0,0,0,0,0]]

#full_numbers_list
full_map = [[4,1,7,3,6,9,8,2,5],
            [6,3,2,1,5,8,9,4,7],
            [9,5,8,7,2,4,3,1,6],
            [8,2,5,4,3,7,1,6,9],
            [7,9,1,5,8,6,4,3,2],
            [3,4,6,9,1,2,7,5,8],
            [2,8,9,6,4,3,5,7,1],
            [5,7,3,2,9,1,6,8,4],
            [1,6,4,8,7,5,2,9,3]]

#Logo
def logo():
  sud="""

          _____           _       _          
          /  ___|         | |     | |         
          \ `--. _   _  __| | ___ | | ___   _ 
          `--.   \| | |/ _` |/ _ \| |/ / | | |
          /\__/ / |_| | (_| | (_) |   <| |_| |
          \____/ \__,_|\__,_|\___/|_|\_\\__,_ |
                                              """

  print ("\033[93m" + (sud) 
        )

#Start

def start_game():
  logo()


  name = input (bcolors.OKBLUE + "         Enter your name: " + bcolors.ENDC)
  if name == "":
      print (bcolors.OKGREEN + "          Welcome " +  str(name) + " to Sudoku game!" + bcolors.ENDC)
  else:
      welcome = bcolors.OKGREEN +  "          Welcome " +  str(name) + " to Sudoku game!" + bcolors.ENDC
      for i in range(len(welcome)):
        print(welcome[:i])
        time.sleep(0.2)
        os.system("clear")
        logo()
      print(welcome)
      #time.sleep(1)
  

  welcome = bcolors.OKGREEN +  "          Welcome " +  str(name) + " to Sudoku game!" + bcolors.ENDC

  press = bcolors.OKGREEN +  "                 Press enter to start a new game" + bcolors.ENDC
  for i in range(len(press)):
    print(welcome)
    print(press[:i])
    time.sleep(0.2)
    os.system("clear")
    logo()
  print(welcome)
  print(press)
  #time.sleep(1)szerena
  while True:
      i = input(" ")
      if not i:
          break

  #choose level

   

def main_game():
    start_game()
    name = " anonymous "
    #main_function
    while True:
      os.system("clear")
      p_map()
      player_input_position = input("Position:")
      player_numbers = [1,2,3,4,5,6,7,8,9]
      player_position = ["A1","B1","C1","D1","E1","F1","G1","H1","I1","A2","B2","C2","D2","E2","F2","G2","H2","I2","A3","B3","C3","D3","E3","F3","G3","H3","I3","A4","B4","C4","D4","E4","F4","G4","H4","I4","A5","B5","C5","D5","E5","F5","G5","H5","I5","A6","B6","C6","D6","E6","F6","G6","H6","I6","A7","B7","C7","D7","E7","F7","G7","H7","I7","A8","B8","C8","D8","E8","F8","G8","H8","I8"]

    
      #CHEAT
      if player_input_position == "CHEAT":   
      
        for i in range(2):
          for color in range(31, 37):
            os.system("clear")
            p_full_map()
            print("\033[" + str(color) + "m          WELL PLAYED!\033[39m")
            time.sleep(1)
        os.system("clear")
        p_full_map()


      #Position_change_number
      elif player_input_position == "B1":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[0][1] = str(player_numbers[y])
            p_map()
      elif player_input_position == "C1":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[0][2] = str(player_numbers[y])
            p_map()
      elif player_input_position == "D1":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[0][3] = str(player_numbers[y])
            p_map()
      elif player_input_position == "E1":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[0][4] = str(player_numbers[y])
            p_map()
      elif player_input_position == "F1":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[0][5] = str(player_numbers[y])
            p_map()
      elif player_input_position == "H1":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[0][7] = str(player_numbers[y])
            p_map()
      elif player_input_position == "I1":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[0][8] = str(player_numbers[y])
            p_map()
      elif player_input_position == "A2":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[1][0] = str(player_numbers[y])
            p_map()
      elif player_input_position == "C2":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[1][2] = str(player_numbers[y])
            p_map()
      elif player_input_position == "D2":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[1][3] = str(player_numbers[y])
            p_map()
      elif player_input_position == "E2":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[1][4] = str(player_numbers[y])
            p_map()
      elif player_input_position == "F2":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[1][5] = str(player_numbers[y])
            p_map()
      elif player_input_position == "G2":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[1][6] = str(player_numbers[y])
            p_map()
      elif player_input_position == "H2":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[1][7] = str(player_numbers[y])
            p_map()
      elif player_input_position == "I2":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[1][8] = str(player_numbers[y])
            p_map()
      elif player_input_position == "A3":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[2][0] = str(player_numbers[y])
            p_map()
      elif player_input_position == "B3":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[2][1] = str(player_numbers[y])
            p_map()
      elif player_input_position == "C3":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[2][2] = str(player_numbers[y])
            p_map()
      elif player_input_position == "E3":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[2][4] = str(player_numbers[y])
            p_map()
      elif player_input_position == "F3":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[2][5] = str(player_numbers[y])
            p_map()
      elif player_input_position == "G3":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[2][6] = str(player_numbers[y])
            p_map()
      elif player_input_position == "H3":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[2][7] = str(player_numbers[y])
            p_map()
      elif player_input_position == "I3":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[2][8] = str(player_numbers[y])
            p_map()
      elif player_input_position == "A4":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[3][0] = str(player_numbers[y])
            p_map()
      elif player_input_position == "C4":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[3][2] = str(player_numbers[y])
            p_map()
      elif player_input_position == "D4":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[3][3] = str(player_numbers[y])
            p_map()
      elif player_input_position == "E4":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[3][4] = str(player_numbers[y])
            p_map()
      elif player_input_position == "F4":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[3][5] = str(player_numbers[y])
            p_map()
      elif player_input_position == "G4":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[3][6] = str(player_numbers[y])
            p_map()
      elif player_input_position == "I4":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[3][8] = str(player_numbers[y])
            p_map()
      elif player_input_position == "A5":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[4][0] = str(player_numbers[y])
            p_map()
      elif player_input_position == "B5":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[4][1] = str(player_numbers[y])
            p_map()
      elif player_input_position == "C5":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[4][2] = str(player_numbers[y])
            p_map()
      elif player_input_position == "D5":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[4][3] = str(player_numbers[y])
            p_map()
      elif player_input_position == "F5":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[4][5] = str(player_numbers[y])
            p_map()
      elif player_input_position == "H5":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[4][7] = str(player_numbers[y])
            p_map()
      elif player_input_position == "I5":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[4][8] = str(player_numbers[y])
            p_map()
      elif player_input_position == "A6":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[5][0] = str(player_numbers[y])
            p_map()
      elif player_input_position == "B6":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[5][1] = str(player_numbers[y])
            p_map()
      elif player_input_position == "C6":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[5][2] = str(player_numbers[y])
            p_map()
      elif player_input_position == "D6":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[5][3] = str(player_numbers[y])
            p_map()
      elif player_input_position == "F6":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[5][5] = str(player_numbers[y])
            p_map()
      elif player_input_position == "G6":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[5][6] = str(player_numbers[y])
            p_map()
      elif player_input_position == "H6":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[5][7] = str(player_numbers[y])
            p_map()
      elif player_input_position == "I6":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[5][8] = str(player_numbers[y])
            p_map()
      elif player_input_position == "A7":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[6][0] = str(player_numbers[y])
            p_map()
      elif player_input_position == "B7":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[6][1] = str(player_numbers[y])
            p_map()
      elif player_input_position == "C7":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[6][2] = str(player_numbers[y])
            p_map()
      elif player_input_position == "E7":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[6][4] = str(player_numbers[y])
            p_map()
      elif player_input_position == "G7":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[6][6] = str(player_numbers[y])
            p_map()
      elif player_input_position == "I7":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[6][8] = str(player_numbers[y])
            p_map()
      elif player_input_position == "B8":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[7][1] = str(player_numbers[y])
            p_map()
      elif player_input_position == "C8":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[7][2] = str(player_numbers[y])
            p_map()
      elif player_input_position == "E8":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[7][4] = str(player_numbers[y])
            p_map()
      elif player_input_position == "F8":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[7][5] = str(player_numbers[y])
            p_map()
      elif player_input_position == "G8":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[7][6] = str(player_numbers[y])
            p_map()
      elif player_input_position == "H8":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[7][7] = str(player_numbers[y])
            p_map()
      elif player_input_position == "I8":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[7][8] = str(player_numbers[y])
            p_map()
      elif player_input_position == "B9":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[8][1] = str(player_numbers[y])
            p_map()
      elif player_input_position == "D9":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[8][3] = str(player_numbers[y])
            p_map()
      elif player_input_position == "E9":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[8][4] = str(player_numbers[y])
            p_map()
      elif player_input_position == "F9":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[8][5] = str(player_numbers[y])
            p_map()
      elif player_input_position == "G9":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[8][6] = str(player_numbers[y])
            p_map()
      elif player_input_position == "H9":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[8][7] = str(player_numbers[y])
            p_map()
      elif player_input_position == "I9":    
        player_input_number = input("What's your number?")
        for y in range(0,9):
          if player_input_number == str(player_numbers[y]):
            mapp[8][8] = str(player_numbers[y])
            p_map()
      elif player_input_position == "EXIT":
        break  
      else:
        print("\033[31mWrong Position! :(\033[39m")
        time.sleep(2)
    return None




def main():
  version = input("Choose level '1' or '2'")
  if version == "1":
    main_game()#hARD
  #elif version == "2":
    #version2 = #EASY


if __name__ == "__main__":
    main()
