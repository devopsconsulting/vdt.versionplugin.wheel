from glob import glob
import imp
import logging
import os
import shutil
import subprocess

import mock

from setuptools import setup as _setup

from vdt.versionplugin.wheel.shared import parse_version_extra_args
from vdt.versionplugin.wheel.utils import WheelRunningDistribution

logger = logging.getLogger(__name__)


def build_package(version):
    """
    In here should go code that runs you package building scripts.
    """
    def fixed_version_setup(*args, **kwargs):
        old_version = kwargs.pop('version')
        base_version = ".".join(map(str, version.version))
        python_version = base_version
        if version.build_number is not None:
            python_version = "%src%s" % (base_version, version.build_number)
        logging.info(
            "Version in file is %s, using %s" % (
                old_version, python_version))
        _setup(
            version=python_version,
            distclass=WheelRunningDistribution, *args, **kwargs)

    args, _ = parse_version_extra_args(version.extra_args)

    # importing setup.py is like running it.
    with version.checkout_tag:
        if os.path.isdir('build'):
            shutil.rmtree('build')
        with mock.patch('setuptools.setup', fixed_version_setup):
            imp.load_source('packagesetup', 'setup.py')

    if args.build_dependencies:
        build_dir = os.path.join(os.getcwd(), 'dist')
        wheel = glob(os.path.join(build_dir, '*.whl'))
        wheel.sort(key=os.path.getmtime, reverse=True)
        cmd = ['pip', 'wheel'] + wheel[:1]
        logger.debug("Running command {0}".format(" ".join(cmd)))
        logger.debug(subprocess.check_output(cmd, cwd=build_dir))

    return 0
