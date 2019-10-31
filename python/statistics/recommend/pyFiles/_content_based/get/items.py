#!/usr/bin/env python
# coding=utf-8

# Loading the datasets.
# ------------------------------------------------------------------------------

import pandas as pd

class ImportItems(object):
    """ Importing the items."""
    def __init__(self):
        self.filename = './data/items.csv'

    def main(self):
        articles = pd.read_csv(self.filename, index_col=[0])
        mask = articles['eventType'] == 'CONTENT SHARED'
        articles = articles[mask].reset_index(drop=True)
        return articles

# ------------------------------------------------------------------------------

def main():
    ContentBasedFiltering().main()

# ------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
