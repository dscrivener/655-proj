import pandas as pd
import time
import datetime

class Logger:

    def __init__(self):
        self.df = pd.DataFrame(columns=['req', 'start', 'stop', 'total', 'res'])

    def starttiming(self, hash):
        self.df.loc[len(self.df)] = {'req': hash, 'start': time.time(), 'stop': pd.NA, 'res': pd.NA}
        return len(self.df) - 1

    def stoptiming(self, handle, res):
        self.df.loc[handle]['stop'] = time.time()
        self.df.loc[handle]['total'] = self.df.loc[handle]['start'] - self.df.loc[handle]['stop']
        self.df.loc[handle]['res'] = res
        self.df.to_csv(datetime.datetime.now().strftime("%m%d%Y%H%M%S.csv"))
