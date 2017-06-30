#
# -*- coding: UTF-8 -*- 

# Import arcpy module
import arcpy
#from arcpy import env

# Overwrite pre-existing files
arcpy.env.workspace = r"C:\Data\Projects\IceCharts"
arcpy.env.overwriteOutput = "True"

'''
# Create a pollution file geodatabase if it doesn't exist
try:
    arcpy.CreateFileGDB_management("C:/Data/Projects/IceCharts", "iskart.gdb")
except:
    pass
'''
#outWorkspace = "C:/Data/Projects/IceCharts/iskart.gdb/"

# Set Geoprocessing environments
arcpy.env.scratchWorkspace = "C:\\Data\\Projects\\IceCharts\\iskart.gdb"


# Local variables:
chart_ice_shp = "C:\\Data\\Projects\\IceCharts\\chart_ice.shp"
iskart_gdb = "C:\\Data\\Projects\\IceCharts\\iskart.gdb"
s100Hav = "C:\\Data\\Projects\\IceCharts\\iskart.gdb\\s100Hav"
iskart_Historikk__2_ = "C:\\Data\\Projects\\IceCharts\\iskart.gdb\\iskart_Historikk"
iskart_Project_Clip__4_ = "C:\\Data\\Projects\\IceCharts\\iskart.gdb\\iskart_Project_Clip"
iskart = "C:\\Data\\Projects\\IceCharts\\iskart.gdb\\iskart"
iskart__2_ = "C:\\Data\\Projects\\IceCharts\\iskart.gdb\\iskart"
iskart_Project = "C:\\Data\\Projects\\IceCharts\\iskart.gdb\\iskart_Project"
iskart_Project_Clip = "C:\\Data\\Projects\\IceCharts\\iskart.gdb\\iskart_Project_Clip1"
iskart_Project_Clip__2_ = "C:\\Data\\Projects\\IceCharts\\iskart.gdb\\iskart_Project_Clip1"
Output_Feature_Class = "C:\\Data\\Projects\\IceCharts\\iskart.gdb\\iskart_Project_Clip"

# Process: Feature Class to Feature Class
arcpy.AddMessage("Importer Shapefil til geodatabase")
arcpy.FeatureClassToFeatureClass_conversion(chart_ice_shp, iskart_gdb, "iskart", "", "ID \"ID\" true true false 8 Long 0 8 ,First,#,C:\\Data\\Projects\\IceCharts\\chart_ice.shp,ID,-1,-1;ICE_TYPE \"ICE_TYPE\" true true false 20 Text 0 0 ,First,#,C:\\Data\\Projects\\IceCharts\\chart_ice.shp,ICE_TYPE,-1,-1", "")

# Process: Define Projection
arcpy.DefineProjection_management(iskart, "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]")

# Process: Project
arcpy.AddMessage("Projiser til UTM 33")
arcpy.Project_management(iskart__2_, iskart_Project_Clip, "PROJCS['WGS_1984_UTM_Zone_33N',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',15.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]", "", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]")

# Process: Clip
arcpy.AddMessage("Klipp bort landarealet")
arcpy.Clip_analysis(iskart_Project, s100Hav, iskart_Project_Clip, "")

# Process: Add Field
arcpy.AddMessage("Legg til datofelt")
arcpy.AddField_management(iskart_Project_Clip, "Dato", "DATE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field
arcpy.AddMessage("Legg til dagens dato")
arcpy.CalculateField_management(iskart_Project_Clip__2_, "Dato", "time.strftime('%d/%m/%Y')", "PYTHON_9.3", "")

# Process: Append
arcpy.AddMessage("Legg til datasett i tidsserie")
arcpy.Append_management("C:\\Data\\Projects\\IceCharts\\iskart.gdb\\iskart_Project_Clip1", iskart_Historikk__2_, "TEST", "", "")

# Process: Delete Features
arcpy.AddMessage("Slett gårdagens isdata")
arcpy.DeleteFeatures_management(iskart_Project_Clip__4_)

# Process: Append (2)
arcpy.AddMessage("Legg til dagens isdata")
arcpy.Append_management("C:\\Data\\Projects\\IceCharts\\iskart.gdb\\iskart_Project_Clip1", Output_Feature_Class, "NO_TEST", "ID \"ID\" true true false 4 Long 0 0 ,First,#,C:\\Data\\Projects\\IceCharts\\iskart.gdb\\iskart_Project_Clip1,ID,-1,-1;ICE_TYPE \"ICE_TYPE\" true true false 20 Text 0 0 ,First,#,C:\\Data\\Projects\\IceCharts\\iskart.gdb\\iskart_Project_Clip1,ICE_TYPE,-1,-1;Shape_Length \"Shape_Length\" false true true 8 Double 0 0 ,First,#,C:\\Data\\Projects\\IceCharts\\iskart.gdb\\iskart_Project_Clip1,Shape_length,-1,-1,C:\\Data\\Projects\\IceCharts\\iskart.gdb\\iskart_Project_Clip1,Shape_length,-1,-1;Shape_Area \"Shape_Area\" false true true 8 Double 0 0 ,First,#,C:\\Data\\Projects\\IceCharts\\iskart.gdb\\iskart_Project_Clip1,Shape_area,-1,-1,C:\\Data\\Projects\\IceCharts\\iskart.gdb\\iskart_Project_Clip1,Shape_area,-1,-1;Dato \"Dato\" true true false 8 Date 0 0 ,First,#,C:\\Data\\Projects\\IceCharts\\iskart.gdb\\iskart_Project_Clip1,Dato,-1,-1", "")

