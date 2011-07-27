from ninfo import PluginBase
try :
    import json
except ImportError:
    import simplejson as json

class cif_plug(PluginBase):
    """This plugin returns any information from a CIF server"""
    name    =    'cif'
    title   =    'CIF'
    description   =  'Collective Intelligence Framework'
    cache_timeout   =  60*10
    types   =    ['ip','hostname']
    local = False

    def setup(self):
        import cif
        server  = self.plugin_config['server']
        api_key = self.plugin_config['api_key']
        self.c=cif.Client(server, api_key)

    def get_info(self, arg):
        info = self.c.GET(arg)

        if 'entry' not in info['feed']:
            records = []
        else:
            records = info['feed']['entry']

        return {'records': records}


plugin_class = cif_plug
