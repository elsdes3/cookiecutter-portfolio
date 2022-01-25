#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pandas as pd

# pylint: disable=invalid-name


def filter_data(
    df: pd.DataFrame, col_name: str, col_max_value: int
) -> pd.DataFrame:
    """Filter data using maximum value in a single DataFrame column."""
    df = df[df[col_name] < col_max_value]
    return df
