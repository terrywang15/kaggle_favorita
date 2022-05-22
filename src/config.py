from datetime import datetime

import yaml


def load_config_file(yaml_path):
    with open(yaml_path, "rb") as f:
        conf = yaml.safe_load(f.read())
    return conf


def get_run_id():
    return datetime.today().strftime("%Y%m%d_%H%M%S")
