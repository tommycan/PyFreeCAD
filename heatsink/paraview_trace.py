#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'STL Reader'
heatsinkstl = STLReader(FileNames=['C:\\Users\\tommy\\code\\PyFreeCAD\\heatsink\\heatsink.stl'])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [2638, 1342]

# get color transfer function/color map for 'STLSolidLabeling'
sTLSolidLabelingLUT = GetColorTransferFunction('STLSolidLabeling')

# show data in view
heatsinkstlDisplay = Show(heatsinkstl, renderView1)
# trace defaults for the display properties.
heatsinkstlDisplay.Representation = 'Surface'
heatsinkstlDisplay.ColorArrayName = ['CELLS', 'STLSolidLabeling']
heatsinkstlDisplay.LookupTable = sTLSolidLabelingLUT
heatsinkstlDisplay.OSPRayScaleArray = 'STLSolidLabeling'
heatsinkstlDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
heatsinkstlDisplay.SelectOrientationVectors = 'None'
heatsinkstlDisplay.ScaleFactor = 0.003109999932348728
heatsinkstlDisplay.SelectScaleArray = 'STLSolidLabeling'
heatsinkstlDisplay.GlyphType = 'Arrow'
heatsinkstlDisplay.GlyphTableIndexArray = 'STLSolidLabeling'
heatsinkstlDisplay.DataAxesGrid = 'GridAxesRepresentation'
heatsinkstlDisplay.PolarAxes = 'PolarAxesRepresentation'
heatsinkstlDisplay.GaussianRadius = 0.001554999966174364
heatsinkstlDisplay.SetScaleArray = [None, '']
heatsinkstlDisplay.ScaleTransferFunction = 'PiecewiseFunction'
heatsinkstlDisplay.OpacityArray = [None, '']
heatsinkstlDisplay.OpacityTransferFunction = 'PiecewiseFunction'

# reset view to fit data
renderView1.ResetCamera()

# show color bar/color legend
heatsinkstlDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# save data
SaveData('C:/Users/tommy/code/PyFreeCAD/heatsink/heatsink.vtk', proxy=heatsinkstl, FileType='Ascii')

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.012500000186264515, 0.015549999661743641, 0.08446957641200366]
renderView1.CameraFocalPoint = [0.012500000186264515, 0.015549999661743641, 0.004999999888241291]
renderView1.CameraParallelScale = 0.020568239910581876

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).