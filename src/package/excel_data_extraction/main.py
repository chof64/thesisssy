"""
The main entrypoint of the `excel_data_extraction` package.
This module contains the high level functions that will be used by
the application.
"""

from .clean_data import CleanData
from .excel_data import ExcelData


class ExcelDataExtraction:
    """
    This is the main entrypoint for the `excel_data_extraction` package.

    Functions here will utilize other low level functions in other modules
    to simplify the process and code.
    """

    async def extract(file, override_map=None):
        """
        Called by the `/extract` endpoint.

        This will extract the data from the excel file and return it as JSON.

        Args:
            file (UploadFile): The file to be extracted.
            map (dict): Optional. A map of the data to be extracted.
        """

        excel_data = await ExcelData.get_excel_data(file)
        clean_data = await CleanData.clean(excel_data, override_map)

        return clean_data
