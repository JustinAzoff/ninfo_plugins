from ninfo import PluginBase
import ieeemac


class netdiscoinfo(PluginBase):
    """This plugin looks up the given IP in netdisco
    The data returned consists of:
        The mac addresses for this IP(macs)
        The IP of the switch that this IP is on(switch)
        The port that this IP is on(port)
        The status of this port
        The name of the switch that this IP is on(switchname)
        The type of device
        The location of this switch
        The netbios name of this computer
        The logged in user on this computer
        The domain of this computer
        If the port this computer on has ever been disabled
        The duplex status of the port
        The configured duplex of the port
        The speed of the port
        The description of the port"""

    name    =           'netdisco'
    title   =           'Netdisco'
    description    =    'Information from Netdisco'
    cache_timeout  =    60*5
    types    =       ['ip','ip6','mac']
    remote = False

    def setup(self):
        from netdisco import db
        self.db = db

    def get_info(self, arg):
        ret = {}
        if ieeemac.ismac(arg):
            mac = arg
            ret['ips'] = ips = self.db.util.get_ips_for_mac(mac)
            ip = ips and ips[0]
            ret["macs"] = [mac]
            porto = self.db.Port.get_by_mac(mac)
        else :
            ip = arg
            ret["macs"] = self.db.util.get_macs_for_ip(ip)
            porto = self.db.Port.get_by_ip(ip)
        
        if porto:
            ret['found'] = True
            ret["switch"], ret["port"] = porto.ip, porto.port
        else:
            ret['found'] = False
        if not porto:
            for i in 'location','device_location','switchname','portstatus','speed','duplex','duplex_admin', 'device_type', 'description':
                ret[i] = 'NA'
            ret['hasbeendisabled'] = False
        else :
            d = porto.device
            if d.location and 'Enter' not in d.location:
                ret["device_location"] = d.location
            else :
                ret["device_location"] = d.name
            ret["switchname"] = d.name
            
            if d.vendor == 'cisco':
                ret["device_type"] = "switch"
            else :
                ret["device_type"] = "hub"

            ret["portstatus"] = porto.status

            for i in 'duplex', 'duplex_admin', 'speed':
                ret[i] = getattr(porto, i)

            ret["description"] = porto.name
            ret['hasbeendisabled'] = bool(list(porto.log))

        ret['netbios'] = data = False
        if ip:
            data = self.db.Node_NBT.query.filter(self.db.Node_NBT.ip==ip).first()
        if data:
            ret['netbios'] = True
            ret['nbname'] = data.nbname
            ret['domain'] = data.domain
            ret['nbuser'] = data.nbuser
        else :
            ret['nbname'] = ret['domain'] = ret['nbuser'] = None

        return ret


plugin_class = netdiscoinfo

