#!/usr/bin/env python
# coding=utf-8

# Generate the Universe of most likely Revs for reimplementation given a user.
# ------------------------------------------------------------------------------

import math

import pandas as pd


class ImportInteractions(object):
    """ Import the interactions."""
    def __init__(self):
        self.filename = './data/interactions.csv'
        self.event_type_strength = {
            'VIEW': 1.0,
            'LIKE': 2.0,
            'BOOKMARK': 2.5,
            'FOLLOW': 3.0,
            'COMMENT CREATED': 4.0
        }

    def set_event_type_strength(self, interactions):
        c1 = 'eventStrength'
        c2 = 'eventType'
        set_strength = lambda x: self.event_type_strength[x]
        interactions[c1] = interactions[c2].map(set_strength)
        return interactions

    def filter_users_5_interactions(self, interactions):
        """ To avoid cold-start, we are keeping only users with, at least, 
        5 interactions."""
        user_interaction = (interactions.groupby(['personId', 'contentId'])
                                        .size()
                                        .groupby('personId')
                                        .size()
                                        .rename('total_interactions')
                                        .reset_index(drop=False))
        mask = user_interaction['total_interactions'] >= 5
        user_interaction = user_interaction[mask].reset_index(drop=True)
        usermask = sum([1 for x in mask.tolist() if x])
        interactions = pd.merge(interactions,
                                user_interaction,
                                how='right',
                                on='personId')
        return interactions

    def smooth_user_preference(self, interactions):
        def smooth(x):
            return math.log(1+x, 2)
        interactions = (interactions
                        .groupby(['personId', 'contentId'])['eventStrength']
                        .sum()
                        .apply(smooth)
                        .reset_index(drop=False))
        return interactions

    def main(self):
        interactions = pd.read_csv(self.filename, index_col=[0])
        interactions = self.set_event_type_strength(interactions)
        interactions = self.filter_users_5_interactions(interactions)
        interactions = self.smooth_user_preference(interactions)
        return interactions

# ------------------------------------------------------------------------------

def main():
    ContentBasedFiltering().main()

# ------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
