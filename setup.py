from distutils.core import setup
from glob import glob

setup(name='ninfo-plugins',
    version='0.1.0',
    zip_safe=False,
    packages = ['ninfo_plugins'],
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
