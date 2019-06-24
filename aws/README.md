# AWS

## 1. DynamoDB and Lambda Function

### 1.1 Create Table from the AWS Management Console

- Search for DynamoDB in the console.
- Open dynamodb console.
- Click create table button.
- Give a **Table name** and a **Primary key**.

Important notes:

Save the **Amazon Resource Name (ARN)** located in the Overview tab of the console (e.g. arn:aws:dynamodb:us-west-1:687111944639:table/five_steps_shopify).

### 1.2 Generate a user role to give access to the database

- Search for IAM in the console.
- Click on the Roles Tab.
- Click create Role button.
- Choose Lambda to allow lambda functions to call AWS services on your behalf.
- Add a Policy: AWSLambdaBasicExecutionRole
- Give the Role a name (e.g. LambdaDynamoDBRole)
- Save the Role.
- In order to add 1 more policy to our Role. Open the Role and click: + Add inline policy.
- Expand the Service section and select DynamoDB.
- Select the Actions the Role is allowed. (Best practices say that you should give the least possible permissions to do actions against DynamoDB.):
	- Add actions manually:
		- GetItem
		- PutItem
- Select, in Resources, the specific box and add ARN.
- Click on Review Policy.
- Give a name to the Policy (e.g. DynamoReadWriteAccess).
- Click on Create Policy.

Everything is ready. From now on, in order to use a **lambda function** to read and write into a dynamo database, you should give this Role.


## 2. DynamoDB, Boto3 and Python

The first step is to get the permissions to access DynamoDB using Python. So a new **User** has to be created using the IAM console in AWS. This user must have attached a Policy that allows Read and Write in Dynamo. An option could be: `AmazonDynamoDBFullAccess`.

Before setting up the dynamo object in python, make sure:

1. Install the configparser dependency in python: `pip install configparser`
2. Have the credentials file ready. It could be in the following file: `cat ~/.aws/credentials`. Get all the details in the [credentials template](https://github.com/josemariasosa/jomtools/blob/master/bash/setup/credentials_template).

```
[dynamo]
env = staging
test = True
notification = True
region = us-west-1
s3_key_id = A*******************Q
s3_secret = G*******************************************D
s3_bucket = elasticbeanstalk-us-west-1-687111944639
dynamo_key_id = A********************Q
dynamo_secret = F*****************************************Q
```

3. Make sure you also set up the config.py file. Get all the details in the [config template](https://github.com/josemariasosa/jomtools/blob/master/python/config/config.py).

Perfect! We are ready to set up Get and Post from DynamoDB. Setting up the dynamodb instance:

```
import boto3
from config import dynamo

table_name = 'test_table'

dynamodb = boto3.resource('dynamodb',
                          region_name='us-west-1',
                          aws_access_key_id=dynamo['AWS_KEY_ID'],
                          aws_secret_access_key=dynamo['AWS_SECRET_KEY'])
dynamo_table = dynamodb.Table(table_name)
```

Generate (POST) items in the database.

```
dynamo_table.put_item(
    Item = {
        'Name': 'try2catch',
        'Age': 28,
        'Location': 'india'
    }
)
```

Query (GET) items from the database.

```
dynamo_table.get_item(
	Key = {
		'Name': 'try2catch'
	}
)
```
