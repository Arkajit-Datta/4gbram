import pandas as pd

class CsvParser:
    def __init__(self,file_path) -> None:
        self.df = pd.read_csv(file_path)
    
    def _get_blinker(self) -> int:
        turn_indications = self.df["TurnIndicationSts"].to_list()
        turn_indications = [x*50 for x in turn_indications]
        on_blinks = []
        temp = []
        for blink_status in turn_indications:
            if blink_status == 0 and temp:
                if len(temp)<10:
                    temp.clear()
                    continue
                x = temp.copy()
                on_blinks.append(x)
                temp.clear()
            if blink_status != 0:
                temp.append(blink_status)
        return len(on_blinks)

    def _get_gear_similar_percentage(self) -> int:
        gear = self.df['ActualGearGSI'].to_list()
        suggested_gear = self.df['SuggestedGearGSI'].to_list()
        times = sum(x == y for x, y in zip(gear, suggested_gear))*0.5
        total_time = len(gear)*0.5
        return times/total_time
    
    def _get_half_clutch(self) -> int:
        clutch_values = self.df['AnalogClutch'].to_list()
        total_time = len(clutch_values)
        time = sum(val>60 and val<120 for val in clutch_values)
        return time/total_time
    
    def _get_mileage(self) -> float:
        return 14.2
    
    def _get_engine_speed(self) -> int:
        engine_speed = self.df['EngineSpeed'].to_list()
        average_engine_speed = sum(engine_speed)/len(engine_speed)
        return average_engine_speed - 700 if average_engine_speed > 700 else 0
    
    def _get_idling_time(self) -> int:
        idling = self.df["NeutralSwSts"].to_list()
        return sum(idling)/len(idling)
    
    
        