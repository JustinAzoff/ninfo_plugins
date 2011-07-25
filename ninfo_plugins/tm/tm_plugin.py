from ninfo import PluginBase
import timemachine

class tm(PluginBase):
    name        =  'tm'
    title       =  'Time Machine'
    description =  'Time Machine captures'
    long_description = 'This plugin returns any time machine files for a particular ip'
    cache_timeout   =  60*2
    types   =    ['ip']

    def setup(self):
        self.c=timemachine.Client(self.plugin_config['server'])

    def get_info(self, ip):
        data = self.c.list_pcaps_for_ip(ip)
        return dict(pcaps=data)

plugin_class = tm
