import pygame
import numpy as np
import sys
import Board
TRAP = 1
FREE = 0


# creating a running loop



def ask_user():
    pygame.init()

    # creating display



    response = ''

    # creating a loop to check events that
    # are occurring
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # checking if keydown event happened or not
        if event.type == pygame.KEYDOWN:

            # checking if key "A" was pressed
            if event.key == pygame.K_UP:
                response = "up"

            if event.key == pygame.K_LEFT:
                response = "left"

            # checking if key "P" was pressed
            if event.key == pygame.K_RIGHT:
                response = "right"

            # checking if key "M" was pressed
            if event.key == pygame.K_DOWN:
                response = "down"

            if event.key == pygame.K_l:
                response = "look"
            if event.key == pygame.K_q:
                response = "exit"

    return response






class Maze:


    def __init__(self, game_map, start_position, exit_position):
        self._game_map = game_map
        self._start_position = start_position
        self._exit_position = exit_position
        self.playing = True
        self.count = 0
        self.start_holder = start_position
        self.new_game_map = np.zeros((len(self._game_map), len(self._game_map[0])))
        self.old_pos = start_position
        self.hit_wall_flag = 0


    def up(self):
        self.hit_wall_flag = 0
        if(self._start_position[0] != 0):
            self.old_pos = self._start_position
            self._start_position = (self._start_position[0] - 1, self._start_position[1])
        else:
            self.hit_wall_flag = 1
            print("You hit the wall!")

        if (self._game_map[self._start_position[0]][self._start_position[1]] == 1):
            self.trapped()



    def down(self):
        self.hit_wall_flag = 0
        if (self._start_position[0] != len(self._game_map[0])-1):
            self.old_pos = self._start_position

            self._start_position = (self._start_position[0] + 1, self._start_position[1])
        else:
            print("You hit the wall!")
            self.hit_wall_flag = 1
        if(self._game_map[self._start_position[0]][self._start_position[1]] == 1):
            self.trapped()

    def left(self):
        self.hit_wall_flag = 0
        if (self._start_position[1] != 0):
            self.old_pos = self._start_position
            self._start_position = (self._start_position[0], self._start_position[1]-1)
        else:
            print("You hit the wall!")
            self.hit_wall_flag = 1
        if(self._game_map[self._start_position[0]][self._start_position[1]] == 1):
            self.trapped()

    def right(self):
        self.hit_wall_flag = 0
        if (self._start_position[1] != len(self._game_map)-1):
            self.old_pos = self._start_position
            self._start_position = (self._start_position[0], self._start_position[1] + 1)
        else:
            print("You hit the wall!")
            self.hit_wall_flag = 1
        if(self._game_map[self._start_position[0]][self._start_position[1]] == 1):

            self.trapped()

    def trapped(self):
        print("! YOU GOT TRAPPED ")
        self.new_game_map = np.zeros((len(self._game_map), len(self._game_map[0])))
        self._start_position = self.start_holder
        self.count += 1
        print("You have been trapped ", self.count, "time(s).")

    def look(self):
        print("You can move:")
        if (self._start_position[0] != 0):
            print("up")
        if (self._start_position[0] != len(self._game_map[0]) - 1):
            print("down")
        if (self._start_position[1] != len(self._game_map) - 1):
            print("right")
        if (self._start_position[1] != 0):
            print("left")
        print(self._start_position)

    def win(self):
        if(self._start_position == self._exit_position):
            print("!!! YOU WIN !!!")
            self.count += 1
            print("You found the path in " , self.count , "fails.")




    def visualize(self):




        self.new_game_map[self._start_position[0]][self._start_position[1]] = 1
        print(self.new_game_map)
        print("  ")

    def devisualize(self):
        if(self.hit_wall_flag !=1 ):

            self.new_game_map[self.old_pos[0]][self.old_pos[1]] = 0
            print(self.new_game_map)
            print("  ")
        else:
            print(self.new_game_map)
            print("  ")

    def run(self):
        start = 0
        while self.playing:
            response = ask_user()

            if start == 0:
                print("!!! GO !!!")

                self.visualize()
                start =1

            if response == "exit":
                print("Sorry see you leaving...")
                exit()

                self.visualize()
                self.win()

            elif response == "left":
                self.left()
                if (self.new_game_map[self._start_position[0]][self._start_position[1]] == 1):
                    self.devisualize()
                else:
                    self.visualize()
                self.win()

            elif response == "right":
                self.right()
                if (self.new_game_map[self._start_position[0]][self._start_position[1]] == 1):
                    self.devisualize()
                else:
                    self.visualize()

                self.win()

            elif response == "up":
                self.up()
                if (self.new_game_map[self._start_position[0]][self._start_position[1]] == 1):
                    self.devisualize()
                else:
                    self.visualize()
                self.win()

            elif response == "down":
                self.down()
                if (self.new_game_map[self._start_position[0]][self._start_position[1]] == 1):
                    self.devisualize()
                else:
                    self.visualize()
                self.win()

            elif response == "look":
                self.look()
                self.visualize()

            #print(self._start_position) #BU KISMI SİL
            #print(self._game_map[self._start_position[0]][self._start_position[1]])




if __name__ == '__main__':









    new_map = Board.Map(size=5, exit=(3, 5)).run()


    Maze(game_map=new_map, start_position=(0, 0), exit_position=(4, 2)).run()






