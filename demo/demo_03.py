import Part, FreeCAD, math, sys, os, time
from FreeCAD import Base

# run script in freecad python console with this command
# execfile("/home/tommy/scratch/projects/PyFreeCAD/demo/demo_03.py")

def makeEllipseFace(iS1=Base.Vector(2.0,0.0,0.0), iS2=Base.Vector(0.0,1.0,0.0), iC=Base.Vector(0.0,0.0,0.0)):
	
	ellipse = Part.Ellipse(iS1, iS2, iC).toShape()
	wire = Part.Wire(ellipse.Edges)
	face = Part.Face(wire.Wires)
		
	return [face, wire]
  
def makePillar(iFace, iExtrudeDir=Base.Vector(0.0,0.0,5.0)):
  
  extrude = iFace.extrude(iExtrudeDir)
  
  return extrude

def makeChamfer(iExtrude, iRadius=0.2):
	
	pillar = iExtrude.makeFillet(iRadius, [extrude.Edges[2]])

	return pillar

def makePillarWithChamfer(iFace, iRadius=0.2, iExtrudeDir=Base.Vector(0.0,0.0,5.0)):
	
	extrude = iFace.extrude(iExtrudeDir)
	pillar = extrude.makeFillet(iRadius, [extrude.Edges[2]])

	return pillar

isGui=True; doSave=False
#isGui=False; doSave=True

delay = 2.0

S1 = Base.Vector(5.0,0.0,0.0)
S2 = Base.Vector(0.0,2.0,0.0)
#C = Base.Vector(0.0,0.0,0.0)
[face1, wire1] = makeEllipseFace(Base.Vector(5.0,0.0,0.0), Base.Vector(0.0,2.0,0.0), Base.Vector(0.0,0.0,0.0))
[face2, wire2] = makeEllipseFace(Base.Vector(5.0,0.0,2.0), Base.Vector(0.0,2.0,2.0), Base.Vector(0.0,0.0,2.0))
[face3, wire3] = makeEllipseFace(Base.Vector(5.0,0.0,4.0), Base.Vector(0.0,2.0,4.0), Base.Vector(0.0,0.0,4.0))
Part.show(face1)
Part.show(face2)
Part.show(face3)

loft = Part.makeLoft([wire1, wire2, wire3])
Part.show(loft)

#if isGui:
#  Part.show(face)
#  Gui.SendMsgToActiveView("ViewFit")
#  time.sleep(delay)
#  Gui.ActiveDocument.getObject("Shape").Visibility=False
#
#r = 0.5
#extdir = Base.Vector(0.0,0.0,10.0)
#extrude = makePillar(face, extdir)
#if isGui:
#  Part.show(extrude)
#  Gui.SendMsgToActiveView("ViewFit")
#  time.sleep(delay)
#  Gui.ActiveDocument.getObject("Shape001").Visibility=False
#
#
#pillar = makeChamfer(extrude, r)
#if isGui:
#  Part.show(pillar)
#  Gui.SendMsgToActiveView("ViewFit")
#  time.sleep(delay)
#  Gui.ActiveDocument.getObject("Shape002").Visibility=False
#
#if doSave:
#  pillar.exportStl("pillar.stl")
#  pillar.exportStep("pillar.stp")
