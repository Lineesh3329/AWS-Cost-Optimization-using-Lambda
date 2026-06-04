import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):

    # Create EC2 client
    ec2 = boto3.client('ec2')

    # Get all snapshots owned by this AWS account
    snapshots_response = ec2.describe_snapshots(
        OwnerIds=['self']
    )

    snapshots = snapshots_response['Snapshots']

    # Get all running EC2 instances
    instances_response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': ['running']
            }
        ]
    )

    active_instance_ids = set()

    # Store running instance IDs
    for reservation in instances_response['Reservations']:
        for instance in reservation['Instances']:
            active_instance_ids.add(instance['InstanceId'])

    # Process each snapshot
    for snapshot in snapshots:

        snapshot_id = snapshot['SnapshotId']
        volume_id = snapshot.get('VolumeId')

        print(f"Checking Snapshot: {snapshot_id}")

        # Snapshot has no associated volume
        if not volume_id:

            ec2.delete_snapshot(
                SnapshotId=snapshot_id
            )

            print(
                f"Deleted EBS snapshot {snapshot_id} "
                f"because it is not associated with any volume."
            )

            continue

        try:

            # Check whether the volume exists
            volume_response = ec2.describe_volumes(
                VolumeIds=[volume_id]
            )

            volume = volume_response['Volumes'][0]

            attachments = volume.get('Attachments', [])

            # Delete snapshot if volume is not attached
            if not attachments:

                ec2.delete_snapshot(
                    SnapshotId=snapshot_id
                )

                print(
                    f"Deleted EBS snapshot {snapshot_id} "
                    f"because the volume is not attached to any instance."
                )

            else:

                print(
                    f"Volume {volume_id} is still attached. "
                    f"Skipping snapshot {snapshot_id}."
                )

        except ClientError as error:

            error_code = error.response['Error']['Code']

            # Volume no longer exists
            if error_code == 'InvalidVolume.NotFound':

                ec2.delete_snapshot(
                    SnapshotId=snapshot_id
                )

                print(
                    f"Deleted EBS snapshot {snapshot_id} "
                    f"because its associated volume was deleted."
                )

            else:

                print(
                    f"Error processing snapshot {snapshot_id}: "
                    f"{str(error)}"
                )
