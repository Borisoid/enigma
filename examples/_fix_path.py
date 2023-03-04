"""
Add project root to sys.path so that the modules can be imported from there.
"""

import site
import sys
from importlib import reload
from pathlib import Path


sys.path.append(str(Path(f"{__file__}/../../").resolve()))
reload(site)
