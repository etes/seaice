'''
Created on 5. sep. 2012

@author: ermias
'''
import arcpy
from arcpy import env

# Local variables:
Input_Features = arcpy.GetParameterAsText(0)
out_wspace = arcpy.GetParameterAsText(1)
cellsize = arcpy.GetParameterAsText(2)

Cell_assignment_type = "CELL_CENTER"
Priority_field = "NONE"

# todo: get fields from input RulePoly attributes
value_fields = "BOL BOH SUB ALP TAW TAS TUN".split()

env.workspace = out_wspace

try:
    for vf in value_fields:
        out_rast = '%s/value_%s' % (out_wspace, vf)
        print "Running PolygonToRaster, output: %s" % out_rast
        arcpy.PolygonToRaster_conversion(Input_Features, vf, out_rast,
            Cell_assignment_type, Priority_field, cellsize)
        print arcpy.GetMessages()

except Exception as e:
    print e.message
    arcpy.AddError(e.message)

print arcpy.GetMessages()
