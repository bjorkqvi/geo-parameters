from geo_parameters.metaparameter import MetaParameter
from typing import Optional, Union
from .relationships import _get_family_dict, _verify_param_type


class AtmosphereParameter(MetaParameter):
    @classmethod
    def my_family(
        cls, param_type: Optional[str] = None
    ) -> Union[dict[str, type["AtmosphereParameter"]], type["AtmosphereParameter"], None]:
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


class AirTemperature(AtmosphereParameter):
    name = "t"
    _long_name = "air_temperature"
    _standard_name = "air_temperature"
    _unit = 'K'

class RelativeHumidity(AtmosphereParameter):
    name = "r"
    _long_name = "relative_humidity"
    _standard_name = "relative_humidity"
    _unit = '%'

class SpecificHumidity(AtmosphereParameter):
    name = "q"
    _long_name = "specific_humidity"
    _standard_name = "specific_humidity"
    _unit = '-'

class MeanSeaLevelPressure(AtmosphereParameter):
    name = 'mslp'
    _long_name = 'mean_sea_level_pressure'
    _standard_name = ['air_pressure_at_mean_sea_level', 'air_pressure_at_sea_level']
    _unit = 'N/m**2'