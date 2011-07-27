%for i in [r['Incident'] for r in records]:
${i['EventData']['Flow']['System']['Node']['Address']} ${i['DetectTime']} ${i['Description']}
%endfor
