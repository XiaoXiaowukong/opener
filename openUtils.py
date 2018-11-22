__version__ = '$Id: umOpener.py 27349 2014-05-16 18:58:51Z rouault $'
type_list = ('nc', 'grib2', 'img', 'GeoTiff')
export_list = ('nc', 'grib2', 'img', 'GeoTiff')
datatype_list = ('int8', 'int16', 'float32', 'float64', 'float128')
order = ("asc", "desc")
proj = ("mercator",)
read_file_error = "read file error"


class OpenUtils():
    def __init__(self):
        pass

    def initParams(self, inputFile, **kwargs):
        arguments = []
        for kwarg_key in kwargs.keys():
            arguments.append("--%s" % kwarg_key)
            arguments.append(kwargs[kwarg_key])
        self.inputFile = inputFile
        self.optparse_init()
        (self.options, self.args) = self.parser.parse_args(args=arguments)
        self.stopped = False
        self.process()

    # -------------------------------------------------------------------------

    def optparse_init(self):
        """Prepare the option parser for input (argv)"""
        from optparse import OptionParser, OptionGroup
        usage = 'Usage: %prog [options] input_file(s) [output]'
        p = OptionParser(usage, version='%prog ' + __version__)
        p.add_option(
            '-t',
            '--file_type',
            dest='intPutType',
            type='choice',
            choices=type_list,
            help="Tile cutting profile (%s) - default 'mercator' (Google Maps compatible)"
                 % ','.join(type_list),
        )
        p.add_option(
            '-o',
            '--out_file',
            dest='outFile',
            help="out_file", )
        p.add_option(
            '-e',
            '--export_type',
            dest='exportType',
            type='choice',
            choices=export_list,
            help='export file type(%s)' % ",".join(export_list)
        )
        p.add_option(
            '-d',
            '--data_type',
            dest='dataType',
            type='choice',
            choices=datatype_list,
            help='output file data type'
        )
        p.add_option(
            '-l',
            '--lat_order',
            dest="latOrder",
            type='choice',
            choices=order,
            help='lat list order'
        )
        p.add_option(
            '-p',
            '--proj',
            dest="proj",
            type='choice',
            choices=proj,
            help='data set proj'
        )
        p.add_option(
            '-n',
            '--nc_values',
            dest='ncValues',
            help='intput every band name',
        )
        p.add_option(
            '-v',
            '--values_strs',
            dest='valueStrs',
            help='output every band name',
        )
        p.set_defaults(
            export_type='GTiff',
            data_type="float32",
            lat_order="asc",
            proj="mercator"
        )

        self.parser = p

    # =================================================================================================
    def openFile(self):
        if (self.options.intPutType == "nc"):
            import netcdf4reader
            try:
                nc_data, nc_attrs = netcdf4reader.read(self.inputFile, self.options.ncValues, self.options.dataType)
                self.lats = nc_data[0]
                self.lons = nc_data[1]
                self.data = nc_data
                self.nc_attrs = nc_attrs
            except Exception, e:
                self.stop()
                print read_file_error
        if (self.options.intPutType == "GeoTiff"):
            print "gtif"
            import geotiffreader
            try:
                (in_geotransf, in_proj, in_lats, in_lons, in_data, no_data) = geotiffreader.read(self.inputFile)
                self.lats = in_lats
                self.lons = in_lons
                self.data = in_data
                self.no_data = no_data

            except Exception, e:
                self.stop()
                print read_file_error

    # =================================================================================================
    def wirteNetcdfFile(self):
        if (not self.stopped):
            if (self.options.exportType == "nc"):
                print "create netcdf4"
                import netcdf4reader
                netcdf4reader.wirte(self.options.outFile, self.data, self.options.valueStrs, self.nc_attrs,
                                    self.options.dataType)
            if (self.options.exportType == "GeoTiff"):
                import geotiffreader
                geotiffreader.wirte(self.lats, self.lons, self.data, self.no_data, self.options.outFile,
                                    self.options.latOrder, self.options.proj)

        else:
            print "stop wirte file"

    # ==================================================================================================
    def stop(self):
        self.stopped = True

    # ===================================================================================================
    def process(self):
        self.openFile()
        self.wirteNetcdfFile()
