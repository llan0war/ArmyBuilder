from distutils.core import setup
import py2exe
 
setup(windows=['main.py'], options={"py2exe": {"includes": ["sip", "PyQt4.QtGui", "elixir"], "dll_excludes": ["MSVCP90.dll", "HID.DLL", "w9xpopen.exe"], "packages": ["sqlalchemy"]}})