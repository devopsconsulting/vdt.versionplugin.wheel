"""
This file contains only functions that deal with the version
of the repository. It can set a new version as a tag and look
up the current version.
"""
import subprocess
import logging

from vdt.version.shared import VersionNotFound, Version
from vdt.versionplugin.default import get_version as get_git_version

log = logging.getLogger('vdt.versionplugin.wheel.version')


__all__ = ('get_version')


def get_python_version(version_args):
    result = subprocess.check_output(['python', 'setup.py', '--version'])
    return Version(result.decode("utf-8"), extra_args=version_args)


def get_version(version_args):
    """
    Retrieve the version from the repo, if no version tag
    can be found, read it from the setup script

    It can be assumed that this script will be ran in the
    root of the repository.
    """
    python_version = get_python_version(version_args)
    try:
        gitversion = get_git_version(version_args)
        return gitversion if gitversion >= python_version else python_version
    except VersionNotFound:
        log.debug('no version tag found, taking version from setup.py')
        return python_version
