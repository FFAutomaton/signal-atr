from datetime import datetime
import pandas as pd
from signal_atr.atr import ATR


def dosya_yukle(coin, baslangic, pencere):
    tum_data_dosya_adi = f'./coindata/{coin}/{coin}_{pencere}_all.csv'
    main_dataframe = pd.read_csv(tum_data_dosya_adi)

    main_dataframe['Open Time'] = main_dataframe[["Open Time"]].apply(pd.to_datetime)
    main_dataframe = main_dataframe.sort_values(by='Open Time', ascending=False, ignore_index=True)
    main_dataframe = main_dataframe[main_dataframe['Open Time'] < baslangic].reset_index(drop=True)
    main_dataframe = main_dataframe.iloc[0:200]
    print('Tum data ddfghdfgh!')
    return main_dataframe


def run_test(series):
    _atr = ATR(series, 14)
    print(_atr.average_true_range)


if __name__ == "__main__":
    _config = {
        "coin": 'ETHUSDT', "pencere": "4h", "arttir": 4
    }

    baslangic_gunu = datetime.strptime('2021-12-04 00:00:00', '%Y-%m-%d %H:%M:%S')
    bitis_gunu = datetime.strptime('2022-01-15 08:00:00', '%Y-%m-%d %H:%M:%S')
    series = dosya_yukle(_config.get("coin"), baslangic_gunu, _config.get("pencere"))

    run_test(series)