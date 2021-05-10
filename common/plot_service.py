
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import Image

class PlotService(object):

    def __init__(self, df):
        self._df = df

    def plot_time_series(self, chart_name: str, target_idx: any, features: list, last_n_steps: int = 1000):

        fig, ax = plt.subplots(figsize=(15, 3))
        df_ts = self._df.copy()
        df_ts[target_idx] = None

        chart_name += ' ({})'.format(','.join(features))

        for f in features:
            if ax:
                df_ts.iloc[-last_n_steps:,].plot.scatter(x='ID', y=f, title='Feature Historical Trend - {}'.format(chart_name), s=1, c='blue', ax=ax)
            else:
                ax = df_ts.iloc[-last_n_steps:,].plot.scatter(x='ID', y=f, title='Feature Historical Trend - {}'.format(chart_name), s=1, c='blue')

        ax.set_ylabel('Features')
        del df_ts
        
    def plot_dist(self, features: list):
        for f in features:
            sns.displot(self._df, x=f, hue='Y', kind='kde', fill=True) 