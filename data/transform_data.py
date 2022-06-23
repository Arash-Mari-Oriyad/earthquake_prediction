import datetime
from dateutil.relativedelta import relativedelta

import pandas as pd


def main():
    raw_data_address = 'raw_data/1966_2016/raw_data.csv'
    start_date = datetime.date(year=1966, month=10, day=1)
    end_date = datetime.date(year=2016, month=9, day=30)
    start_longitude, end_longitude = 75, 119
    start_latitude, end_latitude = 23, 45
    m_h, m_v = 3, 3

    number_of_months = (end_date.year - start_date.year) * 12 + end_date.month - start_date.month + 1
    months = {((start_date + relativedelta(months=i)).strftime('%Y-%m-%d'),
               (start_date + relativedelta(months=i+1) - datetime.timedelta(days=1)).strftime('%Y-%m-%d')): i+1
              for i in range(number_of_months)}
    longitude_delta = (end_longitude - start_longitude) / m_h
    latitude_delta = (end_latitude - start_latitude) / m_v
    sub_regions = {((start_longitude + longitude_delta * i, start_longitude + longitude_delta * (i+1)),
                    (end_latitude - latitude_delta * (j+1), end_latitude - latitude_delta * j)):
                       m_v*i + j + 1
                   for i in range(m_h)
                   for j in range(m_v)}

    raw_df = pd.read_csv(raw_data_address)[['time', 'latitude', 'longitude', 'mag']]
    raw_df['time'] = raw_df['time'].apply(lambda time: time.split('T')[0])
    raw_df.rename(columns={'time': 'date'}, inplace=True)

    transformed_df = pd.DataFrame(columns=['month ID', 'sub-region ID', 'occurrence'])

    for index, row in raw_df.iterrows():
        print(index)

    print(raw_df.shape)
    print(raw_df.columns.values)
    print(raw_df.head())


if __name__ == '__main__':
    main()
