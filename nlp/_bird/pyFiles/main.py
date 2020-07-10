#!/usr/bin/env python
# coding=utf-8

# Generate the Universe of most likely Revs for reimplementation given a user.
# ------------------------------------------------------------------------------

from bson import ObjectId

from config import db_connection

from mod.universe.level_1 import RevUniverseLevel1
from mod.universe.level_2 import RevUniverseLevel2
from mod.universe.level_3 import RevUniverseLevel3

from mod.display_results import DisplayResults


class MostLikelyRevUniverse(object):
    """Generate the Universe of most likely Revs for reimplementation given 
    a user."""

    def __init__(self):
        self.db_sat = db_connection['SiteAttribute']
        self.db_org = db_connection['Organization']
        self.db_bus = db_connection['BusinessUnit']
        self.db_com = db_connection['RevComment']
        self.db_att = db_connection['Attribute']
        self.db_acc = db_connection['Account']
        self.db_cou = db_connection['Country']
        self.db_sha = db_connection['Share']
        self.db_sit = db_connection['Site']
        self.db_rev = db_connection['Rev']

    def get_user_attributes(self, site_attributes):
        queryDB = {
            '_id': {
                '$in': site_attributes
            }
        }
        projeDB = {
            '_id': 0,
            'parentAttribute': 1
        }
        results = self.db_sat.find(queryDB, projeDB)
        results = list(results)
        if len(results) > 0:
            results = [x['parentAttribute'] for x in results]
        return results

    def transform_attributes(self, user):
        """Convert siteAttributes into the parent Attribute."""
        if 'siteAttributes' in user.keys():
            site_attributes = user['siteAttributes']
            if isinstance(site_attributes, list):
                site_attributes = list(set(site_attributes))
                attributes = self.get_user_attributes(site_attributes)
                return attributes
        return []

    def get_user_data(self, user_id):
        queryDB = {
            '_id': user_id
        }
        projeDB = {
            '_id': 1,
            'siteAttributes': 1,
            'site': 1,
            'businessUnit': 1,
            'organization': 1,
            'language': 1
        }
        results = self.db_acc.find_one(queryDB, projeDB)
        if bool(results):
            results.update({
                'parentAttribute': self.transform_attributes(results)
            })
            if not bool(results['siteAttributes']):
                results['siteAttributes'] = []
            return results

    def generate_rev_universe(self, user):
        rev_universe = {}
        rev_universe.update({
            'revs_in_level_1': RevUniverseLevel1().get(user),
            'revs_in_level_2': RevUniverseLevel2().get(user),
            'revs_in_level_3': RevUniverseLevel3().get(user)
        })
        return rev_universe

    def main(self, user_id):
        user = self.get_user_data(user_id)
        rev_universe = self.generate_rev_universe(user)
        return rev_universe

# ------------------------------------------------------------------------------

def main():
    user_id = ObjectId("5aa29adb68f26f000f5c412e")
    user_id = ObjectId("5c3e6da6677cd2001633e40f")
    user_id = ObjectId("5bf77f4a77f59e001672a21e")
    user_id = ObjectId("58b3a2d8aff91e1000d2ec1f")
    user_id = ObjectId("5b304587bc79880019e52476")
    results = MostLikelyRevUniverse().main(user_id)

    DisplayResults().print(user_id, results)
    print(results)

# ------------------------------------------------------------------------------


if __name__ == '__main__':
    main()

