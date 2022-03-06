from pathlib import Path

from dagster_dbt import dbt_cli_resource

dbt_resource = dbt_cli_resource.configured(
    {"project_dir": (Path(__file__).parents[2] / "dbt_wow").as_posix()}
)
