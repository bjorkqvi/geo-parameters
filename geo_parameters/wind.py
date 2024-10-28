from geo_parameters.metaparameter import MetaParameter
from geo_parameters.ureg import ureg
from typing import Optional, Union
from .relationships import _get_family_dict, _verify_param_type


class WindParameter(MetaParameter):
    @classmethod
    def my_family(
        cls, param_type: Optional[str] = None
    ) -> Union[dict[str, type["WindParameter"]], type["WindParameter"], None]:
        """Returns the dictonary containing the parameters where cls is in.
        Use .my_family('direction') to get the parameter isntead of a dict"""

        _verify_param_type(param_type)
        family_dict = _get_family_dict(cls)

        if param_type is None:  # Return entire family_dict
            return_dict = {}
            for key, value in family_dict.items():
                # E.g. eval("XWind"), which can't be done outside of this module
                return_dict[key] = eval(value)
            return return_dict
        else:  # Retrun class for requested parameter type
            return eval(family_dict.get(param_type, "None"))


class XWind(WindParameter):
    name = "x_wind"
    _long_name = "x_wind_component"
    _standard_name = [
        "x_wind",
        "grid_eastward_wind",
    ]
    _unit = ureg.m / ureg.s


class YWind(WindParameter):
    name = "y_wind"
    _long_name = "y_wind_component"
    _standard_name = [
        "y_wind",
        "grid_northward_wind",
    ]
    _unit = ureg.m / ureg.s


class Wind(WindParameter):
    name = "ff"
    _long_name = "wind_speed"
    _standard_name = "wind_speed"
    _unit = ureg.m / ureg.s


class WindDir(WindParameter):
    name = "dd"
    _long_name = "wind_direction"
    _standard_name = "wind_from_direction"
    _unit = ureg.deg


class WindDirTo(WindParameter):
    name = "dd"
    _long_name = "wind_direction"
    _standard_name = "wind_to_direction"
    _unit = ureg.deg


class XGust(WindParameter):
    name = "x_gust"
    _long_name = "x_gust_component"
    _standard_name = "x_wind_gust"
    _unit = ureg.m / ureg.s


class YGust(WindParameter):
    name = "y_gust"
    _long_name = "y_gust_component"
    _standard_name = "y_wind_gust"
    _unit = ureg.m / ureg.s


class Gust(WindParameter):
    name = "gust"
    _long_name = "wind_gust"
    _standard_name = "wind_speed_of_gust"
    _unit = ureg.m / ureg.s


class GustDir(WindParameter):
    name = "gust_dir"
    _long_name = "wind_gust_direction"
    _standard_name = "wind_gust_from_direction"
    _unit = ureg.deg


class GustDirTo(WindParameter):
    name = "gust_dir"
    _long_name = "wind_gust_direction"
    _standard_name = "wind_gust_to_direction"
    _unit = ureg.deg
    _cf = False


class XFrictionVelocity(WindParameter):
    name = "x_fv"
    _long_name = "x_friction_velocity"
    _standard_name = "eastward_friction_velocity_in_air"
    _unit = ureg.m / ureg.s


class YFrictionVelocity(WindParameter):
    name = "y_fv"
    _long_name = "y_friction_velocity"
    _standard_name = "northward_friction_velocity_in_air"
    _unit = ureg.m / ureg.s


class FrictionVelocity(WindParameter):
    name = "fv"
    _long_name = "friction_velocity"
    _standard_name = "friction_velocity_in_air"
    _unit = ureg.m / ureg.s
    _cf = False


class FrictionVelocityDir(WindParameter):
    name = "fv_dir"
    _long_name = "friction_velocity_direction"
    _standard_name = "friction_velocity_in_air_from_direction"
    _unit = ureg.deg
    _cf = False


class FrictionVelocityDirTo(WindParameter):
    name = "fv_dir"
    _long_name = "friction_velocity_direction"
    _standard_name = "friction_velocity_in_air_to_direction"
    _unit = ureg.deg
    _cf = False
