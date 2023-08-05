import zarr
import os

sp = "/Users/abigailmcgovern/Data/coombes-lab/live_nTnG_3D_MTG_x2900-3412_y2600-3112.zarr"
data = zarr.open(sp)

# t = 100, t = 250, t = 40, t = 0
# save separate for each channel

save_dir = '/Users/abigailmcgovern/Data/iterseg/kidney_development'
prefix = 'live_nTnG_3D_MTG_x2900-3412_y2600-3112'

time_points = [0, 40, 100, 250] # selected time points that look different

def save_3D_frames(data, time_points, save_dir, prefix):
    channels = range(data.shape[1])
    for t in time_points:
        t_arr = data[t, ...]
        for c in channels:
            tc_arr = t_arr[c, ...]
            sn = prefix + f'_t{t}_c{c}.zarr'
            p = os.path.join(save_dir, sn)
            zarr.save(p, tc_arr)


