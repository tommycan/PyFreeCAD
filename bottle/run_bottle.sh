f="/c/Program Files/FreeCAD 0.16/bin/FreeCADCmd.exe"
if [ -f "$f" ]; then
	"$f" export_bottle.py
else
	echo "$f not found"
fi
