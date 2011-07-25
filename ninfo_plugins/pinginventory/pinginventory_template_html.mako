%if hist:
<table border="1" cellpadding="1" cellspacing="0">
<tr><th>Time</th><th>State</th></tr>
%for endtime, state in hist:
<tr><td>${endtime.strftime("%Y-%m-%d %H:%M")}</td> <td>${state}</td></tr>
%endfor
</table>
%endif
