from distutils.core import setup
from setuptools import find_packages
from glob import glob

setup(name='ninfo-plugins',
    version='0.1.0',
    zip_safe=False,
    packages = find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=[
        "ninfo>=0.1.0",
    ],
    entry_points = {
        'ninfo.plugin': [
            'nfi_stats      = ninfo_plugins.nfi_stats.nfi_stats_plugin',
            'siteadvisor    = ninfo_plugins.siteadvisor_check.siteadvisor_plugin',
            'passivedns     = ninfo_plugins.passivedns.passivedns_plugin',
            'ipblocker      = ninfo_plugins.ipblocker.ipblocker_plugin',
            'tm             = ninfo_plugins.tm.tm_plugin',
        ]
    }
) 
