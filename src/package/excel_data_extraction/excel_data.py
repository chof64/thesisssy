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

    def __init__(self, file_path: str = None):
        self.file_path = file_path

    async def get_excel_data(self, file_object=None):
        """
        This will get the excel data using aiofiles to make the function
        async. And pass the data to pandas to be converted into a dataframe.

        args:
            @file_object - (Optional) The file object from Excel file.

        returns: pandas dataframe
        """
        # ? If file_object arg is not passed, use file_path of the class.
        if self.file_path != None:
            dataframe = pd.read_excel(self.file_path)
            return dataframe

        # TODO: Revisit to remove or keep.
        dataframe = pd.read_excel(file_object)
        return dataframe

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
