# support for file upload:
# pipenv install python-mulitpart

from fileinput import filename
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel
import pandas as pd
from io import StringIO
import tempfile
from typing import Union


# import python modules
from handler import sum_up
from file_creator import create_html_plot, create_plot_using_values


class ProcValues(BaseModel):
    group1: str
    group2: str
    title: Union[str, None] = "The Plot"


app = FastAPI()


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    content = await file.read()
    return {"contents": content}



@app.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...)):
    df_by_csv = pd.read_csv(StringIO(str(file.file.read(), "utf-8")), encoding="utf-8")
    print(df_by_csv)


@app.post("/upload-excel/")
async def upload_excel(file: UploadFile = File(...)):
    df_by_excel = pd.read_excel(file.file.read())
    print(df_by_excel)


# upload an excel file which gets processed
@app.post("/upload-excel-processor/")
async def receive_and_process(file: UploadFile = File(...)):
    sum_first_row = sum_up(pd.read_excel(file.file.read()))
    return {"sum_first_row": sum_first_row}

# send html file stored on disk to client
@app.get("/get-file-from-disk/")
async def file_to_client():
    file_path = "files/dummy_html.html"
    return FileResponse(file_path, media_type="text/html", filename="dummy_html_response.html")


# response html file coming from function
@app.get("/get-file-from-function/")
async def get_file_from_function():

    html_string = create_html_plot()

    with tempfile.TemporaryDirectory() as tmpdirname:
        file = open(str(tmpdirname + "sample.html"),"w")
        file.write(html_string)

        def iterfile(): 
            with open(str(tmpdirname + "sample.html"), mode="rb") as file_like:
                yield from file_like

    return StreamingResponse(iterfile(), media_type="text/html", headers={'Content-Disposition': 'attachment; filename="yourfilename.html"'})


# post values to api and use them for processing response
@app.post("/post-processing-values/")
async def processing_using_values(processing_values: ProcValues):

    # call function with arguments
    html_string = create_plot_using_values(
        group1= processing_values.group1,
        group2=processing_values.group2,
        title=processing_values.title)

    # store file in temp dir and create iterable object
    with tempfile.TemporaryDirectory() as tmpdirname:
        file = open(str(tmpdirname + "sample.html"),"w")
        file.write(html_string)

        def iterfile(): 
            with open(str(tmpdirname + "sample.html"), mode="rb") as file_like:
                yield from file_like

    return StreamingResponse(iterfile(), media_type="text/html", headers={'Content-Disposition': 'attachment; filename="yourfilename.html"'})