%if records:
<table border="1" cellpadding="1" cellspacing="0">
<tr><th>Address</th><th>CIDR</th><th>confidence</th><th>description</th><th>detecttime</th></tr>
%for r in records:
<tr><td>${r['address']}</td> <td>${r['cidr']}</td> <td>${r['confidence']}</td> <td>${r['description']}</td> <td>${r['detecttime']}</td></tr>
%endfor
</table>
%endif
