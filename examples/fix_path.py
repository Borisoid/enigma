"""
Add project root to sys.path so that the modules can be imported from there.
"""

import sys
from pathlib import Path
import site
from importlib import reload


sys.path.append(Path(f'{__file__}/../../').resolve())
reload(site)
