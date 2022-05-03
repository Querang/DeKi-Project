import sqlite3
import yaml

"""yaml"""


def read_config(file_path):
    try:
        with open(file_path, "r") as f:
            return yaml.safe_load(f)
    except:
        print("mistake")  # here will be append dialog window with mistake


def write_config(file_path, config_dict):
    try:
        with open(file_path, "w") as f:
            yaml.dump(config_dict, f, default_flow_style=False)
    except:
        print("mistake")