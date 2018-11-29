# opener
##基础环境
* 1.numpy
* 2.Netcdf4
* 3.brew gdal>=2.1
* 4.pyhton

##使用说明：

```
from openUtils import OpenUtils

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
```
##说明

* 输入文件
* 1.file_type：输入文件格式（'nc', 'grib2', 'img', 'GeoTiff'）
* 2.out_file ：输出文件地址
* 3.export_type ：输出文件格式（'nc', 'grib2', 'img', 'GeoTiff'）
* 4.data_type ：输出数据类型('int8', 'int16', 'float32', 'float64', 'float128')
* 5.lat_order ：维度顺序（"asc"/"desc"）
* 6.values_strs ：输出NC格式要素(前两个必须为 维度 经度) 示例：["lats", "lons", "abc"]
* 7.nc_values ：输入NC格式要提取的要素（前两个必须为 维度 经度）示例：["LAT", "LON", "PAIR"]
* 8.is_rewirte_data：是否去写出数据（True/False）
* 9.proj:投影方式（mercator）

```


##示例
```
from openUtils import OpenUtils

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
```