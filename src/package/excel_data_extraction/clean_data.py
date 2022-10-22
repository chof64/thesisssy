"""
This module is the low level function that will clean the excel data.
"""

import json
import re
from array import array

import aiofiles


class CleanData:
    """"""

    async def _mapping(override_map: array = None):
        """
        Utility function that returns the default mapping of the data,
        with the optional override_coord.

        args:
            @override_coord - (Optional) The coordinate of the data to be
                               override.
        """
        async with aiofiles.open("./test/config/clean_config.json", "r") as file:
            config = await file.read()
            config = json.loads(config)

        coord = config["default_map"]

        if override_map != None:
            for item in override_map:
                index = [i for i, x in enumerate(coord) if x["sheet"] == item["sheet"]][
                    0
                ]
                for key in item:
                    coord[index][key] = item[key]

        mappings = []

        for sheet in coord:
            sheet_map = {"sheet": sheet["sheet"], "data": []}

            for item in sheet["data"]:
                converted_coord = re.findall(r"[A-Za-z]+|\d+", item["coord"])
                sheet_map["data"].append(
                    {
                        "name": item["name"],
                        "coord": item["coord"],
                        "column": config["letter_mapping"][converted_coord[0]],
                        "row": str(int(converted_coord[1]) - 2),
                    }
                )

            mappings.append(sheet_map)

        return mappings

    async def clean(raw_json, override_coord: array = None):
        """
        Low level function that will clean the raw json data using the
        mapping provided.

        args:
            @raw_json - The raw json data.
            @override_coord - The mapping of the data.

        return: dictionary
        """
        clean_json = {}
        mappings = await CleanData._mapping(override_coord)

        for sheet in mappings:
            for item in sheet["data"]:
                index = [
                    i for i, x in enumerate(raw_json) if x["sheet"] == sheet["sheet"]
                ][0]

                clean_json[item["name"]] = raw_json[index]["data"][item["column"]][
                    item["row"]
                ]

        return clean_json
