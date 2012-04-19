from ninfo import PluginBase
import datetime

class snortinfo(PluginBase):
    """This plugin returns any information found in the snort(IDS) database in the last 14 days"""

    name    =      'snort'
    title   =      'Snort IDS'
    description =  'IDS information'
    cache_timeout =  60*5
    types=    ['ip']

    options = { "startdate": {"description": "How far back to search for alerts", "type":"datetime"}}

    def setup(self):
        from snort import snortdb
        self.sdb = snortdb.sdb()
        self.sdb.setlimit(100000)

    def get_info(self, ip, options):
        if 'startdate' in options:
            time_ago = options['startdate']
        else:
            time_ago = datetime.date.today() - datetime.timedelta(days=14)
            time_ago = time_ago.strftime("%Y-%m-%d")
        self.sdb.setwhere(startdate=time_ago)
        data = [dict(r) for r in self.sdb.get_events_for_ip(ip)]
        return { 'idsdata': data }

    def to_json(self, result):
        d = []
        for x in result['idsdata']:
            x = x.copy()
            x['last'] = str(x['last'])
            x['first'] = str(x['first'])
            d.append(x)
        result['idsdata'] = d
        return result

plugin_class = snortinfo
