import Part, FreeCAD, math
from FreeCAD import Base

# execfile("C:/Users/tommy/code/PyFreeCAD/pillars/ellipse/create_ellipse.py")
# execfile("/home/tommy/scratch/projects/PyFreeCAD/pillars/ellipse/test.py")

def makeEllipseFace(iS1=Base.Vector(2.0,0.0,0.0), iS2=Base.Vector(0.0,1.0,0.0), iC=Base.Vector(0.0,0.0,0.0)):
	
	ellipse = Part.Ellipse(iS1, iS2, iC).toShape()
	wire = Part.Wire(ellipse.Edges)
	face = Part.Face(wire.Wires)
		
	return face

def makePillar(iFace, iExtrudeDir=Base.Vector(0.0,0.0,5.0)):
  
  extrude = iFace.extrude(iExtrudeDir)
  
  return extrude

def makePillarWithChamfer(iFace, iRadius=0.3, iExtrudeDir=Base.Vector(0.0,0.0,5.0)):
	
	extrude = iFace.extrude(iExtrudeDir)
	pillar = extrude.makeFillet(iRadius, [extrude.Edges[2]])

	return pillar
  
def makePillarWithFillet(iPillar, iRadius=0.3):
	
	bb = iPillar.BoundBox
	
	lc = Base.Vector(2*bb.XMin,2*bb.YMin,bb.ZMin-1)
	uc = Base.Vector(2*bb.XMax,2*bb.YMax,bb.ZMin)
	box = Part.makeBox(uc[0]-lc[0],uc[1]-lc[1],uc[2]-lc[2], lc)
	
	fuse = iPillar.fuse(box)
	fuse = fuse.makeFillet(iRadius, [fuse.Edges[9]])
	fuse = fuse.cut(box)
	
	return fuse

def makeBaseWithMultiplePillars(iFusePillar, iLx=40, iLy=60, iLz=1, iNx=4, iNy=6):
	
	bb = iFusePillar.BoundBox

	lc = Base.Vector(0.0, 0.0, -iLz)
	uc = Base.Vector(iLx, iLy, 0.0)
	ret = Part.makeBox(iLx, iLy, iLz, lc)

	dx = iLx/(iNx+1.0)
	dy = iLy/(iNy+1.0)
	
	for ix in xrange(1,iNx+1):
		for iy in xrange(1,iNy+1):
			p = iFusePillar.copy()
			p.translate(Base.Vector(ix*dx, iy*dy, 0.0))
			ret = ret.fuse(p)
			#Part.show(ret)
			#Gui.SendMsgToActiveView("ViewFit")
	
	return ret

S1 = Base.Vector(2.0,0.0,0.0)
S2 = Base.Vector(0.0,0.5,0.0)
C = Base.Vector(0.0,0.0,0.0)
face = makeEllipseFace(S1, S2, C)
#Part.show(face)
#Gui.SendMsgToActiveView("ViewFit")

r = 0.3
dir = Base.Vector(0.0,0.0,5.0)
pillar = makePillar(face, dir)
#pillar = makePillarWithChamfer(face, r, dir)
#Part.show(pillar)
#Gui.SendMsgToActiveView("ViewFit")

r = 0.3
#fuse = makePillarWithFillet(pillar, r)
#Part.show(fuse)
#Gui.SendMsgToActiveView("ViewFit")

lx=40
ly=60
lz=1
nx=3
ny=12
#tot = makeBaseWithMultiplePillars(fuse, lx, ly, lz, nx, ny)
tot = makeBaseWithMultiplePillars(pillar, lx, ly, lz, nx, ny)
Part.show(tot)
Gui.SendMsgToActiveView("ViewFit")
