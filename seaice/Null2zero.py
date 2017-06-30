'''
Created on 5. sep. 2012

@author: ermias
'''


# Import system modules
import arcpy
#from arcpy import env
#from arcpy import sa

# Set environment settings
arcpy.env.workspace = "C:/data/Projects/IsAnalyse/isanalyse.gdb"

# Set local variables
inRaster = "ras20110105"

# Execute Con
#outCon = Con(IsNull(inRaster), inTrueRaster, inFalseRaster)
outCon = Con(IsNull(inRaster),0,inRaster)


# Save the output 
outCon.save("C:/data/Projects/IsAnalyse/isanalyse.gdb/g20110105")


