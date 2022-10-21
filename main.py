from fastapi import FastAPI, File, UploadFile
import aiofiles

# import src.package.excel_data_extraction.main.ExcelDataExtraction as excel_data_extraction
from src.package.excel_data_extraction.main import ExcelDataExtraction

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/upload")
async def pds_upload(file: UploadFile = File(...)):

    # For testing, save the file to the `test` directory
    # TODO: Remove this line in production.
    async with aiofiles.open(f"./test/{file.filename}", "wb") as f:
        content = await file.read()
        await f.write(content)

    return {"message": "File uploaded successfully", "filename": file.filename}


@app.post("/extract")
async def pds_extract(file: UploadFile = File(...), map=None):
    """
    Accepts a the pds from the frontend, and extracts the data from it.

    Args:
        file (UploadFile): The file to be extracted.
        map (dict): Optional. A map of the data to be extracted.
    """
    # file = await file.read()

    # TODO: Pass the file to the extractor.

    extracted = await ExcelDataExtraction.extract(await file.read(), map)

    # TODO: Return the extracted data to the frontend as JSON.

    # TODO: Remove this line before testing.
    return extracted
