import Part, FreeCAD, math
from FreeCAD import Base

# execfile("C:/Users/tommy/code/PyFreeCAD/pillars/ellipse/create_ellipse.py")

def makeEllipseFace(iS1=Base.Vector(2.0,0.0,0.0), iS2=Base.Vector(0.0,1.0,0.0), iC=Base.Vector(0.0,0.0,0.0)):
	
	ellipse = Part.Ellipse(iS1, iS2, iC).toShape()
	wire = Part.Wire(ellipse.Edges)
	face = Part.Face(wire.Wires)
	
	return face

def makePillarWithChamfer(iFace, iRadius=0.3, iExtrudeDir=Base.Vector(0.0,0.0,5.0)):
	
	extrude = iFace.extrude(iExtrudeDir)
	pillar = extrude.makeFillet(iRadius, [extrude.Edges[2]])
	
	return pillar

def makePillarWithFillet(iPillar, iRadius=0.3):
	
	bb = iPillar.BoundBox
	
	lc=Base.Vector(2*bb.XMin,2*bb.YMin,bb.ZMin-1)
	uc=Base.Vector(2*bb.XMax,2*bb.YMax,bb.ZMin)
	box = Part.makeBox(uc[0]-lc[0],uc[1]-lc[1],uc[2]-lc[2], lc)
	
	fuse = iPillar.fuse(box)
	fuse = fuse.makeFillet(iRadius, [fuse.Edges[9]])
	fuse = fuse.cut(box)
	
	return fuse
	
face = makeEllipseFace()
pillar = makePillarWithChamfer(face)
fuse = makePillarWithFillet(pillar)

Part.show(fuse)