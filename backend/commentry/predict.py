from imp import load_module
from sklearn import model_selection
import lightgbm 
import os
import pickle
from pycaret import *
from pycaret.classification import *
import pandas as pd
import statistics
import json
import glob
import random
  
THIS_FILE = os.path.dirname(os.path.abspath(__file__))
PROJ_FILE = os.path.abspath(os.path.join(THIS_FILE, "../"))

db_path = PROJ_FILE + '/commentry/db.json'

class PredictComment:
    def __init__(self) -> None:
        self.loaded_model = load_model(PROJ_FILE + '/commentry/rash_drive')
        self.mode = 'beNice'
    
    def set_mode(self,mode):
        self.mode = mode
    
    def rash(self,a):
        print(self.loaded_model.predict(a))
        print(a)
        if self.loaded_model.predict(a)[0] == 1:
            return True 
        return False
    
    def overspeed(self,speeds):
        f = 0
        for speed in speeds:
            if(speed < 80):
                f = 1
        if f:
            return 0
        else:
            return 1
        
    def idle(self,values,rpm):
        return all([x == 15 for x in values]) and all([x>700 for x in rpm])

    def tricking(self,a):
        i = 0
        j = -1
        k = -1
        p = 0
        d = 0
        n = 0
        
    
        if (len(a) < 3):
            return 0
            
        for i in range(len(a) - 1):
            if (a[i + 1] > a[i]):
                
                
                if (k != -1):
                    k = -1
                    j = -1
                
                
                if (j == -1):
                    j = i
            else:
                
                
                if (a[i + 1] < a[i]):
                    
                    
                    if (j != -1):
                        k = i + 1
                        
                    
                    if (k != -1 and j != -1):
                        
                        
                        if (d < k - j + 1):
                            d = k - j + 1
                
                
                else:
                    k = -1
                    j = -1
        
        
        if (k != -1 and j != -1):
            if (d < k - j + 1):
                d = k - j + 1
                
        if d < len(a)//4:
            return True
        return False

    def predict(self,values):
        t_steer = []
        t_throtle = []
        t_rpm = []
        t_break = []
        t_speed = []
        t_gear = []
        #print(values)
        for value in values:
            t_steer.append(value[0])
            t_throtle.append(value[1])
            t_rpm.append(value[2])
            t_break.append(value[3])
            t_speed.append(value[4])
            t_gear.append(value[5])
        values = [x[:4] for x in values]
        s_steer = sum(t_steer)/len(t_steer)
        s_throtle = statistics.stdev(t_throtle)
        s_rpm = statistics.stdev(t_rpm)
        s_break = statistics.stdev(t_break)
        values = [[s_steer,s_throtle,s_rpm,s_break]]
        df = pd.DataFrame(data = values,columns=['steer', 'throtle', 'rpm', 'break'])
        
        f = open(db_path,'r')
        data = json.load(f)
        print(data)
        f.close()
        f = open(db_path,'w')
        if self.overspeed(t_speed):
            print("overspeed")
            path = PROJ_FILE + '/audios/' + self.mode + '/overspeed/*.mp3'
            l = glob.glob(path)
            print(l)
            a = random.choice(l)
            print(l)
            data['1'].append(a)
        elif self.idle(t_gear,t_rpm):
            print("idle")
            path = PROJ_FILE + '/audios/' + self.mode + '/idling/*.mp3'
            l = glob.glob(path)
            a = random.choice(l)
            data['1'].append(a)
        # elif self.tricking(t_throtle):
        #     path = PROJ_FILE + '/audios/' + self.mode + '/tricking'
        #     l = glob.glob(path + '/*')
        #     a = random.choice(l)
        #     data['1'].append(path)
        # elif self.tricking(t_break):
        #     path = PROJ_FILE + '/audios/' + self.mode + '/tricking'
        #     l = glob.glob(path + '/*')
        #     a = random.choice(l)
        #     data['1'].append(path)
        elif self.rash(df):
            print("rash")
            path = PROJ_FILE + '/audios/' + self.mode + '/rash/*.mp3'
            l = glob.glob(path)
            a = random.choice(l)
            data['1'].append(a)
        print(data)
        json.dump(data,f)
        
        f.close()

# te = PredictComment()
# t = [[4,5,6,3]]
# df = pd.DataFrame(data = t,columns=['steer', 'throtle', 'rpm', 'break'])
# print(te.predict(df))y

