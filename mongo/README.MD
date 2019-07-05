# Mongo DB

## Description:

This is a recopilation of hacks and tricks to move around Mongo DB with ease.

## Common queries:

This is a list of the most common and useful queries using MongoDB.

### 1. Get duplicated values in a field within different documents.

```javascript
db.getCollection('articulo').aggregate([
    {
        $match: {
                'marca_refaccion': 'nissan'
            } 
    },
    {
        $group: {
                _id: {texto_articulo: '$texto_articulo'},
                uniqueIds: {$addToSet: '$_id'},
                count: {$sum: 1}
            }
    },
    {
        $match: {
                count: {'$gt': 1}
            }
    }
])
```

### 2. Query documents containing a list with at least 1 element match.

```javascript
db.getCollection('articulo').find({
    attributes: {
        $elemMatch: {
            attribute_id: 10,
            codes: {
                $in: [3]
            }
        }
    }
})
```

## Mongo APIS:

### 1 - pyMongo Python Client

#### 1.1 find query

```python
    queryDB = {
        'shopify_id': {
            '$exists': 1
        },
        'price_last_update': {
            '$exists': 0
        },
        '_id': {
            '$in': product_list
        }
    }
    projeDB = {
        '_id': 0,
        'product_id': 1,
        'shopify_id': 1
    }
    results = self.stagingDB.find(queryDB, projeDB).limit(self.BATCH_SIZE)
    results = list(results)
    results = pd.DataFrame(results)

    return results
```

#### 1.2 aggregate query
    
```python
    from bson.son import SON
    from bson import ObjectId

    queryDB = {
        'shopify_id': {
            '$exists': 1
        },
        'price_last_update': {
            '$exists': 0
        },
        '_id': {
            '$in': [ObjectId(x) for x in product_list]
        }
    }
    projeDB = {
        '_id': 0,
        'product_id': 1,
        'shopify_id': 1
    }
    aggreDB = [
        { "$match" : queryDB },
        { "$project" : projeDB },
        { "$sort" : SON([("price_last_update", 1)]) },
        { "$limit" : self.BATCH_SIZE }
    ]
    results = self.stagingDB.aggregate(aggreDB)
    results = list(results)
    results = pd.DataFrame(results)

    return results
```

#### 1.3 Move around in the whole collection by batch

```python
    self.STEP_SIZE = 100000
    self.length = self.articuloDB.find({}).count()

    steps = range(0, self.length, self.STEP_SIZE)
        for start in steps:
            queryDB = {
                'attributes': {
                    '$exists': 1
                }
            }
            constDB = {
                '_id': 0,
                'clasificacion': 1,
                'attributes.attribute_id': 1
            }
            results = (self.articuloDB.find(queryDB, constDB)
                                        .skip(start)
                                        .limit(self.STEP_SIZE))
            results = list(results)
            results = pd.DataFrame(results)
```



