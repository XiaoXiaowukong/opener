# -*- coding:utf-8 -*-
import numpy as np
from osgeo import gdal, ogr


# 插值脚本
class GdalGridTools():
    def __init__(self):
        pass

    def initParams(self, lats, lons, data):
        print "gdalgird…"
        self.lats = lats
        self.lons = lons
        self.data = data
        self.gridProcess()

    def gridProcess(self):
        # self.makePolygon()
        self.makePolygonP()
        self.gdal_grid()

    def makePolygon(self):
        myPolygon = {"type": "Polygon"}
        maxSize = self.lons.__len__()
        intCount = 0;
        myWkt = 'POLYGON (('
        for index_lat, lat in enumerate(self.lats):
            for index_lon, lon in enumerate(self.lons):
                intCount = intCount + 1
                # print intCount
                uvdata = round(self.data[index_lon, index_lat], 2)
                myWkt = myWkt + "%s %s %s" % (lon, lat, uvdata)
                if (intCount == maxSize):
                    myWkt = myWkt + "))"
                else:
                    myWkt = myWkt + ","
        self.myWkt = myWkt

    # 经纬度和数据都是二维且数量相等
    def makePolygonP(self):
        print self.data[0].shape
        print self.lats.shape
        self.data = np.asarray(self.data)
        print len(self.lats.shape)
        if (len(self.lats.shape) == 3):
            if (self.lats[0].shape == self.lons[0].shape == self.data[0].shape):
                print "gdalgird…", self.data.shape
                self.lat0 = np.nanmin(self.lats)
                self.lat1 = np.nanmax(self.lats)
                self.lon0 = np.nanmin(self.lons)
                self.lon1 = np.nanmax(self.lons)
                self.pRows = self.lats[0].shape[0]
                self.pCols = self.lats[0].shape[1]
                myWkt = 'POLYGON (('
                for pRowIndex, pRow in enumerate(range(self.pRows)):
                    for pColIndex, pCol in enumerate(range(self.pCols)):
                        lat = self.lats[0][pRow][pCol]
                        lon = self.lons[0][pRow][pCol]
                        value = self.data[0][pRow][pCol]
                        myWkt = myWkt + "%s %s %s" % (lon, lat, value)
                        if (pRowIndex + 1 == self.pRows and pColIndex + 1 == self.pCols):
                            myWkt = myWkt + "))"
                        else:
                            myWkt = myWkt + ","
                self.myWkt = myWkt

            else:
                print "grid data is error"

    def gdal_grid(self):
        polygon = ogr.CreateGeometryFromWkt(self.myWkt)
        grid_data = gdal.Grid('', polygon.ExportToJson(), \
                              width=self.pCols, height=self.pRows, outputType=gdal.GDT_Float32, outputSRS='EPSG:4326',
                              outputBounds=[self.lon0, self.lat0, self.lon1, self.lat1], noData=0.0, \
                              # format='GTiff', algorithm='invdist')
                              format='MEM', algorithm='nearest')
        # format='GTiff', algorithm='invdistnn')
        # format='GTiff', algorithm='linear')

        self.grid_data = grid_data
