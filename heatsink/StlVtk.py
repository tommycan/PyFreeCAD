#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
#paraview.simple._DisableFirstRenderCameraReset()

# create a new 'STL Reader'
heatsinkstl = STLReader(FileNames=['C:\\Users\\tommy\\code\\PyFreeCAD\\heatsink\\heatsink.stl'])

# save data
SaveData('C:/Users/tommy/code/PyFreeCAD/heatsink/heatsink.vtk', proxy=heatsinkstl, FileType='Ascii')
