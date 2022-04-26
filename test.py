import unittest
from io import StringIO
import Timer
import Menu

#global variables for user input mocking



 
class FocusTimer(unittest.TestCase):
    def test_Timer_default_time(self):
        ob = Timer.Timer()
        #time is default set to 1200 seconds or 20 min
        self.assertEqual(ob.time, 1200)


    def test_Timer_get_time(self):
        ob = Timer.Timer()
        time = ob.get_time()
        #default time is 20 min (1200 sec)
        self.assertEqual(time, 1200)


    def test_Timer_get_min_whole(self):
        ob = Timer.Timer()
        min = ob.get_min(ob.get_time())
        #default time is 20 min
        self.assertEqual(min, 20)


    def test_Timer_get_min_part(self):
        ob = Timer.Timer()
        ob.time = 1195
        #this should be 19 min 55 sec
        min = ob.get_min(ob.get_time())
        self.assertEqual(min, 19)


    def test_Timer_get_sec_none(self):
        ob = Timer.Timer()
        sec = ob.get_sec(ob.get_time())
        #default time is 20 min, no seconds should be here
        self.assertEqual(sec, 0)


    def test_Timer_get_min_some(self):
        ob = Timer.Timer()
        ob.time = 1195
        #this should be 19 min 55 sec
        sec = ob.get_sec(ob.get_time())
        self.assertEqual(sec, 55)


    def test_Timer_start(self):
        ob = Timer.Timer()
        ob.time = 60
        #i don't want these tests to run forever
        result = ob.start()
        self.assertEqual(result, 1)


    def test_Menu_init_select(self):
        ob = Menu.Menu()
        #selection should default to 1
        self.assertEqual(ob.select, 1)


    def test_Menu_init_type(self):
        ob = Menu.Menu()
        #type should default to 0
        self.assertEqual(ob.type, 0)


    def test_Menu_init_work(self):
        ob = Menu.Menu()
        #work's time should default to 1200
        self.assertEqual(ob.work.time, 1200)


    def test_Menu_init_off(self):
        ob = Menu.Menu()
        #off's time should default to 120
        self.assertEqual(ob.off.time, 120)


    def test_Menu_option_start(self):
        #user should be prompted to put in selection in function before this and then option called
        #this option will start the timer
        ob = Menu.Menu()
        ob.work.time = 60
        #i don't want these tests to run forever
        #default initilization is 1
        self.assertEqual(ob.option(), 1)


    def test_Menu_option_quit(self):
        #user should be prompted to put in selection in function before this and then option called
        #this option will exit the loop
        ob = Menu.Menu()
        ob.select = 0
        self.assertEqual(ob.option(), 0)


    def test_Menu_option_bad_entry(self):
        #user should be prompted to put in selection in function before this and then option called
        #this option will display error message
        ob = Menu.Menu()
        ob.select = 18
        self.assertEqual(ob.option(), -1)


    def test_Menu_loop(self):
        ob = Menu.Menu()
        ob.select = 0
        self.assertEqual(ob.loop(), 1)
    
    
    def test_Menu_time_start_work(self):
        ob = Menu.Menu()
        ob.work.time = 60
        #i don't want these tests to run forever
        #type is default set to 0
        self.assertEqual(ob.time_start(), 0)


    def test_Menu_time_start_off(self):
        ob = Menu.Menu()
        ob.off.time = 60
        #i don't want these tests to run forever
        ob.type = 1
        self.assertEqual(ob.time_start(), 1)


    #integration tests
    def test_Menu_select_input(monkeypatch):
        select_input_mock0 = StringIO('0\n')
        monkeypatch.setattr('builtins.input', lambda x: "0")
        ob = Menu.Menu()
        assert ob.time_start() == 0


    #def test_Menu_edit_work(monkeypatch):
        #ob = Menu.Menu()
        #edit_mock1 = StringIO('1\n')
        #monkeypatch.setattr('sys.stdin', edit_mock1)
        #ob.edit_work()
        #edit work will take in user input for the amount of minutes
        #assert ob.work.time == 60
        #Work's time should now be equal to 60 times the user inputted time


    #def test_Menu_edit_off(monkeypatch):
        #ob = Menu.Menu()
        #edit_mock1 = StringIO('1\n')
        #monkeypatch.setattr('sys.stdin', edit_mock1)
        #ob.edit_off()
        #edit work will take in user input for the amount of minutes
        #assert ob.off.time == 60
        #Work's time should now be equal to 60 times the user inputted time


    #def test_Menu_option_change_work(self):
        #user should be prompted to put in selection in function before this and then option called
        #this option will open menu to change work time
        #ob = Menu.Menu()
        #ob.select = 2
        #self.assertEqual(ob.option(), 2)


    #def test_Menu_option_change_off(self):
        #user should be prompted to put in selection in function before this and then option called
        #this option will open menu to change break time
        #ob = Menu.Menu()
        #ob.select = 3
        #self.assertEqual(ob.option(), 3)

































if __name__ == '__main__':
    unittest.main()
