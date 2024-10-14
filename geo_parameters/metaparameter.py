from abc import ABC, abstractmethod
import numpy as np
from typing import Union
from pint import Unit

from .relationships import RELATIONSHIPS
from typing import Iterable


class MetaParameter(ABC):
    _cf = True

    def __init__(self, name: str = ""):
        self.name = name or self.name

    @staticmethod
    @abstractmethod
    def _long_name() -> str:
        pass

    @staticmethod
    @abstractmethod
    def _standard_name() -> str:
        pass

    @staticmethod
    @abstractmethod
    def _unit() -> str:
        pass

    @classmethod
    def cf(cls) -> bool:
        return cls._cf

    @classmethod
    def long_name(cls) -> str:
        return cls._long_name

    @classmethod
    def standard_name(cls, strict: bool = False, alias: bool = False) -> str:
        names = np.atleast_1d(cls._standard_name)
        if cls.cf() or not strict:
            if alias:
                return str(names[-1])
            return str(names[0])

        return ""

    @classmethod
    def standard_aliases(cls, strict=False) -> list[str]:
        """Returns a list of all aliases, possible a list of only one name"""
        if cls.cf() or not strict:
            if isinstance(cls._standard_name, list):
                return cls._standard_name
            else:
                return [cls._standard_name]

        return [""]

    @classmethod
    def units(cls) -> Unit:
        return cls._unit

    def quantify(self):
        return self * self.units()

    @classmethod
    def cf(cls) -> str:
        return cls._cf

    @classmethod
    def meta_dict(cls, alias: bool = False) -> dict:
        return {
            "short_name": cls.name,
            "long_name": cls.long_name(),
            "standard_name": cls.standard_name(alias=alias),
            "units": str(cls.units()),
        }

    @classmethod
    def find_me_in_ds(
        cls, ds, return_first: bool = False
    ) -> Union[list[str], str, None]:
        """Takes an Xarray Dataset and returns list of all variable names that matches the parameter based on standard_name

        If return_first = True, then returns first name as a sting"""
        data_vars = list(ds.data_vars)
        coords = list(ds.coords)

        if not return_first:
            vars = []

        for var in data_vars:
            if hasattr(ds.get(var), "standard_name"):
                if ds.get(var).standard_name in cls.standard_aliases():
                    if return_first:
                        return var
                    else:
                        vars.append(var)

        for var in coords:
            if hasattr(ds.get(var), "standard_name"):
                if ds.get(var).standard_name in cls.standard_aliases():
                    if return_first:
                        return var
                    else:
                        vars.append(var)

        if return_first:
            return None
        else:
            return vars

    @classmethod
    def i_am(cls) -> str:
        """Finds what role this parameter has in a possible relationship to other parameters.
        Roles are:
        'x', 'y', 'mag', 'dir', 'opposite_dir'
        'period', 'frequency', 'angular_frequency'
        """
        if cls.my_family() is None:
            return None
        for key, value in cls.my_family().items():
            if cls.is_same(value):
                return key
        return None

    @classmethod
    def is_same(cls, gp) -> bool:
        """Compares name of parameter and standard_name and returns true if they match

        param = gp.wave.Hs
        param.is_same(gp.wave.Hs) [True]
        param.is_same(gp.wave.Hs()) [True]
        param.is_same(gp.wave.Hs('other_name')) [True]
        param.is_same(gp.wave.Hmax) [False]
        """
        try:
            gp = gp()
        except TypeError:
            pass

        type_match = type(cls()).__name__ == type(gp).__name__
        try:
            std_name_match = cls.standard_name() == gp.standard_name()
            return type_match and std_name_match
        except AttributeError:
            return False

    @classmethod
    def is_in(cls, parameters: Iterable) -> bool:
        """Checks if the parameter class is in (using .is_same()) in the list of provided parameters

        Examples:
        >> gp.wave.Hs.is_in([gp.wave.Hs, gp.wave.Tp]) -> True
        >> gp.wave.Hs.is_in([gp.wave.Dirp, gp.wave.Tp]) -> False
        >> gp.wave.Hs.is_in([]) -> False
        >> gp.wave.Hs.is_in(['hs']) -> False
        >> gp.wave.Hs.is_in([gp.wave.Hs(), 'hs']) -> True
        """

        for param in parameters:
            if cls.is_same(param):
                return True
        return False

    @classmethod
    def dir_type(cls) -> str:
        for std_name in cls.standard_aliases():
            if "to_direction" in std_name:
                return "to"
            if "from_direction" in std_name:
                return "from"
        return None
