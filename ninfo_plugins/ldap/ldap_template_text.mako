<%
    fields = ("preferredDisplayName", "eduPersonPrimaryAffiliation", "eduPersonAffiliation", "title", "albanyEduPersonPrimaryDivision", "albanyEduPersonPrimarySubdivision", "eduPersonPrimaryOrgUnitDN", "mail", "campusAddress", "telephoneNumber", "uid")
    if fields in plugin_config:
        fields = plugin_config['fields'].split()
%>

%for f in [x for x in fields if x in record]:
${f}  ${record[f]}
%endfor
