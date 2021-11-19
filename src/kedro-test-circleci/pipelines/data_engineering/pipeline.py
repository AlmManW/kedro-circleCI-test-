from kedro.pipeline import Pipeline, node

from .nodes import load_csv_data

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=load_csv_data,
                inputs="csv_data_read",
                outputs="csv_data_load",
                name="load_csv_data",
            ),
        ]
    )