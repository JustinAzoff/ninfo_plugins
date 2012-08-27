from ninfo import PluginBase
class ipb(PluginBase):
    """This plugin returns the ipblocker history for this ip"""

    name    =   'ipblocker'
    title   =   'IP Blocker'
    description = 'IP Blocker records'
    cache_timeout =  60*1
    types   = ['ip','ip6']

    def setup(self):
        import ipblocker
        self.ipblocker = ipblocker

    def get_info(self, ip):
        records = self.ipblocker.model.search_ip(ip)
        return {'records': records}

plugin_class = ipb
