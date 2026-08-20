import numpy as np
from . import dir_conversions
from functools import partial
def one_over_x(x):
    return 1/x

def times_2pi(x):
    return x*2*np.pi

def one_over_2pi(x):
    return x/2/np.pi

def one_over_x2pi(x):
    return 2/np.pi

def one_over_x_times_2pi(x):
    return 1/x*2*np.pi

def flip_180deg(x):
    return np.mod(x+180,360)

def mag_from_uv(u,v):
    return np.sqrt(u**2+v**2)

def id(x):
    return x

def dir_from_u_v(u,v, dir_type):
    data = dir_conversions.compute_math_direction(u, v)
    data = dir_conversions.convert_from_math_dir(data, dir_type=dir_type)
    return data

def dir_from_v_u(v,u, dir_type):
    data = dir_conversions.compute_math_direction(u, v)
    data = dir_conversions.convert_from_math_dir(data, dir_type=dir_type)
    return data


def get_compute_function_one_var(cls, param):
    if param not in cls.my_family().values():
        return None


    elif cls.i_am() in ['direction', 'opposite_direction'] and param.i_am() in ['direction', 'opposite_direction']:
        return flip_180deg 
    elif cls.i_am() in ['frequency', 'period']  and param.i_am() in ['frequency', 'period']:
        return one_over_x
    elif cls.i_am() == 'angular_frequency':
        if param.i_am() == 'frequency':
            return times_2pi
        if param.i_am() == 'period':
                return one_over_x_times_2pi
        return None
    elif param.i_am() == 'angular_frequency':
        if cls.i_am() == 'frequency':
            return one_over_2pi
        if cls.i_am() == 'period':
                return one_over_x_times_2pi
        return None

def get_compute_function_two_vars(cls, param, param2):

    if param not in cls.my_family().values():
        return None
    if param2 not in cls.my_family().values():
        return None

    if cls.i_am() == 'magnitude':
        if param.i_am() in ['x','y'] and param2.i_am() in ['x','y']:
            return mag_from_uv
        if param.i_am() in ['east','north'] and param2.i_am() in ['east','north']:
            return mag_from_uv
    
    if cls.i_am() in ['direction', 'opposite_direction']:
        if param.i_am() == 'east' and param2.i_am() == 'north':
            return partial(dir_from_u_v, dir_type=cls.dir_type())
        if param.i_am() == 'north' and param2.i_am() == 'east':
            return partial(dir_from_v_u, dir_type=cls.dir_type())

# COMPUTE_FROM = {'Tp': {'Fp': one_over_x, 'Wp': one_over_x_times_2pi},
#                 'Fp': {'Wp': one_over_2pi, 'Tp': one_over_x},
#                 'Wp': {'Tp': one_over_x_times_2pi, 'Fp': times_2pi },
#                 'Wind': {('EastWind', 'NorthWind'): mag_from_uv, ('NorthWind', 'EastWind'): mag_from_uv}

# }



# def _get_compute_from_dict(cls) -> dict:
#     """Gets a comput from dictionary of parameters as strings"""
#     return COMPUTE_FROM.get(type(cls()).__name__,{})

