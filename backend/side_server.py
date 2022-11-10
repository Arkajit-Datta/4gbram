

import os
from commentry.predict import PredictComment
import time
from driver_analysis.pickcsv import PickCsv
import json
PROJ_FILE = os.path.dirname(os.path.abspath(__file__))

def start_ride(path):
    pick = PickCsv(path)
    time.sleep(0.1)
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
def qtask():
    initial = {"1":[],"share":""}
    with open(PROJ_FILE + '/commentry/db.json','w') as f:
        json.dump(initial,f)
    while True:
        try:
            print("Running.....")
            time.sleep(1)
            with open(f"{PROJ_FILE}/commentry/db.json", "r") as f:
                read = json.load(f)
            try:
                if read["share"] != "":
                    print("kjadf")
                    start_ride(read["share"])
                    return
            except Exception as e:
                continue
        except Exception as e:
            continue

if __name__ == "__main__":
    qtask()
