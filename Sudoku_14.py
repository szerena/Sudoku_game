import random
import sys
import os
import time


def p_map():      
  print_map = (  "\033[35m   Position for example:01,02,34,56,47,28,....\n"
                 "\033[36m           Type 'EXIT' to exit\n"
                 " \n"
                 "     \033[33m     S  E  C  O  N  D\n"
                 "       \033[33m0 1 2   3 4 5   6 7 8\n"
                  "    0 |\033[31m" + str(map_hard[0][0]) + "\033[39m \033[32m" + str(map_hard[0][1]) + " " + str(map_hard[0][2]) +"\033[33m | \033[32m" + str(map_hard[0][3]) + " " + str(map_hard[0][4]) + " " + str(map_hard[0][5]) + "\033[33m | \033[31m" + str(map_hard[0][6]) + "\033[39m \033[32m" + str(map_hard[0][7]) + " " + str(map_hard[0][8]) + "\033[33m | \n"
                  " F  1 |\033[32m" + str(map_hard[1][0]) + " \033[31m" + str(map_hard[1][1]) + "\033[32m " + str(map_hard[1][2]) +"\033[33m | \033[32m" + str(map_hard[1][3]) + " " + str(map_hard[1][4]) + " " + str(map_hard[1][5]) + "\033[33m | \033[32m" + str(map_hard[1][6]) + " " + str(map_hard[1][7]) + " " + str(map_hard[1][8]) + "\033[33m | \n"
                  "    2 |\033[32m" + str(map_hard[2][0]) + " " + str(map_hard[2][1]) + " " + str(map_hard[2][2]) +"\033[33m | \033[31m" + str(map_hard[2][3]) + "\033[39m \033[32m" + str(map_hard[2][4]) + " " + str(map_hard[2][5]) + "\033[33m | \033[32m" + str(map_hard[2][6]) + " " + str(map_hard[2][7]) + " " + str(map_hard[2][8]) + "\033[33m | \n"
                  " I    |------+-------+-------|\n"
                  "    3 |\033[32m" + str(map_hard[3][0]) + " \033[31m" + str(map_hard[3][1]) + "\033[39m \033[32m" + str(map_hard[3][2]) +"\033[33m | \033[32m" + str(map_hard[3][3]) + " " + str(map_hard[3][4]) + " " + str(map_hard[3][5]) + "\033[33m | \033[32m" + str(map_hard[3][6]) + " \033[31m" + str(map_hard[3][7]) + "\033[39m \033[32m" + str(map_hard[3][8]) + "\033[33m | \n"
                  " R  4 |\033[32m" + str(map_hard[4][0]) + " " + str(map_hard[4][1]) + " " + str(map_hard[4][2]) +"\033[33m | \033[32m" + str(map_hard[4][3]) + " \033[31m" + str(map_hard[4][4]) + "\033[39m \033[32m" + str(map_hard[4][5]) + "\033[33m | \033[31m" + str(map_hard[4][6]) + "\033[39m \033[32m" + str(map_hard[4][7]) + " " + str(map_hard[4][8]) + "\033[33m | \n"
                  "    5 |\033[32m" + str(map_hard[5][0]) + " " + str(map_hard[5][1]) + " " + str(map_hard[5][2]) +"\033[33m | \033[32m" + str(map_hard[5][3]) + " \033[31m" + str(map_hard[5][4]) + "\033[32m " + str(map_hard[5][5]) + "\033[33m | \033[32m" + str(map_hard[5][6]) + " " + str(map_hard[5][7]) + " " + str(map_hard[5][8]) + "\033[33m | \n"
                  " S    |------+-------+-------|\n"
                  "    6 |\033[32m" + str(map_hard[6][0]) + " " + str(map_hard[6][1]) + " " + str(map_hard[6][2]) +"\033[33m | \033[31m" + str(map_hard[6][3]) + "\033[32m " + str(map_hard[6][4]) + " \033[31m" + str(map_hard[6][5]) + "\033[33m | \033[32m" + str(map_hard[6][6]) + " \033[31m" + str(map_hard[6][7]) + "\033[32m " + str(map_hard[6][8]) + "\033[33m | \n"
                  " T  7 |\033[31m" + str(map_hard[7][0]) + "\033[32m " + str(map_hard[7][1]) + " " + str(map_hard[7][2]) +"\033[33m | \033[31m" + str(map_hard[7][3]) + "\033[32m " + str(map_hard[7][4]) + " " + str(map_hard[7][5]) + "\033[33m | \033[32m" + str(map_hard[7][6]) + " " + str(map_hard[7][7]) + " " + str(map_hard[7][8]) + "\033[33m | \n"
                  "    8 |\033[31m" + str(map_hard[8][0]) + "\033[32m " + str(map_hard[8][1]) + " \033[31m" + str(map_hard[8][2]) +"\033[33m | \033[32m" + str(map_hard[8][3]) + " " + str(map_hard[8][4]) + " " + str(map_hard[8][5]) + "\033[33m | \033[32m" + str(map_hard[8][6]) + " " + str(map_hard[8][7]) + " " + str(map_hard[8][8]) + "\033[33m |\033[39m \n")
  print(print_map)


