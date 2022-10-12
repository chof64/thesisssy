"""

"""
import asyncio
import aiofiles
import json


class TempFunctions:
    """"""

    async def save_to_file(dictionary: dict, file_path: str):
        """"""
        async with aiofiles.open(file_path, mode="w") as file:
            await file.write(json.dumps(dictionary, indent=2))
