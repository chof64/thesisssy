"""
The main entrypoint of the `excel_data_extraction` package.
This module contains the high level functions that will be used by
the application.
"""
import asyncio

from excel_data import ExcelData
from clean_data import CleanData
from temp_functions import TempFunctions


class ExcelDataExtraction:
    """
    This is the main entrypoint for the `excel_data_extraction` package.

    Functions here will utilize other low level functions in other modules
    to simplify the process and code.
    """

    def __init__(self):
        """
        self.config - add a default config values, but allow the user to override.
        """
        # self.config = config

    async def extract(self):
        """ """
        pass

    # TODO: Remove when function works as expected.
    async def test_extract(self):
        """
        This is a test
        """
        client_excel = ExcelData(file_path="./temp/PDS-Lucy-2021.xlsx")

        dataframe = await client_excel.get_excel_data()
        dictionary = await client_excel.convert_excel_to_dict(dataframe)
        await TempFunctions.save_to_file(dictionary, "./temp/pds-raw.json")

        client_clean = CleanData()
        clean_json = await client_clean.clean(dictionary)
        await TempFunctions.save_to_file(clean_json, "./temp/pds-clean.json")


if __name__ == "__main__":
    asyncio.run(ExcelDataExtraction().test_extract())
