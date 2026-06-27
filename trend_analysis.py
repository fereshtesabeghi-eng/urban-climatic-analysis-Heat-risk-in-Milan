import xarray as xr
import matplotlib.pyplot as plt
import pandas as pd
import os

def plot_utci_trends(nc_file, output_img):
    ds = xr.open_dataset(nc_file)
    milan_point = ds['high_utci_days'].sel(lat=45.50, lon=9.20, height=2.0, method="nearest")
    milan_trend = milan_point.sel(time=slice("1973-01-01", "2023-12-31"))

    month_settings = {
        6: {"name": "Jun.", "linestyle": (0, (1, 1, 1, 1))},
        7: {"name": "Jul.", "linestyle": (0, (1, 0, 1, 0))},
        8: {"name": "Aug.", "linestyle": (0, (5, 5, 3))},
        9: {"name": "Sep.", "linestyle": (0, (9, 3, 1, 3))}
    }

    plt.figure(figsize=(24, 6))
    for month, month_data in milan_trend.groupby("time.month"):
        if month in month_settings:
            years = month_data["time.year"].values
            plt.plot(years, month_data.values, color="0.1", linestyle=month_settings[month]["linestyle"], linewidth=3)
            plt.text(years[-1] + 0.5, month_data.values[-1], month_settings[month]["name"], fontsize=18, va="center")

    plt.axvline(x=2012, color="red", linestyle="-", linewidth=5, alpha=0.66)
    plt.savefig(output_img, dpi=100, bbox_inches='tight')
    plt.show()