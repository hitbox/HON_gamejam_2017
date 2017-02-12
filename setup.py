import cx_Freeze
import os

os.environ['TCL_LIBRARY'] = 'C:\\Users\\cdsup\\AppData\\Local\\Programs\\Python\\Python35-32\\tcl\\tcl8.6'
os.environ['TK_LIBRARY'] = 'C:\\Users\\cdsup\\AppData\\Local\\Programs\\Python\\Python35-32\\tcl\\tk8.6'

executables = [cx_Freeze.Executable('main.py')]

cx_Freeze.setup(
    name='Nature\'s Vengeance',
    options={'build_exe' : {'packages' : ['pygame', 'sys'], 'include_files' : ['assets/']}},
    executables = executables


)
