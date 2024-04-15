from geo_parameters.metaparameter import MetaParameter
from geo_parameters.ureg import ureg

class XWind(MetaParameter):
    name = "x_wind"
    _long_name = "x_wind_component"
    _standard_name = [
        "x_wind",
        "grid_eastward_wind",
    ]
    _unit = ureg.m / ureg.s


class YWind(MetaParameter):
    name = "y_wind"
    _long_name = "y_wind_component"
    _standard_name = [
        "y_wind",
        "grid_northward_wind",
    ]
    _unit = ureg.m / ureg.s


class Wind(MetaParameter):
    name = "wind"
    _long_name = "wind_speed"
    _standard_name = "wind_speed"
    _unit = ureg.m / ureg.s


class WindDir(MetaParameter):
    name = "wind_dir"
    _long_name = "wind_direction"
    _standard_name = "wind_from_direction"
    _unit = ureg.deg

class WindDirTo(MetaParameter):
    name = "wind_dir"
    _long_name = "wind_direction"
    _standard_name = "wind_to_direction"
    _unit = ureg.deg

class XGust(MetaParameter):
    name = "x_gust"
    _long_name = "x_gust_component"
    _standard_name = "x_wind_gust"
    _unit = ureg.m / ureg.s


class YGust(MetaParameter):
    name = "y_gust"
    _long_name = "y_gust_component"
    _standard_name = "y_wind_gust"
    _unit = ureg.m / ureg.s


class Gust(MetaParameter):
    name = "gust"
    _long_name = "wind_gust"
    _standard_name = "wind_speed_of_gust"
    _unit = ureg.m / ureg.s


class GustDir(MetaParameter):
    name = "gust_dir"
    _long_name = "wind_gust_direction"
    _standard_name = "wind_gust_from_direction"
    _unit = ureg.deg
    
class GustDirTo(MetaParameter):
    name = "gust_dir"
    _long_name = "wind_gust_direction"
    _standard_name = "wind_gust_to_direction"
    _unit = ureg.deg
    _cf = False
