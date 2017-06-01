import Part, FreeCAD, math
from FreeCAD import Base

#execfile("C:/Users/tommy/code/freecad/bottle.py") 
execfile("bottle.py") 
bottle = makeBottle(50,70,30)
Part.show(bottle)
#bottle.exportStep("C:/Users/tommy/code/freecad/bottle.stp")
bottle.exportStep("bottle.stp")
 