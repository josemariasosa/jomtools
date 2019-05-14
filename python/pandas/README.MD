# Pandas for Python

[TOC]

## 1. In and Out I/O

### 1.1 Importing data to Python using Pandas

### 1.2 Exporting data from Python using Pandas

I. Exporting a Pandas DataFrame as a **JSON** file:

```
import json

with open('file_name.csv', 'w') as f:
	dataframe = dataframe.to_dict(orient='records')
    json.dump(dataframe, f)
```

II. Exporting a Pandas DataFrame to a **CSV** file:

```
dataframe.to_csv("file_name.csv", header=True, encoding='utf-8', index=False)
```

III. Appending a Pandas DataFrame to a current **CSV** file:

```
with open('file_name.csv', 'a') as f:
	vehicles.to_csv(f, header=False, encoding='utf-8', index=False)
```


