#!/usr/bin/env python
# coding=utf-8

# ------------------------------------------------------------------------------
# Lambda Function 1
# ------------------------------------------------------------------------------
# jose maria sosa

import re
import json
import boto3
from botocore.vendored import requests

from boto3.dynamodb.conditions import Key, Attr

def getKeys(x):
    return {
        'url': x['url'],
        'image': x['image']['source'],
        'title': x['title'],
        'brand': x['brand'],
        'price': x['price'],
        'stock': x['stock']
    }

def alphaNumeric(s):
    s = (s.lower()
          .replace('á', 'a')
          .replace('é', 'e')
          .replace('í', 'i')
          .replace('ó', 'o')
          .replace('ú', 'u'))
    return re.sub(r'\W', '', s)

def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb', region_name='us-west-1')
    table_1 = dynamodb.Table('table_1')
    table_2 = dynamodb.Table('table_2')
    
    # Set Credentials.
    user = 'a*******************************8'
    password = '3*******************************3'

    body = json.loads(event['body'])
    if "body" in body.keys():
        body = json.loads(body['body'])
    
    action = body['action']
    p_value = body['partition_key']
    
    if action == 'action_1':
        response = table_1.query(
            KeyConditionExpression=Key('partition_key').eq(p_value)
        )
        items = response['Items']
        elem1_list = list(set([x['elem1'] for x in items]))
        elem1_list.sort()
        
        results = elem1_list
        
    elif action == 'action_2':
        elem1 = body['elem1']
        s_value = alphaNumeric(elem1)
        
        response = table_1.query(
            KeyConditionExpression=(Key('partition_key').eq(p_value)
                & Key('sort_key').begins_with(s_value))
        )
        items = response['Items']
        elem2_list = list(set([x['elem2'] for x in items]))
        elem2_list.sort()
        
        results = elem2_list
        
    elif action == 'action_3':
        elem1 = body['elem1']
        elem2 = body['elem2']
        s_value = alphaNumeric(elem1) + '|' + alphaNumeric(elem2)
        
        response = table_1.query(
            KeyConditionExpression=(Key('partition_key').eq(p_value)
                & Key('sort_key').begins_with(s_value))
        )
        items = response['Items']
        elem3_list = list(set([x['elem3'] for x in items]))
        elem3_list.sort()
        
        results = elem3_list
        
    elif action == 'action_4':
        elem1 = body['elem1']
        elem2 = body['elem2']
        elem3 = body['elem3']
        s_value = (alphaNumeric(elem1)
                   + '|'
                   + alphaNumeric(elem2)
                   + '|'
                   + alphaNumeric(elem3))
        
        # Query Vehicle Database
        response = table_1.query(
            KeyConditionExpression=(Key('partition_key').eq(p_value)
                & Key('sort_key').begins_with(s_value))
        )
        items = response['Items']
        
        if len(items) > 0:
            item_id = response['Items'][0]['item_id']
        
            # Query Products Database
            response = table_2.query(
                KeyConditionExpression=Key('item_id').eq(item_id)
            )
            items = response['Items']
            type_list = list(set([x['p_type'] for x in items]))
            type_list.sort()
        
        else:
            type_list = []

        results = type_list
        
    elif action == 'action_5':
        elem1 = body['elem1']
        elem2 = body['elem2']
        elem3 = body['elem3']
        part_type = body['product_type']
        s_value = (alphaNumeric(elem1)
                   + '|'
                   + alphaNumeric(elem2)
                   + '|'
                   + alphaNumeric(elem3))
        
        # Query Vehicle Database
        response = table_1.query(
            KeyConditionExpression=(Key('partition_key').eq(p_value)
                & Key('sort_key').begins_with(s_value))
        )
        items = response['Items']
        
        if len(items) > 0:
            item_id = response['Items'][0]['item_id']
        
            # Query Products Database
            response = table_2.query(
                KeyConditionExpression=Key('item_id').eq(item_id),
                FilterExpression=Attr('p_type').eq(part_type)
            )
            items = response['Items']
            shopify_id = list(set([x['shopify_id'] for x in items]))
            
            if len(shopify_id) > 0:
                # Shopify Request
                shopify_id = ','.join(shopify_id)
                url = 'https://jose-maria.myshopify.com/admin/api/2019-04/products.json?ids={}'
                url = url.format(shopify_id)
                
                products = shopify_id

        results = items

    return {
        'statusCode': 200,
        'headers': {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        'body': json.dumps(results)
    }
