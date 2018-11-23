from openUtils import OpenUtils


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
        proj="mercator")


def nc2nc():
    myOpenUtils = OpenUtils()
    myOpenUtils.initParams(
        "/Volumes/pioneer/gdal_Demo/cldas_/Z_NAFP_C_BABJ_20180701091809_P_CLDAS_RT_ASI_0P0625_HOR-PRS-2018070109.nc",
        file_type="nc",
        out_file="./nc2nc.nc",
        export_type="nc",
        data_type='float32',
        values_strs=["lats", "lons", "nc2nc"],
        nc_values=["LAT", "LON", "PAIR"],
        proj="mercator")


def nc2tif():
    myOpenUtils = OpenUtils()
    myOpenUtils.initParams(
        "/Volumes/pioneer/gdal_Demo/cldas_/Z_NAFP_C_BABJ_20180701091809_P_CLDAS_RT_ASI_0P0625_HOR-PRS-2018070109.nc",
        file_type="nc",
        out_file="./nc2tif.tif",
        export_type="GeoTiff",
        data_type='float32',
        values_strs=["lats", "lons", "abc"],
        nc_values=["LAT", "LON", "PAIR"],
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


if __name__ == '__main__':
    # tif2tif()
    # print "0-----"
    # nc2nc()
    # print "1-----"
    # nc2tif()
    # print "2-----"
    tif2nc()
    print "3-----"

