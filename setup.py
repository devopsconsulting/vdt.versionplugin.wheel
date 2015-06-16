# coding: utf-8
from setuptools import find_packages, setup

pkgname = "vdt.versionplugin.wheel"

setup(name=pkgname,
      version="0.0.2",
      description="vdt.version plugin for building python wheels.",
      author="Lars van de Kerkhof",
      author_email="lars@devopsconsulting.nl",
      maintainer="Lars van de Kerkhof",
      maintainer_email="lars@devopsconsulting.nl",
      packages=find_packages(),
      include_package_data=True,
      namespace_packages=['vdt', 'vdt.versionplugin'],
      zip_safe=True,
      install_requires=[
          "setuptools",
          "vdt.version",
          "vdt.versionplugin.debianize",
          "mock"
      ],
      entry_points={},
)
