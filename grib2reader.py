from osgeo import gdal
import numpy as np


def read(currentGrb2File):
    dataset = gdal.Open(currentGrb2File, gdal.GA_ReadOnly)
    x_size = dataset.RasterXSize
    y_size = dataset.RasterYSize
    geotrans = dataset.GetGeoTransform()  # 仿射矩阵
    print geotrans
    gdata = dataset.ReadAsArray(0, 0, x_size, y_size)

    print geotrans[3], geotrans[3] + y_size * geotrans[5], geotrans[5]
    print geotrans[0], geotrans[0] + x_size * geotrans[1], geotrans[1]
    glat = np.arange(geotrans[3], geotrans[3] + y_size * geotrans[5], geotrans[5])
    glon = np.arange(geotrans[0], geotrans[0] + x_size * geotrans[1], geotrans[1])
    print "glat", glat.shape
    print "glon", glon.shape
    print "gdata", np.array(gdata).shape
    del dataset
    return glat, glon, gdata
