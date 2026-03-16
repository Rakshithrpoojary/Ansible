# import boto3

# ec2 = boto3.resource("ec2", region_name="ap-south-1")

# # Filter only running instances
# running_instances = ec2.instances.filter(
#     Filters=[
#         {"Name": "instance-state-name", "Values": ["running"]}
#     ]
# )
# print(running_instances)
# # key='Pub.pem'
# for idx, instance in enumerate(running_instances, start=1):



import boto3

client = boto3.client("ec2", region_name="ap-south-1")

response = client.describe_instances(
    Filters=[
        {"Name": "instance-state-name", "Values": ["running"]}
    ]
)
b=[]
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        instance_id = instance["InstanceId"]
        public_ip = instance.get("PublicIpAddress")
        b.append(public_ip)  # may be None if no public IP
        print(instance_id, public_ip)

for c in b:
    