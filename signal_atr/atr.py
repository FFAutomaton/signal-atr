import numpy as np
import pandas as pd


class ATR:
    def __init__(self, data, window):
        high_low = data['high'] - data['low']
        high_cp = np.abs(data['high'] - data['close'].shift())
        low_cp = np.abs(data['low'] - data['close'].shift())

        df = pd.concat([high_low, high_cp, low_cp], axis=1)
        true_range = np.max(df, axis=1)

        self.average_true_range = true_range.rolling(window).mean()

