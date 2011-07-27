%if records:
<table border="1" cellpadding="1" cellspacing="0">
<tr><th>Address</th><th>description</th><th>detecttime</th></tr>
%for i in [r['Incident'] for r in records]:
<tr>
    <td> ${i['EventData']['Flow']['System']['Node']['Address']} </td>
    <td> ${i['DetectTime']} </td>
    <td>
%if 'AlternativeID' in i:
        <a href="${i['AlternativeID']['IncidentID']['content']}">
            ${i['Description']}
        </a>
%else:
        ${i['Description']}
%endif
    </td>
</tr>
%endfor
</table>
%endif
