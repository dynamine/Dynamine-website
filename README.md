# Dynamine-website
Dynamine Public Facing Website using Django

## Deployment

To deploy the website to the Dynamine GCP project, use the deploy_to_gcp.sh script located at project root.

NOTE: Before you can use this script you must do the following:

1. Install and configure the Google Cloud SDK on your machine. More info about this [here.](https://cloud.google.com/sdk/)
2. Make sure you have docker installed on your machine
3. Please make sure you have bash installed (check that /usr/bin/bash exists)

To deploy, simply run `sh deploy_to_gcp.sh`. The script will prompt you to add a tag version. This is simply used to 
differentiate between different versions of the website that have been deployed. A list of existing image versions should be displayed
so just choose one version after the lates in GCP (e.g. `v7`). 

That's it. You can verify the correct version is running in kubernetes by typing `kubectl get pods -o wide`.
