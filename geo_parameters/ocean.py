from .metaparameter import MetaParameter
import pint

ureg = pint.UnitRegistry()


class WaterDepth(MetaParameter):
    _short_name = "depth"
    _long_name = "water_depth"
    _standard_name = "sea_floor_depth_below_sea_surface"
    _unit = ureg.m

class SeaLevel(MetaParameter):
    _short_name = "eta"
    _long_name = "sea_surface_height"
    _standard_name = [
        "sea_surface_elevation",
        "sea_surface_elevation_anomaly",
        "sea_surface_height_above_geoid",
    ]
    _unit = ureg.m


class XCurrent(MetaParameter):
    _short_name = "x_current"
    _long_name = "eastward_current_component"
    _standard_name = [
        "sea_water_x_velocity",
        "x_sea_water_velocity",
    ]
    _unit = ureg.m / ureg.s


class YCurrent(MetaParameter):
    _short_name = "y_current"
    _long_name = "northward_current_component"
    _standard_name = [
        "sea_water_y_velocity",
        "y_sea_water_velocity",
    ]
    _unit = ureg.m / ureg.s


class IceFraction(MetaParameter):
    _short_name = "ice_fraction"
    _long_name = "sea_ice_fraction"
    _standard_name = "sea_ice_area_fraction"
    _unit = ureg.percent


class IceThickness(MetaParameter):
    _short_name = "ice_thickness"
    _long_name = "sea_ice_thickness"
    _standard_name = "sea_ice_thickness"
    _unit = ureg.m

