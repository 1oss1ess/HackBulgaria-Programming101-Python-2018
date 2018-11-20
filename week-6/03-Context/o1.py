import time
import datetime


class Log:
    def __init__(self, fname):
        self.fname = fname
        self.file_handler = None

    def performance(self, text_result):
        self.file_handler.write(text_result)

    def __enter__(self):
        self.file_handler = open(self.fname, 'a')
        return self

    def __exit__(self, *args):
        self.file_handler.close()
        return True


with Log('log_file.txt') as f:
    date_now = datetime.datetime.now()
    seconds_time_now = time.time()
    time.sleep(1)
    text_result = 'Date ' + str(date_now) + '. Execution time: ' + str(time.time() - seconds_time_now) + '\n'
    f.performance(text_result)
