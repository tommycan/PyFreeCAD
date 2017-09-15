import Part, FreeCAD, math
from FreeCAD import Base

# execfile("C:/Users/tommy/code/PyFreeCAD/wursterbed/WursterBed.py")

def makeRevolve(iL = [Base.Vector(0.050,0.0,0.0), Base.Vector(0.125,0.0,0.320)], iRC = Base.Vector(0.0,0.0,0.0), iRA = Base.Vector(0.0,0.0,1.0)):
	L1 = Part.makePolygon(iL); 
	W1 = Part.Wire(L1.Edges);
	return W1.revolve(iRC, iRA);
	
OutCone = makeRevolve([Base.Vector(0.050,0.0,0.0), Base.Vector(0.125,0.0,0.320)], Base.Vector(0.0,0.0,0.0), Base.Vector(0.0,0.0,1.0));
OutCone.translate(Base.Vector(0.160,0.160,0.0));
Part.show(OutCone);
OutCone.exportStl("OutCone.stl");

MidCyl = makeRevolve([Base.Vector(0.0250,0.0,0.0), Base.Vector(0.025,0.0,0.060)], Base.Vector(0.0,0.0,0.0), Base.Vector(0.0,0.0,1.0));
MidCyl.translate(Base.Vector(0.160,0.160,0.0));
MidCyl.translate(Base.Vector(0.0,0.0,0.015));
Part.show(MidCyl);
MidCyl.exportStl("MidCyl.stl");

InnPoly = makeRevolve([Base.Vector(0.0075,0.0,0.0), Base.Vector(0.0075,0.0,0.0050), Base.Vector(0.0025,0.0,0.010)], Base.Vector(0.0,0.0,0.0), Base.Vector(0.0,0.0,1.0));
InnPoly.translate(Base.Vector(0.160,0.160,0.0));
Part.show(InnPoly);
InnPoly.exportStl("InnPoly.stl");

