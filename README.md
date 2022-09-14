# thermal_conversion_demo

Tutorial on how to use thermal_parser and exiftool to convert DJI radiometric JPG (R-JPG) to TIF with temp values and append GPS metadata

*** for Windows PC only, need to install Anaconda prior (https://www.anaconda.com/) ***

Follow these steps to batch process all R-JPG in a folder and output converted TIF files with same base name in the same folder:

1. Clone this repository to your computer and unzip it

2. Move the file called exiftool.exe to a folder that is listed in your PATH variable such as 'C:/Windows'

3. Open the Anaconda terminal and create a new python 3.6 environment using: `conda create -n thermal_env python=3.6 gdal numpy matplotlib -y`

4. Activate the new environment using: `conda acivate thermal_env`

5. Move any R-JPG images to be converted into the 'images' folder. (There is a sample H20-T image provided called 'DJI_0002_T.JPG')

6. In the anaconda terminal, navigate to the folder that contains the python scripts 'thermal.py' and 'tir_convert.py' as well as the 'images' and 'plugins' directories

7. Process the images using: `python tir_convert.py`

8. Find the converted images in the same folder as the inputs with the same root names and the '.tif' file extension


YouTube video showing more detailed process for how this was created can be found here: https://youtu.be/ulnPtSWGg18

Credits:

-SanNianYiSi on github and their thermal_parser repo: https://github.com/SanNianYiSi/thermal_parser

-Exiftool by Phil Harvey: www.exiftool.com
