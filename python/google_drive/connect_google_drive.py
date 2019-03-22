#!/usr/bin/env python
# coding=utf-8

# ------------------------------------------------------------------------------
# Connect to Google Drive API | Mi Refacción
# ------------------------------------------------------------------------------
#                                                                jose maria sosa

import json
import gspread

import pandas as pd

from config import credentials
from oauth2client.service_account import ServiceAccountCredentials


class ConnectGoogleSpreadSheet(object):

    """ Connect to the influencer's file in Google Drive.
    """
    def __init__(self, book_name, sheet_name):

        self.book_name = book_name  
        self.sheet_name = sheet_name

        # Connect to the spread sheet.
        self.connectToSpreadSheet() 

    # --------------------------------------------------------------------------

    def numberToLetters(self, q):

        """ Use this function to select a range of cells ('A1:B4' for example)
        """

        q = q - 1
        result = ''

        while q >= 0:
            remain = q % 26
            result = chr(remain+65) + result;
            q = q//26 - 1

        return result

    # --------------------------------------------------------------------------

    def connectToSpreadSheet(self):

        """ General script to connect to a google spread sheet.
        """

        # Google Drive Credentials.
        scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name(credentials, scope)

        client = gspread.authorize(creds)
        sheet = client.open(self.book_name).worksheet(self.sheet_name)

        # Turn sheet into an attribute.
        self.sheet = sheet

        return None

    # --------------------------------------------------------------------------

    def updateAllTable(self, results):

        """ Get and format the data from Google Analytics.
        """

        # Reshape the old Spreadsheet.
        num_lines, num_columns = results.shape
        self.sheet.resize(rows=num_lines+1)

        # Select the list of cells.
        cells = 'A2:' + self.numberToLetters(num_columns) + str(num_lines + 1)
        cell_list = self.sheet.range(cells)

        # Modifying the values in the range.
        for cell in cell_list:
            val = results.iloc[cell.row-2,cell.col-1]
            cell.value = val

        # Update in batch. Setting up parameters.
        limit = len(cell_list)
        batch_size = 20000 # The batch size was arbitrarily selected, but it works.
        range_init = 0
        range_end = batch_size

        while limit > 0:
            new_list = cell_list[range_init:range_end]
            self.sheet.update_cells(new_list)

            range_init = range_init + batch_size
            range_end = range_end + batch_size
            limit = limit - batch_size

        return None

    # --------------------------------------------------------------------------
    
    def getAllTable(self):

        table = self.sheet.get_all_values()
        headers = table.pop(0)

        table = pd.DataFrame(table, columns=headers)

        return table

    # --------------------------------------------------------------------------
# ------------------------------------------------------------------------------


