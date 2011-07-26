<%
    fields = ("preferredDisplayName", "eduPersonPrimaryAffiliation", "eduPersonAffiliation", "title", "albanyEduPersonPrimaryDivision", "albanyEduPersonPrimarySubdivision", "eduPersonPrimaryOrgUnitDN", "mail", "campusAddress", "telephoneNumber", "uid")
    if fields in plugin_config:
        fields = plugin_config['fields'].split()
%>

<table border="1" cellpadding="1" cellspacing="0">
%for f in [x for x in fields if x in record]:
<tr>
    <td> ${f} </td>
    <td> ${record[f]} </td>
</tr>
%endfor
</table>
