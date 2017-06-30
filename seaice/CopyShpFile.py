'''
Created on 5. sep. 2012

@author: ermias
'''
 
# Import system modules
import arcpy
from arcpy import env
 
# Set environment settings
#theWksp = arcpy.GetParameterAsText(0)
#env.workspace = "C:/data/projects/isanalyse/isdata/barents_shp"
#env.workspace = theWksp


# Set local variables
inFeatures = arcpy.GetParameterAsText(0)

outLocation = arcpy.GetParameterAsText(1)    
#outLocation = "C:\Data\Projects\IsAnalyse\Isanalyse.gdb"
 
# Execute TableToGeodatabase
arcpy.FeatureClassToGeodatabase_conversion(inFeatures, outLocation)