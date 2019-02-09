import datetime

class Items(object):

   def __init__(self, task):
        self.time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.is_task_complete = False
        self.task = task
