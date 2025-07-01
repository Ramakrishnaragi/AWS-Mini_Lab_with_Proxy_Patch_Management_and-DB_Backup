import boto3
import os
import datetime
#Define bucket name here
bucket_name = 'ansible-proj' #here replace bucket name
timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')
backup_file = f"/tmp/backup_{timestamp}.sql"
#Perform MySQL dump
os.system(f"mysqldump -u root sampledb > {backup_file}")
#Upload to S3
s3 = boto3.client('s3')
s3.upload_file(backup_file, bucket_name, f"backup_{timestamp}.sql")
print("Backup completed and uploaded to S3")
