# Databricks Locally with VS Code

This repository contains information about running Databricks locally using the VS Code extension and how to install Python libraries for individual Python files or treat them as Databricks notebooks.

## Prerequisites

- Visual Studio Code installed
- Databricks extension for Visual Studio Code installed
- Authentication to your Databricks workspace (via token or Azure Active Directory)

## Steps to Run Python Code on a Databricks Cluster

Follow the steps below to set up and run your Python scripts on a Databricks cluster using Visual Studio Code.

### 1. Install the Databricks Extension for Visual Studio Code

Make sure that the Databricks extension is installed in your VS Code. You can install it from the Extensions Marketplace.

1. Open Visual Studio Code.
2. Go to the **Extensions** view by clicking on the Extensions icon in the Activity Bar.
3. Search for **Databricks**.
4. Install the extension named **Databricks**.

### 2. Authenticate with Your Databricks Workspace

You need to authenticate to your Databricks workspace to run Python files on the cluster. There are two methods for authentication:

1. **Using a Personal Access Token**:
   - Generate a personal access token from the Databricks workspace.
   - In VS Code, go to the Databricks extension settings and input your workspace URL and token.

2. **Using Azure Active Directory (for Azure Databricks)**:
   - Follow the AAD authentication process from within the VS Code Databricks extension.

### 3. Install Python Libraries in Your Script

If you need to install a Python library for a specific Python file (and not across the whole cluster), use the `install_lib_locally.py` script as a reference.

#### Example: Installing a Library Locally in a Python Script

Use the following code snippet at the top of your Python script to install the necessary library:

```python
import subprocess
import sys

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install the 'imbalanced-learn' library
install_package('imbalanced-learn')
```

This code ensures that the `imbalanced-learn` library is installed before the main code runs. You can replace `'imbalanced-learn'` with any other package you need.

### 4. Upload and Run the Python File on Databricks

Once you have your Python script ready:

1. Right-click on the Python file in the VS Code Explorer view.
2. Select **Upload and Run File on Databricks**.
3. The file will be uploaded and executed on your Databricks cluster.

You can view the results in the Databricks workspace or in the output section of VS Code.

### 5. Alternatively, You Can Consider a Python File as a Notebook

If you are working with Python files but want to treat them as Databricks notebooks, you can follow this method to run them locally as workflows within VS Code. This is particularly useful if you want to include magic commands like `%pip install` within the script.

1. **Create a Python file** that starts with the following comment to denote it's a Databricks notebook:

    ```python
    # Databricks notebook source
    ```

2. **Add any necessary Databricks-specific commands**, such as `%pip install` for package installations. For example:

    ```python
    # Databricks notebook source

    # MAGIC %pip install imbalanced-learn

    import imblearn


    ```

3. **Run the Notebook as a Workflow in VS Code**:
   - Right-click on the Python file.
   - Select **Run File as Workflow on Databricks** to run it on the cluster.
   - The file will be uploaded and executed on your Databricks cluster as a workflow.


   This allows you to treat your Python file as a Databricks notebook, complete with notebook-style commands.

---

## Example of a Python Script with Library Installation and Notebook Source

```python
# Databricks notebook source
# MAGIC %pip install imbalanced-learn

import imblearn

print('hello world')
```

### Notes

- Ensure that your cluster can access external libraries like `imbalanced-learn`.
- Use the **Run on Databricks** feature in VS Code to treat the file as a notebook and execute it on the Databricks cluster.
