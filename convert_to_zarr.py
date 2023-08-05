from imaris_ims_file_reader.ims import ims
import zarr

p = '/Volumes/ANC_LAB_2TB/For Abi/Live data/live_nTnG_3D_MTG.ims'
img = ims(p, ResolutionLevelLock=6)

def print_info(a):
    print(a.ResolutionLevelLock)
    print(a.ResolutionLevels)
    print(a.TimePoints)
    print(a.Channels)
    print(a.shape)
    print(a.chunks)
    print(a.dtype)
    print(a.ndim)


print_info(img)

# data is in TCZXY

def get_desired_slice(a, x_start=2900, x_stop=3412, y_start=2600, y_stop=2885):
    crop = a[:, :, :, y_start:y_stop, x_start:x_stop]
    return crop


def save_desired_slice(a, x_start=2900, x_stop=3412, y_start=2600, y_stop=3112):
    crop = a[:, :, :, y_start:y_stop, x_start:x_stop]
    sp = f"/Users/abigailmcgovern/Data/coombes-lab/live_nTnG_3D_MTG_x{x_start}-{x_stop}_y{y_start}-{y_stop}.zarr"
    zarr.save(sp, crop)
    return crop


roi0 = get_desired_slice(img)
sp = "/Users/abigailmcgovern/Data/coombes-lab/live_nTnG_3D_MTG_x2941-3384_y2588-2885.zarr"
zarr.save(sp, roi0)

roi1 = save_desired_slice(img)

sp = "/Users/abigailmcgovern/Data/coombes-lab/live_nTnG_3D_MTG_x2900-3412_y2600-3112.zarr"
data = zarr.open(sp)

# looks good