from pathlib import Path

from dagster import AssetGroup, asset
from dagster_dbt import load_assets_from_dbt_project

from orchestrate import data
from orchestrate.resources import dbt_resource


@asset
def avatar_history():
    path = data.create_db()
    conn = data.connection(path)
    data.import_data_in_table(conn)


dbt_assets = load_assets_from_dbt_project(
    project_dir=(Path(__file__).parents[2] / "dbt_wow").as_posix()
)

assets = AssetGroup(
    [avatar_history] + dbt_assets, resource_defs={"dbt": dbt_resource}
).build_job("Assets")
