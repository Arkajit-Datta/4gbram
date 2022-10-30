from distutils.log import debug
from mimetypes import init
from urllib import request
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from pydantic import BaseModel
import logging
import uvicorn
import shutil
import os   
from commentry.getcomment import GetComment
from commentry.predict import PredictComment
import uuid
import time
from driver_analysis.pickcsv import PickCsv
logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s] %(levelname)s: %(message)s"
)
logger = logging.getLogger(__name__)
logging.getLogger("pipeline").setLevel(logging.INFO)

app = FastAPI(title="Chaarminar", version="1.0.0")

#CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

    
@app.get("/commentry")
def commentry():
    comment = GetComment()
    new,path = comment.checkdb_commentry()
    if new == 0:
        return {
            'status': 200,
            'result':{
                "new": new
            }
        }
    else:
        return {
            'status': 200,
            'result':{
                "new": new,
                "path": path
            }
        }


@app.post('/goals')
def goals(slat: float = Form(...),
            slong: float = Form(...),
            dlat: float = Form(...),
            dlong: float = Form(...)):
    time.sleep(2)
    # generating the goals

    #starting the ride
    start_ride()
    return{
        'status':200,
        'result':
        [
            {'name':'bot', 'status':False},
            {'name':'bot','status':False},
            {'name':'bot','status':False},
            {'name':'bot','status':False},
            {'last':[{"name":"croma","location":{'lat': 28.7010461, 'lng': 77.1358362}, "rating":4.7},{"name":"croma","location":{'lat': 28.7010461, 'lng': 77.1358362}, "rating":4.7},{"name":"croma","location":{'lat': 28.7010461, 'lng': 77.1358362}, "rating":4.7}],'status':False}
        ]
    }

def start_ride():
    pick = PickCsv('/home/anirudh/Desktop/4gbram/backend/driver_analysis/c1can_2020_01_14_02_evening.csv')
    time.sleep(0.5)
    r_no = 0
    sending_to_commentry = []
    try:
        if r_no%40 == 0:
            obj = PredictComment()
            obj.predict(sending_to_commentry)
        row_data = pick.get_data(r_no)
        sending_to_commentry.append(row_data)
        r_no+=1
    except Exception as e:
        pass

# def generate_job_id():
#     try:
#         logging.info("generating unique job id")
#         id = uuid.uuid4().hex
#         return id[::2][:10]
#     except Exception as e:
#         logging.error(e)
#         logging.error("error generating unique job_id")


if __name__ == "__main__":
    uvicorn.run(
        app,
        port=5000,
        host="127.0.0.1",
    )


