import requests
from ninfo import PluginBase
            
class siteadvisor_check(PluginBase):
    """This plugin checks to see if a site is listed in McAfee SiteAdvisor"""

    name = "siteadvisor"
    title = "SiteAdvisor"
    description = "SiteAdvisor Check"
    cache_timeout = 60*60*2
    types = ['ip','ip6','hostname']
    local = False

    base_url = "http://www.siteadvisor.com/sites/"

    phrases = (
        ('<div id="siteVerdict"  class="siteGreen">',   'Green'),
        ('<div id="siteVerdict"  class="siteYellow">',  'Yellow'),
        ('<div id="siteVerdict"  class="siteRed">',     'Red'),
    )

    def determine_color(self, content):
        for phrase, color in self.phrases:
            if phrase in content:
                return color
        
        return "Unknown"

    def get_info(self, hostname):
        url = self.base_url + hostname
        resp = requests.get(url)
        content = resp.text
        color = self.determine_color(content)

        return {"result": color}

plugin_class = siteadvisor_check
