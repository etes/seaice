'''
Created on 5. sep. 2012

@author: ermias
'''
# Import arcpy module
import arcpy


# Local variables:
Input_Raster = "C:\\Data\\Projects\\IsAnalyse\\Isdata\\GRID_temp\\g2012_03"
GRID_temp = "C:\\Data\\Projects\\IsAnalyse\\Isdata\\GRID_temp"
g2012_03 = "C:\\Data\\Projects\\IsAnalyse\\Isdata.gdb\\g2012_03"

# Process: Copy Raster
tempEnvironment0 = arcpy.env.workspace
arcpy.env.workspace = ""
arcpy.CopyRaster_management(Input_Raster, g2012_03, "", "", "", "NONE", "NONE", "")
arcpy.env.workspace = tempEnvironment0

