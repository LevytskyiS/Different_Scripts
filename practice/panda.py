import random
from datetime import date, timedelta

import pandas as pd
import numpy as np


def get_sales():
    """Getting random sales for 180 days"""
    sales = [i for i in range(1, 1001)]
    random.shuffle(sales)
    return sales[:180]


sales = get_sales()


def get_dates():
    """Getting 180 days from 1.1.2023"""
    start_df = date(2023, 1, 1)
    end_df = date(2023, 6, 29)
    delta = timedelta(days=1)
    dates = []

    while start_df <= end_df:
        dates.append(start_df)
        start_df += delta

    return dates


dates = get_dates()


array = np.array([dates, sales]).T  # Creating a 2 dimension array of dates and sales
df = pd.DataFrame(array, columns=["dates", "sales"])  # Creating a DataFrame

# Saving data to CSV-file
file = "data/sales.csv"
df.to_csv(file, index=False)
