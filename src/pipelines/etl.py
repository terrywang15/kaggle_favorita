from datetime import datetime
import logging

import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

from src.utils.config import load_config_file, get_run_id
from src.utils.io_funcs import pickle_object, read_csv, save_csv
from src.utils.logging import get_logger

paths = load_config_file("config/paths.yml")
input_conf = load_config_file("config/input.yml")
task_conf = load_config_file("config/pipeline/etl.yml")


def main():
    run_id = get_run_id()
    log = get_logger(f'logs/etl/{run_id}.log')

    log.info("Loading input: train")
    train = read_csv(paths["input"]["train"],
                     index_col=input_conf["train"]["index_col"],
                     dtype=input_conf["train"]["dtype"],
                     parse_dates=input_conf["train"]["parse_dates"])

    log.info("Loading input: stores")
    stores = read_csv(paths["input"]["stores"],
                      dtype=input_conf["stores"]["dtype"])

    log.info("Loading input: stores")


    log.info("ETL pipeline successfully executed!")


if __name__ == "__main__":
    main()
