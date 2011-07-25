%for x in idsdata:
<h3> Rule Triggered: ${x['sig']} (${x['count']} times) </h3>
<dl>
<dt>First time</dt><dd>${x['first']}</dd>
<dt>Last time </dt><dd>${x['last']}</dd>
</dl>
%endfor

<a href="https://portal.datacomm.albany.edu/ids/events?minutes=10080&ip=${arg}">Full IDS info</a>
