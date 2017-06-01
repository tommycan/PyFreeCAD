f="/c/Program Files/FreeCAD 0.16/bin/FreeCADCmd.exe"
if [ -f "$f" ]; then
	"$f" box_pierced.py
else
	echo "$f not found"
fi

#execfile("C:/Users/tommy/code/PyFreeCAD/box_pierced/box_pierced.py")