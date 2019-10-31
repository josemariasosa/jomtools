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

Download the files and put them in the correct location. When everything is ready, run the following command.

```bash
bash main.sh
```

### 2. Importing the data

When you run the script, like in the set-up, the first file that it is going to run is the `main.py`. Which contains a single class, **ContentBasedFiltering()**, that import all the data:

- The **items**. The unit of content that are going to be recommend. It could be music, text articles, movies, etc.
- The **interactions**. Is the relation that exists between the items and the users.

When the data is imported, it goes through a preprocess. The scrips to import and preprocess the data are located in the `get/` directory, and are called as follow.

```python
from get.interactions import ImportInteractions
from get.items import ImportItems
```

### 3. Content-Based Method using python

The most interesting part of this script is the content-based method. It is located in the `mod/` directory, and is called as follow:

```python
from mod.content import ContentBasedModel
```

The content-based method has 3 principal steps, as presented in the main function of the class **ContentBasedModel()**.

1. Get TF-IDF matrix.
2. Build the a profile for every single user.
3. From the model, get user profile and recommendations.

Let's go in detail for each step.

### 4. Get TF-IDF matrix.

The TF-IDF model is created using the **TfidfVectorizer()** function, imported as follow:

```python
from sklearn.feature_extraction.text import TfidfVectorizer
```

When we generate a model and the fit some data to that model, these are the steps that we conceptually do.

```python
tf =  TfidfVectorizer(analyzer='word',
                      ngram_range=(1, 2),
                      min_df=0.003,
                      max_df=0.5,
                      max_features=5000,
                      stop_words=stopwords_list)
tfidf_matrix = tf.fit_transform(text)
```

1. Suppose we have an array of documents. Each document contains a single text string, for example: "In order to work accurately, this type of filter needs rates, and not all users rate products constantly."

2. The text, for every document, is standardized and tokenized, this is, for every text a list of tokens is generated. The **stopwords list** is a list of words that will be ignored, because they do not add any information to the sentence. Stopwords are simply words that add no significant value to our system, like ‘an’, ‘is’, ‘the’, and hence are ignored by the system. `l = ['order', 'work', 'accurately', 'type', 'filter', 'needs', 'rates', 'not', 'all', 'users', 'rate', 'products', 'constantly'].`

3. This process generate a token list for every single document. The result of this process is the `tfidf_matrix`. This matrix, instead of showing the tokens or the documents, it only present us a **token_id** and a **document_id**.

The output of the model is called: **sparse matrix**, the output looks different 
compared to printing a standard dense matrix. See below the main components:

- A tuple represents the document_id and the token_id: (document_id, token_id).
- The value following the tuple represents the tf-idf score of any given token in a given document.
- The tuples that are not there have a tf-idf score of 0.
- If you want to find what token the token_id corresponds to, check the get_feature_names method.

```text
(0, 1123) 0.34234
(0, 324)  0.1001           <- sparse matrix
```

From this example, the 0 represent the original text (the index of the document). The 1123 makes reference to the token, for example, 1123 could make reference to the token 'order' and 324 to the token 'work'. On the far right, we have the raiting Tf-Idf, that measures the relevance of the token within the documents.

As we saw, the sparse matrix contains the information coded with ids. That's the reason why we need 2 more pieces of information in order to decode, and be able to use this matrix:

```python
    return {
        'tfidf_matrix': tf.fit_transform(text),
        'tfidf_feature_names': tf.get_feature_names(),
        'tfidf_items_id_index': items['contentId'].tolist()
    }
```

The returned object contains the `tfidf_matrix`, and also a list containing all the tokens `tfidf_feature_names`, and also a list with all the documents `tfidf_items_id_index`. Notice that the id for the tokens and for the documents is the index (the position) in the list.

This is the code to build the TF-IDF matrix.

