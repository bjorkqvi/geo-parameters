from geo_parameters.metaparameter import MetaParameter
from typing import Optional, Union, Callable
from geo_parameters.relationships import _get_family_dict, _verify_param_type
import geo_parameters.wave as wave

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
            if param_type not in family_dict:
                return None
            return eval(f"wave.{family_dict.get(param_type)}")
            
