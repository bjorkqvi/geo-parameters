from geo_parameters.metaparameter import MetaParameter
from geo_parameters.ureg import ureg
from typing import Optional
from .relationships import RELATIONSHIPS


class WindParameter(MetaParameter):
    @classmethod
    def my_family(cls, param_type: Optional[str] = None):
        """Returns the dictonary containing the parameters where cls is in.
        Use .my_family('direction') to get the parameter isntead of a dict"""
        if param_type is not None:
            assert param_type in [
                "magnitude",
                "direction",
                "x",
                "y",
                "period",
                "frequency",
            ]

        for rel in RELATIONSHIPS:
            for param in rel.values():
                if type(cls()).__name__ == param:
                    # This needs to be done to circument circular imports etc
                    eval_rel = {}
                    for key, value in rel.items():
                        eval_rel[key] = eval(value)
                    if param_type is not None:
                        return eval_rel.get(param_type)
                    else:
                        return eval_rel

        return None


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
