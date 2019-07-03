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

### 1.3 AWS Lambda

- Search for AWS Lambda in the console.
- Click on the create a function button.
- Select the option: Author from scratch, give a name to the function and select the programming language. Also, for the permissions select the role we already created (i.e. LambdaDynamoDBRole).
- Click, again, on the create function button.

The *Designer* tab.

Lambda functions can run after any certain event that trigger the function, some examples of such events could be: uploading a file to an s3 bucket.




## 2. DynamoDB, Boto3 and Python

Please check all the [documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html).

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

### 2.1 Setting up an instance of DynamoDB

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

### 2.2 PutItem Function

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

### 2.3 GetItem Function

Retrieve (GET) items from the database.

```
dynamo_table.get_item(
    Key = {
        'Name': 'try2catch'
    }
)
```

During the GET request, in case you obtain this error:

```
{
    "errorMessage": "An error occurred (ValidationException) when calling the GetItem operation: The provided key element does not match the schema",
    "errorType": "ClientError"
}
```

In [stackoverflow](https://stackoverflow.com/questions/42757872/the-provided-key-element-does-not-match-the-schema-error-when-getting-an-item), I found this:

```
Your table schema has both hash key and sort key defined. When using DynamoDB GetItem you must provide both of them, here is an excerpt from documentation

For the primary key, you must provide all of the attributes. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide values for both the partition key and the sort key.
```

### 2.4 Querying and Scanning ()

With the table full of items, you can then query or scan the items in the table using the `DynamoDB.Table.query()` or `DynamoDB.Table.scan()` methods respectively. To add conditions to scanning and querying the table, you will need to import the `boto3.dynamodb.conditions.Key` and `boto3.dynamodb.conditions.Attr` classes. The `boto3.dynamodb.conditions.Key` should be used when the condition is related to the key of the item. The `boto3.dynamodb.conditions.Attr` should be used when the condition is related to an attribute of the item:

```
from boto3.dynamodb.conditions import Key, Attr
```

This queries for all of the users whose username key equals johndoe:

```
response = table.query(
    KeyConditionExpression=Key('username').eq('johndoe')
)
items = response['Items']
print(items)
```

Expected Output:

```
[{u'username': u'johndoe',
  u'first_name': u'John',
  u'last_name': u'Doe',
  u'account_type': u'standard_user',
  u'age': Decimal('25'),
  u'address': {u'city': u'Los Angeles',
               u'state': u'CA',
               u'zipcode': Decimal('90001'),
               u'road': u'1 Jefferson Street'}}]
```

Similarly you can scan the table based on attributes of the items. For example, this scans for all the users whose age is less than 27:

```
response = table.scan(
    FilterExpression=Attr('age').lt(27)
)
items = response['Items']
print(items)
```

Expected Output:

```
[{u'username': u'johndoe',
  u'first_name': u'John',
  u'last_name': u'Doe',
  u'account_type': u'standard_user',
  u'age': Decimal('25'),
  u'address': {u'city': u'Los Angeles',
               u'state': u'CA',
               u'zipcode': Decimal('90001'),
               u'road': u'1 Jefferson Street'}},
 {u'username': u'bobsmith',
  u'first_name': u'Bob',
  u'last_name': u'Smith',
  u'account_type': u'standard_user',
  u'age': Decimal('18'),
  u'address': {u'city': u'Louisville',
               u'state': u'KY',
               u'zipcode': Decimal('40213'),
               u'road': u'3 Madison Lane'}}]
```

You are also able to chain conditions together using the logical operators: **&** (and), **|** (or), and **~** (not). For example, this scans for all users whose first_name starts with J and whose account_type is super_user:

```
response = table.scan(
    FilterExpression=Attr('first_name').begins_with('J') & Attr('account_type').eq('super_user')
)
items = response['Items']
print(items)
```

Expected Output:

```
[{u'username': u'janedoering',
  u'first_name': u'Jane',
  u'last_name': u'Doering',
  u'account_type': u'super_user',
  u'age': Decimal('40'),
  u'address': {u'city': u'Seattle',
               u'state': u'WA',
               u'zipcode': Decimal('98109'),
               u'road': u'2 Washington Avenue'}}]
```

You can even scan based on conditions of a nested attribute. For example this scans for all users whose state in their address is CA:

```
response = table.scan(
    FilterExpression=Attr('address.state').eq('CA')
)
items = response['Items']
print(items)
```

Expected Output:

```
[{u'username': u'johndoe',
  u'first_name': u'John',
  u'last_name': u'Doe',
  u'account_type': u'standard_user',
  u'age': Decimal('25'),
  u'address': {u'city': u'Los Angeles',
               u'state': u'CA',
               u'zipcode': Decimal('90001'),
               u'road': u'1 Jefferson Street'}},
 {u'username': u'alicedoe',
  u'first_name': u'Alice',
  u'last_name': u'Doe',
  u'account_type': u'super_user',
  u'age': Decimal('27'),
  u'address': {u'city': u'Los Angeles',
               u'state': u'CA',
               u'zipcode': Decimal('90001'),
               u'road': u'1 Jefferson Street'}}]
```

Review a real [example here](), using a Lambda Function to query DynamoDB for a Shopify API.

