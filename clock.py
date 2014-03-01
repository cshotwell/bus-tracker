from apscheduler.scheduler import Scheduler
import update_user

sched = Scheduler()

@sched.interval_schedule(seconds=10)
def timed_job():
    update_user.update_least_updated()


sched.start()

while True:
    pass
