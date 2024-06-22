# ytm-api

A part of the CAU Capstone Project 2024-01, Class 04, Team 05

This is essentially a drop-in replacement for our Capstone Frontend application, which depends on RapidAPI's Shazam Core API. It implements a subset of functions from the aforementioned API that are required by our frontend.

Written in Python, it is provided with a Dockerfile and Kubernetes configurations for deployment in your environment (in the /kube directory, only tested on the K3s cluster).

## Requirements

If your server is in the ROK or any other country/region that requires logging in to access YouTube Music, add the oauth.json file.

You need to create your own Docker (OCI) image, upload it to your own Docker (OCI) Image Registry, and edit `ytm-api.yaml`, as mine is currently private.

If you want to run it in a Kubernetes environment, you need to configure cert-manager and Traefik before creating any deployments. Afterward, point the domain name you want to use to the server, and add a Secret object named `x-rapidapi-key`:

`kubectl create secret generic x-rapidapi-key --from-literal=x-rapidapi-key=asdfbsdfcsdfdsdfbc0f44c85c79p123773asdfbsdfcsdf65c`

Additionally, you may need to change the domain name configured in `ytm-api.yaml` and add your email address in `le-cert-issuer.yaml`.

## License
MIT, if there anyone wants to use it
