%if macs:
MAC addresses:     ${', '.join(macs)}
Company:           ${company}
%endif
%if found:
Switch:            ${switch}
Port:              ${port}
 
Device Location:   ${device_location}
Device Name:       ${switchname}
Device Type:       ${device_type}
Port Status:       ${portstatus}
Port Speed:        ${speed}
Current Duplex:    ${duplex}
Configured duplex: ${duplex_admin}
Port Description : ${description}
%endif
%if netbios:
Netbios Information:
Name of computer:  ${nbname}
Computer domain:   ${domain}
Logged in User:    ${nbuser}
%endif
%if found:
    %if hasbeendisabled:
This Port has been disabled in the past(using netdisco)
    %else :
This Port has never been disabled(using netdisco)
%endif
%endif
