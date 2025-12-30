import schedule
import time

class TaskScheduler:
    @staticmethod
    def daily(time_str, task):
        schedule.every().day.at(time_str).do(task)

    @staticmethod
    def run():
        while True:
            schedule.run_pending()
            time.sleep(1)
