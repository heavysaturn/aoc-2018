from day4.models.timesheet import Timesheet
from utils import load_input

records = load_input()
timesheet = Timesheet()

# Load the records
timesheet.load_records(records)

# Which guard was most frequently asleep on the same minute?
sleepiest = (0, 0, 0)
for guard in timesheet.guards:
    minute, times = timesheet.sleepiest_guard_minute(guard)
    if times > sleepiest[2]:
        sleepiest = (guard, minute, times)

print(f"The guard who was most frequently asleep on the same minute was Guard #{sleepiest[0]}")
print(f"They prefered to sleep on minute {sleepiest[1]}.")
print(f"Sleepiest guard ID * sleepiest minute = {int(sleepiest[0]) * int(sleepiest[1])}")
