import geo_parameters as gp

def test_wind_names():
    assert gp.wind.NorthWind.standard_name() == "northward_wind"
    assert gp.wind.EastWind.standard_name() == "eastward_wind"
    assert gp.wind.XWind.standard_name() == "x_wind"
    assert gp.wind.YWind.standard_name() == "y_wind"

    assert gp.wind.Wind.standard_name() == "wind_speed"
    assert gp.wind.WindDir.standard_name() == "wind_from_direction"
    assert gp.wind.WindDirTo.standard_name() == "wind_to_direction"

def test_gust_names():
    assert gp.wind.NorthGust.standard_name() == "northward_wind_gust"
    assert gp.wind.EastGust.standard_name() == "eastward_wind_gust"
    assert gp.wind.XGust.standard_name() == "x_wind_gust"
    assert gp.wind.YGust.standard_name() == "y_wind_gust"

    assert gp.wind.Gust.standard_name() == "wind_speed_of_gust"
    assert gp.wind.GustDir.standard_name() == "wind_gust_from_direction"
    assert gp.wind.GustDirTo.standard_name() == "wind_gust_to_direction"

def test_fv_names():
    assert gp.wind.NorthFrictionVelocity.standard_name() == "northward_friction_velocity_in_air"
    assert gp.wind.EastFrictionVelocity.standard_name() == "eastward_friction_velocity_in_air"
    assert gp.wind.XFrictionVelocity.standard_name() == "x_friction_velocity_in_air"
    assert gp.wind.YFrictionVelocity.standard_name() == "y_friction_velocity_in_air"

    assert gp.wind.FrictionVelocity.standard_name() ==  "magnitude_of_surface_friction_velocity_in_air"
    assert gp.wind.FrictionVelocityDir.standard_name() == "friction_velocity_in_air_from_direction"
    assert gp.wind.FrictionVelocityDirTo.standard_name() =="friction_velocity_in_air_to_direction"