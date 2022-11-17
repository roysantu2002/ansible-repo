

#!/bin/bash

changed="false"
source $1
display="Application Name: $application_name (version: $application_version)"
if [ "$application_name" == "python" ]; then
  changed="true"
  display="$display \nThis is a Python App"
fi
printf '{"changed": %s, "msg": "%s"}' "$changed" "$display"
exit 0