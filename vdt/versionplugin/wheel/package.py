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
        base_version = ".".join(map(str, version.version))
        python_version = "%src%s" % (base_version, version.build_number)
        logging.info("Version in file is %s, using %s" % (old_version, python_version))
        _setup(version=python_version, distclass=WheelRunningDistribution, *args, **kwargs)

    with mock.patch('setuptools.setup', fixed_version_setup):
        imp.load_source('packagesetup', 'setup.py')
