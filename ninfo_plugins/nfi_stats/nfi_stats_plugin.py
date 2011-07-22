import httplib2
import simplejson
            
class nfi_stats:
    name = "nfi_stats"
    title = "Netflow Stats"
    description = "Netflow Statistics"
    long_description = "This plugin checks to see if the ip was seen at all in the netflow index"
    cache_timeout = 60*30
    types = ['ip']

    def setup(self):
        self.base_url = self.plugin_config['base_url']
        self.url = self.base_url + "stats?ip="

    def get_info(self, ip):
        h = httplib2.Http()
        url = self.url + ip
        resp, content = h.request(url)
        stats = simplejson.loads(content)
        return stats

plugin_class = nfi_stats
