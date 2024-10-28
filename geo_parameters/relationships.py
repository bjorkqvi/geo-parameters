"""This module keeps track of the relationships between the parameters"""

from typing import Union

PARAM_TYPES = [
    "magnitude",
    "direction",
    "opposite_direction",
    "x",
    "y",
    "period",
    "frequency",
]

RELATIONSHIPS = [
    {
        "x": "XWind",
        "y": "YWind",
        "magnitude": "Wind",
        "direction": "WindDir",
        "opposite_direction": "WindDirTo",
    },
    {
        "x": "XGust",
        "y": "YGust",
        "magnitude": "Gust",
        "direction": "GustDir",
        "opposite_direction": "GustDirTo",
    },
    {
        "x": "XFrictionVelocity",
        "y": "YFrictionVelocity",
        "magnitude": "FrictionVelocity",
        "direction": "FrictionVelocityDir",
        "opposite_direction": "FrictionVelocityDirTo",
    },
    {
        "x": "XCurrent",
        "y": "YCurrent",
        "magnitude": "Current",
        "direction": "CurrentDir",
        "opposite_direction": "CurrentDirFrom",
    },
    {
        "x": "XStokes",
        "y": "YStokes",
        "magnitude": "Stokes",
        "direction": "StokesDir",
        "opposite_direction": "StokesDirFrom",
    },
    {"period": "Tp", "frequency": "Fp", "angular_frequency": "Wp"},
    {"period": "TpSwell", "frequency": "FpSwell"},
    {"period": "TpSwell1", "frequency": "FpSwell1"},
    {"period": "TpSwell2", "frequency": "FpSwell2"},
    {"period": "TpSwell3", "frequency": "FpSwell3"},
    {"period": "Tm01", "frequency": "Fm", "angular_frequency": "Wm"},
    {"period": "TmSwell", "frequency": "FmSwell"},
    {"period": "TmSwell1", "frequency": "FmSwell1"},
    {"period": "TmSwell2", "frequency": "FmSwell2"},
    {"period": "TmSwell3", "frequency": "FmSwell3"},
]


def _verify_param_type(param_type: str) -> None:
    """Verifies that the given parameter type is known"""
    if param_type is not None and param_type not in PARAM_TYPES:
        raise ValueError(f"'param_type' need to be {PARAM_TYPES}, not {param_type}!")


def _get_family_dict(cls) -> dict:
    """Gets a family dictionary of parameters as strings"""
    for rel_dict in RELATIONSHIPS:
        if type(cls()).__name__ in rel_dict.values():
            return rel_dict

    return {}
