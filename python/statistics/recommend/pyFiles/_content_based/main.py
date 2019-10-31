#!/usr/bin/env python
# coding=utf-8

# Example for Content-based filtering method.
# ------------------------------------------------------------------------------

import pandas as pd
import rubik as rk

from mod.content import ContentBasedModel
from get.interactions import ImportInteractions
from get.items import ImportItems


class ContentBasedFiltering(object):
    """ Content-based filtering method."""
    def filter_interactions(self, items, interactions):
        known_items = items['contentId']
        interacted_items = interactions['contentId']

        mask = interacted_items.isin(known_items)
        return interactions[mask].reset_index(drop=True)

    def main(self):
        items = ImportItems().main()
        interactions = ImportInteractions().main()
        interactions = self.filter_interactions(items, interactions)

        ContentBasedModel().main(items, interactions)

# ------------------------------------------------------------------------------

def main():
    ContentBasedFiltering().main()

# ------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
