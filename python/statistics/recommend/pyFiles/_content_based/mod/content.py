#!/usr/bin/env python
# coding=utf-8

# Content-based filtering method
# -----------------------------------------------------------------------------

import scipy
import sklearn

import numpy as np
import pandas as pd

from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class ContentBasedModel(object):
    """Content-based model for Rever recommender system."""
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

    def main(self, items, interactions):
        # 1. Get TF-IDF matrix.
        tfidf = self.get_tfidf(items)
        # 2. Build the a profile for every single user.
        users_profile = self.build_users_profile(items, interactions, tfidf)
        # 3. From the model, get user profile and recommendations.
        # Print a test_user profile
        test_user_id = -1479311724257856983
        self.print_user_profile(test_user_id,
                                tfidf,
                                users_profile,
                                print_output=False)
        recommended = self.get_recommended_items(test_user_id,
                                                 tfidf,
                                                 users_profile,
                                                 interactions)
        print(recommended)

# -----------------------------------------------------------------------------
