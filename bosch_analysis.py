# Bosch manufacturing data set

import sys
import pandas as pd
import os
os.chdir('/Users/michaelgoff/Desktop/Machine Learning/Manufacturing/bosch_small_data')

# Three training files: train_cat.csv, train_date.csv, train_numeric.csv
# Three test files: test_cat.csv, test_date.csv, test_numeric.csv

# Uncomment these lines to load the training data.
#train_cat = pd.read_csv("train_cat.csv")
#train_date = pd.read_csv("train_date.csv")
#train_numeric = pd.read_csv("train_numeric.csv")

# Get a row: train_numeric.loc[1234]
# row = row[1:]
# row = row[row.notnull()]
# Get indices: row.index.tolist()

# For use on the categorical data, get the nonnull values
def get_unique_by_col(df):
    cols = df.columns
    uniques = {}
    for i in range(len(cols)):
        uniques[cols[i]] = df[cols[i]].unique()
    return uniques
    
# The following code takes a row number and returns the set of stations it hits
# Example: get_stations(1234, train_numeric)
def get_stations(row_num, df):
    if (row_num%100 == 0):
        print row_num # Just to track progress
    row = df.loc[row_num]
    row = row[1:]
    row = row[row.notnull()]
    indices = row.index.tolist()
    return array_to_paths(indices)

def array_to_paths(arr):
    blocks = [arr[i].split('_') for i in range(len(arr))]
    blocks = [blocks[i] for i in range(len(blocks)) if len(blocks[i])==3]
    stations = sort(list(set([int(blocks[i][1][1:]) for i in range(len(blocks))])))
    stations = [str(stations[i]) for i in range(len(stations))]
    return '-'.join(stations)

# To run: load data sets and get_all_paths(train_numeric)
# Warning: takes a while
# There are 2505 unique paths.
def get_all_paths(df):
    # Could rewrite with apply()
    all_paths = [get_stations(i,df) for i in range(len(df))]
    df["path"] = all_paths
    return df
    
