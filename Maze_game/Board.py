import random

import numpy as np
import nx as nx

TRAP = 1
FREE = 0


class Map:
    def __init__(self, size,exit):
        self._map = np.ones((size,size))
        self._size = size
        self._start = (0,0)
        self._exit = (exit[0]-1,exit[1]-1)

    def check(self):
        if(self._exit[0] != self._size-1 and self._exit[1] != self._size-1):
            print("You have set a wrong exit!")
            raise ValueError("You can't exit from the middle.")






    def path_creator(self):
        self.check()
        y = self._start[0]
        x = self._start[1]
        self._map[y][x] = FREE

        times_right = self._size-1
        times_left = 0
        times_up = 0
        times_down = self._size-1



        while (x != self._exit[1] or y != self._exit[0]):
            #print("y=",y)
            #print("x=",x)

            generated_number = random.randint(0, 100)


            if (generated_number < 50 and times_down != 0):
                y += 1
                times_down -= 1
                times_up += 1
                self._map[y][x] = FREE

            if (generated_number % 10 == 1 and times_left != 0):
                x-=1
                times_left -= 1
                times_right += 1
                self._map[y][x] = FREE

            if (generated_number % 10 == 0 and times_up != 0):
                y -= 1
                times_up -= 1
                times_down += 1
                self._map[y][x] = FREE

            if (generated_number > 50 and times_right!=0):
                x+=1
                times_right -= 1
                times_left += 1
                self._map[y][x] = FREE

            else:
                continue

        return self._map





    def run(self):

        return self.path_creator()
        print(self._map)

    def exit(self):
        return self





if __name__ == '__main__':
    """x = np.zeros((5,5))
    x[3][4] = "4"
    print(x)"""

    a = Map(size=5, exit=(5,5)).run()

    print(type(a), a)


