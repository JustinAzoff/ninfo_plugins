import urllib
import httplib2
from ninfo import PluginBase

class SafeBrowsing(PluginBase):
    """This plugin looks up the address using the google safe browsing API"""

    name =         'google_safebrowsing'
    title =        'Google Safe Browsing'
    description =  'Google Safe Browsing check'
    cache_timeout =   60*60
    types =     ['ip','ip6','hostname']
    local =     False

    def setup(self):
        api_key = self.plugin_config['api_key']
        self.base_url = "https://sb-ssl.google.com/safebrowsing/api/lookup?client=ninfo&apikey=%s&appver=1.5.2&pver=3.0" % api_key

    def get_info(self, arg):
        h = httplib2.Http()
        url = self.base_url + "&url=" + urllib.quote(arg)
        resp, content = h.request(url)

        if resp.status == 204:
            return {}

        status = content

        return { 'status': status}

    def render_template(self, output_type, arg, result):
        if not result:
            return ''
        if output_type == 'text':
            return result['status']
        else:
            return '<pre>%s</pre>' % result['status']

plugin_class = SafeBrowsing
