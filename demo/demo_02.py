import Part, FreeCAD, math, sys, os, time
from FreeCAD import Base

# run script in freecad python console with this command
# execfile("/home/tommy/scratch/projects/PyFreeCAD/demo/demo_02.py")

def makeEllipseFace(iS1=Base.Vector(2.0,0.0,0.0), iS2=Base.Vector(0.0,1.0,0.0), iC=Base.Vector(0.0,0.0,0.0)):
	
	ellipse = Part.Ellipse(iS1, iS2, iC).toShape()
	wire = Part.Wire(ellipse.Edges)
	face = Part.Face(wire.Wires)
		
	return face
  
def makePillar(iFace, iExtrudeDir=Base.Vector(0.0,0.0,5.0)):
  
  extrude = iFace.extrude(iExtrudeDir)
  
  return extrude

def makeChamfer(iExtrude, iRadius=0.2):
	
	pillar = iExtrude.makeFillet(iRadius, [extrude.Edges[2]])

	return pillar

def makeBase(iLx=40, iLy=60, iLz=1):
 	
  lc = Base.Vector(0.0, 0.0, -iLz)
  uc = Base.Vector(iLx, iLy, 0.0)
	
  return Part.makeBox(iLx, iLy, iLz, lc)

def makeFuseBoxPillars(iBox, iPillar, iLx=40, iLy=60, iLz=1, iNx=4, iNy=6):
	
	dx = iLx/(iNx+1.0)
	dy = iLy/(iNy+1.0)
	ret = iBox.copy()
	for ix in xrange(1,iNx+1):
		for iy in xrange(1,iNy+1):
			p = iPillar.copy()
			p.translate(Base.Vector(ix*dx, iy*dy, 0.0))
			ret = ret.fuse(p)
	
	return ret

isGui=True;
#isGui=False;

delay = 0.25

S1 = Base.Vector(2.0,0.0,0.0)
S2 = Base.Vector(0.0,1.0,0.0)
C = Base.Vector(0.0,0.0,0.0)
face = makeEllipseFace(S1, S2, C)
if isGui:
  Part.show(face)
  Gui.SendMsgToActiveView("ViewFit")
  time.sleep(delay)
  Gui.ActiveDocument.getObject("Shape").Visibility=False

r = 0.2
extdir = Base.Vector(0.0,0.0,5.0)
extrude = makePillar(face, extdir)
if isGui:
  Part.show(extrude)
  Gui.SendMsgToActiveView("ViewFit")
  time.sleep(delay)
  Gui.ActiveDocument.getObject("Shape001").Visibility=False

pillar = makeChamfer(extrude, r)
if isGui:
  Part.show(pillar)
  Gui.SendMsgToActiveView("ViewFit")
  time.sleep(delay)
#  Gui.ActiveDocument.getObject("Shape002").Visibility=False


lx=40
ly=60
lz=1
boxbase = makeBase(lx, ly, lz)
if isGui:
  Part.show(boxbase)
  Gui.SendMsgToActiveView("ViewFit")
  time.sleep(delay)
#  Gui.ActiveDocument.getObject("Shape003").Visibility=False

nx=4
ny=6
fuse = makeFuseBoxPillars(boxbase, pillar, lx, ly, lz, nx, ny)
if isGui:
  Part.show(fuse)
  Gui.SendMsgToActiveView("ViewFit")
  time.sleep(delay)
  Gui.ActiveDocument.getObject("Shape002").Visibility=False
  Gui.ActiveDocument.getObject("Shape003").Visibility=False
#  Gui.ActiveDocument.getObject("Shape004").Visibility=False

