import pandas as pd
import pickle
import logging


def pickle_object(obj, path):
    logging.info(f"Pickling {obj} to {path}")
    with open(path, 'wb') as f:
        pickle.dump(obj, f)
    logging.info("Done!")


def unpickle_object(path):
    logging.info(f"Unpickling from {path}")
    with open(path, 'rb') as f:
        obj = pickle.load(f)
    logging.info("Done!")
    return obj


def read_csv(path, **kwargs):
    logging.info(f"Reading csv from {path}")
    df = pd.read_csv(path, **kwargs)
    logging.info("Done!")
    return df


def save_csv(pandas_df, path, **kwargs):
    logging.info(f"Saving {pandas_df} to {path}")
    pandas_df.to_csv(path_or_buf=path, **kwargs)
    logging.info("Done!")
