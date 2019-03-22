// Query duplicated products in MongoDB.

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
