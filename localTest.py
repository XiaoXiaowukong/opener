# -*- coding:utf-8 -*-
from openUtils import OpenUtils
import os
import matplotlib.pyplot as plt


def tif2tif():
    myOpenUtils = OpenUtils()
    myOpenUtils.initParams(
        "/Volumes/pioneer/gdal_Demo/translateResult/Z_NAFP_C_BABJ_20180701091809_P_CLDAS_RT_ASI_0P0625_HOR-PRS-2018070109.tif",
        file_type="GeoTiff",
        out_file="./tif2tif.tif",
        export_type="GeoTiff",
        data_type='float32',
        lat_order="asc",
        values_strs=["lats", "lons", "abc"],
        nc_values=["LAT", "LON", "PAIR"],
        is_rewirte_data=False,
        proj="mercator")

    print myOpenUtils.lats


def nc2nc():
    myOpenUtils = OpenUtils()
    myOpenUtils.initParams(
        "/Volumes/pioneer/gdal_Demo/cldas_/Z_NAFP_C_BABJ_20180701091809_P_CLDAS_RT_ASI_0P0625_HOR-PRS-2018070109.nc",
        file_type="nc",
        out_file="/Volumes/pioneer/gdal_Demo/cldas_/Z_NAFP_C_BABJ_20180701091809_P_CLDAS_RT_ASI_0P0625_HOR-PRS-2018070109_100.nc",
        export_type="nc",
        data_type='float32',
        values_strs="lats,lons,nc2nc",
        nc_values="LAT,LON,PAIR",
        is_rewirte_data="True",
        eval_str="data/100",
        proj="mercator")


def img2img():
    myOpenUtils = OpenUtils()
    myOpenUtils.initParams(
        "/Volumes/pioneer/img_hdr/FY3C_L_2016_08_29_11_28_A_G_VIRRX_L1B.img",
        file_type="img",
        out_file="./img2img.img",
        export_type="img",
        data_type='float32',
        # lat_order="asc",
        # data_order="desc",
        values_strs="lats,lons,img2img",
        nc_values="LAT,LON, PAIR",
        proj="mercator")


def girb2_girb2():
    myOpenUtils = OpenUtils()
    myOpenUtils.initParams(
        "/Volumes/pioneer/liaoning/grb2/20180806/Z_SURF_C_BABJ_20180806001030_P_CMPA_FAST_CHN_0P05_HOR-PRE-2018080600.GRB2",
        # "./utm.grb2",
        file_type="grib2",
        out_file="./grib2_2_grib2.grb2",
        export_type="grib2",
        data_type='float32',
        proj="mercator")


def nc2tif():
    myOpenUtils = OpenUtils()
    myOpenUtils.initParams(
        "/Volumes/pioneer/gdal_Demo/cldas_/NAFP_CLDAS2.0_RT_GRB_WIV10_20181128-18.nc",
        file_type="nc",
        out_file="/Volumes/pioneer/gdal_Demo/cldas_/NAFP_CLDAS2.0_RT_GRB_WIV10_20181128-18.tif",
        export_type="GeoTiff",
        data_type='float32',
        is_rewirte_data="True",
        values_strs="lats,lons,abc",
        nc_values="LAT,LON,WIV10",
        proj="mercator")


def tif2nc():
    myOpenUtils = OpenUtils()
    myOpenUtils.initParams(
        "/Volumes/pioneer/gdal_Demo/translateResult/Z_NAFP_C_BABJ_20180701091809_P_CLDAS_RT_ASI_0P0625_HOR-PRS-2018070109.tif",
        file_type="GeoTiff",
        out_file="./tif2nc.nc",
        export_type="nc",
        data_type='float32',
        lat_order="asc",
        values_strs=["lats", "lons", "tif2nc"],
        nc_values=["LAT", "LON", "PAIR"],
        proj="mercator")


def nc2img():
    myOpenUtils = OpenUtils()
    myOpenUtils.initParams(
        "/Volumes/pioneer/gdal_Demo/cldas_/Z_NAFP_C_BABJ_20180701091809_P_CLDAS_RT_ASI_0P0625_HOR-PRS-2018070109.nc",
        file_type="nc",
        out_file="/Volumes/pioneer/gdal_Demo/cldas_/Z_NAFP_C_BABJ_20180701091809_P_CLDAS_RT_ASI_0P0625_HOR-PRS-2018070109.img",
        export_type="img",
        data_type='float32',
        is_rewirte_data="True",
        values_strs="lats,lons,abc",
        nc_values="LAT,LON,PAIR",
        eval_str="data/1000",
        proj="mercator")


