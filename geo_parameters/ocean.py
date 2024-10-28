from geo_parameters.metaparameter import MetaParameter
from geo_parameters.ureg import ureg
from typing import Optional, Union
from .relationships import _get_family_dict, _verify_param_type


class OceanParameter(MetaParameter):
    @classmethod
    def my_family(
        cls, param_type: Optional[str] = None
    ) -> Union[dict[str, type["OceanParameter"]], type["OceanParameter"], None]:
        """Returns the dictonary containing the parameters where cls is in.
        Use .my_family('direction') to get the parameter isntead of a dict"""

        _verify_param_type(param_type)
        family_dict = _get_family_dict(cls)

        if param_type is None:  # Return entire family_dict
            return_dict = {}
            for key, value in family_dict.items():
                # E.g. eval("WaterDepth"), which can't be done outside of this module
                return_dict[key] = eval(value)
            return return_dict
        else:  # Retrun class for requested parameter type
            return eval(family_dict.get(param_type, "None"))


class WaterDepth(OceanParameter):
    name = "depth"
    _long_name = "water_depth"
    _standard_name = "sea_floor_depth_below_sea_surface"
    _unit = ureg.m


class SeaLevel(OceanParameter):
    name = "eta"
    _long_name = "sea_surface_height"
    _standard_name = [
        "sea_surface_elevation",
        "sea_surface_elevation_anomaly",
        "sea_surface_height_above_geoid",
    ]
    _unit = ureg.m


class XCurrent(OceanParameter):
    name = "x_current"
    _long_name = "eastward_current_component"
    _standard_name = [
        "sea_water_x_velocity",
        "x_sea_water_velocity",
    ]
    _unit = ureg.m / ureg.s


class YCurrent(OceanParameter):
    name = "y_current"
    _long_name = "northward_current_component"
    _standard_name = [
        "sea_water_y_velocity",
        "y_sea_water_velocity",
    ]
    _unit = ureg.m / ureg.s


class Current(OceanParameter):
    name = "current"
    _long_name = "current_speed"
    _standard_name = "sea_water_speed"
    _unit = ureg.m / ureg.s


class CurrentDir(OceanParameter):
    name = "current_dir"
    _long_name = "current_direction"
    _standard_name = [
        "sea_water_velocity_to_direction",
        "sea_water_to_direction",
        "direction_of_sea_water_velocity",
    ]
    _unit = ureg.deg


class CurrentDirFrom(OceanParameter):
    name = "current_dir"
    _long_name = "current_direction"
    _standard_name = [
        "sea_water_velocity_from_direction",
        "sea_water_from_direction",
    ]
    _unit = ureg.deg


class IceFraction(OceanParameter):
    name = "ice_fraction"
    _long_name = "sea_ice_fraction"
    _standard_name = "sea_ice_area_fraction"
    _unit = ureg.percent


class IceThickness(OceanParameter):
    name = "ice_thickness"
    _long_name = "sea_ice_thickness"
    _standard_name = "sea_ice_thickness"
    _unit = ureg.m
