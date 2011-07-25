%for x in records:
blocked on ${x.entered.strftime("%Y-%m-%d")} by ${x.who}
%if x.unblocked:
unblocked on ${x.unblocked.strftime("%Y-%m-%d")}
%endif
 ${x.comment}
%endfor
