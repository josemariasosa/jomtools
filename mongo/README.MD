# Mongo DB

## Description:

This is a recopilation of hacks and tricks to move around Mongo DB with ease. 

## Mongo APIS:

### 1 - pyMongo Python Client

#### 1.1 find query

```
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
    
```
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

