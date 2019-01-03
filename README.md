# opener 格式转换工具

## 运行环境
* python 2.7

## 依赖库
* numpy 版本:1.15.3 
* Netcdf4 版本:1.4.2
* gdal 版本:>=2.1

## 使用说明：(带*号为必传参数)
* ***输入文件**（没有参数名）
* ***file_type**：输入文件格式（'nc', 'grib2', 'img', 'GeoTiff'）如果输入为nc 必须要有nc_values参数 注意！！！ nc_p格式是为wrfout数据定制的处理方式
* ***out_file** ：输出文件地址
* ***export_type** ：输出文件格式（'nc', 'nc_p','grib2', 'img', 'GeoTiff'）如果输出为nc 必须要有values_strs参数
* data_type ：输出数据类型('int8', 'int16','float', 'float32', 'float64', 'float128')(默认'float32')
* is_rewirte_data：是否去写出数据（True/False）默认False
* eval_str :对数据进行计算 例（"data/100"）
* values_strs ：输出NC格式要素(前两个必须为 维度 经度) 示例："lats,lons,abc"（如果输出数据格式为nc 此参数必传）
* nc_values ：输入NC格式要提取的要素（前两个必须为 维度 经度）示例："LAT,LON,PAIR"（如果输入数据格式为nc 此参数必传）
* proj:投影方式（mercator）默认mercator
* lat_order ：维度顺序（"asc"/"desc"）默认 asc
* data_order :数据顺序（默认asc）


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
        eval_str="data/1000",
        values_strs="lats,lons,abc",
        nc_values="LAT,LON,WIV10",
        proj="mercator")
```

## 外部调用说明((带*号为必传参数) 参数名（key）和参数（value）要用空格隔开)
* ***输入文件**（没有参数名）
* ***--file_type**：输入文件格式（'nc','nc_p', 'grib2', 'img', 'GeoTiff'）如果输入为nc 必须要有nc_values参数 注意！！！ nc_p格式是为wrfout数据定制的处理方式
* ***--out_file** ：输出文件地址
* ***--export_type** ：输出文件格式（'nc', 'grib2', 'img', 'GeoTiff'）如果输出为nc 必须要有values_strs参数
* --data_type：输出数据类型('int8', 'int16','float','float32', 'float64', 'float128')(默认'float32')
* --is_rewirte_data：是否去写出数据（True/False）默认False
* --eval_str :对数据进行计算 例（"data/100"）
* --values_strs ：输出NC格式要素(前两个必须为 维度 经度) 示例："lats,lons,abc"（如果输出数据格式为nc 此参数必传）
* --nc_values ：输入NC格式要提取的要素（前两个必须为 维度 经度）示例："LAT,LON,PAIR"（如果输入数据格式为nc 此参数必传）
* --proj:投影方式（mercator）默认mercator
* --lat_order ：维度顺序（"asc"/"desc"）默认 asc
* --data_order :数据顺序（默认asc）

## 外部调用示例
```
python openUtils.py /Volumes/pioneer/gdal_Demo/cldas_/NAFP_CLDAS2.0_RT_GRB_WIV10_20181128-18.nc \
                    --file_type nc \
                    --out_file /Volumes/pioneer/gdal_Demo/cldas_/NAFP_CLDAS2.0_RT_GRB_WIV10_20181128-18.tif \
                    --export_type GeoTiff \
                    --data_type float32 \
                    --is_rewirte_data True \
                    --nc_values LAT,LON,WIV10 \
                    --proj mercator
```

