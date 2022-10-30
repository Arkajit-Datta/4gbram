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
    try:
        new,path = comment.checkdb_commentry()
    except:
        new = comment.checkdb_commentry()
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
    time.sleep(0.1)
    r_no = 1
    sending_to_commentry = []
    obj = PredictComment()
    while True:
        try:
            #time.sleep(0.1)
            if r_no%30 == 0:
                obj.predict(sending_to_commentry)
                sending_to_commentry.clear()
            row_data = pick.get_data(r_no)
            row_data = row_data.values.tolist()
            sending_to_commentry.append(row_data[0])
            r_no+=1
            print(r_no)
        except Exception as e:
            print('exception' + str(e))
            break


if __name__ == "__main__":
    uvicorn.run(
        app,
        port=5000,
        host="127.0.0.1",
    )


