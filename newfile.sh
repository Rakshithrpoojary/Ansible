#!/bin/bash

# Fetch instance IDs that match Environment=dev and Role=web
instance_ids=$(aws ec2 describe-instances \
  --filters "Name=instance-state-name,Values=running" \
  --query 'Reservations[*].Instances[*].InstanceId' \
  --output text)

# Sort instance IDs deterministically
sorted_ids=($(echo "$instance_ids" | tr '\t' '\n' | sort))
echo ${sorted_ids[*]}
# Rename instances sequentially

for id in "${sorted_ids[@]}"; do
 

  aws ec2 create-tags --resources "$id" \
    --tags Key=Environment,Value="dev"

done

