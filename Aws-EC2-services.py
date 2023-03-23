import boto3
val=1
while val != 8:
    print("\nAWS Operations\n")
    print("1.Create Instance\n2.Describe Instance\n3.Terminate All\n4.Stop Specific\n5.Start Specific\n6.Terminate Specific\n7.Stop all")
    
    val = int(input("Enter your Choice: "))

    if val == 1:    #create instance
        ec2_client = boto3.client("ec2", region_name="us-west-2")
        instances = ec2_client.run_instances(
        ImageId="ami-00f7e5c52c0f43726",
        InstanceType="t2.micro",
        MaxCount=1,
        MinCount=1,
        SecurityGroupIds=['sg-049a065b86a129031'],
        KeyName='rootkey',
        SubnetId='subnet-03f7f825be5254345',
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'my-ec2-instance'
                    },
                ]
            },
        ]
        )
        print("\nLaunched Instance ID :")
        print(instances["Instances"][0]["InstanceId"])
    elif val == 2:   #Describe instances
        AWS_REGION = "us-west-2"
        EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
        INSTANCE_STATE = 'running'

        instances = EC2_RESOURCE.instances.filter(
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': [
                    INSTANCE_STATE
                ]
            }
        ]
        )

        for instance in instances:
            print(f'Instance ID: {instance.id}')
            print(f'Instance state: {instance.state["Name"]}')
            print(f'Instance AMI: {instance.image.id}')
            print(f'Instance type: "{instance.instance_type}')
            print(f'Public IPv4 address: {instance.public_ip_address}')
    elif val == 3:      #Terminate all
        AWS_REGION = "us-west-2"
        EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
        INSTANCE_STATE = 'running'

        instances = EC2_RESOURCE.instances.filter(
            Filters=[
                {
                    'Name': 'instance-state-name',
                    'Values': [
                        'running','stopped'
                    ]
                }
            ]
        )

        print('Terminated Instance Id :')
        for instance in instances:
            instance1 = EC2_RESOURCE.Instance(instance.id)
            instance1.terminate()
            print(instance1.id)

    elif val == 4:          #Stop Specific
        AWS_REGION = "us-west-2"
        EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
        INSTANCE_ID = input("\nEnter Instance ID : ")

        instance = EC2_RESOURCE.Instance(INSTANCE_ID)

        instance.stop()

        print(f'Stopping EC2 instance: {instance.id}')
            
        instance.wait_until_stopped()

        print(f'EC2 instance "{instance.id}" has been stopped')
    elif val == 5:      #start Specific
        AWS_REGION = "us-west-2"
        EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
        INSTANCE_ID = input("\nEnter Instance ID : ")

        instance = EC2_RESOURCE.Instance(INSTANCE_ID)

        instance.start()

        print(f'Starting EC2 instance: {instance.id}')
            
        instance.wait_until_running()

        print(f'EC2 instance "{instance.id}" has been started')
    elif val == 6:      #terminate specific
        AWS_REGION = "us-west-2"
        EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
        INSTANCE_ID = input("\nEnter Instance ID : ")

        instance = EC2_RESOURCE.Instance(INSTANCE_ID)

        instance.terminate()

        print(f'Terminating EC2 instance: {instance.id}')
            
        instance.wait_until_terminated()

        print(f'EC2 instance "{instance.id}" has been terminated')
    elif val == 7:    #stop all
        AWS_REGION = "us-west-2"
        EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
        INSTANCE_STATE = 'running'

        instances = EC2_RESOURCE.instances.filter(
            Filters=[
                {
                    'Name': 'instance-state-name',
                    'Values': [
                        'running','stopped'
                    ]
                }
            ]
        )

        print('Stopped Instances :')
        for instance in instances:
            instance1 = EC2_RESOURCE.Instance(instance.id)
            instance.stop()

            print(f'Stopping EC2 instance: {instance.id}')
            
            instance.wait_until_stopped()

            print(f'EC2 instance "{instance.id}" has been stopped')





