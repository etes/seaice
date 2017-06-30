'''
Created on 16. aug. 2012

@author: ermias
'''
class LicenseError(Exception):
    pass

import arcpy
from arcpy import env
from arcpy import *

try:
    if arcpy.CheckExtension("sa") == "Available":
        arcpy.CheckOutExtension("sa")
    else:
        # raise a custom exception
        #
        raise LicenseError

    env.workspace = "C:/Data/Projects/IsAnalyse/Isanalyse.gdb"
    rasters = arcpy.ListRasters("*", "GRID")
    print rasters
    arcpy.RasterToGeodatabase_conversion(rasters.mean, "C:/Data/Projects/IsAnalyse/Isanalyse.gdb/mean2", None)
    arcpy.CheckInExtension("sa")

except LicenseError:
    print "sa Analyst license is unavailable"
except:
    print arcpy.GetMessages(2)