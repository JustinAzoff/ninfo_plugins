%if pcaps:
<table border="1" cellpadding="1" cellspacing="0">
<tr><th>PCAP</th><th>Time</th><th>Size</th><th>Download</th> <th>Urlsnarf</th></tr>
%for r in pcaps:
<tr>
    <td>${r['pcap']}</td>
    <td>${r['mtime']}</td>
    <td>${r['size']}</td>
    <td><a href="https://portal.datacomm.albany.edu/tm/get/${r['pcap']}">Download</a></td>
    <td><a href="https://portal.datacomm.albany.edu/tm/urlsnarf/${r['pcap']}">Urlsnarf</a></td>
</tr>
%endfor
</table>
%endif
