#!/usr/bin/env python3
"""
Process PDZ files

Many current implementations of using information gathered from XRF devices are
complicated and meant for *any* usage, such as PyXRF, and may be difficult to
run on certain platforms, such as Windows.
This project aims to provide a simple usage: read the PDZ files produced from a
given handheld XRF device, and produce certain statistics and information.
"""

from subprocess import check_output

__author__ = "Dylan Armitage"
__credits__ = ["Dylan Armitage (author)", "Nathan Simpson (inspiration)"]
__license__ = "Apache-2.0"
__copyright__ = "Copyright © 2019 Dylan Armitage"
__maintainer__ = "Dylan Armitage"
__email__ = "dylanjarmitage@gmail.com"
__version__ = check_output(["git", "describe", "--all", "--long"]).decode("utf-8")

__all__ = ["input"]
