from setuptools import setup, find_packages

setup(name='ninfo-plugins',
    version='0.1.1',
    zip_safe=False,
    packages = find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=[
        "ninfo>=0.1.5",
    ],
    entry_points = {
        'ninfo.plugin': [
            'nfi_stats      = ninfo_plugins.nfi_stats.nfi_stats_plugin',
            'siteadvisor    = ninfo_plugins.siteadvisor_check.siteadvisor_plugin',
            'passivedns     = ninfo_plugins.passivedns.passivedns_plugin',
            'ipblocker      = ninfo_plugins.ipblocker.ipblocker_plugin',
            'tm             = ninfo_plugins.tm.tm_plugin',
            'snort          = ninfo_plugins.snort.snort_plugin',
            'cif            = ninfo_plugins.cif.cif_plugin',
            'pinginventory  = ninfo_plugins.pinginventory.pinginventory_plugin',
            'netdisco       = ninfo_plugins.netdisco.netdisco_plugin',
            'ldap           = ninfo_plugins.ldap.ldap_plugin',
            'google_safebrowsing = ninfo_plugins.google_safebrowsing.google_safebrowsing_plugin',
        ]
    }
) 