def img2nc():
    myOpenUtils = OpenUtils()
    myOpenUtils.initParams(
        "/Volumes/pioneer/gdal_Demo/cldas_/Z_NAFP_C_BABJ_20180701091809_P_CLDAS_RT_ASI_0P0625_HOR-PRS-2018070109.img",
        file_type="img",
        out_file="/Volumes/pioneer/gdal_Demo/cldas_/Z_NAFP_C_BABJ_20180701091809_P_CLDAS_RT_ASI_0P0625_HOR-PRS-2018070109_original.nc",
        export_type="nc",
        data_type='float32',
        # lat_order="asc",
        # data_order="desc",
        is_rewirte_data="True",
        values_strs="LAT,LON,PAIR",
        nc_values="LAT,LON,PAIR",
        proj="mercator")


def tif2img():
    myOpenUtils = OpenUtils()
    myOpenUtils.initParams(
        "/Volumes/pioneer/gdal_Demo/translateResult/Z_NAFP_C_BABJ_20180701091809_P_CLDAS_RT_ASI_0P0625_HOR-PRS-2018070109.tif",
        file_type="GeoTiff",
        out_file="./tif2img.img",
        export_type="img",
        data_type='float32',
        lat_order="asc",
        values_strs=["lats", "lons", "tif2img"],
        nc_values=["LAT", "LON", "PAIR"],
        proj="mercator")


def img2tif():
    myOpenUtils = OpenUtils()
    myOpenUtils.initParams(
        "/Volumes/pioneer/img_hdr/FY3C_L_2016_08_29_11_28_A_G_VIRRX_L1B.img",
        file_type="img",
        out_file="./img2tif_asc.tif",
        export_type="GeoTiff",
        data_type='float32',
        # lat_order="asc",
        # data_order="desc",
        values_strs=["lats", "lons", "img2tif"],
        nc_values=["LAT", "LON", "PAIR"],
        proj="mercator")


def makeSmtif():
    smdir = "/Volumes/pioneer/gdal_Demo/cldas_nrt_day/2018/12"
    smtifdir = "/Volumes/pioneer/gdal_Demo/cldas_nrt_day/2018/12_tif"
    smdir = "/Volumes/pioneer/gdal_Demo/cldas_nrt_5day/2018"
    smtifdir = "/Volumes/pioneer/gdal_Demo/cldas_nrt_5day/2018_tif"
    rsmdir = "/Volumes/pioneer/gdal_Demo/cldas_nrt_day/2018/12/avg"
    rsmtifdir = "/Volumes/pioneer/gdal_Demo/cldas_nrt_day/2018/12/avg_tif"
    dirlist = os.listdir(rsmdir)
    myOpenUtils = OpenUtils()
    for smFile in dirlist:
        input_file = "%s/%s" % (rsmdir, smFile)
        print input_file
        out_file = "%s/%s.tif" % (rsmtifdir, os.path.splitext(smFile)[0])
        myOpenUtils.initParams(
            input_file,
            file_type="nc",
            out_file=out_file,
            export_type="GeoTiff",
            data_type='float',
            is_rewirte_data="True",
            nc_values="LAT,LON,RSM",
            lat_order="desc",
            proj="mercator")


def readFY4():
    myOpenUtils = OpenUtils()
    input_file = "/Volumes/pioneer/风云4/FY4A-_AGRI--_N_REGC_1047E_L1-_FDI-_MULT_NOM_20181202042334_20181202042750_4000M_V0001.img"
    myOpenUtils.initParams(
        input_file,
        file_type="img",
        out_file="./FY4A.img",
        export_type="img",
        data_type='float32',
        is_rewirte_data="True",
        data_order="desc",
        proj="mercator"
    )
    print myOpenUtils.data.shape
    data = myOpenUtils.data[0]
    import numpy as np
    print np.max(data)
    print np.nanmean(data)
    print np.nanmax(data)
    print np.nanmin(data)
    plt.imshow(data)
    plt.show()


def nc2imgPlus():
    myOpenUtils = OpenUtils()
    myOpenUtils.initParams(
        "/Volumes/pioneer/gdal_Demo_内蒙三维数据/wrfout_4km/2018/20181115/wrfout_SMOIS000010_t00Z_F000.nc",
        file_type="nc_p",
        out_file="/Volumes/pioneer/gdal_Demo_内蒙三维数据/wrfout_4km/2018/20181115/wrfout_SMOIS000010_t00Z_F000_1.nc",
        export_type="nc",
        data_type='float32',
        is_rewirte_data="True",
        values_strs="lats,lons,abc",
        nc_values="XLAT,XLONG,SMOIS",
        proj="mercator")


if __name__ == '__main__':
    # makeSmtif()
    # readFY4()
    # tif2tif()
    # print "0-----"
    # nc2nc()
    # print "1-----"
    # img2img()
    # print "8-----"
    # nc2tif()
    # print "2-----"
    # tif2nc()
    # print "3-----"
    #     nc2img()
    #     print "4-----"
    #     img2nc()
    #     print "5-----"

    # tif2img()
    # print "6-----"
    # img2tif()
    # print "7-----"
    # girb2_girb2()
    # print "8-----"
    nc2imgPlus()
    print "9----"
