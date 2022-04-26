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
            return 1
        elif self.select == 2:
            self.edit_work()
            return 2
        elif self.select == 3:
            self.edit_off()
            return 3
        elif self.select == 0:
            self.goodbye()
            return 0
        else:
            self.bad_entry()
            return -1


    def loop(self):
        #need integration test for
        while self.select != 0:
            self.select_input()

    
    #def time_start():