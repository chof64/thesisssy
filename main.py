import asyncio
import aiofiles

from excel_extraction.components.get_data import GetData
from excel_extraction.components.get_information import GetInformation

if __name__ == "__main__":

    async def runner():
        df = await GetData.get_excel_data("./test/assets/PDS-Lucy-2021.xlsx")
        json = await GetData.convert_excel_to_json(df)

        # # use aiofiles to save json to file
        async with aiofiles.open("./test/assets/PDS-Lucy-2021.json", "w+") as f:
            await f.write(json)

        clean_data = await GetInformation.get_specific_information(json)
        print(clean_data)

    asyncio.run(runner())
