import imp
import logging
import mock
from setuptools import setup as _setup

from vdt.versionplugin.wheel.utils import WheelRunningDistribution

logger =logging.getLogger(__name__)


def build_package(version):
    """
    In here should go code that runs you package building scripts.
    """
    def fixed_version_setup(*args, **kwargs):
        old_version = kwargs.pop('version')
        logging.info("Version in file is %s, using %s" % (old_version, version))
        _setup(version=str(version), distclass=WheelRunningDistribution, *args, **kwargs)

    with mock.patch('setuptools.setup'):
        imp.load_source('packagesetup', 'setup.py')


# def set_package_version(version):
#     """
#     If there need to be modifications to source files before a
#     package can be built (changelog, version written somewhere etc.)
#     that code should go here
#     """
