import xarray as xr
import rioxarray
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def create_utci_animation(nc_file, output_gif):
    ds = xr.open_dataset(nc_file)
    data_2012 = ds['high_utci_days'].sel(time=ds.time.dt.year == 2012, height=2.0)
    
    # Set CRS and reproject
    data_2012 = data_2012.rio.write_crs("EPSG:4326")
    projected = data_2012.rio.reproject("EPSG:32632")
    
    fig, ax = plt.subplots(figsize=(8, 12))
    im = ax.imshow(projected.isel(time=0).values, cmap="coolwarm", vmin=0, vmax=31)
    
    def update(frame):
        im.set_data(projected.isel(time=frame).values)
        return im

    anim = FuncAnimation(fig, update, frames=len(projected.time), interval=1000)
    anim.save(output_gif, writer="pillow", fps=1)