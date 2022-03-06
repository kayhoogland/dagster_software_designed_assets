import sqlite3
from pathlib import Path

import pandas as pd

from orchestrate.constants import DB_PATH


def create_db():
    path = DB_PATH
    if path.exists():
        return path
    path.touch()
    return path


def connection(path):
    conn = sqlite3.connect(path)
    return conn


def import_data_in_table(conn):
    path = Path(__file__).parents[2] / "data/wowah_data.csv"
    history_df = pd.read_csv(path)
    history_df.columns = [c.strip() for c in history_df.columns]
    history_df.to_sql("avatar_history", conn, if_exists="replace", index=False)
