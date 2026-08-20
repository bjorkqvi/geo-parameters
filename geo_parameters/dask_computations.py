import numpy as np
import xarray as xr

from typing import Union, TYPE_CHECKING

try:
    import dask.array as da
except ModuleNotFoundError:
    pass

try:
    import xarray as xr
except ModuleNotFoundError:
    pass

if TYPE_CHECKING:
    import dask.array as da
    import xarray as xr

def transpose(
    data: Union[np.ndarray, "da.array", "xr.DataArray"], coord_order: tuple[int]
) -> Union[np.ndarray, "da.array", "xr.DataArray"]:
    """Transpose a dask or numpy array"""
    if data_is_dask(data):
        return da.transpose(data, coord_order)
    else:
        return np.transpose(data, coord_order)

def reshape(
    data: Union[np.ndarray, "da.array", "xr.DataArray"], shape: tuple[int]
) -> Union[np.ndarray, "da.array", "xr.DataArray"]:
    """Reshapes a dask or numpy array"""
    if data_is_dask(data):
        return da.reshape(data, shape)
    else:
        return np.reshape(data, shape)

def expand_dims(
    data: Union[np.ndarray, "da.array", "xr.DataArray"], axis=tuple[int]
) -> Union[np.ndarray, "da.array", "xr.DataArray"]:
    """Expand the dimensions of a dask or numpy array"""
    if data_is_dask(data):
        return da.expand_dims(data, axis=axis)
    else:
        return np.expand_dims(data, axis=axis)

def deg2rad(data: Union[np.ndarray, "da.array", "xr.DataArray"]) -> Union[np.ndarray, "da.array", "xr.DataArray"]:
    """deg2rad on either dask or numpy array"""
    if data_is_dask(data):
        return da.deg2rad(data)
    else:
        return np.deg2rad(data)
def rad2deg(data: Union[np.ndarray, "da.array", "xr.DataArray"]) -> Union[np.ndarray, "da.array", "xr.DataArray"]:
    """rad2deg on either dask or numpy array"""
    if data_is_dask(data):
        return da.rad2deg(data)
    else:
        return np.rad2deg(data)

def cos(data: Union[np.ndarray, "da.array", "xr.DataArray"]) -> Union[np.ndarray, "da.array", "xr.DataArray"]:
    """cos on either dask or numpy array"""
    if data_is_dask(data):
        return da.cos(data)
    else:
        return np.cos(data)


def sin(data: Union[np.ndarray, "da.array", "xr.DataArray"]) -> Union[np.ndarray, "da.array", "xr.DataArray"]:
    """sin on either dask or numpy array"""
    if data_is_dask(data):
        return da.sin(data)
    else:
        return np.sin(data)


def mod(
    data: Union[np.ndarray, "da.array", "xr.DataArray"], mod: Union[float, int]
) -> Union[np.ndarray, "da.array", "xr.DataArray"]:
    """mod on either dask or numpy array"""
    if data_is_dask(data):
        return da.mod(data, mod)
    else:
        return np.mod(data, mod)


def arctan2(
    y: Union[np.ndarray, "da.array", "xr.DataArray"], x: Union[np.ndarray, "da.array", "xr.DataArray"]
) -> Union[np.ndarray, "da.array", "xr.DataArray"]:
    """arctan2 on either dask or numpy array"""
    if data_is_dask(y) and data_is_dask(x):
        return da.arctan2(y, x)
    else:
        return np.arctan2(y, x)


def atleast_1d(
    data: Union[np.ndarray, "da.array", "xr.DataArray"]
) -> Union[np.ndarray, "da.array", "xr.DataArray"]:
    """atleadt_1d on either dask or numpy array"""
    if data_is_dask(data):
        if not data_is_xarray(data):
            return da.atleast_1d(data)
        else:
            if data.shape == ():
                return data.expand_dims((0,))
            else:
                return data
    else:
        if not data_is_xarray(data):
            return np.atleast_1d(data)
        else:
            if data.shape == ():
                return data.expand_dims((0,))
            else:
                return data


def data_is_dask(data: Union[np.ndarray, "da.array", "xr.DataArray"]) -> bool:
    """Checks if a data array is a dask array or an xarray Dataset containing a dask array"""
    try:
        import dask.array as da
        if isinstance(data, da.Array):
            return True
        elif hasattr(data, 'data'):
            return isinstance(data.data, da.Array)
    except ModuleNotFoundError:
        return False
    
def data_is_xarray(data: Union[np.ndarray, "da.array", "xr.DataArray"]) -> bool:
    """Checks if data is an xarray DataArray"""
    try:
        import xarray as xr
        return isinstance(data, xr.DataArray)
    except ModuleNotFoundError:
        return False


def undask_me(
    data: Union[np.ndarray, "da.array", "xr.DataArray"]
) -> Union[np.ndarray, "da.array", "xr.DataArray"]:
    """Convert a dask array to a numpy array if needed"""
    if data is None:
        return None
    if data_is_dask(data):
        return data.compute()
    return data
