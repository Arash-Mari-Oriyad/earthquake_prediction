import datetime
from dateutil.relativedelta import relativedelta

import pandas as pd

from configurations import START_DATE, END_DATE, START_LONGITUDE, END_LONGITUDE, START_LATITUDE, END_LATITUDE, \
    N_HORIZONTAL, N_VERTICAL, TEMPORAL_COLUMN_NAME, SPATIAL_COLUMN_NAME, TARGET,\
    RAW_DATA_ADDRESS, TRANSFORMED_DATA_ADDRESS


def main():
    print("The data transformation process is started!")
    number_of_months = (END_DATE.year - START_DATE.year) * 12 + END_DATE.month - START_DATE.month + 1
    print(f"Number of months = {number_of_months}")
    months = {
        ((START_DATE + relativedelta(months=i)).strftime("%Y-%m-%d"),
         (START_DATE + relativedelta(months=i + 1) - datetime.timedelta(days=1)).strftime("%Y-%m-%d")): i + 1
        for i in range(number_of_months)
    }
    longitude_delta = (END_LONGITUDE - START_LONGITUDE) / N_HORIZONTAL
    latitude_delta = (END_LATITUDE - START_LATITUDE) / N_VERTICAL
    sub_regions = {
        ((START_LONGITUDE + longitude_delta * i, START_LONGITUDE + longitude_delta * (i + 1)),
         (END_LATITUDE - latitude_delta * (j + 1), END_LATITUDE - latitude_delta * j)): N_VERTICAL * i + j + 1
        for i in range(N_HORIZONTAL)
        for j in range(N_VERTICAL)}
    print(f"number of sub-regions = {len(sub_regions)}")
    raw_df = pd.read_csv(RAW_DATA_ADDRESS)[["time", "latitude", "longitude", "mag"]]
    print(f"Raw data shape = {raw_df.shape}")
    raw_df["time"] = raw_df["time"].apply(lambda time: time.split('T')[0])
    raw_df.rename(columns={"time": "date"}, inplace=True)
    transformed_df = pd.DataFrame(data={TEMPORAL_COLUMN_NAME:
                                            [i + 1 for i in range(len(months)) for _ in range(len(sub_regions))],
                                        SPATIAL_COLUMN_NAME:
                                            [i + 1 for _ in range(len(months)) for i in range(len(sub_regions))],
                                        TARGET:
                                            [0 for _ in range(len(months) * len(sub_regions))]})
    temp_month_id, temp_sub_region_id = None, None
    for index, row in raw_df.iterrows():
        for (start_date, end_date), month_id in months.items():
            if start_date <= row["date"] <= end_date:
                temp_month_id = month_id
                break
        for ((start_longitude, end_longitude), (start_latitude, end_latitude)), sub_region_id in sub_regions.items():
            if start_longitude <= row["longitude"] <= end_longitude and \
                    start_latitude <= row["latitude"] <= end_latitude:
                temp_sub_region_id = sub_region_id
                break
        transformed_df.loc[(transformed_df[TEMPORAL_COLUMN_NAME] == temp_month_id) &
                           (transformed_df[SPATIAL_COLUMN_NAME] == temp_sub_region_id), TARGET] = 1
    print(f"Transformed data shape = {transformed_df.shape}")
    transformed_df.to_csv(TRANSFORMED_DATA_ADDRESS, index=False)
    print("The data transformation process is finished!")
    return


if __name__ == "__main__":
    main()
