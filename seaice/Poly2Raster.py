'''
Created on 5. sep. 2012

@author: ermias
'''

# Import system modules
import arcpy, arcgisscripting
from arcpy import env
from arcpy.sa import *
from arcpy import sa

gp = arcgisscripting.create()

#theSnapRaster = arcpy.GetParameterAsText(0)
#theOutWorkSpace = arcpy.GetParameterAsText(1)
theOutWorkSpace = "C:/data/Projects/IsAnalyse/Isdata/barents_shp2"
#theSnapRaster = "C:/data/Projects/IsAnalyse/Isanalyse.gdb/ice_grid_25km"
theSnapRaster = "C:/data/Projects/IsAnalyse/Isdata/GRID/ice_grid_25km"
#theOutWorkSpace = "C:/data/Projects/IsAnalyse/isanalyse.gdb"

# Set environment settings
#cellSize = arcpy.env.cellSize
arcpy.env.cellSize = theSnapRaster
cellSize = arcpy.env.cellSize
print cellSize

arcpy.env.outputCoordinateSystem = theSnapRaster
CoordSys = arcpy.env.outputCoordinateSystem
arcpy.env.snapRaster = theSnapRaster

arcpy.env.workspace = theOutWorkSpace

fcs = arcpy.ListFeatureClasses()
for fc in fcs:
    # Set local variables
    #inFeatures = "ice20110104"
    inFeatures = fc
    valField = "IceConc"
    #outRaster = "c:/Data/Projects/IsAnalyse/Isanalyse.gdb/ras20110104"
    outRaster = theOutWorkSpace + "/ras" + fc.lstrip('ice')
    assignmentType = "MAXIMUM_AREA"
    priorityField = ""

    arcpy.env.cellSize = cellSize
    arcpy.env.outputCoordinateSystem = CoordSys

    # Execute PolygonToRaster
    arcpy.PolygonToRaster_conversion(inFeatures, valField, outRaster, assignmentType, priorityField, cellSize)

    outCon = Con(IsNull(outRaster),0,outRaster)
    outCon.save("C:/data/Projects/IsAnalyse/isanalyse.gdb/temp" + fc.lstrip('ice'))

    # Mask land
    inRaster = theOutWorkSpace + "/temp" + fc.lstrip('ice')
    finalRaster = theOutWorkSpace + "/g" + fc.lstrip('ice')
    inMask = "C:/Data/Projects/IsAnalyse/Isdata/GRID/sea"

    gp.ExtractByMask_sa(inRaster, inMask, finalRaster)


    

