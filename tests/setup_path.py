import os
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), os.pardir)
PROJECT_MODULES = os.path.join(PROJECT_ROOT, '\modules')
sys.path.append(PROJECT_ROOT)
sys.path.append(PROJECT_MODULES)