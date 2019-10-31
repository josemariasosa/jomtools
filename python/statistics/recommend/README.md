# Recommender system

## Content-Based Filter Method

### 1. Set-up

Set up the virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate
pip install sklearn nltk pandas git+https://github.com/josemariasosa/rubik
```

Make sure the `main.sh` file is poiting to the correct python File for this model. We are going to run the specific code for a content-based filter method. The python route must be:

```bash
PYTHON_FILE=$PYTHON_FOLDER'/pyFiles/_content_based/main.py'
```

The `data/` files are available here:

- [**data/interactions.csv**](https://github.com/josemariasosa/jomtools-data/blob/master/python/statistics/recommend/data/interactions.csv)
- [**data/items.csv**](https://github.com/josemariasosa/jomtools-data/blob/master/python/statistics/recommend/data/items.csv)

Download the files and put them in the correct location.


# # """
# # Está interesante observar cómo el modelo que se creó,

# # print(tf)

# # nos permite pasar a nuestro arreglo de cadenas por algún preproceso. 

# # Quizá se puedan correr procesos como el steam (o no recuerdo cómo se llama),
# # que permiten normalizar el lenguaje a base de un "modelo de lenguaje".
# # De esta manera quedarían mejor hechos los tokens, y podría arrojar mejores
# # resultados.

# # TfidfVectorizer.fit_transform()

# # Los resultados arrojan lo siguiente:

# # Note that you are printing a sparse matrix so the output looks different 
# # compared to printing a standard dense matrix. See below the main components:

# # - The tuple represents: (document_id, token_id)
# # - The value following the tuple represents the tf-idf score of a given token 
# #     in a given document
# # - The tuples that are not there have a tf-idf score of 0
# # - If you want to find what token the token_id corresponds to, check the 
# #     get_feature_names method.

# # el token_id, es muy interesante, entonces por cada documento (o muestra) se hacen
# # tokens y se tokenizan, asignándole un token_id a cada uno. la matrix resultante,
# # entonces tiene la longitud de todos los tokens de todos los documentos. Me imagino
# # que se hace referencia después a un diccionario para cambiar ese token_id por el
# # token real. Posteriormente, tiene una columna ya con el valor del cálculo 
# # del Tf-Idf.

# # Also, stop words are simply words that add no significant value to our system,
# # like ‘an’, ‘is’, ‘the’, and hence are ignored by the system.

# # Los pasos que se siguen, conceptualmente, son:

# # 1. Se tiene el texto original: "In order to work accurately, this type of filter
# # needs rates, and not all users rate products constantly."

# # 2. El texto se estandariza y se tokeniza, o sea, se genera una lista con los
# # tokens. l = ['order', 'work', 'accurately', 'type', 'filter', 'needs',
# # 'rates', 'not', 'all', 'users', 'rate', 'products', 'constantly'].

# # 3. Este proceso se lleva a cabo para todos los documentos. El resultado es la
# # matriz de tokens, en donde en lugar de mostrar el token, se muestra un token_id.

# # (0, 1123) 0.34234
# # (0, 324)  0.1001           <- sparse matrix

### el cero está en el índice del item_id

"""

Standardization of datasets is a common requirement for many machine learning estimators implemented in scikit-learn; they might behave badly if the individual features do not more or less look like standard normally distributed data: Gaussian with zero mean and unit variance.

Normalization is the process of scaling individual samples to have unit norm. This process can be useful if you plan to use a quadratic form such as the dot-product or any other kernel to quantify the similarity of any pair of samples.

This assumption is the base of the Vector Space Model often used in text classification and clustering contexts.

normalize and Normalizer accept both dense array-like and sparse matrices from scipy.sparse as input.

Normalization is the process of scaling individual samples to have unit norm. In basic terms you need to normalize data when the algorithm predicts based on the weighted relationships formed between data points. Scaling inputs to unit norms is a common operation for text classification or clustering.

One of the key differences between scaling (e.g. standardizing) and normalizing, is that normalizing is a row-wise operation, while scaling is a column-wise operation.

1. Normalization makes training less sensitive to the scale of features, so we can better solve for coefficients.

2. Standardizing tends to make the training process well behaved because the numerical condition of the optimization problems is improved.

Normalization
The boring definition of this mathematical approach would be,

Normalization is performed on data to remove amplitude variation and only focus on the underlying distribution shape.

Normalization is performed on data to compare numeric values obtained from different scales.

Normalizing: https://personal.utdallas.edu/~herve/abdi-Normalizing2010-pretty.pdf

We often want to compare scores or sets of scores obtained on different scales. For example, how do we compare a score of 85 in
a cooking contest with a score of 100 on an I.Q. test? In order to
do so, we need to “eliminate” the unit of measurement, this operation is called to normalize the data. There are two main types of
normalization. The first first type of normalization originates from
linear algebra and treats the data as a vector in a multidimensional
space. In this context, to normalize the data is to transform the
data vector into a new vector whose norm (i.e., length) is equal to
one. The second type of normalization originates from statistics,
and eliminates the unit of measurement by transforming the data
into new scores with a mean of 0 and a standard deviation of 1.
These transformed scores are known as Z-scores.



In basic terms you need to normalize data when the algorithm predicts based on the weighted relationships formed between data points.

normalize(X, norm=’l2’, axis=1, copy=True, return_norm=False)

norm= could be:

norm="max"
Max is quite similar to Min Max normalization. The only difference being is that the the normalized values will fall between a range of 1 and to a value less than or equal to 0.

norm="l1" (Least Absolute Deviation or LAD)
L1 is basically minimizing the sum of the absolute differences (S) between the target value (x) and the estimated values (x’).
To understand it easily, its just adding all the values in the array and dividing each of it using the sum.

l2 L2 Normalization (Least Square Error or LSE)
L2 minimizes the sum of the square of the differences (S) between the target value (x) and the estimated values (x’).
Or in simpler terms, just divide each value by δ. Where δ is nothing but the square root of the sum of all the squared values.

There are four proven steps in the preparation of data for learning with sci-kit-learn. They include:

rescale the data
standardization of data
normalize the data
turn data into binary

        ## step 1. multiply each strenght by the token tf-idf calculations.
        # user_item_profiles.multiply(user_item_strengths)

        ## setp 2. sum all the token-values using np.sum with axis=0, check the example
        #   >>> np.sum([[0, 1], [0, 5]], axis=0)
        #   array([0, 6])
        #   >>> np.sum([[0, 1], [0, 5]], axis=1)
        #   array([1, 5])

        ## step 3. divide the resultant vector with the scalar resultant from
        # np.sum(user_item_strengths)   


"""

# # Por lo tanto, el 0 representa el texto original (el número de la fila),
# # el 1123 hace referencia al token, por ejemplo, de 'order' y 324 hace referencia
# # al token 'work'. En la extrema derecha, qué feo suena eso, tenemos el raiting
# # Tf-Idf, que mide la relevancia del token dentro de los documentos.

# # # Now, linear_kernel. What do we know? We know it comes from the module 
# # sklearn.metrics.pairwise. So it help us measure distances using a pairwise method.

# # The sklearn.metrics.pairwise submodule implements utilities to evaluate pairwise
# # distances or affinity of sets of samples.

# # This module contains both distance metrics and kernels. A brief summary is given
# # on the two here.

# # Distance metrics are functions d(a, b) such that d(a, b) < d(a, c) if objects
# # a and b are considered “more similar” than objects a and c.

# # The Euclidean distance rules:

# # 1. d(a, b) >= 0, for all a and b
# # 2. d(a, b) == 0, if and only if a = b, positive definiteness
# # 3. d(a, b) == d(b, a), symmetry
# # 4. d(a, c) <= d(a, b) + d(b, c), the triangle inequality



# # The ultimate reason behind using cosine is that the value of cosine will 
# # increase as the angle between vectors with decreases, which signifies more 
# #     similarity.
# # The vectors are length-normalized, after which they become vectors of 
# #     length 1.

# # Cosine similarity is a metric used to measure how similar the documents are
# # irrespective of their size. Mathematically, it measures the cosine of the angle
# # between two vectors projected in a multi-dimensional space. The cosine similarity
# # is advantageous because even if the two similar documents are far apart by the
# # Euclidean distance (due to the size of the document), chances are they may still
# # be oriented closer together. The smaller the angle, higher the cosine similarity.

# # To compute the cosine similarity, you need the word count of the words in each
# # document. The CountVectorizer or the TfidfVectorizer from scikit learn lets us
# # compute this. The output of this comes as a sparse_matrix.

# # Even better, I could have used the TfidfVectorizer() instead of CountVectorizer(),
# # because it would have downweighted words that occur frequently across docuemnts.

# # Then, use cosine_similarity() to get the final output. It can take the document
# # term matri as a pandas dataframe as well as a sparse matrix as inputs.

# # ## Here it talK About the step from the tf-idf results to cosine_similarities.
# # Now we have the TF-IDF matrix (tfidf_matrix) for each document (the number of rows 
# # of the matrix) with 11 tf-idf terms (the number of columns from the matrix), we can
# # calculate the Cosine Similarity between the first document (“The sky is blue”) with
# # each of the other documents of the set:
# # The tfidf_matrix[0:1] is the Scipy operation to get the first row of the sparse
# # matrix and the resulting array is the Cosine Similarity between the first document
# # with all documents in the set. Note that the first value of the array is 1.0
# # because it is the Cosine Similarity between the first document with itself.
# # Also note that due to the presence of similar words on the third document (“The
# # sun in the sky is bright”), it achieved a better score.

# # The result of

# # linear_kernel
# # cosine_similarities

# # is a matrix with the computations of the distances among all the documents.

# # resultant matrix:
# # distance = [[1.  0.10  0.06  0.06  0.05  0.06]
# #             [0.10  1.  0.41  0.03  0.06  0.06]
# #             [0.06  0.41  1.  0.03  0.04  0.05]
# #             [0.06  0.03  0.03  1.  0.04  0.04]
# #             [0.06  0.06  0.04  0.04  1.  0.36]
# #             [0.06  0.06  0.05  0.04  0.36  1.]]
# # (6, 6)

# # See how all the distance from the principal diagonal are 1 due to the comparison
# # of the documents with itself. Remember that the cosine of 0 is 1.

# # A computer program is said to learn from experience E with respect to some task T and some performance measure P, if its performance on T, as measured by P, improves with experience E.” — Tom Mitchell, Carnegie Mellon University

# # for each document:

# #     A related function is argsort, which instead returns the `indices` of the
# #     sorted elements.

# #     los indices [:-100:-1] se utilizan para, recordar la forma [from:to:by] 
# #         from = the begining
# #         to = -100
# #         by -1

# #     in this case the begining is -1 (the last element), then -2 ... and so on.
# #     The indexes are sorted backwards until 100 elements are reached. Keeping only
# #     the 100 most relevant tokens.

# #     [(cosine_similarities[idx][i], ds['id'][i]) for i in similar_indices] 
# #         genera una lista de tuples, donde (A, B)
# #             A - el valor de la matriz de distancias, o sea desde el documento
# #             iterado, hacia todos los documentos listados como menores en el índice
# #             B - Te dice qué documento es. Obviamente el primero en la lista
# #             siempre va a ser el mismo documento evaluado, pues la distancia consigo
# #             mismo siempre es 1.

# #     Por la razón mencionada en B, el último paso es retirar el elemento que está
# #     en el primer índice para que los documentos no se consideren a sí mismos.

# #     similar_items[1:]

# # """

# # print(tf)
# # print('-----------------------')

# # tfidf_matrix = tf.fit_transform(ds['description'])

# # print(tfidf_matrix)
# # print('-----------------------')

# # cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)


# # print(cosine_similarities)
# # print(cosine_similarities.shape)
# # print('-----------------------')

# # results = {}
# # for idx, row in ds.iterrows():
# #     similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
# #     similar_items = [(cosine_similarities[idx][i], ds['id'][i]) for i in similar_indices] 
# #     results[row['id']] = similar_items[1:]

# # print(pd.DataFrame(results))

# # # def item(id):  
# # #     return ds.loc[ds['id'] == id]['description'].tolist()[0].split(' - ')[0]

# # # # Just reads the results out of the dictionary.
# # # def recommend(item_id, num):
# # #     print("Recommending " + str(num) + " products similar to " + item(item_id) + "...")   
# # #     print("-------")
# # #     recs = results[item_id][:num]
# # #     print(recs); exit()
# # #     for rec in recs: 
# # #         print("Recommended: " + item(rec[1]) + " (score:" +      str(rec[0]) + ")")

