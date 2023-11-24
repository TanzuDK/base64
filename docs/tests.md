# Tests

You must have Docker installed, and be able to run [Docker Compose](https://docs.docker.com/compose/), to run the application locally.


Runing 

```
make build
``` 

Builds the containers.


Running 

```
make up
``` 

runs the application, and it's avaliable at http://localhost:8080 for the frontend, and http://localhost:8000/docs for the backend swagger interface.

Run `CTRL + c` to exit out of the app.

Runing 

```
make down
```

cleans up the deployment.

# Loadtest

Loadtest is done using [Locust](https://docs.locust.io/en/stable/index.html) 

Run 
```
make loadtest-cli
```

To do an automated test headless

Run 
```
make loadtest-ui
```

To do an test using the UI.
Note you need to open your browser to [http://localhost:8089/](http://localhost:8089/) and start it.
