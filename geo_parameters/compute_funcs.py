import numpy as np

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

# COMPUTE_FROM = {'Tp': {'Fp': one_over_x, 'Wp': one_over_x_times_2pi},
#                 'Fp': {'Wp': one_over_2pi, 'Tp': one_over_x},
#                 'Wp': {'Tp': one_over_x_times_2pi, 'Fp': times_2pi },
#                 'Wind': {('EastWind', 'NorthWind'): mag_from_uv, ('NorthWind', 'EastWind'): mag_from_uv}

# }



# def _get_compute_from_dict(cls) -> dict:
#     """Gets a comput from dictionary of parameters as strings"""
#     return COMPUTE_FROM.get(type(cls()).__name__,{})