```python
    def get_tfidf(self, items):
        """ The 'text' variable have a pandas Series with the concatenated
            text from all the items.
        """
        stopwords_list = (stopwords.words('portuguese')
                          + stopwords.words('english'))
        tf =  TfidfVectorizer(analyzer='word',
                              ngram_range=(1, 2),
                              min_df=0.003,
                              max_df=0.5,
                              max_features=5000,
                              stop_words=stopwords_list)
        text = items['title'] + ' ' + items['text']
        return {
            'tfidf_matrix': tf.fit_transform(text),
            'tfidf_feature_names': tf.get_feature_names(),
            'tfidf_items_id_index': items['contentId'].tolist()
        }
```

**Improving the Tf-Idf results**

The tokenization process is up for multiple improvements. Bad spelled words, specially in a context when the user could have several errors, impact in a bad way the results of the model.

A more **tailored** preprocess could be used to standardize the input we are using from the user. Also, there are "language models" for spanish and english that could help obtaining better results.

### 5. Build the a profile for every single user.

What we did, to get the user profile, is to group all the user interactions and apply a function, **get_user_profile()**, to all the group of items a user have interacted with. The first steps in this function is to get the indexes of the items the user have interacted with `tdidf_index`, and the strength (weight) of those items `items_strength`. The **reshape** method help us generate a matrix with the shape (N, 1), from an array of length N.

```python
    get_tdidf_index = lambda x: tfidf['tfidf_items_id_index'].index(x)
    tdidf_index = df['contentId'].map(get_tdidf_index).tolist()
    items_strength = np.array(df['eventStrength'].tolist())
    items_strength = items_strength.reshape(-1, 1)
```

For each item, a subset of the tfidf matrix is generated using list comprehension. Then all the matrix are stacked using `scipy`.

```python
    tfidf_matrix = tfidf['tfidf_matrix']
    items_profile = [tfidf_matrix[idx:idx+1] for idx in tdidf_index]
    item_profiles = scipy.sparse.vstack(items_profile)
```

At last, The weighted average of the items profiles by the interactions stregth is calculated.

```python
    weighted = (np.sum(item_profiles.multiply(items_strength), axis=0)
                / np.sum(items_strength))
    normalized = sklearn.preprocessing.normalize(weighted)
```

Let's follow, that code, step by step:

- Step 1. Multiply each strenght by the token tf-idf calculations. Code: `item_profiles.multiply(items_strength)`. The variable `item_profiles`, remember that is the stacked tfidf matrix, has N rows (N is the number of interacted items) and T columns (T is the number of tokens). And `items_strength` is a matrix that has (N, 1) dimensions.

- Step 2. Sum all the token-values using np.sum with axis=0, check the example:

```python
    >>> np.sum([[0, 1], [0, 5]], axis=0)
    array([0, 6])
    >>> np.sum([[0, 1], [0, 5]], axis=1)
    array([1, 5])
```

- Step 3. Divide the resultant vector with the scalar resultant from `np.sum(items_strength)`

**Normalization and standardization**

**Normalization** is the process of scaling individual samples to have unit norm. In basic terms you need to normalize data when the algorithm predicts based on the weighted relationships formed between data points. Scaling inputs to unit norms is a common operation for text classification or clustering.

The normalize and Normalizer methods, from `sklearn.preprocessing`, accept both dense array-like and sparse matrices from scipy.sparse as input.

The boring definition of Normalization, mathematical approach would be:

- Normalization is performed on data to remove amplitude variation and only focus on the underlying distribution shape.

- Normalization is performed on data to compare numeric values obtained from different scales.

We often want to compare scores or sets of scores obtained on different scales. For example, how do we compare a score of 85 in a cooking contest with a score of 100 on an I.Q. test? In order to do so, we need to “eliminate” the unit of measurement, this operation is called to normalize the data. There are two main types of normalization. The first first type of normalization originates from linear algebra and treats the data as a vector in a multidimensional space. In this context, to normalize the data is to transform the data vector into a new vector whose norm (i.e., length) is equal to one. The second type of normalization originates from statistics, and eliminates the unit of measurement by transforming the data into new scores with a mean of 0 and a standard deviation of 1. These transformed scores are known as Z-scores.

