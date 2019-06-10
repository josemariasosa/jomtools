# Python

[TOC]

## Shebangs and encoding

```
#!/usr/bin/env python
# coding=utf-8
```

## Virtual Environment

Automatic generate requirement file with dependensies.

```
pip freeze > requirements.txt
```

Create a virtual evironment and install the requirement list.

```
pip install virtualenv

virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Try / Except

Whenever you want to break a **try/except** command in a running script using `cmd + D`, the following scructure must be used, in order to catch the *KeyboardInterrupt*, *SystemExit* errors.

```
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

## Recursion

### Recursion examples

This is a list of scripts that show examples of recursions:

#### Example 1. 

Extract the <'ObjectId'> objects from a nested list with dictionaries. The goal was to change from the nested structure to a much simpler one. Check an example of this issue:

```
from:
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

to:
[
    ObjectId('5ac5742f26dc4b07604d6079'),
    ObjectId("59eb5bd43c46f0186c8dfe1c")
]

```

The function that does this is, using Python 2.7:

```
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

    # --------------------------------------------------------------------------
```

## Processing XML files

The class **Xml2Json**, located in [xml2json](https://github.com/josemariasosa/jomtools/blob/master/python/xml/xml2json.py), can help us loop trough the Xml keys and extract the attributes and values from them. 

Some code extracted from the class:

```
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





