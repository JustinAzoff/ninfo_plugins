from ninfo import PluginBase
class ipb(PluginBase):
    name    =   'ipblocker'
    title   =   'IP Blocker'
    description = 'IP Blocker records'
    long_description = 'This plugin returns the ipblocker history for this ip'
    cache_timeout =  60*1
    types   = ['ip']

    def setup(self):
        import ipblocker
        self.ipblocker = ipblocker

    def get_info(self, ip):
        records = self.ipblocker.model.get_ip(ip)
        return {'records': records}

plugin_class = ipb
