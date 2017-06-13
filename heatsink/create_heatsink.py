import Part, FreeCAD, math, sys, os
from FreeCAD import Base

# execfile("C:/Users/tommy/code/PyFreeCAD/heatsink/create_heatsink.py")

	
def makeHeatSink(iW=0.0311, iL=0.025, iH=0.002, iN=7, iHF=0.01, iTF=0.001):
	
	baseplate = Part.makeBox(iL, iW, iH)
	
	fin = Part.makeBox(iL, iTF, iHF);
	
	fuse = baseplate.fuse(fin)
	
	disp = (iW-iTF)/(iN-1.0)
	
	if disp<=iTF:
		raise NameError("The design is not realizable")
	
	for i in xrange(1,iN):
		f = fin.copy()
		f.translate(Base.Vector(0.0, i*disp, 0.0))
		fuse = fuse.fuse(f)
	
	return fuse

try:
	heatsink = makeHeatSink(0.0311, 0.025, 0.002, 7, 0.01, 0.001)
	heatsink.exportStl("C:/Users/tommy/code/PyFreeCAD/heatsink/heatsink.stl")
	#heatsink.exportStep("C:/Users/tommy/code/PyFreeCAD/heatsink/heatsink.stp")
	#Part.show(heatsink)
	#Gui.SendMsgToActiveView("ViewFit")
except NameError:
	print 'An exception flew by!'
	raise
	
	
	
	
	
	
