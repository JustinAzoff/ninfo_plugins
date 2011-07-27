%if records:
<table border="1" cellpadding="1" cellspacing="0">
<tr><th>Address</th><th>Detect Time</th> <th>Description</th> <th>Impact</th> <th>Severity</th></tr>
%for i in records:
<tr>
    <td> ${i['address']}
    <td> ${i['detecttime']} </td>
    <td>
%if 'alternativeid' in i:
        <a href="${i['alternativeid']}">
            ${i['description']}
        </a>
%else:
        ${i['description']}
%endif
    </td>
    <td> ${i['impact']} </td>
    <td> ${i['severity']} </td>
</tr>
%endfor
</table>
%endif
