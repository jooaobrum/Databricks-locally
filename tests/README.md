"""
# Using Pytest in Databricks Locally with VSCode Extension

This guide explains how to set up and use `pytest` for testing in Databricks when working locally using the VSCode extension. It includes instructions for handling package installations and running tests.

## Prerequisites

- **Visual Studio Code** installed
- **Databricks Extension** for Visual Studio Code installed
- **Python** and **PySpark** environments configured
- **Pytest** installed or available for installation within the script

## Setting Up Pytest for Local Testing

When developing locally in VSCode and testing in a Databricks environment, `pytest` can be used to structure and automate your tests. Since we cannot install libraries on the Databricks cluster, we install the required packages (such as `pytest`) within the script itself.

### Step 1: Install Pytest in the Script

To ensure that `pytest` is available for the test, we check if it’s installed and, if not, install it using `pip`. Below is a Pythonic way to handle this:

```python
import importlib
import subprocess
import sys


def install_package(package):
    """Install a package using pip if it's not already installed."""
    try:
        importlib.import_module(package)
        print(f"'{package}' is already installed.")
    except ImportError:
        print(f"'{package}' is not installed. Installing now...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])


# Ensure pytest is installed before running tests
install_package('pytest')
```


### Step 2: Running Files on a Databricks Cluster

To run tests on a Databricks cluster:

1. **Upload Files**:
   - Upload `spark_test.py` and `run_tests.py` to your workspace.

2. **Run Tests**:
   - Right-click on `run_tests.py` and select **"Upload and Run File on Databricks"**.
   - This will scan all files matching `*_test.py`, run the tests, and generate a pytest report.

Example output:
```bash
=============================== test session starts ===============================
collected 10 items
test_spark_logic.py .......                                                 [ 70%]
test_data_validation.py ...                                                  [100%]
=============================== 10 passed in 2.31s ================================
