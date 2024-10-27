import importlib
import subprocess
import sys
import os
from pyspark.sql import SparkSession

def install_package(package):
    """Install a package using pip if it's not already installed."""
    try:
        importlib.import_module(package)
        print(f"'{package}' is already installed.")
    except ImportError:
        print(f"'{package}' is not installed. Installing now...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install_package('pytest')
import pytest


def setup_environment():
    """
    Sets up the environment for running the tests:
    - Installs required packages.
    - Configures the working directory.
    - Disables bytecode caching.
    """
   
    # Get the path to the directory for this file in the workspace.
    dir_root = os.path.dirname(os.path.realpath(__file__))
    
    # Switch to the root directory.
    os.chdir(dir_root)

    # Skip writing .pyc files to the bytecode cache on the cluster.
    sys.dont_write_bytecode = True
    print(f"Environment setup complete. Current working directory: {dir_root}")


def run_pytest():
    """
    Runs pytest in the current environment.
    By default, pytest searches through all files with filenames ending
    with "_test.py" for tests, and runs functions beginning with "test_".
    """
    try:
        # Run pytest from the root directory, using the provided arguments.
        retcode = pytest.main(sys.argv[1:])
        if retcode == 0:
            print("All tests passed successfully.")
        else:
            print(f"Tests failed with return code: {retcode}")
        return retcode
    except Exception as e:
        print(f"Error occurred while running pytest: {e}")
        sys.exit(1)


if __name__ == "__main__":
    """
    Main execution entry point. This script does the following:
    - Sets up the environment.
    - Runs pytest.
    """
    setup_environment()
    run_pytest()
