
'''
Created on 5. sep. 2012

@author: ermias
'''

import arcpy
import os, glob, shutil

theDir = arcpy.GetParameterAsText(0)
#theDir = 'i:/2011/barents_shp'

fileNames = glob.glob(theDir + '/*.shp')

for f in fileNames:
    newf = f.strip(theDir) + 'prj'
    print newf
    shutil.copyfile("i:\\adm\\icechart.prj", theDir + "\\" + newf)


