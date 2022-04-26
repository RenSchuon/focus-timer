import Timer

class Menu(object):
    def __init__(self):
        self.select = 1
        self.type = 0
        self.work = Timer.Timer()
        self.off = Timer.Timer()
        self.off.time = 120

    
    def select_input(self):
        self.select = input("1 start timer\n2 change work timer\n3 change break timer\n0 exit")
        self.option()
        return self.select


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
            print("goodbye")
            return 0
        else:
            print("invalid selection")
            return -1


    def loop(self):
        while self.select != 0:
            self.select_input()
        return 1

    
    def time_start(self):
        if self.type == 0:
            self.work.start()
            self.type = 1
            return 0
        else:
            self.off.start()
            self.type = 0
            return 1

    
    def edit_work(self):
        new_time = input("input the new time in minutes")
        new_time = new_time * 60
        self.work.time = new_time
        return new_time


    def edit_off(self):
        new_time = input("input the new time in minutes")
        new_time = new_time * 60
        self.off.time = new_time
        return new_time


    def bad_entry(self):
        print("invalid selection")
        self.select_input()