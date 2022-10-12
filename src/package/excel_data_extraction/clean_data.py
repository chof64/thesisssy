"""
This module is the low level function that will clean the excel data.
"""

from array import array
import asyncio
import json
import re

import aiofiles


class CleanData:
    """"""

    def __init__(self):
        pass

    async def _mapping(self, override_coord: array = None):
        """
        Utility function that returns the default mapping of the data,
        with the optional override_coord.

        args:
            @override_coord - (Optional) The coordinate of the data to be
                               override.
        """
        async with aiofiles.open("./temp/mapping_config.json", "r") as file:
            config = await file.read()
            config = json.loads(config)

        coord = config["default_pds"]

        # TODO: Check if override_coord is working properly
        if override_coord != None:
            for map in override_coord:
                coord[map["name"]] = map["coord"]

        mappings = []

        for item in coord:
            map = {}
            map["name"] = item["name"]
            map["coord"] = item["coord"]

            converted_coord = re.findall(r"[A-Za-z]+|\d+", item["coord"])
            map["column"] = config["letter_mapping"][converted_coord[0]]
            map["row"] = str(int(converted_coord[1]) - 2)

            mappings.append(map)

        return mappings

    async def clean(self, raw_json, override_coord: array = None):
        """
        Low level function that will clean the raw json data using the
        mapping provided.

        args:
            @raw_json - The raw json data.
            @override_coord - The mapping of the data.

        return: dictionary
        """
        clean_json = {}
        mappings = await self._mapping(override_coord)

        for map in mappings:
            clean_json[map["name"]] = raw_json[map["column"]][map["row"]]

        return clean_json
