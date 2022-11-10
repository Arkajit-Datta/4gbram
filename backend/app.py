from concurrent.futures import thread
import concurrent.futures
from fastapi import FastAPI, File, UploadFile, Form, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from pydantic import BaseModel
import logging
import uvicorn
import asyncio
import shutil
import os
from CsvParser.CsvParser import CsvParser   
from commentry.getcomment import GetComment
from commentry.predict import PredictComment
import uuid
import time
from driver_analysis.pickcsv import PickCsv
from FindPatners.FindPatners import FindPatners, GetTurnings
import json
from playsound import playsound
PROJ_FILE = os.path.dirname(os.path.abspath(__file__))


logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s] %(levelname)s: %(message)s"
)
logger = logging.getLogger(__name__)
logging.getLogger("pipeline").setLevel(logging.INFO)

app = FastAPI(title="4GBRam", version="1.0.0")

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
        os.system('mpg123 ' + path)
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
    findpatners = FindPatners(slat, slong, dlat, dlong)
    places = findpatners.get_place()
    
    get_turnings = GetTurnings(slat, slong, dlat, dlong)
    turnings = get_turnings.turnings
    path = PROJ_FILE + '/CsvParser/db.json'
    with open(path,"r") as f:
        prev_json = json.load(f)
    
    csvparser = CsvParser('/home/anirudh/Desktop/4gbram/backend/driver_analysis/c1can_2020_01_14_02_evening.csv')
    csvparser.parse(turnings)
    
    with open(path,"r") as f:
        curr_json = json.load(f)
    
    Mileage_Goal = "Mileage: " + str(prev_json['mileage'] + 2)
    Blinker = "Blinker Percentage to Achieve: " + str(prev_json['blinker'] + 10)
    Half_Clutch = "Half_Clutch Percentage to Achieve: " + str(prev_json['half_clutch'] - 15)
    Idling = "Idling Percentage to Achieve: " + str(prev_json['idling'] - 20)
    
    #starting the ride
    # bg = BackgroundTasks()
    # bg.add_task(start_ride,'dgds')
    # with concurrent.futures.ThreadPoolExecutor() as executor:
    #     p = executor.submit(start_ride)
    #     print(p.result())
    with open(PROJ_FILE + '/commentry/db.json','r') as f:
        j = json.load(f)
    f.close()
    with open(PROJ_FILE + '/commentry/db.json','w') as f:
        j['share'] = '/home/anirudh/Desktop/4gbram/backend/driver_analysis/c1can_2020_01_14_02_evening.csv'
        json.dump(j,f)    
    f.close()
    return {
        'status':200,
        'result':
        [
            {'name':Mileage_Goal, 'status':False},
            {'name':Blinker,'status':False},
            {'name':Half_Clutch,'status':False},
            {'name':Idling,'status':False},
            {'last': places, 'status': False}
        ]
    }

def start_ride():
    pick = PickCsv('/home/anirudh/Desktop/4gbram/backend/driver_analysis/c1can_2020_01_14_02_evening.csv')
    time.sleep(0.5)
    r_no = 1
    sending_to_commentry = []
    obj = PredictComment()
    while True:
        try:
            time.sleep(0.5)
            if r_no%28 == 0:
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


