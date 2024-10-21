# Geo-parameters
[![Tests (python)](https://github.com/bjorkqvi/geo-parameters/actions/workflows/tests.yml/badge.svg)](https://github.com/bjorkqvi/geo-parameters/actions/workflows/tests.yml)

Metadata of geophysical (especially wave) parameters. The main idea is to be able to use standard CF-names without having to remember or check the names.

# Quick Installation

To get started with geo-parameters, you can install it with pip or conda:

```shell
$ pip install geo-parameters
```

or

```shell
$ conda install -c conda-forge geo-parameters
```

## Names of parameters

The parameters are classes in sub-modules according to the physical property (wave, ocean, wind)

```python
>>> import geo_parameters as gp
```

These classes have information about the parameter, such as CF standard name, units and directional convention. Units are tracked by using the ```pint``` package, and the directional type is parsed from the standard names.

```python
>>> gp.wave.Hs.standard_name()
'sea_surface_wave_significant_height'

>>> gp.wave.Hs.units()
<Unit('meter')>
>>> str(gp.wave.Hs.units())
'm'

>>> gp.wave.Hs.dir_type()
None

>>> gp.wave.Dirp.standard_name()
'sea_surface_wave_from_direction_at_variance_spectral_density_maximum'
>>> gp.wave.Dirp.dir_type()
'from'

>>> gp.wave.DirpTo.standard_name()
'sea_surface_wave_to_direction_at_variance_spectral_density_maximum'
>>> gp.wave.DirpTo.dir_type()
'to'
```

Every parameters has a pre-defined name

```python
>>> gp.wave.Hs.name
'hs'
```
If you want to define some other names for the parameters, then you can create an instance. By default the name of the instance is the short name, but this can be changed:

```python
>>> hsig = gp.wave.Hs()
>>> hsig.name
'hs'

>>> hsig = gp.wave.Hs('hsig')
>>> hsig.name
'hsig'
```

The instance still contains the standard name (and some long name that doesn't follow any standard):

```python
>>> hsig.standard_name() 
'sea_surface_wave_significant_height'

>>> hsig.long_name() 
'significant_wave_height'
```

If the parameter has several standard names, you can use the alias-keyword

```python
>>> hsig.standard_name(alias=True) 
'significant_height_of_wind_and_swell_waves'
```

If the parameter has only one standard name, alias does nothing:

```python
>>> Tp.standard_name()
'sea_surface_wave_period_at_variance_spectral_density_maximum'

>>> Tp.standard_name(alias=True)
'sea_surface_wave_period_at_variance_spectral_density_maximum'
```
## Decoding parameters

If the code can receive either a geo-parameter or a string, there are some helpful functions to deal with this situation. First we can check if a geo-parameter (class or isntance) is provided

```python
>>> gp.is_gp(gp.wave.Hs)
True
>>> gp.is_gp(gp.wave.Hs())
True

>>> gp.is_gp_class(gp.wave.Hs)
True
>>> gp.is_gp_class(gp.wave.Hs())
False

>>> gp.is_gp_instance(gp.wave.Hs)
False
>>> gp.is_gp_instance(gp.wave.Hs())
True
```

In addition we can decode a geo-parameter or string to a string with the name and the geo-parameter (or None):

```python
>>> gp.decode('hs')
'hs', None

>>> gp.decode(gp.wave.Hs)
'hs', gp.wave.Hs

>>> gp.decode(gp.wave.Hs('hsig')
'hsig', gp.wave.Hs('hsig')

>>> gp.decode(gp.wave.Hs, init=True)
'hs', gp.wave.Hs()
```

## Relationships between parameters

The parameters also have some knowledge about their relationships with other parameters (if any). These relationships can be e.g. that components make up a magnitude or direction, the direction is the same but opposite direction, or the parameter is the inverse of another (period vs. frequency).

```python
>>> gp.wind.XWind.standard_name()
'x_wind'
>>> gp.wind.XWind.i_am()
'x'

>>> gp.wind.XWind.my_family()
{'x': <class 'geo_parameters.wind.XWind'>, 'y': <class 'geo_parameters.wind.YWind'>,
'magnitude': <class 'geo_parameters.wind.Wind'>, 'direction': <class 'geo_parameters.wind.WindDir'>,
'opposite_direction': <class 'geo_parameters.wind.WindDirTo'>}

>>> gp.wind.XWind.my_family('magnitude')
<class 'geo_parameters.wind.Wind'>
```

```python
>>> gp.wave.Tp.standard_name()
'sea_surface_wave_period_at_variance_spectral_density_maximum'
>>> gp.wave.Tp.i_am()
'period'

>>> gp.wave.Tp.my_family()
{'period': <class 'geo_parameters.wave.Tp'>, 'frequency': <class 'geo_parameters.wave.Fp'>,
'angular_frequency': <class 'geo_parameters.wave.Wp'>}

>>> assert gp.wave.Tp == gp.wave.Tp.my_family('period')
>>> gp.wave.Tp.my_family('frequency')
<class 'geo_parameters.wave.Fp'>
```

```python
>>> gp.wave.StokesDir.standard_name()
'sea_surface_wave_stokes_drift_to_direction'
>>> gp.wave.StokesDir.i_am()
'direction'

>>> gp.wave.StokesDir.my_family('x')
<class 'geo_parameters.wave.XStokes'>
>>> gp.wave.StokesDir.my_family('opposite_direction')
<class 'geo_parameters.wave.StokesDirFrom'>

>>> gp.wave.StokesDir.my_family('x').standard_name()
'sea_surface_wave_stokes_drift_x_velocity'
>>> gp.wave.StokesDir.my_family('opposite_direction').standard_name()
'sea_surface_wave_stokes_drift_from_direction'
```

```python
>>> gp.wave.Hs.my_family()
{}
>>> gp.wave.Hs.i_am()
None
>>> gp.wave.Hs.my_family('period')
None 
```

## Finding parameters

The right class can be found usin the standard name with the get function:

```python
>>> gp.get("sea_surface_wave_significant_height")
<class 'geo_parameters.geo_parameters.wave.Hs'>

>>> gp.get("significant_height_of_wind_and_swell_waves") # alias of standard name
<class 'geo_parameters.geo_parameters.wave.Hs'>
```

If an xarray Dataset has standard_name attributes, the correct key(s) can be found using the class-method:

```python
>>> ds
<xarray.Dataset> Size: 1kB
Dimensions:              (lat: 11, lon: 6)
Coordinates:
  * lon                  (lon) float64 48B 5.0 6.0 7.0 8.0 9.0 10.0
  * lat                  (lat) float64 88B 50.0 51.0 52.0 ... 58.0 59.0 60.0
Data variables:
    interesting_hs_name  (lat, lon) float64 528B 0.0 0.0 0.0 ... 0.0 0.0 0.0
    peak_period          (lat, lon) float64 528B 1.0 1.0 1.0 1.0 ... 1.0 1.0 1.0
```
```python
>>> ds.interesting_hs_name
<xarray.DataArray 'interesting_hs_name' (lat: 11, lon: 6)> Size: 528B
array([[0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0.],
        ...
       [0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0.]])
Coordinates:
  * lon      (lon) float64 48B 5.0 6.0 7.0 8.0 9.0 10.0
  * lat      (lat) float64 88B 50.0 51.0 52.0 53.0 54.0 ... 57.0 58.0 59.0 60.0
Attributes:
    standard_name:  sea_surface_wave_significant_height
```

```python
>>> gp.wave.Hs.find_me_in_ds(ds)
['interesting_hs_name']

>>> gp.wave.Tp.find_me_in_ds(ds)
['peak_period']

>>> Tp.find_me_in_ds(ds, return_first=True)
'peak_period'
```

We can also used built-in methods to compare and find parameters, since '==' comparison between difference instances wont work:

```python
>>> gp.wave.Hs.is_same(gp.wave.Hs()) # class and instance match
True
```

We can also check if a parameter is found within a list:

```python
>>> gp.wave.Hs.is_in([gp.wave.Tp, 'pdir', gp.wave.Hs('swh')])
True
```

We can also get a parameter in a list that matches a class (or an instance)

```python
>>> gp.wave.Hs.find_me_in([gp.wave.Tp, 'pdir', gp.wave.Hs('swh')])
[<geo_parameters.wave.Hs object at 0x797d8b9ba060>] # Returned: gp.wave.Hs('swh')
>>> gp.wave.Hs('dont_worry_about_name').find_me_in([gp.wave.Tp, 'pdir', gp.wave.Hs('swh')], return_first=True)
<geo_parameters.wave.Hs object at 0x7ae7433b70b0>

>>> gp.wave.Hs.find_me_in([gp.wave.Tp, 'pdir', gp.wave.Hs('swh'), gp.wave.Hs])
[<geo_parameters.wave.Hs object at 0x7ae7433b7b90>, <class 'geo_parameters.wave.Hs'>]
>>> gp.wave.Hs.find_me_in([gp.wave.Tp, 'pdir', gp.wave.Hs('swh')], return_first=True)
<geo_parameters.wave.Hs object at 0x7ae7433b7720>

>>> gp.wave.Hs.find_me_in([gp.wave.Tp, 'pdir'])
[]
>>> gp.wave.Hs.find_me_in([gp.wave.Tp, 'pdir'], return_first=True)
None
```



