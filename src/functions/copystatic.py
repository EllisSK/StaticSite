import pathlib
import shutil

def copy_static():
    path_to_main = pathlib.Path.cwd()
    path_to_static = path_to_main / "static"
    path_to_public = path_to_main / "public"

    shutil.rmtree(path_to_public)
    shutil.copytree(path_to_static, path_to_public)