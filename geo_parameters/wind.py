from .metaparameter import MetaParameter
import pint

ureg = pint.UnitRegistry()


class XWind(MetaParameter):
    _short_name = "x_wind"
    _long_name = "eastward_wind_component"
    _standard_name = [
        "x_wind",
        "grid_eastward_wind",
    ]
    _unit = ureg.m / ureg.s


class YWind(MetaParameter):
    _short_name = "y_wind"
    _long_name = "northward_wind_component"
    _standard_name = [
        "y_wind",
        "grid_northward_wind",
    ]
    _unit = ureg.m / ureg.s
