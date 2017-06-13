f="/c/Program Files/FreeCAD 0.16/bin/FreeCADCmd.exe"
if [ -f "$f" ]; then
	"$f" create_heatsink.py
else
	echo "$f not found"
fi
