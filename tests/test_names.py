from geo_parameters.wave import Hs


def test_name_of_class():
    assert Hs.name == "hs"
    assert Hs.long_name() == "significant_wave_height"
    assert Hs.standard_name() == "sea_surface_wave_significant_height"
    assert Hs.standard_name(alias=True) == "significant_height_of_wind_and_swell_waves"


def test_units_of_class():
    assert str(Hs.unit()) == "m"


def test_name_of_instance():
    assert Hs().name == "hs"
    assert Hs(name="hsig").name == "hsig"
    assert Hs("hsig").name == "hsig"
    assert Hs().long_name() == "significant_wave_height"
    assert Hs().standard_name() == "sea_surface_wave_significant_height"
    assert (
        Hs().standard_name(alias=True) == "significant_height_of_wind_and_swell_waves"
    )


def test_units_of_instance():
    assert str(Hs().unit()) == "m"
