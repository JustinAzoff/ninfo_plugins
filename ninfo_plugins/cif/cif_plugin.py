from ninfo import PluginBase
try :
    import json
except ImportError:
    import simplejson as json

class cif_plug(PluginBase):
    name    =    'cif'
    title   =    'CIF'
    description   =  'Collective Intelligence Framework'
    long_description   = 'This plugin returns any information from a CIF server'
    cache_timeout   =  60*10
    types   =    ['ip','hostname']
    local = False

    def setup(self):
        import cif
        server  = self.plugin_config['server']
        api_key = self.plugin_config['api_key']
        self.c=cif.Client(server, api_key)

    def get_info(self, arg):
        self.c.GET(arg)
        info = json.loads(self.c.responseContent)
        if info['status'] != 200:
            return { 'records': [],
                     'status': "error",
                     'code': info['status'],
                     'message' :info['message']
                   }

        if 'result' not in info['data']:
            records = []
        else:
            records = info['data']['result']['feed']['items']
        return {'records': records}


plugin_class = cif_plug
