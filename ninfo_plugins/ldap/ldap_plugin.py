from ninfo import PluginBase

class ldap_plugin(PluginBase):
    """This plugin looks up a user in ldap and returns their information"""

    name = "ldap"
    title = "LDAP"
    description = "LDAP Lookup"
    cache_timeout = 60*60
    types = ['username']

    def setup(self):
        c = self.plugin_config
        import ldap
        self.ldap = ldap
        ldap_user   = c['user']
        ldap_pw     = c['pw']
        server      = c['server']
        dsn         = c['dsn']
        ignore_cert = 'ignore_cert' in c
        if ignore_cert:
            ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, 0)

        self.l = ldap.initialize(server)
        username = 'uid=%s,%s' % (ldap_user, dsn)
        self.l.simple_bind_s(username, ldap_pw)
        self.dsn = dsn

    def get_info(self, arg):
        search = "uid=%s" % arg
        res = self.l.search_s(self.dsn, self.ldap.SCOPE_SUBTREE, search)
        if not res:
            return None
        res = res[0]
        key, values = res

        ret = {}
        for k,v in values.items():
            ret[k] = ', '.join(v)

        return {'record': ret}

plugin_class = ldap_plugin
