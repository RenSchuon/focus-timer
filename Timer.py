import time

class Timer(object):
      def __init__(self):
        self.time = 1200


      def get_time(self):
        return self.time


      def get_min(self, value):
        result = int(value/60)
        return result


      def get_sec(self, value):
        return value%60


      def start(self):
        for i in range(self.time):
          print(self.get_min(self.time-i))
          print(':')
          print(self.get_sec(self.time-i))
          time.sleep(1)
        print('Done!\a')
        return 1
        

      