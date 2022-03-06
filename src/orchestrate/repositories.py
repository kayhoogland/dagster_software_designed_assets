from dagster import repository

from orchestrate.assets import assets


@repository
def my_repository():
    return [assets]
