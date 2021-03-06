import Part, FreeCAD, math
from FreeCAD import Base

# execfile("C:/Users/tommy/projects/PyFreeCAD/wursterbed/WursterBed.py")
# execfile("/home/tommy/scratch/projects/PyFreeCAD/wursterbed/WursterBed.py");

def makeRevolve(iL = [Base.Vector(0.050,0.0,0.0), Base.Vector(0.125,0.0,0.320)], iRC = Base.Vector(0.0,0.0,0.0), iRA = Base.Vector(0.0,0.0,1.0)):
	L1 = Part.makePolygon(iL); 
	W1 = Part.Wire(L1.Edges);
	return W1.revolve(iRC, iRA);

OutPoly = makeRevolve([Base.Vector(0.050,0.0,0.0), Base.Vector(0.125,0.0,0.320), Base.Vector(0.125,0.0,0.960)], Base.Vector(0.0,0.0,0.0), Base.Vector(0.0,0.0,1.0));
OutPoly.translate(Base.Vector(0.160,0.160,0.0));
Part.show(OutPoly);
#OutPoly.exportStl("OutPoly.stl");
	
OutCone = makeRevolve([Base.Vector(0.050,0.0,0.0), Base.Vector(0.125,0.0,0.320)], Base.Vector(0.0,0.0,0.0), Base.Vector(0.0,0.0,1.0));
OutCone.translate(Base.Vector(0.160,0.160,0.0));
Part.show(OutCone);
#OutCone.exportStl("OutCone.stl");

MidCyl = makeRevolve([Base.Vector(0.0250,0.0,0.0), Base.Vector(0.025,0.0,0.060)], Base.Vector(0.0,0.0,0.0), Base.Vector(0.0,0.0,1.0));
MidCyl.translate(Base.Vector(0.160,0.160,0.0));
MidCyl.translate(Base.Vector(0.0,0.0,0.015));
Part.show(MidCyl);
#MidCyl.exportStl("MidCyl.stl");

InnPoly = makeRevolve([Base.Vector(0.0075,0.0,0.0), Base.Vector(0.0075,0.0,0.0050), Base.Vector(0.0025,0.0,0.010)], Base.Vector(0.0,0.0,0.0), Base.Vector(0.0,0.0,1.0));
InnPoly.translate(Base.Vector(0.160,0.160,0.0));
Part.show(InnPoly);
#InnPoly.exportStl("InnPoly.stl");

TopPlane = Part.makePlane(0.250,0.250,Base.Vector(-0.125,-0.125,0.320),Base.Vector(0.0,0.0,1.0));
TopPlane.translate(Base.Vector(0.160,0.160,0.0));
Part.show(TopPlane);
#TopPlane.exportStl("TopPlane.stl");

BotPlane = Part.makePlane(0.10,0.10,Base.Vector(-0.05,-0.05,0.0),Base.Vector(0.0,0.0,1.0));
BotPlane.translate(Base.Vector(0.160,0.160,0.0));
Part.show(BotPlane);
#BotPlane.exportStl("BotPlane.stl");
