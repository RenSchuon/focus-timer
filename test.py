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


    def test_Menu_init(self):
        ob = Menu.Menu()
        #selection should default to 1
        self.assertEqual(ob.select, 1)

if __name__ == '__main__':
    unittest.main()
