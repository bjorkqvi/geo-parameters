from geo_parameters.metaparameter import MetaParameter
from geo_parameters.ureg import ureg
from typing import Optional, Union
from .relationships import _get_family_dict, _verify_param_type


class GridParameter(MetaParameter):
    @classmethod
    def my_family(cls, param_type: Optional[str] = None) -> Union[dict, None]:
        """Returns the dictonary containing the parameters where cls is in.
        Use .my_family('direction') to get the parameter isntead of a dict"""

        _verify_param_type(param_type)
        family_dict = _get_family_dict(cls)

        if param_type is None:  # Return entire family_dict
            return_dict = {}
            for key, value in family_dict.items():
                # E.g. eval("Lon"), which can't be done outside of this module
                return_dict[key] = eval(value)
            return return_dict
        else:  # Retrun class for requested parameter type
            return eval(family_dict.get(param_type, "None"))


class Lon(GridParameter):
    name = "lon"
    _long_name = "longitude"
    _standard_name = "longitude"
    _unit = "degrees_east"


class Lat(GridParameter):
    name = "lat"
    _long_name = "latitude"
    _standard_name = "latitude"
    _unit = "degrees_north"


class X(GridParameter):
    name = "x"
    _long_name = "x_distance"
    _standard_name = "distance_in_x_direction"
    _unit = ureg.m
    _cf = False


class Y(GridParameter):
    name = "y"
    _long_name = "y_distance"
    _standard_name = "distance_in_y_direction"
    _unit = ureg.m
    _cf = False


class Inds(GridParameter):
    name = "inds"
    _long_name = "index_of_points"
    _standard_name = "index_of_geophysical_points"
    _unit = "-"
    _cf = False
