from fastapi import FastAPI, File, UploadFile

from src.package.excel_data_extraction.main import ExcelDataExtraction

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
