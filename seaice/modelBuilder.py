# Import arcpy module
import arcpy


# Local variables:
Cellsize = "0,25"
ice20120801_shp = "C:\\Data\\Projects\\IsAnalyse\\Isdata\\barents_shp2\\ice20120801.shp"
ice20120801_shp__2_ = "C:\\Data\\Projects\\IsAnalyse\\Isdata\\barents_shp2\\ice20120801.shp"
ice20120801_shp__3_ = "C:\\Data\\Projects\\IsAnalyse\\Isdata\\barents_shp2\\ice20120801.shp"
ice20120801 = "C:\\Data\\Projects\\IsAnalyse\\Isdata\\GRID_temp\\ice20120801"

# Process: Add Field
arcpy.AddField_management(ice20120801_shp, "IceConc", "SHORT", "", "", "", "", "NON_NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field
arcpy.CalculateField_management(ice20120801_shp__2_, "IceConc", "ifBlock( !ICE_TYPE!)", "PYTHON", "def ifBlock(iceName):\\n    if iceName == 'Fast Ice':\\n        return 100\\n    elif iceName == 'Very Close Drift Ice':\\n        return 95\\n    elif  iceName== 'Close Drift Ice':\\n        return 80\\n    elif  iceName== 'Open Drift Ice':\\n        return 55\\n    elif  iceName== 'Very Open Drift Ice':\\n        return 25\\n    elif  iceName== 'Open Water':\\n        return 5")

# Process: Polygon to Raster
arcpy.PolygonToRaster_conversion(ice20120801_shp__3_, "IceConc", ice20120801, "MAXIMUM_AREA", "NONE", Cellsize)

