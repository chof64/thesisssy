"""

"""

import asyncio
import pandas as pd


class GetData:
    """
    Gets data from Excel by converting Excel file into a
    Pandas DataFrame, then converting the DataFrame into
    a JSON object.
    """

    async def get_excel_data(fileName: str):
        """Get data from Excel file."""

        df = pd.read_excel(fileName)

        return df

    async def convert_excel_to_json(dataframe: pd.DataFrame):
        """Convert Excel data to JSON."""

        # default orient is columns. Change if needed.
        return dataframe.to_json(indent=2)
