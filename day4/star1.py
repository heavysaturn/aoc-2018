from day4.models.timesheet import Timesheet
from utils import load_input

records = load_input()
timesheet = Timesheet()

# Load the records
timesheet.load_records(records)

# Who is the sleepiest guard?
sleepy_guard = timesheet.sleepiest_guard()
print(f"The sleepiest guard is Guard #{sleepy_guard}")

# What minute did he sleep the most?
sleepy_minute = timesheet.sleepiest_guard_minute(sleepy_guard)
print(f"The minute that guard was most frequently asleep was minute {sleepy_minute}")

# Solve the problem
print(f"The ID of the guard multiplied by the minute = {int(sleepy_guard) * int(sleepy_minute)}")
