from ninfo import PluginBase

class tm(PluginBase):
    """This plugin returns any time machine files for a particular ip"""

    name        =  'tm'
    title       =  'Time Machine'
    description =  'Time Machine captures'
    cache_timeout   =  60*2
    types   =    ['ip']

    def setup(self):
        import timemachine
        self.c=timemachine.Client(self.plugin_config['server'])

    def get_info(self, ip):
        data = self.c.list_pcaps_for_ip(ip)
        return dict(pcaps=data)

plugin_class = tm
