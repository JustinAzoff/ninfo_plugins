from ninfo import PluginBase

class passivedns(PluginBase):
    name = "passivedns"
    title = "Passive DNS"
    description = "Passive DNS"
    long_description = "This plugin returns any hostnames seen to resolve to this ip"
    cache_timeout = 60*10
    types = ['ip', 'hostname']

    def setup(self):
        from passive_dns import client
        self.c=client.SearchClient()
        return True

    def get_info(self, arg):
        info = self.c.search_answer(arg) + self.c.search_question(arg)
        return {'records':info}

plugin_class = passivedns
