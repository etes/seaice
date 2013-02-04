'''
Created on 5. sep. 2012

@author: ermias
'''

# import system modules
import arcpy
from arcpy import env
import os

# set workspace environment where the shapefiles are located
env.workspace = "C:\\BaseFolderName\\FolderOfShapefiles"
# creates a list of feature classes or shapefiles in the current workspace
fcs = arcpy.ListFeatureClasses('*') 

# set local variables
try:
    for file in fcs:
        inData = file
        coordinateSystem = "PROJCS[\"MGI_Austria_GK_East\",GEOGCS[\"GCS_MGI\",DATUM[\"D_MGI\",SPHEROID[\"Bessel_1841\",6377397.155,299.1528128]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],PROJECTION[\"Transverse_Mercator\"],PARAMETER[\"False_Easting\",0.0],PARAMETER[\"False_Northing\",-5000000.0],PARAMETER[\"Central_Meridian\",16.33333333333333],PARAMETER[\"Scale_Factor\",1.0],PARAMETER[\"Latitude_Of_Origin\",0.0],UNIT[\"Meter\",1.0],AUTHORITY[\"EPSG\",31256]]"
        arcpy.DefineProjection_management(inData, coordinateSystem)

except arcpy.ExecuteError:
    print arcpy.GetMessages(2)
    arcpy.AddError(arcpy.GetMessages(2))
except Exception as e:
    print e.args[0]
    arcpy.AddError(e.args[0]) 
