import requests
import simplejson
from ninfo import PluginBase
            
class nfi_stats(PluginBase):
    """This plugin checks to see if the ip was seen at all in the netflow index"""

    name = "nfi_stats"
    title = "Netflow Stats"
    description = "Netflow Statistics"
    cache_timeout = 60*30
    types = ['ip']

    def setup(self):
        if not self.plugin_config:
            return False
        self.base_url = self.plugin_config['base_url']
        self.url = self.base_url + "stats?ip="

    def get_info(self, ip):
        url = self.url + ip
        resp = requests.get(url, verify=False)
        stats = simplejson.loads(resp.raw.read())
        return stats

plugin_class = nfi_stats
