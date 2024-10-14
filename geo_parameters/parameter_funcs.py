from . import wave, ocean, wind
import inspect
from .metaparameter import MetaParameter
from .wind import WindParameter
from .wave import WaveParameter
from .ocean import OceanParameter
from .grid import GridParameter

BaseParameters = [
    MetaParameter,
    WindParameter,
    WaveParameter,
    OceanParameter,
    GridParameter,
]


def list_of_parameters() -> list:
    """Get a list of all available geo-parameters"""
    parameter_list = []
    modules_to_inspect = [wave, ocean, wind]
    for module in modules_to_inspect:
        for __, obj in inspect.getmembers(module):
            if inspect.isclass(obj):
                if issubclass(obj, MetaParameter) and not obj in BaseParameters:
                    parameter_list.append(obj)
    return parameter_list


def dict_of_parameters(short: bool = False, alias: bool = False) -> dict:
    """Get a dict of all availabel geo-parameters.

    Key is either standard_name (default), alias (alias=True) or non standard short name (short=True)
    """
    if short:
        return {c.name: c for c in list_of_parameters()}
    return {c.standard_name(alias=alias): c for c in list_of_parameters()}


def shortget(key: str):
    """Find a geo-parameter based on a short string. Warning, these short strings follow no standard convention."""
    return dict_of_parameters(short=True).get(key)


def get(key: str):
    """Find a geo-parameter based on a string of the standard_name (or an alias)."""
    return dict_of_parameters().get(key) or dict_of_parameters(alias=True).get(key)


def create_parameter_dict(parameter_strings: list[str]):
    """Create a dict of geo-parameters based on a list of strings of standard_names"""
    metaparameter_dict = {}
    for param in parameter_strings:
        val = get(param)
        if val is not None:
            metaparameter_dict[param] = val
    return metaparameter_dict
