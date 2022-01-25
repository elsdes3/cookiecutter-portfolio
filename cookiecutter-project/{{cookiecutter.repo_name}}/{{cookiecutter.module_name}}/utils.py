#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Utility functions for notebooks and standalone scripts."""


from typing import List

from IPython.display import display
from pandas import DataFrame

# pylint: disable=invalid-name


def show_df(df: DataFrame, nrows: int = 5, header: List = None) -> None:
    """Show a few of the first and last rows of a DataFrame."""
    df_slice = df.head(nrows).append(df.tail(nrows)) if nrows else df
    if not header:
        header = f"First & Last {nrows} rows" if nrows else "All rows"
    display(df_slice.style.set_caption(header))


def show_df_dtypes_nans(df: DataFrame) -> None:
    """Show datatypes and number of missing rows in DataFrame."""
    display(
        df.isna()
        .sum()
        .rename("num_missing")
        .to_frame()
        .merge(
            df.dtypes.rename("dtype").to_frame(),
            left_index=True,
            right_index=True,
            how="left",
        )
        .style.set_caption("Column Datatypes and Missing Values")
    )


def summarize_df(df: DataFrame, col_dtype_to_show: str) -> None:
    """Show dtype, number of NaNs and sample value from DataFrame columns."""
    if col_dtype_to_show == "object":
        # Get string dtype columns
        cols_to_show = list(df.select_dtypes("object"))
        # Get max length of string
        df_max = (
            df[cols_to_show]
            .astype(str)
            .apply(lambda x: x.str.len().max(), axis=0)
            .rename("max_length")
            .to_frame()
        )
    else:
        # Get non-string (numerical) dtype columns
        cols_to_show = list(
            set(list(df)) - set(list(df.select_dtypes("object")))
        )
        # Get max numerical value
        df_max = df[cols_to_show].max().rename("max_value").to_frame()
    display(
        df_max.merge(
            df[cols_to_show].dtypes.rename("dtype").to_frame(),
            left_index=True,
            right_index=True,
            how="left",
        )
        .merge(
            df[cols_to_show].isna().sum().rename("num_missing").to_frame(),
            left_index=True,
            right_index=True,
            how="left",
        )
        .merge(
            df[cols_to_show]
            .dropna(how="any")
            .sample(1)
            .squeeze()
            .rename("single_non_nan_value")
            .to_frame(),
            left_index=True,
            right_index=True,
            how="left",
        )
    )
