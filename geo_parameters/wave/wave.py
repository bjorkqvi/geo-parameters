from geo_parameters.metaparameter import MetaParameter
from typing import Optional, Union
from geo_parameters.relationships import _get_family_dict, _verify_param_type
from geo_parameters.compute_from import _get_compute_from_dict
from geo_parameters import wave

class WaveParameter(MetaParameter):
    @classmethod
    def my_family(
        cls, param_type: Optional[str] = None
    ) -> Union[dict[str, type["WaveParameter"]], type["WaveParameter"], None]:
        """Returns the dictonary containing the parameters where cls is in.
        Use .my_family('direction') to get the parameter isntead of a dict"""

        _verify_param_type(param_type)
        family_dict = _get_family_dict(cls)

        if param_type is None:  # Return entire family_dict
            return_dict = {}
            for key, value in family_dict.items():
                # E.g. eval("Hs"), which can't be done outside of this module
                return_dict[key] = eval(f"wave.{value}")
            return return_dict
        else:  # Retrun class for requested parameter type
            return eval(family_dict.get(param_type, "None"))
    @classmethod
    def compute_from(cls):
        compute_dict = _get_compute_from_dict(cls)
        return_dict = {}
        for key, value in compute_dict.items():
            # E.g. eval("Hs"), which can't be done outside of this module
            return_dict[eval(f"wave.{key}")] = value

        return return_dict