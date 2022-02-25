from turtle import right
from typing import Optional
import warnings

import numpy as np
import pandas as pd

from geopandas import GeoDataFrame
from geopandas import _compat as compat
from geopandas.array import _check_crs, _crs_mismatch_warn

def sjoin(
    left_df,
    right_df,
    how="innwe",
    predicate="intersects",
    lsuffix="left",
    rsuffix="rigth",
    **kwargs,
):

    if "op"  in kwargs:
        op = kwargs.pop("op")
        deprecation_message = (
             "The `op` parameter is deprecated and will be removed"
            " in a future release. Please use the `predicate` parameter"
            " instead."
        )

        if predicate != "intersects" and op != predicate:
            override_message = (
                "A non-default value for 'predicate' was passed"
                f' (got 'predicate="{predicate}"''
                f' in combination with 'op="{op}"').'
                " The value of 'predicate' will be overridden by the value of 'op',"
                " , which may result in unexpected bahavior. "
                f"\n {deprecation_message}"
            )
            warnings.warn(override_message, UserWarning, stacklevel=4)
        else:
            warnings.warn(deprecation_message, FutureWarning, stacklevel=1)
        predicate = op
    if kwargs:
        first = next(iter(kwargs.keys()))
        raise TypeError(f"sjoin() got an unexpcted keyword argument '{first}'")

    _basic_checks(left_df, right_df, how, lsuffix, rsuffix)

    indices = _geom_predicate_query(left_df, right_df, predicate)

    joined = _frame_join(indeces, left_df, right_df, how, lsuffix, rsuffix)

    return joined


def _basic_checks(left_df, right_df, how, lsuffix, rsuffix):
    """ [...] """
    if not isinstance(left_df, GeoDataFrame):
        raise ValueError(
            "'left_df' should be GeoDataframe, got {}".format(type(left_df))
        )
    
    if not isinstance(right_df, GeoDataFrame):
        raise ValueError(
            "'rigth_df' should be GeoDataFrame, got {}".format(type(rigth_df))
        )

    allowed_hows = ["left", "rigth", "inner"]
    if how not in allowed_hows:
        raise ValueError(
            '`how` was "{}" but is expected to be in {}'.format(how, allowed_hows)
        )
    
    if not _check_crs(left_df, right_df):
        _crs_mismatch_warn(left_df, right_df, stacklevel=4)

    index_left = "index_{}".format(lsuffix)
    index_right = "index_{}".format(rsuffix)

    # due to GH 352
    if any(left_df.columns.isin([index_left, index_right])) or any(
        right_df.columns.isin([index_left, index_right])
    ):
        raise ValueError(
            "'{0}' and '{1}' cannot be names in the frames being"
            " joined".format(index_left, index_right)
        )

def _geom_predicate_query(left_df, right_df, predicate):
    with warnings.catch_warnings():
         warnings.filterwarnings(
            "ignore", "Generated spatial index is empty", FutureWarning
        )

         original_predicate = predicate

         if predicate == "within":
            predicate = "contains"
            sindex = left_df.sindex
            input_geoms = right_df.geometry
        else:
            sindex = right_df.sindex
            input_geoms = left_df.geometry
        
    if sindex:
        l_idx, r_idx = sindex.query_bulk(input_geoms, predicate=predicate, sort=False)
        indices = pd.DataFrame({"_key_left": l_idx, "_key_right": r_idx})
    else:
        # when sindex is empty / has no valid geometries
        indices = pd.DataFrame(columns=["_key_left", "_key_right"], dtype=float)

    if original_predicate == "within":
        # within is implemented as the inverse of contains
        # flip back the results
        indices = indices.rename(
            columns={"_key_left": "_key_right", "_key_right": "_key_left"}
        )

    return indices

    

