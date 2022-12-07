import pandas as pd
import time
import datetime

class Logger:

    def __init__(self):
        self.df = pd.DataFrame(columns=['img_name', 'img_size', 'start', 'stop', 'total', 'result'])
        self.filename = datetime.datetime.now().strftime("%m%d%Y%H%M%S.csv")

    def starttiming(self, name, length):
        self.df.loc[len(self.df)] = {'img_name': name, 'img_size': length, 'start': time.time(), 'stop': pd.NA, 'total': pd.NA, 'result': pd.NA}
        return len(self.df) - 1

    def stoptiming(self, handle, res):
        self.df.at[handle, 'stop'] = time.time()
        self.df.at[handle, 'total'] = self.df.iloc[handle]['stop'] - self.df.iloc[handle]['start']
        self.df.at[handle, 'result'] = res
        self.df.to_csv(self.filename)
