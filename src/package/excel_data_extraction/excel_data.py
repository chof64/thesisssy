"""
The main module that interact with the excel file and extract the data
needed by other package module.
"""
import asyncio
import pandas as pd
import aiofiles
import json


class ExcelData:
    """
    This class contains functions that will interact directly with the
    excel file.
    """

    # def __init__(self):

    async def get_excel_data(file=None):
        """
        This will get the excel data using aiofiles to make the function
        async. And pass the data to pandas to be converted into a dataframe.

        args:
            @file_object - (Optional) The file object from Excel file.

        returns: dictionary
        """
        # dataframe = pd.read_excel(file)

        xls = pd.ExcelFile(file)

        all_sheets = []

        for sheet in xls.sheet_names:
            dataframe = pd.read_excel(xls, sheet_name=sheet)
            metadata = {"sheet": sheet, "data": json.loads(dataframe.to_json())}

            all_sheets.append(metadata)

        return all_sheets

    # TODO: Consider merging this function with get_excel_data.
    async def convert_excel_to_dict(self, dataframe):
        """
        This will convert the pandas dataframe into a dictionary.

        args:
            @dataframe - The dataframe to be converted.

        returns: dictionary
        """
        dictionary = json.loads(dataframe.to_json())

        return dictionary
