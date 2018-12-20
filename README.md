# opener

## 基础环境
* 1.numpy
* 2.Netcdf4
* 3.brew gdal>=2.1
* 4.pyhton

## 使用说明：(带*号为必传参数)
* *1.输入文件（没有参数名）
* *2.file_type：输入文件格式（'nc', 'grib2', 'img', 'GeoTiff'）如果输入为nc 必须要有nc_values参数
* *3.out_file ：输出文件地址
* *4.export_type ：输出文件格式（'nc', 'grib2', 'img', 'GeoTiff'）如果输出为nc 必须要有values_strs参数
* 5.data_type ：输出数据类型('int8', 'int16','float', 'float32', 'float64', 'float128')(默认'float32')
* 6.lat_order ：维度顺序（"asc"/"desc"）默认 asc
* 7.values_strs ：输出NC格式要素(前两个必须为 维度 经度) 示例："lats,lons,abc"（如果输出数据格式为nc 此参数必传）
* 8.nc_values ：输入NC格式要提取的要素（前两个必须为 维度 经度）示例："LAT,LON,PAIR"（如果输入数据格式为nc 此参数必传）
* 9.is_rewirte_data：是否去写出数据（True/False）默认False
* 10.proj:投影方式（mercator）默认mercator

## 示例

```
from openUtils import OpenUtils

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
```

## 外部调用说明((带*号为必传参数) 参数名（key）和参数（value）要用空格隔开)
* *1.输入文件（没有参数名）
* *2.--file_type：输入文件格式（'nc', 'grib2', 'img', 'GeoTiff'）如果输入为nc 必须要有nc_values参数
* *3.--out_file ：输出文件地址
* *4.--export_type ：输出文件格式（'nc', 'grib2', 'img', 'GeoTiff'）如果输出为nc 必须要有values_strs参数
* *5.--data_type ：输出数据类型('int8', 'int16','float','float32', 'float64', 'float128')
* *6.--lat_order ：维度顺序（"asc"/"desc"）默认 asc
* 7.--values_strs ：输出NC格式要素(前两个必须为 维度 经度) 示例："lats,lons,abc"（如果输出数据格式为nc 此参数必传）
* 8.--nc_values ：输入NC格式要提取的要素（前两个必须为 维度 经度）示例："LAT,LON,PAIR"（如果输入数据格式为nc 此参数必传）
* 9.--is_rewirte_data：是否去写出数据（True/False）默认False
* 10.--proj:投影方式（mercator）默认mercator

## 外部调用示例
python openUtils.py /Volumes/pioneer/gdal_Demo/cldas_/NAFP_CLDAS2.0_RT_GRB_WIV10_20181128-18.nc --file_type nc --out_file /Volumes/pioneer/gdal_Demo/cldas_/NAFP_CLDAS2.0_RT_GRB_WIV10_20181128-18.tif --export_type GeoTiff --data_type float32 --is_rewirte_data True --nc_values LAT,LON,WIV10 --proj mercator

