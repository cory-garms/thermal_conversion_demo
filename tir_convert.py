from asyncio import subprocess
from os import mkdir, path
import numpy as np
from thermal import Thermal
import matplotlib.pyplot as plt
from osgeo import gdal, ogr

import pathlib
import subprocess

thermal = Thermal(
    dirp_filename='plugins/dji_thermal_sdk_v1.1_20211029/windows/release_x64/libdirp.dll',
    dirp_sub_filename='plugins/dji_thermal_sdk_v1.1_20211029/windows/release_x64/libv_dirp.dll',
    iirp_filename='plugins/dji_thermal_sdk_v1.1_20211029/windows/release_x64/libv_iirp.dll',
    exif_filename='plugins/exiftool-12.35.exe',
    dtype=np.float32,
)


files = list(pathlib.Path('images').glob('*T.JPG'))


for i in files:    
    temperature = thermal.parse_dirp2(image_filename=i)
    filename = pathlib.Path(i).stem
    # create the output image
    driver = gdal.GetDriverByName('GTiff')
    outDs = driver.Create('images/' + filename + '.tif', temperature.shape[1], temperature.shape[0], 1, gdal.GDT_Float32)
    outband = outDs.GetRasterBand(1)
    #write temp to array
    outband.WriteArray(temperature)
    outDs = None


subprocess.Popen(['exiftool','-tagsfromfile','%d%f.JPG' , "'-gps*'", '-ext', 'tif', "images" ], stdout=None)
