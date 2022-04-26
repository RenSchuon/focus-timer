import Timer

class Menu(object):
    def __init__(self):
        self.select = 1
        self.type = 0
        self.work = Timer.Timer()
        self.off = Timer.Timer()
        self.off.time = 120

    
    def select_input(self):
        #need integration test for
        self.select = input("1 start timer\n2 change work timer\n3 change break timer\n0 exit")
        self.option()


    def option(self):
        if self.select == 1:
            self.time_start()


    def loop(self):
        #need integration test for
        while self.select not 0:
            self.select_input()