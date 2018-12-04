import datetime
import operator


class Timesheet:
    """
    A class for keeping track
    of guard sleep times.
    """

    def __init__(self):
        self.records = {}
        self.guards = set()

    @staticmethod
    def _parse_record(record):
        """
        Take a record and parse it into a nice dict.
        """

        timestamp, action = record.split("] ")
        timestamp = datetime.datetime.strptime(timestamp, "[%Y-%m-%d %H:%M")

        return timestamp, action

    def sleepiest_guard(self):
        """
        Go through the records and determine
        which guard has the most sleep minutes.
        """

        guards = {}

        for day in self.records.values():
            # Count the minutes
            minutes_asleep = len([s for s in day['minutes'] if s == "asleep"])

            # Add the guard.
            guard = day['guard_number']
            if guard not in guards:
                guards[guard] = minutes_asleep
            else:
                guards[guard] += minutes_asleep

        return max(guards.items(), key=operator.itemgetter(1))[0]

    def sleepiest_guard_minute(self, guard):
        """
        Go through the records and determine
        which minute a specific guard slept
        most frequently.
        """

        minutes = {n: 0 for n in range(60)}

        for day in self.records.values():
            if day["guard_number"] == guard:
                for minute, state in enumerate(day["minutes"]):
                    if state == "asleep":
                        minutes[minute] += 1

        return max(minutes.items(), key=operator.itemgetter(1))

    def load_records(self, records):
        """
        Load records into a sheet.
        """

        records = sorted(records)

        for record in records:
            # Parse the record
            timestamp, action = self._parse_record(record)
            minute = timestamp.minute
            hour = timestamp.hour

            # This is a shift start record.
            if "Guard" in action:
                if hour == 23:
                    timestamp = timestamp + datetime.timedelta(days=1)
                guard_number = action.split("#")[1].split(" ")[0]
                date = f"{timestamp.month}-{timestamp.day}"

                # Add the guard to the set
                self.guards.add(guard_number)

                # Make a new record.
                self.records[date] = {
                    "guard_number": guard_number,
                    "minutes": ["awake" for _ in range(60)]
                }

            # This is a sleep start record
            if "falls" in action:
                date = f"{timestamp.month}-{timestamp.day}"

                for minute_ in range(minute, 60):
                    self.records[date]["minutes"][minute_] = "asleep"

            # This is a sleep end record
            if "wakes" in action:
                date = f"{timestamp.month}-{timestamp.day}"

                for minute_ in range(minute, 60):
                    self.records[date]["minutes"][minute_] = "awake"

        return self.records




