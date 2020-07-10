# Python

[TOC]

## Python setup

### Install Python

Download the lastest version of Python from the [official website](https://www.python.org).

### Install Pip on MacOS

Install pip on MacOS, using easy_install command and upgrade pip to the latest version:

```bash
$ sudo easy_install pip
$ sudo pip install --upgrade pip
```

## PEP 8

This will only list some of the most important points from the most popular Style Guide for Python (AKA [PEP 8](https://www.python.org/dev/peps/pep-0008/)).

- **Indentation** - Use 4 spaces per indentation level.
- **Tabs or Spaces?** - Spaces are the preferred indentation method.
- **Maximum Line Length** - Limit all lines to a maximum of 79 characters.
- **Blank Lines** - Surround top-level function and class definitions with two blank lines. Method definitions inside a class are surrounded by a single blank line.
- **Source File Encoding** - Code in the core Python distribution should always use UTF-8 (or ASCII in Python 2). Files using ASCII (in Python 2) or UTF-8 (in Python 3) should not have an encoding declaration.
- **Imports** - Imports should usually be on separate lines.
- **Most Importan Naming Conventions**:
    - **regular_variables**: variable names should be lowercase, where necessary separating words by underscores.
    - **CONSTANTS**: to indicate that a variable should be treated as if it were a constant, names should be uppercase, where necessary separating words by underscores.
    - **function_names()**: names of functions and class methods should be lowercase, where necessary separating words by underscores.
    - **ClassNames**: class names should capitalize the first letter of each word.
    - **FactoryFunctionNames()**: factory functions return objects. Therefore, to users of your code, factory functions act like class definitions. To reflect this, factory function names should also capitalize the first letter of each word.

## Shebangs and encoding

```python
#!/usr/bin/env python
# coding=utf-8
```

## Virtual Environment

Automatic generate requirement file with dependensies.

```bash
$ pip freeze > requirements.txt
```

Create a virtual evironment and install the requirement list.

```bash
$ pip install virtualenv

$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Create a new virtual environment inside the directory:

```bash
# Python 2:
$ virtualenv env

# Python 3
$ python3 -m venv env
```

## Config

A good way to work with the keys and configuration on a server is using the [configparser library](https://docs.python.org/3/library/configparser.html).

```python
#!/usr/bin/env python
# coding=utf-8

import os
import configparser
from pymongo import MongoClient

_parser = configparser.ConfigParser()
_parser.read_file(open(os.path.expanduser(os.environ['RIGS_SETTINGS'])))

_general = _parser["general"]

_database = _parser[("database %s" % _general["env"])]
_mongo_uri = "mongodb://%s:%s@%s:%s" % (_database["user"],
                                        _database["password"],
                                        _database["socket"],
                                        _database["port"])

_mongo_client = MongoClient(_mongo_uri)
db_rigs = _mongo_client["rigs"]
```

You can also create multiple attributes on a class using the `setattr` function.

```python
#!/usr/bin/env python
# coding=utf-8

import os
import configparser
from pymongo import MongoClient

_parser = configparser.ConfigParser()
_parser.read_file(open(os.path.expanduser(os.environ['_SETTINGS'])))

_general = _parser["general"]
_environment = _parser["facturbo"]["env"]

_database = _parser[("database %s" % _environment)]
_mongo_uri = "mongodb://%s:%s@%s:%s" % (_database["user"],
                                        _database["password"],
                                        _database["socket"],
                                        _database["port"])

_config = {
    "AWS_BUCKET_NAME": "business-invoices",
    "OFFICE_ZIP_CODE": "44160",
    "PAYMENT_METHOD": "pue",
    "FIXED_DECIMALS": "2",
    "FIXED_CURRENCY": "mxn",
    "TAX_RATE": 0.16,
    "TAX_NAME": "iva",
    "IS_RETENTION": "false",
    "UNIT": "pieza",
    "UNIT_CODE": "h87",
    "PRODUCT_CODE": "25174800",
    "DEFAULT_DISCOUNT": "0.0",
    "DEFAULT_NAME_ID": "1",
    "DEFAULT_CFDI_TYPE": "i",
    "DEFAULT_INVOICE_TYPE": "g01"
}

env_config = {
    "development": {
        "IS_SANDBOX": True,
        "API_URL": "https://apisandbox.facturama.mx/cfdi/{}/issued/{}",
        "API_URL_2": "https://apisandbox.facturama.mx/2/cfdis",
        "API_CLIENT": "https://apisandbox.facturama.mx/Client",
        "API_EMAIL": "https://apisandbox.facturama.mx/Cfdi?cfdiType=issued&cfdiId={}&email={}&subject={}&comments={}"
    },
    "production": {
        "IS_SANDBOX": False,
        "API_URL": "https://www.api.facturama.com.mx/cfdi/{}/issued/{}",
        "API_URL_2": "https://www.api.facturama.com.mx/2/cfdis",
        "API_CLIENT": "https://www.api.facturama.com.mx/Client",
        "API_EMAIL": "https://www.api.facturama.com.mx/Cfdi?cfdiType=issued&cfdiId={}&email={}&subject={}&comments={}"
    }
}

_config.update(env_config[_environment])

_mongo_client = MongoClient(_mongo_uri)
db_rigs = _mongo_client["rigs"]
db_business = _mongo_client["business"]
db_ecommerce = _mongo_client["ecommerce"]

```

```python
# Insert the _config attributes in a Class. ----->

from config import _config, db_business


class FileCreator(object):

    """ API GET Request Parameters
            'https://apisandbox.facturama.mx/cfdi/{pdf|xml|html}/{issued}/{id}'
    """

    def __init__(self, cfdi_id, order_id):

        # Config attributes.
        for key in _config:
            setattr(self, key, _config[key])

        self.slack = Slack()
        self.cfdi_id = cfdi_id
        self.order_id = order_id
        self.date = self.getCurrentDate()

        # Mongo Collections.
        self.invoiceDB = db_business['invoice']

    # ----------------------------------------------------------
```

## Try / Except

Whenever you want to break a **try/except** command in a running script using `cmd + D`, the following scructure must be used, in order to catch the *KeyboardInterrupt*, *SystemExit* errors.

```python
try:
    title_success = self.updateTitle(shopify_id, title)
    body_success = self.updateBody(shopify_id, body)

    if not all([title_success, body_success]):
        _id_to_remove.append(row['product_id'])

except (KeyboardInterrupt, SystemExit):
    raise ValueError('Script stopped manually!')

except:
    # self.notifyPriceStockIssue(row, 6)
    _id_to_remove.append(row['product_id'])
```

## Regular Expressions

I know it's a good idea to do a little reference about the documentation of this in Python, although, for now, it's more than enough to list some practical examples of the use of `re.match()`, `re.search()`, and some others methods of the **re** library.

### Match

#### Example 1

Taken from the [RE Documentation](https://docs.python.org/2/library/re.html).

```python
import re

m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")

m.group(0)       # The entire match
# 'Isaac Newton'

m.group(1)       # The first parenthesized subgroup.
'Isaac'

m.group(2)       # The second parenthesized subgroup.
'Newton'

m.group(1, 2)    # Multiple arguments give us a tuple.
('Isaac', 'Newton')
```

#### Example 2

Parsing a url using match. The goal was to extract the string that was at the right position of a given string.

```python
text = '/products/banda-tiempo-cloyes-b281'

m = re.match(r"(.+cloyes)(.+)", text)

m.group(1)
'/products/banda-tiempo-cloyes'

m.group(2)
'-b281'
```

### Search

Search method is way easier. It help us to find if any given expression exists in a string.

```python
if bool(re.search(r'cloyes', s)):
    print('The expression exists in the string: s')

else:
    print('The expression does not exist in the string: s')
```

## Recursion

### Recursion examples

This is a list of scripts that show examples of recursions:

#### Example 1.

Extract the <'ObjectId'> objects from a nested list with dictionaries. The goal was to change from the nested structure to a much simpler one. Check an example of this issue:

**From**:
```python
[
    {
        "price": None,
        "product_id": {
            "price": None,
            "product_id": ObjectId('5ac5742f26dc4b07604d6079')
        }
    },
    {
        "price": None,
        "product_id": {
            "price": None,
            "product_id": {
                "price": None,
                "product_id": {
                    "price": None,
                    "product_id": ObjectId("59eb5bd43c46f0186c8dfe1c")
                }
            }
        }
    }
]
```

**To**:
```python
[
    ObjectId('5ac5742f26dc4b07604d6079'),
    ObjectId("59eb5bd43c46f0186c8dfe1c")
]
```

The function that does this is, using Python 2.7:

```python
def keepOnlyValues(self, l):

    def objectify(x):
        if isinstance(x, str) or isinstance(x, unicode):
            if len(x) == 24:
                x = ObjectId(x)

        if isinstance(x, ObjectId):
            return x
        elif isinstance(x, dict):
            new = x.values()
            new = [objectify(value) for value in new]
            while None in new:
                new.remove(None)
            if len(new) > 0:
                return new[0]
        else:
            return None

    l = [objectify(x) for x in l]

    return l
```

### Example 2. Get all the nested keys from an object

Using recurssion.

```json
// For 
{
    "_id": 1,
    "user": {
        "name": "jose",
        "surname": "sosa",
        "email": "josemariasosa@github.com"
    },
    "modules": {
        "data": {
            "basic": 100,
            "advanced": 90
        },
        "programming": {
            "basic": 80,
            "advanced": 85
        }
    }
}

// To
{
    "_id": 1,
    "user.name": "jose",
    "user.surname": "sosa",
    "user.email": "josemariasosa@github.com",
    "modules.data.basic": 100,
    "modules.data.advanced": 90,
    "modules.programming.basic": 80,
    "modules.programming.advanced": 85
}
```

```python
def get_new_keys(self, v):
        all_keys = []
        for k, v in v.items():
            if isinstance(v, dict):
                new_keys = self.get_new_keys(v)
                new_keys = [k + '.' + x for x in new_keys]
                all_keys.extend(new_keys)
            else:
                all_keys.append(k)
        return all_keys

    def ___get_fields(self, results):
        fields = []
        for doc in results:
            date = False
            keys = []
            for k, v in doc.items():
                if k == '_id':
                    date = v.generation_time
                else:
                    if isinstance(v, dict):
                        new_keys = self.get_new_keys(v)
                        new_keys = [k + '.' + x for x in new_keys]
                        keys.extend(new_keys)
                    else:
                        keys.append(k)
            fields.append({
                'date': date,
                'keys': keys
            })
        return fields
```




---

## Processing XML files

The class **Xml2Json**, located in [xml2json](https://github.com/josemariasosa/jomtools/blob/master/python/xml/xml2json.py), can help us loop trough the Xml keys and extract the attributes and values from them. 

Some code extracted from the class:

```python
import xml.etree.ElementTree as ET

tree = ET.parse(file_path)
root = tree.getroot()

for node in root:
        new_app = {}
        qual_list = []
        desc_list = []
        if node.tag == 'App':
            for childnode in node:
                if childnode.tag in self.id_keys:
                    _id = childnode.attrib['id']
                    if _id.isdigit():
                        new_app[childnode.tag] = int(_id)
```

## Input/Output Python IO


## Classes overview

### 1. Defining a `class` in Python

```python
class Person(object):
    """Simple class representing a Person"""
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
```

### 2. Property decorator

This decorator `@property` will convert a method into an attribute.

```python
class Person(object):
    """Simple class representing a Person"""
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    @property
    def real_age(self):
        return int(self.age) + 5

def main():
    person = Person('Jose', 'Sosa', 30)

    print(person.real_age)
    ## --> 35

if __name__ == '__main__':
    main()
```

### 3. Classes Inheritance

Inheritance allows us to define a class that inherits all the methods and properties from another class. **Parent class** is the class being inherited from, also called base class. **Child class** is the class that inherits from another class, also called derived class.

```python
class Product(object):
    """Simple class representing a Product"""
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    @property
    def subtotal(self):
        return float(self.price) * int(self.quantity)

class Vehicle(Product):
    """Simple class representing a Vehicle"""
    def __init__(self, name, quantity, price, brand, model):
        Product.__init__(self, name, quantity, price)
        self.brand = brand
        self.model = model
```

### 4. Special Methods for Classes

#### 4.1 `__str__` Method

We can design the way a class is printed, using the `print` function, or whenever we just call the object. So, to change the print results from: `<__main__.Person object at 0x10e135128>`, to another with a more adequate structure.

```python
class Person(object):
    """Simple class representing a Person"""
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        text = '{}\t{}\t{}'
        text = text.format(self.name,
                           self.surname,
                           self.age)
        return text

    @property
    def real_age(self):
        return int(self.age) + 5

class Student(Person):
    """Simple class representing a Student"""
    def __init__(self, name, surname, age, course, grade):
        Person.__init__(self, name, surname, age)
        self.course = course
        self.grade = grade

    def __str__(self):
        text = '{}\t{}\t{}\t{}\t{}'
        text = text.format(self.name,
                             self.surname,
                             self.edad,
                             self.course,
                             self.grade)
        return text
```

## zip

```python
from itertools import izip_longest, chain

models = [[('nissan', 'tiida')], [('volkswagen', 'jetta'), ('volkswagen', 'jetta city')]]

args = tuple(models)     
models = izip_longest(*args)
models = [tuple(j for j in i if j is not None)for i in models]
models = list(chain(*models))

print models
# [('nissan', 'tiida'), ('volkswagen', 'jetta'), ('volkswagen', 'jetta city')]


## Passing arguments as a single variable.

Arguments = 1, 2, 3
SumOf(*Arguments)
(*) operator will unpack the arguments to multiple parameters.
```


## Obtaining arguments from bash in python

From bash, run:

```bash
(venv)$ python main.py test=stress
```

Get the keyword arguments as a dictionary.

```python
#!/usr/bin/env python
# coding=utf-8

# Only for Data Testing. | Rever inc
# ------------------------------------------------------------------------------

import sys

from controller.analytics import OnGetAnalytics

def main():
    i = OnGetAnalytics('mq')
    i.start('channel', 'method', 'props', 'body')



if __name__ == '__main__':
    if len(sys.argv) > 1:
        kwargs = {
            arg.split('=')[0]:arg.split('=')[1]
            for arg in sys.argv[1:] if '=' in arg
        }

    print(kwargs)
    exit()
    main()
```

