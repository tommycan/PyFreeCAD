import Part, FreeCAD, math
from FreeCAD import Base

# Run in terminal: 
# FreeCADCmd MultiSphereViz.py
#
# Run in py-console in FreeCAD
# execfile("C:/Users/tommy/projects/PyFreeCAD/multisphere/MultiSphereViz.py");

def makeMuliSphere(iR,iP):
	if(len(iR) != len(iP)):
		print "Bad input. Lists must have same lengths, len(iR)=%d and len(iP)=%d. Abort!" %(len(iR), len(iP))
	for i, val in enumerate(iR):
		p = Part.makeSphere(iR[i])
		p.translate(iP[i]);
		Part.show(p)
		if (i>0):
			# try 
			f = f.fuse(p);
			# catch
		else:
			f = p;
			
	return f;

r = [1.5, 2.0, 3.0]
p = [Base.Vector(0.0, 0.0, 0.0), Base.Vector(1.5, 0.0, 0.0), Base.Vector(0.0, 2.5, 0.0)]

ms = makeMuliSphere(r, p);
Part.show(ms)
ms.exportStl("ms.stl");
#ms.exportStl("C:/Users/tommy/projects/PyFreeCAD/multisphere/ms.stl");
