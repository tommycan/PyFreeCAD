f="/c/Program Files/ParaView 5.4.0-Qt5-OpenGL2-Windows-64bit/bin/pvpython.exe"
if [ -f "$f" ]; then
	"$f" StlVtk.py
else
	echo "$f not found"
fi


