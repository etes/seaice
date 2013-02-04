'''
Created on 5. sep. 2012

@author: ermias
'''

# Import system modules
import arcpy
# import arcgisscripting
from arcpy import env
# from arcpy.sa import *
from arcpy import sa

#gp = arcgisscripting.create()


#theOutWorkspace = arcpy.GetParameterAsText(0)
theOutWorkspace = "C:/Data/Projects/IsAnalyse/Isanalyse.gdb"
arcpy.env.workspace = theOutWorkspace

#inRasters = arcpy.GetParameterAsText(0)
#inRaster2 = arcpy.GetParameterAsText(1)
inRaster1 = theOutWorkspace + "/g20110103"
#inRaster2 = theOutWorkspace + "/g20110104"

#gp.workspace = "C:/Data/Projects/IsAnalyse/Isanalyse.gdb"

rasters = arcpy.ListRasters("*", "GRID")
arcpy.env.workspace = theOutWorkspace
i = 0

for ras in rasters:
    i = i + 1
    if i == 1:
        outRaster = ras
    else:
        outRaster = (arcpy.Raster(outRaster)) + (arcpy.Raster(ras))

        
#outRaster = outRaster / i
outRaster.save("C:/Data/Projects/IsAnalyse/Isanalyse.gdb/mean1")
