import datetime
from dateutil.relativedelta import relativedelta

import pandas as pd


def main():
    raw_data_address = 'raw_data/1966_2016/raw_data.csv'
    transformed_data_address = 'transformed_data/1966_2016/transformed_data.csv'
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

    transformed_df = pd.DataFrame(data={'month ID':
                                            [i+1 for i in range(len(months)) for _ in range(len(sub_regions))],
                                        'sub-region ID':
                                            [i+1 for _ in range(len(months)) for i in range(len(sub_regions))],
                                        'occurrence':
                                            [0 for _ in range(len(months) * len(sub_regions))]})

    month_id, sub_region_id = None, None
    for index, row in raw_df.iterrows():
        for (start_date, end_date), m_id in months.items():
            if start_date <= row['date'] <= end_date:
                month_id = m_id
                break
        for ((start_longitude, end_longitude), (start_latitude, end_latitude)), s_r_id in sub_regions.items():
            if start_longitude <= row['longitude'] <= end_longitude and \
                    start_latitude <= row['latitude'] <= end_latitude:
                sub_region_id = s_r_id
                break
        transformed_df.loc[
            (transformed_df['month ID'] == month_id) & (transformed_df['sub-region ID'] == sub_region_id),
            'occurrence'] = 1

    transformed_df.to_csv(transformed_data_address, index=False)

    return


if __name__ == '__main__':
    main()
