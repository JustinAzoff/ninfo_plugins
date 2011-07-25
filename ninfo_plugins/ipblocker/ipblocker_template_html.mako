%if records:
<ul>
%for x in records:
<li>blocked on ${x.entered.strftime("%Y-%m-%d")} by ${x.who}
%if x.unblocked:
unblocked on ${x.unblocked.strftime("%Y-%m-%d")}
%endif
    <ul>
        <li>${x.comment}</li>
    </ul>
</li>
%endfor
</ul>

<a href="${plugin_config['web_url']}${arg}">Full IPBlocker info</a>
%endif
