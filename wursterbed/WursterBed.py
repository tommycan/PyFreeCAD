import Part, FreeCAD, math
from FreeCAD import Base

# execfile("C:/Users/tommy/code/PyFreeCAD/wursterbed/WursterBed.py")

def makeRevolve(iL = [Base.Vector(0.050e-3,0.0,0.0), Base.Vector(0.125e-3,0.0,0.320e-3)], iRC = Base.Vector(0.0,0.0,0.0), iRA = Base.Vector(0.0,0.0,1.0)):
	L1 = Part.makePolygon(iL) 
	W1 = Part.Wire(L1.Edges);
	return W1.revolve(iRC, iRA);
	
OutCone = makeRevolve([Base.Vector(0.050e-3,0.0,0.0), Base.Vector(0.125e-3,0.0,0.320e-3)], Base.Vector(0.0,0.0,0.0), Base.Vector(0.0,0.0,1.0));
Part.show(OutCone);
#OutCone.exportStl("C:/Users/tommy/code/PyFreeCAD/wursterbed/OutCone.stl");

MidCyl = makeRevolve([Base.Vector(0.0250e-3,0.0,0.0), Base.Vector(0.025e-3,0.0,0.060e-3)], Base.Vector(0.0,0.0,0.0), Base.Vector(0.0,0.0,1.0));
Part.show(MidCyl);
#MidCyl.exportStl("C:/Users/tommy/code/PyFreeCAD/wursterbed/MidCyl.stl");

InnPoly = makeRevolve([Base.Vector(0.0075e-3,0.0,0.0), Base.Vector(0.0075e-3,0.0,0.0050e-3), Base.Vector(0.0025e-3,0.0,0.010e-3)], Base.Vector(0.0,0.0,0.0), Base.Vector(0.0,0.0,1.0));
Part.show(InnPoly);
#InnPoly.exportStl("C:/Users/tommy/code/PyFreeCAD/wursterbed/InnPoly.stl");

