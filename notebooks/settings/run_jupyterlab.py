import os
import pathlib
import sys
import webbrowser
from logging import getLogger
from notebook.app import JupyterNotebookApp
import platform

logger = getLogger(__name__ )

if platform.system() == "Windows":
    folder_path_base = str(pathlib.Path(__file__).parents[2].resolve().as_posix()).replace('/', '\\')
    folder_path_settings = folder_path_base + '\\notebooks\\settings'
    folder_path_src = f'{folder_path_base}\\notebooks\\src\\'
    folder_path_venv = folder_path_base + '\\.venv'
    folder_path_jupyter_config_dir = f'{folder_path_settings}\\config'
    folder_path_jupyter_data_dir = f'{folder_path_settings}\\data'
    folder_path_jupyter_runtime_dir = f'{folder_path_settings}\\runtime'

    webbrowser.open(url='http://localhost:8888/lab', new=2)
else:
    folder_path_base = str(pathlib.Path(__file__).parents[2].resolve().as_posix())
    folder_path_settings = folder_path_base + '/notebooks/settings'
    folder_path_src = f'{folder_path_base}/notebooks/src/'
    folder_path_venv = folder_path_base + '/.venv'
    folder_path_jupyter_config_dir = f'{folder_path_settings}/config'
    folder_path_jupyter_data_dir = f'{folder_path_settings}/data'
    folder_path_jupyter_runtime_dir = f'{folder_path_settings}/runtime'


os.environ['JUPYTER_CONFIG_DIR'] = folder_path_jupyter_config_dir
os.environ['JUPYTER_DATA_DIR'] = folder_path_jupyter_data_dir
os.environ['JUPYTER_RUNTIME_DIR'] = folder_path_jupyter_runtime_dir

print(folder_path_base)
print(folder_path_settings)
print(folder_path_venv)
print(folder_path_src)
print(os.environ['JUPYTER_CONFIG_DIR'])
print(os.environ['JUPYTER_DATA_DIR'])
print(os.environ['JUPYTER_RUNTIME_DIR'])
print(folder_path_src)

args = []
args.extend(["--notebook-dir=" + f"{folder_path_src}",
             "--no-browser"])
JupyterNotebookApp.launch_instance(argv=args)