In basic terms you need to normalize data when the algorithm predicts based on the weighted relationships formed between data points.

At least, three methods for normalization exist:

Using **norm="max"**:

Max is quite similar to Min Max normalization. The only difference being is that the the normalized values will fall between a range of 1 and to a value less than or equal to 0.

Using **norm="l1" (Least Absolute Deviation or LAD)**:

L1 is basically minimizing the sum of the absolute differences (S) between the target value (x) and the estimated values (x’).
To understand it easily, its just adding all the values in the array and dividing each of it using the sum.

Using **norm="l2" (Least Square Error or LSE)**:

This one runs by default. L2 minimizes the sum of the square of the differences (S) between the target value (x) and the estimated values (x’). Or in simpler terms, just divide each value by δ. Where δ is nothing but the square root of the sum of all the squared values.

**Standardization** of datasets is a common requirement for many machine learning estimators implemented in scikit-learn; they might behave badly if the individual features do not more or less look like standard normally distributed data: Gaussian with zero mean and unit variance.

One of the key differences between scaling (e.g. standardizing) and normalizing, is that normalizing is a row-wise operation, while scaling is a column-wise operation.

1. Normalization makes training less sensitive to the scale of features, so we can better solve for coefficients.

2. Standardizing tends to make the training process well behaved because the numerical condition of the optimization problems is improved.

