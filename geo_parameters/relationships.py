"""This module keeps track of the relationships between the parameters"""

RELATIONSHIPS = [
    {
        "x": "XWind",
        "y": "YWind",
        "mag": "Wind",
        "dir": "WindDir",
        "opposite_dir": "WindDirTo",
    },
    {
        "x": "XGust",
        "y": "YGust",
        "mag": "Gust",
        "dir": "GustDir",
        "opposite_dir": "GustDirTo",
    },
    {
        "x": "XCurrent",
        "y": "YCurrent",
        "mag": "Current",
        "dir": "CurrentDir",
        "opposite_dir": "CurrentDirFrom",
    },
    {
        "x": "XStokes",
        "y": "YStokes",
        "mag": "Stokes",
        "dir": "StokesDir",
        "opposite_dir": "StokesDirFrom",
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
