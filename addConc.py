'''
Created on 5. sep. 2012

@author: ermias
'''

# Import arcpy module
import arcpy, arcgisscripting
import time
start = time.time()

arcpy.env.workspace = 'C:/Data/Projects/IsAnalyse/Isdata/barents_shp2'
gp = arcgisscripting.create()

theField = 'IceConc'

fcs = arcpy.ListFeatureClasses()

for fc in fcs:
    fields = gp.ListFields(fc, theField)
    field_found = fields.Next()
    if field_found:
        pass
    else:
        arcpy.AddField_management(fc,'IceConc',"SHORT")


fcs = arcpy.ListFeatureClasses()

# Local variables:
# Process: Calculate Field
for fc in fcs:
    arcpy.CalculateField_management(fc, "IceConc", "ifBlock( !ICE_TYPE!)", "PYTHON",
                                    "def ifBlock(iceName):\\n    if iceName == 'Fast Ice':\\n        return 100\\n    elif iceName == 'Very Close Drift Ice':\\n        return 95\\n    elif  iceName== 'Close Drift Ice':\\n        return 80\\n    elif  iceName== 'Open Drift Ice':\\n        return 55\\n    elif  iceName== 'Very Open Drift Ice':\\n        return 25\\n    elif  iceName== 'Open Water':\\n        return 5")
    

proctime = (time.time() - start)
print "Done! Elapsed time:", proctime