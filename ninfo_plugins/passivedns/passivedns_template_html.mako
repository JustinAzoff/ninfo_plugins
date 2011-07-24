%if records:
<table border="1" cellpadding="1" cellspacing="0">
<tr><th>Key</th><th>Value</th><th>Type</th><th>TTL</th><th>First</th><th>Last</th></tr>
%for r in records:
<tr><td>${r['key']}</td> <td>${r['value']}</td> <td>${r['type']}</td> <td>${r['ttl']}</td> <td>${r['first']}</td> <td>${r['last']}</td></tr>
%endfor
</table>
%endif
