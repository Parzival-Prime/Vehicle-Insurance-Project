from src.cloud_storage.aws_storage import SimpleStorageService

client = SimpleStorageService()
print(client)
print(client.s3_client)
print(client.s3_resource)
print(client.s3_key_path_available(bucket_name='vehicleprojbucket', s3_key='Directory_structure.png'))