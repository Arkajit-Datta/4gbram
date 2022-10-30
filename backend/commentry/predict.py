from imp import load_module
from backend.commentry.overspeed import tricking
from sklearn import model_selection
import lightgbm 
import os
import pickle
from pycaret import *
from pycaret.classification import *
import pandas as pd
import statistics

THIS_FILE = os.path.dirname(os.path.abspath(__file__))
PROJ_FILE = os.path.abspath(os.path.join(THIS_FILE, "../"))


class PredictComment:
    def __init__(self) -> None:
        self.loaded_model = load_model(PROJ_FILE + '/commentry/rash_drive')
        self.mode = 'beNice'
    
    def set_mode(self,mode):
        self.mode = mode
    
    def rash(self,a):
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
        
    def idle(self,values):
        return all([x == 15 for x in values])

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

        for value in values:
            t_steer.append(value[0])
            t_throtle.append(value[1])
            t_rpm.append(value[2])
            t_break.append(value[3])
            t_speed.append(value[4])
            t_gear.append(value[5])
        values = [x[:4] for x in values]
        df = pd.DataFrame(data = values,columns=['steer', 'throtle', 'rpm', 'break'])
        
        if self.overspeed(t_speed):
            pass
        elif self.idle(t_gear,t_rpm):
            pass
        elif self.tricking(t_throtle):
            pass
        elif self.tricking(t_break):
            pass
        elif self.rash(df):
            pass

te = PredictComment()
t = [[4,5,6,3]]
df = pd.DataFrame(data = t,columns=['steer', 'throtle', 'rpm', 'break'])
print(te.predict(df))
