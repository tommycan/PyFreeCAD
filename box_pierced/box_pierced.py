import Part, FreeCAD, math
from FreeCAD import Base

s=10
r=2
myBox = Part.makeBox(s,s,s)
myCyl = Part.makeCylinder(r,2*s)
myCyl.translate(FreeCAD.Vector(0.5*s, 0.5*s, -0.5*s))

#Part.show(myBox)
#Part.show(myCyl)

myCut = myBox.cut(myCyl)
Part.show(myCut)
#Gui.SendMsgToActiveView("ViewFit")
myCut.exportStep("box_pierced.stp")
