#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# pylint: disable=invalid-name


def filter_data(df, col_name, col_max_value):
    """Filter data using maximum value in a single DataFrame column."""
    df = df[df[col_name] < col_max_value]
    return df
