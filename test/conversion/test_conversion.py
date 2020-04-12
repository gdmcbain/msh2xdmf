import os
import sys
sys.path.append('.')
from msh2xdmf import msh2xdmf


def test_conversion():
    """
    Test the conversion from msh to xdmf.
    """
    # Get the current directory
    current_dir = "{}/{}".format(os.getcwd(), "test/conversion")
    # Run the conversion
    msh2xdmf("multidomain.msh", dim=2, directory=current_dir)
    # Check if the files have been create
    assert os.path.isfile("{}/{}".format(current_dir, "domain.xdmf"))
    assert os.path.isfile("{}/{}".format(current_dir, "domain.h5"))
    assert os.path.isfile("{}/{}".format(current_dir, "boundaries.xdmf"))
    assert os.path.isfile("{}/{}".format(current_dir, "boundaries.h5"))
    # Remove the files
    os.remove("{}/{}".format(current_dir, "domain.xdmf"))
    os.remove("{}/{}".format(current_dir, "domain.h5"))
    os.remove("{}/{}".format(current_dir, "boundaries.xdmf"))
    os.remove("{}/{}".format(current_dir, "boundaries.h5"))
