class Timer(object):
      def __init__(self):
        self.time = 1200

      def get_time(self):
        return self.time

      def get_min(self):
        result = int(self.time/60)
        return result

      