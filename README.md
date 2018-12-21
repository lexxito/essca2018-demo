# Serverless event gateway, kubernetes and cloudchekr
This a demostration to show how serverless event gateway works together with kubernetes. How to centralize function calls via distributed platforms and achive benefits and extended functionality for cloud management platforms(CMP) in this case with CloudcheckR 

## Requirements
* The [**just**](https://github.com/casey/just) binary
* The *kubectl* binary
* The *minikube* binary
* The *kubeless* binary
* The *serverless* binary

## Usage
Type `just --list` to get an overview of the available recipes.

## Cluster Setup
The *clst-prepare* recipe will get you started quickly.

> **Note:** If you're uncertain about your minikube state it's advised to start with a clean state by running `minikube delete` (`just clst-cleanup`) first.

## Event gateway and etcd start 

The *gateway-start* and *etcd-start* will start containers easily. To check containers avalability run *check-config-status* or *kubectl get pods*

## Register functions and subcriptions

The *echo-register-any* and * echo-register-aws* will register functions on both aws and gc. To create a subscription run *sub-register* with function registered id

**Note:** If while registering subsciption the error "no httpd type" has appeared, 
run:

    curl -k --request POST --url https://{minikube_ip}/serverless-event-gateway/config/v1/spaces/default/eventtypes --header 'content-type: application/json' --data '{ "name": "http.request" }'

## Test commands

When all the subcriptions are created, run commands from command file to test centralized functions call. All commands are assuming that $AWS_ACCESS, $AWS_SECRET, $CLOUD_CHECK variables are exported in enviroment

