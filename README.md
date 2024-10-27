# Databricks Locally with VS Code

This repository contains information about running Databricks locally using the VS Code extension and how to install Python libraries for individual Python files.

## Prerequisites

- Visual Studio Code installed
- Databricks extension for Visual Studio Code installed
- Authentication to your Databricks workspace (via token or Azure Active Directory)
- A valid Python environment set up locally or on your Databricks cluster

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

