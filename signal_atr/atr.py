import numpy as np
import pandas as pd


class ATR:
    def __init__(self, data, window):
        high_low = data['High'] - data['Low']
        high_cp = np.abs(data['High'] - data['Close'].shift())
        low_cp = np.abs(data['Low'] - data['Close'].shift())

        df = pd.concat([high_low, high_cp, low_cp], axis=1)
        true_range = np.max(df, axis=1)

        self.average_true_range = true_range.rolling(window).mean()

