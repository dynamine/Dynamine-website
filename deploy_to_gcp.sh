#!/bin/bash

# keeping the dynamine project id in a variable for later use
PROJECT_ID="$(gcloud config get-value project -q)"

# prompting user for a tag version
echo "The following pysite images are available in the gcloud docker repo:"
echo "$(gcloud docker --verbosity=error -- image  ls | grep py-site)"

read -p 'image tag version: ' tag_version 

# building image and pushing to GCP repo
docker build -t us.gcr.io/$PROJECT_ID/py-site\:${tag_version} .
gcloud docker --verbosity=error -- push us.gcr.io/${PROJECT_ID}/py-site\:${tag_version}

# delete existing deployment or supress 'no such resource' message
kubectl delete deployment py-test &>/dev/null
kubectl run py-test --image=us.gcr.io/${PROJECT_ID}/py-site\:${tag_version} --port 8000

# expose deployment or surpress 'service already exists" messsage
kubectl expose deployment py-test --type=LoadBalancer --port 80 --target-port 8000 &>/dev/null


