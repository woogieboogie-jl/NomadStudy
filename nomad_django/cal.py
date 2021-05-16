from django.utils import timezone
import calendar


class Day:
    def __init__(self, number, past, month, year):
        self.number = number
        self.past = past
        self.month = month
        self.year = year

    def __str__(self):
        return str(self.number)


class Calendar(calendar.Calendar):

    def __init__(self, year, month):
        super().__init__(firstweekday=6)
        self.year = year
        self.month = month
        self.day_names = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
        self.months = (
            "January",
            "Feburary",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        )

    def get_days(self):
        weeks = self.monthdays2calendar(self.year, self.month)
        days = []
        for week in weeks:
            for day,_ in week:
                now = timezone.now()
                month = now.month
                past = False
                today = now.day
                if month == self.month:
                    if day <= today:
                        past = True
                new_day = Day(number=day, past=past, month=self.month, year=self.year)
                days.append(new_day)
        return days


    def get_month(self):
        return self.months[self.month - 1]


    def get_date_info(self, count):
        now = timezone.now()
        year = now.year
        month = now.month + count

        if (now.month + count) > 12:
            year = now.year + (now.month+count)//12
            month = (now.month+count) % 12
            
        return Calendar(year, month)
        