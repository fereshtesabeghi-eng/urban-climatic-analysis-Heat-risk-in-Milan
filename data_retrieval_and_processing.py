import cdsapi
import os
import xarray as xr
import pandas as pd
import numpy as np

# 1. Download Dataset via CDS API
def download_era5_data():
    client = cdsapi.Client()
    dataset = "reanalysis-era5-single-levels"
    request = {
        "product_type": ["reanalysis"],
        "variable": [
            "10m_u_component_of_wind", "10m_v_component_of_wind",
            "2m_dewpoint_temperature", "2m_temperature",
            "surface_pressure", "clear_sky_direct_solar_radiation_at_surface",
            "surface_solar_radiation_downwards"
        ],
        "year": ["2012"], "month": ["07"], "day": ["27"],
        "time": [f'{h:02d}:00' for h in range(24)],
        "data_format": "netcdf4",
        "download_format": "unarchived",
        "area": [45.4642, 9.1893, 45.4642, 9.1893],
        "grid": [0.0, 0.0]
    }
    client.retrieve(dataset, request).download()

# 2. Process Meteorological Data
def calculate_rh(temp_c, dewpoint_c):
    es = 6.112 * np.exp((17.67 * temp_c) / (temp_c + 243.5))
    e = 6.112 * np.exp((17.67 * dewpoint_c) / (dewpoint_c + 243.5))
    return (e / es) * 100

def process_meteo_data(instant_nc, accum_nc, output_csv):
    ds_instant = xr.open_dataset(instant_nc)
    ds_accum = xr.open_dataset(accum_nc)
    
    times = ds_instant["valid_time"].to_index()
    df = pd.DataFrame({"year": times.year, "DoY": times.dayofyear, "hour": times.hour})
    
    # Temperature conversion
    df["temp"] = ds_instant["t2m"].values.flatten() - 273.15
    df["relathumid"] = calculate_rh(df["temp"], ds_instant["d2m"].values.flatten() - 273.15)
    
    # Wind speed
    df["windspeed"] = np.sqrt(ds_instant["u10"].values.flatten()**2 + ds_instant["v10"].values.flatten()**2)
    
    # Radiation conversion
    df["surfrad"] = ds_accum["ssrd"].values.flatten() / 3600
    df["dirsurfrad"] = ds_accum["cdir"].values.flatten() / 3600
    df["diffsurfrad"] = (df["surfrad"] - df["dirsurfrad"]).clip(lower=0)
    
    df.to_csv(output_csv, index=False, float_format="%.2f")