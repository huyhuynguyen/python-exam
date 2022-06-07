import os
import sys

# root project path
PROJECT_ROOT = os.path.join(os.path.dirname(__file__), os.pardir)

# modules package path
PROJECT_MODULES = os.path.join(PROJECT_ROOT, '\modules')

PROJECT_HELPER = os.path.join(PROJECT_ROOT, '\helpers')

# append to sys
sys.path.append(PROJECT_ROOT)
sys.path.append(PROJECT_MODULES)
sys.path.append(PROJECT_HELPER)