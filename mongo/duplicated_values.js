// Query duplicated fields in a collection.

db.getCollection('attribute_code').aggregate([
  {"$match":{attribute_id: 19999}},
  {"$project": {
      "label":1,
      "label_en":1,
      "aEq": {"$eq":["$label","$label_en"]}
    }
  },
  {"$match":{"aEq": true}}
])

db.getCollection('attribute_code').find({$where: "this.label == this.label_en", attribute_id: 19999 }).sort({code: 1})

