from ninfo import PluginBase
import datetime

class snortinfo(PluginBase):
    name    =      'snort'
    title   =      'Snort IDS'
    description =  'IDS information'
    long_description = 'This plugin returns any information found in the snort(IDS) database in the last 14 days'
    cache_timeout =  60*5
    types=    ['ip']

    def setup(self):
        from snort import snortdb
        self.sdb = snortdb.sdb()
        self.sdb.setlimit(100000)
        return True

    def get_info(self, ip):
        time_ago = datetime.date.today() - datetime.timedelta(days=14)
        time_ago = time_ago.strftime("%Y-%m-%d")
        self.sdb.setwhere(startdate=time_ago)
        data = [dict(r) for r in self.sdb.get_events_for_ip(ip)]
        return { 'idsdata': data }

plugin_class = snortinfo
