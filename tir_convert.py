from os import mkdir, path, remove
import numpy as np
from thermal import Thermal
import matplotlib.pyplot as plt
from osgeo import gdal, ogr
import glob
import pathlib
import subprocess

#from https://github.com/SanNianYiSi/thermal_parser
thermal = Thermal(
    dirp_filename='plugins/dji_thermal_sdk_v1.1_20211029/windows/release_x64/libdirp.dll',
    dirp_sub_filename='plugins/dji_thermal_sdk_v1.1_20211029/windows/release_x64/libv_dirp.dll',
    iirp_filename='plugins/dji_thermal_sdk_v1.1_20211029/windows/release_x64/libv_iirp.dll',
    exif_filename='plugins/exiftool-12.35.exe',
    dtype=np.float32,
)

#get list of JPGs to convert
files = list(pathlib.Path('images').glob('*T.JPG'))

#iterate through JPGs, convert to temperature, and write out to TIFs
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

#use exiftool to append geodata from JPGs to TIFs
p = subprocess.Popen(['exiftool','-tagsfromfile','%d%f.JPG' , "'-gps*'", '-ext', 'tif', "images" ], stdout=None)
#kill subprocess 
p.kill()

#remove redundant files
for orig in glob.iglob(path.join('./images', '*.tif_original')):
    remove(orig)
