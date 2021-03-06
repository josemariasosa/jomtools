# Data Types

## Lists

### Exercise 1 - Generate passwords

Generate a script capable of creating and printing a list of N passwords, of M length, including, at least, one lowercase and one uppercase letter as well as a numerical digit. The values N and M will be a user input, in case the user provide an invalid length, the default value for M will be 8.

### Exercise 2 - Update product list

---

## Sets

1. Define a new set.

```python
s = set([1, 2, 2, 3])
```

2. Add elements to a set.

```python
s.add(3)
print(s)
# {1, 2, 3}

s.add(0)
print(s)
# {0, 1, 2, 3}
```

3. Intersection

```python
s.intersection({1, 2, 4, 5})
# {1, 2}
```

---

## Tuples

### Exercise 3 - Get unique couples

We have a list L, that each of its elements is a list with 2 elements. Each element in L representa a couple of data. Some of the data is duplicated. We would like to get the unique pairs.

```python
    products = [
        ['beer', 7],
        ['chips', 4],
        ['water', 2],
        ['beer', 2],
        ['beer', 7],
        ['gin', 10],
        ['water', 2],
        ['water', 2]
    ]
```

---

## Dictionaries

### Exercise 4 - Dice histogram



### Exercise 4 - Grocery list with price

Generate a script in which the user define a single product he is looking for, and the answer present in which store that product is cheaper. Use the following starting values:

```python
    prices_store_1 = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
    }

    prices_store_2 = {
        "banana": 6,
        "apple": 1.5,
        "orange": 3,
        "pear": 3,
        "tomato": 1
    }
```

### Exercise 5 - Grocery list with price and stock

Generate a script in which the user give a product name and a quantity for that product as an input. Then the output must be the combination of stores that minimize the expenses.

```python
    prices_store_1 = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
    }

    prices_store_2 = {
        "banana": 6,
        "apple": 1.5,
        "orange": 3,
        "pear": 3,
        "tomato": 1
    }

    stock_store_1 = {
        "banana": 1,
        "apple": 30,
        "orange": 3,
        "pear": 1
    }

    stock_store2 = {
        "banana": 10,
        "apple": 1,
        "orange": 1,
        "pear": 3,
        "tomato": 0
    }
```

---


### Epoch & Unix Timestamp Conversion Tools
 
The current Unix epoch time is: `1574113549`.

For more info, check: https://www.epochconverter.com/.


#### How to get the current epoch time

**Python:**

```py
    import time; time.time()
```

**Unix/Linux Shell:**

```bash
date +%s
```

#### Convert from human-readable date to epoch

**Python:**

```py
import calendar, time
calendar.timegm(time.strptime('2000-01-01 12:34:00', '%Y-%m-%d %H:%M:%S'))
```

**Unix/Linux Shell:**

```bash
date -d @1520000000
```

Replace 1520000000 with your epoch, needs recent version of 'date'. Replace '-d' with '-ud' for GMT/UTC time.

#### Convert from epoch to human-readable date

**Python:**

```py
import time
time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(epoch))
```

Replace `time.localtime` with `time.gmtime` for GMT time.

Or using `datetime`:

```py
import datetime
datetime.datetime.utcfromtimestamp(epoch).replace(tzinfo=datetime.timezone.utc)
```

**Unix/Linux Shell:**

```sh
date +%s -d"Jan 1, 1980 00:00:01"
```

Replace `-d` with `-ud` to input in GMT/UTC time.
