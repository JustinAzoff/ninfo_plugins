from distutils.core import setup
from setuptools import find_packages
from glob import glob

setup(name='ninfo-plugins',
    version='0.1.0',
    zip_safe=False,
    packages = find_packages(exclude=["tests"]),
    package_data = { '': ['*.mako'] },
    install_requires=[
        "ninfo>=0.1.0",
    ],
    entry_points = {
        'ninfo.plugin': [
            'nfi_stats = ninfo_plugins.nfi_stats_plugin',
        ]
    }
) 
