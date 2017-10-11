import Part, FreeCAD, math, sys, os
from FreeCAD import Base

# execfile("/home/tommy/scratch/projects/PyFreeCAD/pillars/ellipse/hollow-fin.py")


def makeEllipseWire(iS1=Base.Vector(2.0,0.0,0.0), iS2=Base.Vector(0.0,1.0,0.0), iC=Base.Vector(0.0,0.0,0.0)):
	
	ellipse = Part.Ellipse(iS1, iS2, iC).toShape()
	wire = Part.Wire(ellipse.Edges)
	#face = Part.Face(wire.Wires)
		
	return wire
  
def makeExtrude(iWire, iExtrudeDir=Base.Vector(0.0,0.0,5.0)):
  
  extrude = iWire.extrude(iExtrudeDir)
  
  return extrude


S1 = Base.Vector(4.4e-3,0.0,0.0)
S2 = Base.Vector(0.0,0.5e-3,0.0)
C = Base.Vector(0.0,0.0,0.0)
wire = makeEllipseWire(S1, S2, C)
#Part.show(wire)

#extrude_dir = Base.Vector(0.0,0.0,4.0e-3)
extrude_dir = Base.Vector(0.0,0.0,12.0e-3)
face = makeExtrude(wire, extrude_dir)
Part.show(face)

face.exportStep("hollow-fin.stp")
