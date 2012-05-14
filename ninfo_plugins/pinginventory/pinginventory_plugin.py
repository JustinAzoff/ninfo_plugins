from ninfo import PluginBase

class pinginventory(PluginBase):
    """This plugin returns the ping inventory history for this ip"""

    name    =   'pinginventory'
    title   =   'Ping Inventory'
    description   =  'Ping Inventory log'
    cachetimeout   =  60*5
    types   =    ['ip','ip6']
    remote = False

    def setup(self):
        import pinginventory
        self.p = pinginventory.PingInventory(self.plugin_config['config_file'])

    def get_info(self, ip):
        hist = list(self.p.get_ip_history_short(ip))
        #check for it never being pingable, show nothing
        if len(hist) == 1 and hist[0][1] is False:
            return None
        return {'hist': hist}

    def to_json(self, result):
        h = []
        for date, res in result['hist']:
            h.append((str(date), res))
        result['hist'] = h
        return result

plugin_class = pinginventory
