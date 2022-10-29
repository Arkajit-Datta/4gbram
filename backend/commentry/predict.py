from imp import load_module
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
    def predict(self,a):
        print(self.loaded_model.predict(a))





te = PredictComment()
t = [[4,5,6,3]]
df = pd.DataFrame(data = t,columns=['steer', 'throtle', 'rpm', 'break'])
print(te.predict(df))
