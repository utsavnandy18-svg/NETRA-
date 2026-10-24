import os
import sys
import importlib
import pkgutil
import traceback

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def import_submodules(package_name):
    package = importlib.import_module(package_name)
    errors = []
    
    for _, name, is_pkg in pkgutil.walk_packages(package.__path__, package.__name__ + '.'):
        try:
            importlib.import_module(name)
        except Exception as e:
            if not isinstance(e, ImportError) and not isinstance(e, ModuleNotFoundError):
                # Ignore runtime errors from db connections if they are just not configured
                pass
            errors.append(f"Failed to import {name}: {e}\n{traceback.format_exc()}")
            
    return errors

if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()
    errs = import_submodules('app')
    if errs:
        print("FOUND BUGS:")
        for e in errs:
            print(e)
    else:
        print("ALL IMPORTS SUCCESSFUL")
