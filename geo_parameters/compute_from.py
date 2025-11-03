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

COMPUTE_FROM = {'Tp': {'Fp': one_over_x},
                'Fp': {'Wp': one_over_2pi},
                'Wp': {'Tp': one_over_x_times_2pi }
}


def _get_compute_from_dict(cls) -> dict:
    """Gets a comput from dictionary of parameters as strings"""
    return COMPUTE_FROM.get(type(cls()).__name__,{})
