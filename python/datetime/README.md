# Datetime with Python

## Month time delta

In order to chance the month of a `datetime` object for any specific delta, use the following function.

```python
def monthdelta(date, delta):
    m, y = (date.month+delta) % 12, date.year + ((date.month)+delta-1) // 12
    if not m: m = 12
    d = min(date.day, [31,
        29 if y%4==0 and not y%400==0 else 28,31,30,31,30,31,31,30,31,30,31][m-1])
    return date.replace(day=d,month=m, year=y)
```

Dates operation


Assuming you’ve literally got two date objects, you can subtract one from the other and query the resulting timedelta object for the number of days:

>>> from datetime import date
>>> a = date(2011,11,24)
>>> b = date(2011,11,17)
>>> a-b
datetime.timedelta(7)
>>> (a-b).days
7



def to_elapsed_days(d):
    if bool(d):
        return (today - d).days


def to_elapsed_days(d):
    if bool(d):
        return (today - d).total_seconds()