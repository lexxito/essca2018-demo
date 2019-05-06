import time
import json
import httplib2
import numpy as np

h = httplib2.Http(disable_ssl_certificate_validation=True)
access_key = ''
sec_key = ''
cloudcheckr = ''

for i in range(0):
    post_data = {"access_key": cloudcheckr, "account_name": "test", "aws_access": access_key, "aws_secret": sec_key}
    headers = {"content-type": "application/json"}
    t0 = time.time()
    resp, content = h.request("https://192.168.99.100/serverless-event-gateway/events/aws_create",
                              "POST",
                              json.dumps(post_data),
                              headers=headers)
    acc_id = json.loads(content.decode()[2:-1])['cc_account_id']
    t1 = time.time()
    print("aws_create:" + str(t1-t0))
    t0 = time.time()
    post_data = {"access_key": cloudcheckr,"account_id": acc_id}
    resp, content = h.request("https://192.168.99.100/serverless-event-gateway/events/aws_sync",
                  "POST",
                  json.dumps(post_data),
                  headers=headers)
    t1 = time.time()
    print("aws_sync:" + str(t1-t0))
    t0 = time.time()
    post_data = {"access_key": cloudcheckr, "account_name": "test"}
    resp, content = h.request("https://192.168.99.100/serverless-event-gateway/events/aws_delete",
                              "POST",
                              json.dumps(post_data),
                              headers=headers)
    t1 = time.time()
    print("aws_delete:" + str(t1-t0))




for i in range(0):
    hostname = 'https://api.cloudcheckr.com/api'
    endpoint = '/account.json/add_account_v3'
    body = {'aws_access_key': access_key,
            'aws_secret_key': sec_key,
            'account_name': "test"}
    verb = 'POST'
    url = hostname + endpoint + '?access_key=' + cloudcheckr
    headers = {"content-type": "application/json"}
    t0 = time.time()
    (response, content) = h.request(url,
                                    verb,
                                    body=json.dumps(body),
                                    headers=headers)
    acc_id = json.loads(content.decode())['cc_account_id']

    t1 = time.time()
    print("aws_create_clear:" + str(t1-t0))


    hostname = 'https://api.cloudcheckr.com/api'
    endpoint = '/account.json/get_account'
    verb = 'GET'
    headers = {'Content-Type': 'application/json'}

    url = hostname + endpoint + '?access_key=' + cloudcheckr + '&account_id=' + str(acc_id)
    t0 = time.time()
    (response, content) = h.request(url,
                                         verb,
                                         body=None,
                                         headers=headers)


    t1 = time.time()
    print("aws_sync_clear:" + str(t1-t0))

    hostname = 'https://api.cloudcheckr.com/api'
    endpoint = '/account.json/delete_account'
    verb = 'GET'
    headers = {'Content-Type': 'application/json'}
    url = hostname + endpoint + '?access_key=' + cloudcheckr + '&account_name=' + str("test")
    t0 = time.time()
    (response, content) = h.request(url,
                                    verb,
                                    body=None,
                                    headers=headers)
    t1 = time.time()
    print("aws_delete_clear:" + str(t1-t0))


def get_statistic(name):
    f = open('data.txt', 'r+')
    my_list = []

    for line in f:
        split_line =line.split(':')
        if name == split_line[0]:
            my_list.append(float(split_line[1]))
    for num in my_list:
        print (num)
    return np.array(my_list)

mylist = get_statistic('aws_create')
print (mylist.max(), mylist.min(), mylist.mean() )
mylist = get_statistic('aws_create_clear')
print (mylist.max(), mylist.min(), mylist.mean() )
mylist = get_statistic('aws_sync')
print (mylist.max(), mylist.min(), mylist.mean() )
mylist = get_statistic('aws_sync_clear')
print (mylist.max(), mylist.min(), mylist.mean() )
mylist = get_statistic('aws_delete')
print (mylist.max(), mylist.min(), mylist.mean() )
mylist = get_statistic('aws_delete_clear')
print (mylist.max(), mylist.min(), mylist.mean() )
