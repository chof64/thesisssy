from fastapi import FastAPI, File, UploadFile, Form
from pydantic import BaseModel
import aiohttp

from src.package.excel_data_extraction.main import ExcelDataExtraction


class JSONData(BaseModel):
    file_url: str
    file_name: str
    map: dict


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/extract")
async def pds_extract(file: UploadFile = File(...), map=None):
    """
    Accepts a the pds from the frontend, and extracts the data from it.

    Args:
        file (UploadFile): The file to be extracted.
        map (dict): Optional. A map of the data to be extracted.
    """

    extracted = await ExcelDataExtraction.extract(await file.read(), map)

    return extracted


# Accepts JSON dictionary
@app.post("/extract/json")
async def pds_extract_json(data: JSONData):
    """ """

    async with aiohttp.ClientSession() as session:
        async with session.get(data.file_url) as resp:
            # open the file and store in a variable
            file = await resp.read()

    extracted = await ExcelDataExtraction.extract(file, data.map)
    return extracted
