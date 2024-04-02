from .metaparameter import MetaParameter
import pint

ureg = pint.UnitRegistry()


class XWind(MetaParameter):
    _short_name = "x_wind"
    _long_name = "x_wind_component"
    _standard_name = [
        "x_wind",
        "grid_eastward_wind",
    ]
    _unit = ureg.m / ureg.s


class YWind(MetaParameter):
    _short_name = "y_wind"
    _long_name = "y_wind_component"
    _standard_name = [
        "y_wind",
        "grid_northward_wind",
    ]
    _unit = ureg.m / ureg.s


class Wind(MetaParameter):
    _short_name = "wind"
    _long_name = "wind_speed"
    _standard_name = "wind_speed"
    _unit = ureg.m / ureg.s


class WindDir(MetaParameter):
    _short_name = "wind_dir"
    _long_name = "wind_direction"
    _standard_name = "wind_from_direction"
    _unit = ureg.deg


class XGust(MetaParameter):
    _short_name = "x_gust"
    _long_name = "x_gust_component"
    _standard_name = "x_wind_gust"
    _unit = ureg.m / ureg.s


class YGust(MetaParameter):
    _short_name = "y_gust"
    _long_name = "y_gust_component"
    _standard_name = "y_wind_gust"
    _unit = ureg.m / ureg.s


class Gust(MetaParameter):
    _short_name = "gust"
    _long_name = "wind_gust"
    _standard_name = "wind_speed_of_gust"
    _unit = ureg.m / ureg.s


class GustDir(MetaParameter):
    _short_name = "gust_dir"
    _long_name = "wind_gust_direction"
    _standard_name = "wind_gust_from_direction"
    _unit = ureg.deg
