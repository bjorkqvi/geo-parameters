from geo_parameters.metaparameter import MetaParameter
from geo_parameters.ureg import ureg


class WaterDepth(MetaParameter):
    name = "depth"
    _long_name = "water_depth"
    _standard_name = "sea_floor_depth_below_sea_surface"
    _unit = ureg.m


class SeaLevel(MetaParameter):
    name = "eta"
    _long_name = "sea_surface_height"
    _standard_name = [
        "sea_surface_elevation",
        "sea_surface_elevation_anomaly",
        "sea_surface_height_above_geoid",
    ]
    _unit = ureg.m


class XCurrent(MetaParameter):
    name = "x_current"
    _long_name = "eastward_current_component"
    _standard_name = [
        "sea_water_x_velocity",
        "x_sea_water_velocity",
    ]
    _unit = ureg.m / ureg.s


class YCurrent(MetaParameter):
    name = "y_current"
    _long_name = "northward_current_component"
    _standard_name = [
        "sea_water_y_velocity",
        "y_sea_water_velocity",
    ]
    _unit = ureg.m / ureg.s


class Current(MetaParameter):
    name = "current"
    _long_name = "current_speed"
    _standard_name = "sea_water_speed"
    _unit = ureg.m / ureg.s


class CurrentDir(MetaParameter):
    name = "current_dir"
    _long_name = "current_direction"
    _standard_name = [
        "sea_water_velocity_to_direction",
        "sea_water_to_direction",
        "direction_of_sea_water_velocity",
    ]
    _unit = ureg.deg


class CurrentDirFrom(MetaParameter):
    name = "current_dir"
    _long_name = "current_direction"
    _standard_name = [
        "sea_water_velocity_from_direction",
        "sea_water_from_direction",
    ]
    _unit = ureg.deg


class IceFraction(MetaParameter):
    name = "ice_fraction"
    _long_name = "sea_ice_fraction"
    _standard_name = "sea_ice_area_fraction"
    _unit = ureg.percent


class IceThickness(MetaParameter):
    name = "ice_thickness"
    _long_name = "sea_ice_thickness"
    _standard_name = "sea_ice_thickness"
    _unit = ureg.m
