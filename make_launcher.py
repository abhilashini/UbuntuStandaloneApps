import argparse
import json
import os
import stat
from subprocess import check_output

from console_formats import ConsoleFormat as CF


parser = argparse.ArgumentParser(description="Create a .desktop file to launch Python GUI as standalone Ubuntu application")
parser.add_argument("-c", "--cfg", type=str, required=True, help="JSON file path (with file name) containing parameters to create a .desktop file")
parser.add_argument("-p", "--pyfile", type=str, required=True, help="Python file path (with file name) to convert to standalone Ubuntu application")
parser.add_argument("--launcher-file-name", type=str, required=True, help="Name of .desktop file to create", default="launcher_configs.json")
args = parser.parse_args()


# Get Python3.6 Path
# which_output = check_output(["which", "python3.6"])
# print(type(str(which_output.strip())))
# print(f"which_output = {which_output.strip().decode('utf-8')}")

pyfile = args.pyfile

# chmod +x to the required pyfile
st = os.stat(pyfile)
os.chmod(pyfile, st.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
# ls_pyfile_output = check_output(["ls", "-la", pyfile])
# print(ls_pyfile_output.strip().decode('utf-8'))

try: 
	with open(pyfile) as f:
		shebang = f.readline().strip()
		if not shebang.startswith("#!"):
			raise RuntimeError
except Exception as e:
	print(f"\n\t{CF.BOLD}{CF.FAIL}ERROR{CF.CLEAR_F}")
	print(f"\t{CF.FAIL}Please ensure shebang at the beginning of your {CF.OKCYAN}{CF.BOLD}--pyfile \"{pyfile}\" {CF.CLEAR_F}{CF.FAIL}before proceeding{CF.CLEAR_F}")
else:
	with open(args.cfg) as f:
		launcher_configs = json.load(f)

	launcher_file_name = args.launcher_file_name + ".desktop"

	with open(launcher_file_name, "w") as f:
		f.write("\n")
		f.write("[Desktop Entry]\n")
		f.write(f"Name = {launcher_configs['name']}\n")
		f.write(f"Version = {launcher_configs['version']}\n")
		f.write(f"Exec = {os.path.abspath(pyfile)}\n")
		if launcher_configs.get('icon'):
			f.write(f"Icon = {launcher_configs['icon']}\n")
		f.write(f"Type = Application\n")

	print(f"{launcher_file_name} created successfully at \n {os.getcwd()}")
	print("Copy this file to desired location and check 'Allow executing file as program' in Permissions tab of Properties before running application")