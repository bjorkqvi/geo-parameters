"""This module keeps track of the relationships between the parameters"""

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
