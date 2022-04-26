import unittest
import Timer
import Menu
 
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
        result = ob.start()
        self.assertEqual(result, 1)


    def test_Menu_init_select(self):
        ob = Menu.Menu()
        #selection should default to 1
        self.assertEqual(ob.select, 1)


    def test_Menu_init_type(self):
        ob = Menu.Menu()
        #type should default to 0
        self.assertEqual(ob.type, 1)


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
        #default initilization is 1
        self.assertEqual(ob.option(), 1)


    def test_Menu_option_change(self):
        #user should be prompted to put in selection in function before this and then option called
        #this option will open menu to change work time
        ob = Menu.Menu()
        ob.select = 2
        self.assertEqual(ob.option(), 2)


    def test_Menu_option_change(self):
        #user should be prompted to put in selection in function before this and then option called
        #this option will open menu to change break time
        ob = Menu.Menu()
        ob.select = 3
        self.assertEqual(ob.option(), 3)


    def test_Menu_option_quit(self):
        #user should be prompted to put in selection in function before this and then option called
        #this option will exit the loop
        ob = Menu.Menu()
        ob.aelect = 0
        self.assertEqual(ob.option(), 0)


if __name__ == '__main__':
    unittest.main()
