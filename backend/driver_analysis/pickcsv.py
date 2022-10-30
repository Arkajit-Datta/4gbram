import csv
import pandas as pd
class PickCsv:
    def __init__(self,path) -> None:
        self.path = path
        df = pd.read_csv(path)
        self.data = df[['OverSteering','ThrottlePos','EngineSpeed','BrakePedalSwitchNCSts','REF_VEH_SPEED','ActualGearGSI','SuggestedGearGSI','TurnIndicationSts']]
    
    def get_data(self,linenumber):
        return self.data.iloc[[linenumber]]

pick = PickCsv('/home/anirudh/Desktop/4gbram/backend/driver_analysis/c1can_2020_01_14_02_evening.csv') 
print(pick.get_data(2))