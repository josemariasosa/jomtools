# Pandas for Python

[TOC]

## 1. In and Out I/O

### 1.1 Importing data to Python using Pandas

### 1.2 Exporting data from Python using Pandas

I. Exporting a Pandas DataFrame as a **JSON** file:

```python
import json

with open('file_name.csv', 'w') as f:
	dataframe = dataframe.to_dict(orient='records')
    json.dump(dataframe, f)
```

II. Exporting a Pandas DataFrame to a **CSV** file:

```python
dataframe.to_csv("file_name.csv", header=True, encoding='utf-8', index=False)
```

III. Appending a Pandas DataFrame to a current **CSV** file:

```python
with open('file_name.csv', 'a') as f:
	vehicles.to_csv(f, header=False, encoding='utf-8', index=False)
```

## 2. Using Masks

```python
## Double Mask for Pandas :)

email = [x == row['email'] for x in pending['email']]
price = [x == row['total_price'] for x in pending['total_price']]
mask = pd.Series([a and b for a, b in zip(email, price)])
```


## 3. Split a string into two columns.

Using zip.

```python
from pandas import *

def g_fun(_id):

    """ This function helps parsing the _id into product_id and 
	vehicle_id.
    """
    split_id = _id.split('_')
    return split_id[0], split_id[1]

data_frame[n1], data_frame[n2] = zip(*data_frame[n3].apply(g_fun))
```

## pivot table

### From two columns with factors

| user_id | movie_title                   | rating |
|---------|-------------------------------|--------|
| 1       | 'Round Midnight (1986)        | 3      |
| 3       | 'Round Midnight (1986)        | 1      |
| 1       | 'burbs, The (1989)            | 2      |
| 3       | 'burbs, The (1989)            | 3      |
| 1       | 'night Mother (1986)          | 5      |
| 5       | 'night Mother (1986)          | 4      |
| 2       | ...And Justice for All (1979) | 3      |
| 3       | ...And Justice for All (1979) | 2      |
| 5       | ...And Justice for All (1979) | 3      |

```python
movie_matrix = movies.pivot_table(index='UserID',
                                      columns='Title',
                                      values='Rating')
```

From this table to

| user_id | 'Round Midnight (1986) | 'burbs, The (1989) | 'night Mother (1986) | ...And Justice for All (1979) |
|---------|------------------------|--------------------|----------------------|-------------------------------|
| 1       | 3                      | 2                  | 5                    |                               |
| 2       |                        |                    |                      | 3                             |
| 3       | 1                      | 3                  |                      | 2                             |
| 5       |                        |                    | 4                    | 3                             |


# Working with Dates

The first line convert a pd.Series into DateTime format. The last line, remove the tz.awareness from a DateTime Series.

```py
df['col_name'] = pd.to_datetime(df['col_name'], utc=True, errors='coerce')
df['col_name'] = df['col_name'].dt.tz_localize(None)
```

