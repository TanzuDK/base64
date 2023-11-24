# Base64

## Table of Contents

- [About](#about)


## About <a name = "about"></a>

Demo project for encoding and decoding Base64 strings.
This project is ment to run on Tanzu Application Platform, and will have the requirements for this.

### Testing locally

You must have Docker installed, and be able to run [Docker Compose](https://docs.docker.com/compose/).
Runing `make build` Builds the containers.
Running `make up` runs the application, and it's avaliable at http://localhost:8080 for the frontend, and http://localhost:8000/docs for the backend swagger interface.

Run `CTRL + c` to exit out of the app.

Runing `make down` cleans up the deployment.


### Installing

Push the application to your TAP cluster, in a Namespace with the permissions to deploy the app.

