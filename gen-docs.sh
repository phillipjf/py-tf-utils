#!/bin/bash

MOD_PATH=$1
if [[ $# -ne 1 ]]; then
    MOD_PATH=${PWD}
fi

if [ "$MOD_PATH" == "--help" ]; then
    echo "Generates documentation of Terraform files and outputs to a TF_DOCS.md file."
    echo "Usage: $0 path-to-terraform"
    exit 1
fi

if ! /bin/ls $MOD_PATH/*.tf 1> /dev/null 2>&1; then
    echo "No Terraform files found in $MOD_PATH!"
    exit 1
fi

OUT_PATH=$MOD_PATH/TF_DOCS.md
# Need to escape the pipe character since we are creating markdown tables
VALUES=$(terraform-config-inspect --json ${MOD_PATH} | sed -e 's/|/\\\\|/g')
TITLE="# $(basename $MOD_PATH)"
INPUTS_HEADER="\n## Inputs\n\n| Name | Description | Type | Default | Required |\n|------|-------------|:----:|:-----:|:-----:|"
OUTPUTS_HEADER="\n## Output\n\n| Name | Description |\n|------|-------------|"

INPUTS=$(echo ${VALUES} | jq -r '.variables | .[] | .type = (if has("type") then .type else "string" end) | .required = (has("default") | not) | "| \(.name) | \(.description) | \(.type) | \(.default) | \(.required ) |+EOTF"')
OUTPUTS=$(echo ${VALUES} | jq -r '.outputs | .[] | "| \(.name) | \(.description) |+EOTF"')

# jq seems to add a space to each line, so we trim and split it here
# hoping that '+EOTF' is a unique enough string to split on.
INPUTS=$(echo ${INPUTS} | sed -e 's/+EOTF /\\n/g')
OUTPUTS=$(echo ${OUTPUTS} | sed -e 's/+EOTF /\\n/g')

echo -e $TITLE > $OUT_PATH
echo -e $INPUTS_HEADER >> $OUT_PATH
echo -e $INPUTS >> $OUT_PATH
echo -e $OUTPUTS_HEADER >> $OUT_PATH
echo -e $OUTPUTS >> $OUT_PATH
