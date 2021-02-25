from game import LaunchpadMk2
import atexit
import os
import random


def on_exit():
    os.system(f"python {os.getcwd()}/startMk2.py")


class Game:
    def __init__(self):
        self.n = int(input("Please choose a number of wrong pads: "))
        self.lp = LaunchpadMk2.LaunchpadMk2()
        self.lp.Reset()
        self.lp.register_on_button_press(on_button=self.on_button_press)
        self.wrong = []
        self.pres = []
        self.isDead = False
        self.start_game()

    def start_game(self):
        self.lp.LedAllOn(colorcode=self.lp.COLORS["green"])
        for i in range(self.n):
            x = (random.randint(0, 7), random.randint(1, 8))
            while x in self.wrong:
                x = (random.randint(0, 7), random.randint(1, 8))
            self.wrong.append(x)
        while len(self.pres) <= 63:
            pass
        self.on_win()

    def on_button_press(self, x, y, pres):
        if pres > 0 and (x, y) != self.pres:
            if (x, y) in self.wrong:
                self.on_death()
            else:
                self.pres.append((x, y))
                self.lp.LedCtrlXY(x, y, 0, 0, 0)


    def on_win(self):
        self.lp.Reset()
        self.lp.LedCtrlString("Win", 0, 255, 0, direction=self.lp.SCROLL_LEFT, waitms=50)
        self.lp.continue_listener = False
        self.lp.Close()
        exit()

    def on_death(self):
        self.lp.Reset()
        for i in self.wrong:
            self.lp.LedCtrlXY(i[0], i[1], 255, 0, 0)
        self.lp.continue_listener = False
        self.lp.Close()
        exit()


if __name__ == "__main__":
    atexit.register(on_exit)
    Game()