def p_full_map_hard():
  print_full_map_hard = (   "     \033[31m 0 1 2   3 4 5   6 7 8\n"
                      "   0 |" + str(full_map_hard[0][0]) + " " + str(full_map_hard[0][1]) + " " + str(full_map_hard[0][2]) +" | " + str(full_map_hard[0][3]) + " " + str(full_map_hard[0][4]) + " " + str(full_map_hard[0][5]) + " | " + str(full_map_hard[0][6]) + " " + str(full_map_hard[0][7]) + " " + str(full_map_hard[0][8]) + " | \n"
                      "   1 |" + str(full_map_hard[1][0]) + " " + str(full_map_hard[1][1]) + " " + str(full_map_hard[1][2]) +" | " + str(full_map_hard[1][3]) + " " + str(full_map_hard[1][4]) + " " + str(full_map_hard[1][5]) + " | " + str(full_map_hard[1][6]) + " " + str(full_map_hard[1][7]) + " " + str(full_map_hard[1][8]) + " | \n"
                      "   2 |" + str(full_map_hard[2][0]) + " " + str(full_map_hard[2][1]) + " " + str(full_map_hard[2][2]) +" | " + str(full_map_hard[2][3]) + " " + str(full_map_hard[2][4]) + " " + str(full_map_hard[2][5]) + " | " + str(full_map_hard[2][6]) + " " + str(full_map_hard[2][7]) + " " + str(full_map_hard[2][8]) + " | \n"
                      "     |------+-------+-------|\n"
                      "   3 |" + str(full_map_hard[3][0]) + " " + str(full_map_hard[3][1]) + " " + str(full_map_hard[3][2]) +" | " + str(full_map_hard[3][3]) + " " + str(full_map_hard[3][4]) + " " + str(full_map_hard[3][5]) + " | " + str(full_map_hard[3][6]) + " " + str(full_map_hard[3][7]) + " " + str(full_map_hard[3][8]) + " | \n"
                      "   4 |" + str(full_map_hard[4][0]) + " " + str(full_map_hard[4][1]) + " " + str(full_map_hard[4][2]) +" | " + str(full_map_hard[4][3]) + " " + str(full_map_hard[4][4]) + " " + str(full_map_hard[4][5]) + " | " + str(full_map_hard[4][6]) + " " + str(full_map_hard[4][7]) + " " + str(full_map_hard[4][8]) + " | \n"
                      "   5 |" + str(full_map_hard[5][0]) + " " + str(full_map_hard[5][1]) + " " + str(full_map_hard[5][2]) +" | " + str(full_map_hard[5][3]) + " " + str(full_map_hard[5][4]) + " " + str(full_map_hard[5][5]) + " | " + str(full_map_hard[5][6]) + " " + str(full_map_hard[5][7]) + " " + str(full_map_hard[5][8]) + " | \n"
                      "     |------+-------+-------|\n"
                      "   6 |" + str(full_map_hard[6][0]) + " " + str(full_map_hard[6][1]) + " " + str(full_map_hard[6][2]) +" | " + str(full_map_hard[6][3]) + " " + str(full_map_hard[6][4]) + " " + str(full_map_hard[6][5]) + " | " + str(full_map_hard[6][6]) + " " + str(full_map_hard[6][7]) + " " + str(full_map_hard[6][8]) + " | \n"
                      "   7 |" + str(full_map_hard[7][0]) + " " + str(full_map_hard[7][1]) + " " + str(full_map_hard[7][2]) +" | " + str(full_map_hard[7][3]) + " " + str(full_map_hard[7][4]) + " " + str(full_map_hard[7][5]) + " | " + str(full_map_hard[7][6]) + " " + str(full_map_hard[7][7]) + " " + str(full_map_hard[7][8]) + " | \n"
                      "   8 |" + str(full_map_hard[8][0]) + " " + str(full_map_hard[8][1]) + " " + str(full_map_hard[8][2]) +" | " + str(full_map_hard[8][3]) + " " + str(full_map_hard[8][4]) + " " + str(full_map_hard[8][5]) + " | " + str(full_map_hard[8][6]) + " " + str(full_map_hard[8][7]) + " " + str(full_map_hard[8][8]) + " |\033[31m \n")
  print(print_full_map_hard)

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
map_hard = [[4,0,0,0,0,0,8,0,0],
       [0,3,0,0,0,0,0,0,0],
       [0,0,0,7,0,0,0,0,0],
       [0,2,0,0,0,0,0,6,0],
       [0,0,0,0,8,0,4,0,0],
       [0,0,0,0,1,0,0,0,0],
       [0,0,0,6,0,3,0,7,0],
       [5,0,0,2,0,0,0,0,0],
       [1,0,4,0,0,0,0,0,0]]

#full_numbers_list
full_map_hard = [[4,1,7,3,6,9,8,2,5],
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

logo()


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
      player_numbers = ["1","2","3","4","5","6","7","8","9"]
      player_position = ["00","01","02","03","04","05","06","07","08","10","11","12","13","14","15","16","17","18","20","21","22","23","24","25","26","27","28","30","31","32","33","34","35","36","37","38","40","41","42","43","44","45","46","47","48","50","51","52","53","54","55","56","57","58","60","61","62","63","64","65","66","67","68","70","71","72","73","74","75","76","77","78","80","81","82","83","84","85","86","87","88"]
  
      #CHEAT
      if player_input_position == "CHEAT":   
   
        for i in range(2):
          for color in range(31, 37):
            os.system("clear")
            p_full_map_hard()
            print("\033[" + str(color) + "m          WELL PLAYED!\033[39m")
            time.sleep(1)
        os.system("clear")
        p_full_map_hard()
    


 
    #Position_change_number
    for x in player_position:
      if player_input_position == x:
        player_input_number = input("what's Your Number?")
        for y in player_numbers:
          if player_input_number == y:
            c = int(x[0])
            b = int(x[1])
            map_hard[c][b] = y       
            p_map()


def main():
  version = input("Choose level '1' or '2'")
  if version == "1":
    main_game()#hARD
  #elif version == "2":
    #version2 = #EASY


if __name__ == "__main__":
    main()