Know more about the difference about: [**Normalizing and Standardizing**](https://personal.utdallas.edu/~herve/abdi-Normalizing2010-pretty.pdf).

The code to get the users profile is:

```python
    def build_users_profile(self, items, interactions, tfidf):
        def get_user_profile(df):
            get_tdidf_index = lambda x: tfidf['tfidf_items_id_index'].index(x)
            tdidf_index = df['contentId'].map(get_tdidf_index).tolist()
            items_strength = np.array(df['eventStrength'].tolist())
            items_strength = items_strength.reshape(-1, 1)

            # For each item, get a subset of the tfidf matrix.
            tfidf_matrix = tfidf['tfidf_matrix']
            items_profile = [tfidf_matrix[idx:idx+1] for idx in tdidf_index]
            item_profiles = scipy.sparse.vstack(items_profile)

            # Weighted average of items profiles by the interactions strength.
            weighted = (np.sum(item_profiles.multiply(items_strength), axis=0)
                        / np.sum(items_strength))
            normalized = sklearn.preprocessing.normalize(weighted)
            return {
                'user_profile': normalized
            }
        return (interactions.groupby('personId')['contentId','eventStrength']
                            .apply(get_user_profile)
                            .rename('user_profile'))
```

### 6. From the model, get user profile and recommendations.

Distance metrics are functions d(a, b) such that d(a, b) < d(a, c) if objects a and b are considered “more similar” than objects a and c.

The **Euclidean distance** rules:

1. d(a, b) >= 0, for all a and b
2. d(a, b) == 0, if and only if a = b, positive definiteness
3. d(a, b) == d(b, a), symmetry
4. d(a, c) <= d(a, b) + d(b, c), the triangle inequality

The ultimate reason behind using cosine is that the value of cosine will increase as the angle between vectors with decreases, which signifies more similarity. The vectors are length-normalized, after which they become vectors of length 1.

**Cosine similarity** is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the
Euclidean distance (due to the size of the document), chances are they may still
be oriented closer together. The smaller the angle, higher the cosine similarity.

To compute the cosine similarity, you need the word count of the words in each
document. The CountVectorizer or the TfidfVectorizer from scikit learn lets us
compute this. The output of this comes as a sparse_matrix.

Even better, I could have used the TfidfVectorizer() instead of CountVectorizer(),
because it would have downweighted words that occur frequently across documents.

1. Now we have the TF-IDF matrix (tfidf_matrix) for each document (the number of rows of the matrix) with 11 tf-idf terms (the number of columns from the matrix), we can calculate the Cosine Similarity between the first document (“The sky is blue”) with each of the other documents of the set.

2. The tfidf_matrix[0:1] is the Scipy operation to get the first row of the sparse matrix and the resulting array is the Cosine Similarity between the first document with all documents in the set. Note that the first value of the array is 1.0 because it is the Cosine Similarity between the first document with itself. Also note that due to the presence of similar words on the third document (“The sun in the sky is bright”), it achieved a better score.

The result of linear_kernel and cosine_similarities is a matrix with the computations of the distances among all the documents.

```python
distance = [[1.  0.10  0.06  0.06  0.05  0.06]
            [0.10  1.  0.41  0.03  0.06  0.06]
            [0.06  0.41  1.  0.03  0.04  0.05]
            [0.06  0.03  0.03  1.  0.04  0.04]
            [0.06  0.06  0.04  0.04  1.  0.36]
            [0.06  0.06  0.05  0.04  0.36  1.]]
(6, 6)
```

See how all the distance from the principal diagonal are 1 due to the comparison of the documents with itself. Remember that the cosine of 0 is 1.

> A computer program is said to learn from experience E with respect to some task T and some performance measure P, if its performance on T, as measured by P, improves with experience E.” — Tom Mitchell, Carnegie Mellon University

Taken steps in the script:

For each document a related function is argsort, which instead returns the `indices` of the sorted elements.

```python
    # Gets the top similar items.
    similar_idx = cossim.argsort().flatten()[-topn:]
    # Sort the similar items by similarity.
    tfidf_index = tfidf['tfidf_items_id_index']
    similar_items = [(tfidf_index[i], cossim[0,i]) for i in similar_idx]
    similar_items = sorted(similar_items, key=lambda x: -x[1])
```

Generate a list of tuples, where (A, B):

A - is the value of the distances matrix.
B - is the document id.

Since the the document will always have the less distance with itself it is removed from the vector using the index:

```python
similar_items[1:]
```

The code for get the computations of the distance is:

```python
    def print_user_profile(self, user_id, tfidf,
                           users_profile, print_output=False):
        if print_output:
            test_profile = users_profile[user_id]['user_profile'].flatten()
            test_profile = test_profile.tolist()
            test_profile = zip(tfidf['tfidf_feature_names'], test_profile)
            test_profile = sorted(test_profile, key=lambda x: -x[1])
            test_profile = pd.DataFrame(test_profile,
                                        columns=['token', 'relevance'])
            print(test_profile.head(20))

    def get_interacted_items(self, user_id, interactions):
        mask = interactions['personId'] == user_id
        interacted_items = interactions.loc[mask, 'contentId']
        return set(interacted_items if type(interacted_items) == pd.Series else
            [interacted_items])

    def get_similar_items_to_user_profile(self, user_id, tfidf,
                                          users_profile, topn=1000):
        """ Computes the cosine similarity (cossim) between the user profile
        and all item profiles. """
        single_user_profile = users_profile[user_id]['user_profile']
        cossim = cosine_similarity(single_user_profile,
                                   tfidf['tfidf_matrix'])

        # Gets the top similar items.
        similar_idx = cossim.argsort().flatten()[-topn:]
        # Sort the similar items by similarity.
        tfidf_index = tfidf['tfidf_items_id_index']
        similar_items = [(tfidf_index[i], cossim[0,i]) for i in similar_idx]
        similar_items = sorted(similar_items, key=lambda x: -x[1])
        return similar_items

    def get_recommended_items(self, user_id, tfidf, users_profile,
                              interactions, topn=10):
        """ First, get the content the user have already interact with!"""
        items_to_ignore = self.get_interacted_items(user_id, interactions)
        similar_items = self.get_similar_items_to_user_profile(user_id,
                                                               tfidf,
                                                               users_profile)
        similar_items_filtered = [x for x in similar_items 
            if x[0] not in items_to_ignore]

        return (pd.DataFrame(similar_items_filtered,
                             columns=['contentId', 'recStrength'])
                  .head(topn))
```
