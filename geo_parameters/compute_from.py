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

COMPUTE_FROM = {'Tp': {'Fp': one_over_x, 'Wp': one_over_x_times_2pi},
                'Fp': {'Wp': one_over_2pi, 'Tp': one_over_x},
                'Wp': {'Tp': one_over_x_times_2pi, 'Fp': times_2pi },
                'WindDir': {'WindDirTo': flip_180deg},
                'WindDirTo': {'WindDir': flip_180deg},
                'Dirm': {'DirmTo': flip_180deg},
                'DirmTo': {'Dirm': flip_180deg},
                'Dirp': {'DirpTo': flip_180deg},
                'DirpTo': {'Dirp': flip_180deg},
                'DirmSwell': {'DirmSwellTo': flip_180deg},
                'DirmSwellTo': {'DirmSwell': flip_180deg},
                'DirpSwell': {'DirpSwellTo': flip_180deg},
                'DirpSwellTo': {'DirpSwell': flip_180deg},
                'DirmSwell1': {'DirmSwell1To': flip_180deg},
                'DirmSwell1To': {'DirmSwell1': flip_180deg},
                'DirpSwell1': {'DirpSwell1To': flip_180deg},
                'DirpSwell1To': {'DirpSwell1': flip_180deg},
                'DirmSwell2': {'DirmSwell2To': flip_180deg},
                'DirmSwell2To': {'DirmSwell2': flip_180deg},
                'DirpSwell2': {'DirpSwell2To': flip_180deg},
                'DirpSwell2To': {'DirpSwell2': flip_180deg},                
                'DirmSwell3': {'DirmSwell3To': flip_180deg},
                'DirmSwell3To': {'DirmSwell3': flip_180deg},
                'DirpSwell3': {'DirpSwell3To': flip_180deg},
                'DirpSwell3To': {'DirpSwell3': flip_180deg},
                'DirmSea': {'DirmSeaTo': flip_180deg},
                'DirmSeaTo': {'DirmSea': flip_180deg},
                'DirpSea': {'DirpSeaTo': flip_180deg},
                'DirpSeaTo': {'DirpSea': flip_180deg},
                'CurrentDir': {'CurrentDirFrom': flip_180deg},
                'CurrentDirFrom': {'CurrentDir': flip_180deg},
                'StokesDir': {'StokesDirFrom': flip_180deg},
                'StokesDirFrom': {'StokesDir': flip_180deg},
                'FrictionVelocityDir': {'FrictionVelocityDirTo': flip_180deg},
                'FrictionVelocityDirTo': {'FrictionVelocityDir': flip_180deg},

}



def _get_compute_from_dict(cls) -> dict:
    """Gets a comput from dictionary of parameters as strings"""
    return COMPUTE_FROM.get(type(cls()).__name__,{})
