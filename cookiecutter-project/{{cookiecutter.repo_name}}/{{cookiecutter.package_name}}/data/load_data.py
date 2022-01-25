#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from typing import List

import numpy as np
import pandas as pd

# pylint: disable=invalid-name


def get_data(num_rows: int, col_names: List) -> pd.DataFrame:
    """Retrieve data into a DataFrame."""
    df = pd.DataFrame(
        np.random.rand(num_rows, len(col_names)), columns=col_names
    )
    return df


def export_data_to_csv(
    df: pd.DataFrame,
    filepath: str,
    header: bool = True,
    mode: str = "w",
    index: bool = False,
):
    """Export a DataFrame to a CSV file."""
    df.to_csv(filepath, header=header, mode=mode, index=index)


def save_to_parquet_file(
    dfs: List[pd.DataFrame], parquet_filepaths: str
) -> None:
    """Save DataFrame to parquet file."""
    for parquet_filepath, df in zip(parquet_filepaths, dfs):
        try:
            print(f"Saving data to {parquet_filepath + '.gzip'}", end="...")
            df.to_parquet(
                parquet_filepath + ".gzip",
                engine="auto",
                index=False,
                compression="gzip",
            )
            print("done.")
        except Exception as e:
            print(str(e))
            raise
