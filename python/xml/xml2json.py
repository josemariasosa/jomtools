#!/usr/bin/env python
# coding=utf-8

# ------------------------------------------------------------------------------
# Turn from XML to JSON format
# ------------------------------------------------------------------------------
# jose maria sosa

import xml.etree.ElementTree as ET


class Xml2Json(object):
    
    """ Format a XML file into a JSON.
    """

    def __init__(self):
        
        self.id_keys = [
            'id_key_1',
            'id_key_2',
            'id_key_3'
        ]

    # --------------------------------------------------------------------------

    def convert(self, file_path):

        tree = ET.parse(file_path)
        root = tree.getroot()

        aces = []
        for node in root:
            new_app = {}
            qual_list = []
            desc_list = []
            if node.tag == 'App':
                for childnode in node:
                    if childnode.tag in self.id_keys:
                        _id = childnode.attrib['id']
                        if _id.isdigit():
                            new_app[childnode.tag] = int(_id)

                    if childnode.tag == 'Part':
                        new_app['Part'] = childnode.text.lower().strip()

                    if childnode.tag == 'Qual':
                        for qual in childnode:
                            if qual.text is not None:
                                t = qual.text.lower().strip()
                                qual_list.append(t)
                                qual_list = list(set(qual_list))
                        new_app['Qual'] = qual_list

                    if childnode.tag == 'Qty':
                        t = childnode.text.lower().strip()
                        if t.isdigit():
                            new_app['Qty'] = int(t)

                    if childnode.tag == 'Note':
                        t = childnode.text.lower().strip()
                        desc_list.append(t)
                        desc_list = list(set(desc_list))

                if len(desc_list) > 0:
                    new_app['Desc'] = desc_list 
                aces.append(new_app)

        return aces

    # --------------------------------------------------------------------------
# ------------------------------------------------------------------------------


def main():

    file = './dataPool/xml_file.xml'
    results = Xml2Json().convert(file)

    print results

# ------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
