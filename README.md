# geo-parameters
Metadata of geophysical (especially wave) parameters. The main idea is to be able to use standard CF-names without having to remember or check the names.

## Names of parameters

The parameters are classes in sub-modules according to the physical property (wave, ocean, wind)

```python
from geo_parameters.wave import Hs, Tp
```

These classes have information about the parameter:

```python
Hs.standard_name()
'sea_surface_wave_significant_height'
```
Every parameters has a pre-defined name

```python
Hs.name
'hs'
```
If you want to define some other names for the parameters, then you can create an instance. By default the name of the instance is the short name, but this can be changed:

```python
hsig = Hs()
hsig.name
'hs'

hsig = Hs(name='hsig')
hsig.name
'hsig'
```


The instance still contains the standard name (and some long name that doesn't follow any standard):

```python
hsig.standard_name() 
'sea_surface_wave_significant_height'

hsig.long_name() 
'significant_wave_height'
```

If the parameter has several standard names, you can use the alias-keyword

```python
hsig.standard_name(alias=True) 
'significant_height_of_wind_and_swell_waves'
```

If the parameter has only one standard name, alias does nothing:

```python
Tp.standard_name()
'sea_surface_wave_period_at_variance_spectral_density_maximum'

Tp.standard_name(alias=True)
'sea_surface_wave_period_at_variance_spectral_density_maximum'
```

## Finding parameters

The right class can be found from a name using the get function:

```python
from geo_parameters import get as gpget
```

The parameter can then be fetched using the standard name, the alias or the short name:

```python
gpget("sea_surface_wave_significant_height")
<class 'geo_parameters.geo_parameters.wave.Hs'>

gpget("significant_height_of_wind_and_swell_waves")
<class 'geo_parameters.geo_parameters.wave.Hs'>

gpget("hs")
<class 'geo_parameters.geo_parameters.wave.Hs'>
```

A dict of all available parameters can also be compiled:

```python
from geo_parameters import dict_of_parameters
```

```python
dop = dict_of_parameters()
dop = dict_of_parameters(alias=True)
dop = dict_of_parameters(short=True)
```

where the keywords define what string will serve as key in the dictonary (the value is always the parameter class).

If an xarray Dataset has standard_name attributes, the correct key can be found using the class-method:

```python
ds
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
ds.interesting_hs_name
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
Hs.find_me_in_ds(ds)
'interesting_hs_name'

Tp.find_me_in_ds(ds)
'peak_period'
```

