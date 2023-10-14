# Development log

My first step is to create a small roadmap of the project. This simulates a real-life scenario in which the development tasks are derived from a feature requirements analysis. I will describe features that are outside of the scope of this test - and even outside the scope of the backend - but I think doing this analysis is important to decide the API that the backend should offer.

[Roadmap](./roadmap.md)

## Tasks

Based on this roadmap, I will create some tasks for the backend.

### T1: Create a docker-compose environment that contains Django and Postgres

I have a code-generator (called Moonleap, this is not an AI, but an advanced skaffolding tool) that will take care of this.

### T2: Create a "plans" Django module

### T3: Create a "destinations" Django module

This module will have the Destination django model. I'm assuming that Google Maps place ids are used to unambiguously represent places. The backend will store both the place id and the lat/long (that it receives from the frontend).

When a client (e.g. the frontend) GETs the plan, then they will receive all destinations, but no weather predictions, because this would make the API unnecessarily slow. Also, it's not necessary to couple the GET /plans/:plan_id endpoint to a particular weather prediction service. Clients can use the /weather endpoint is offered by the backend, but they are not forced to use it.

### T4: Create a "weather" Django module

Since the frontend is always showing the latest weather forecasts, they are not stored in the database.

## Things I didn't implement / TODO's

### Showing TextField in the Django admin

I used to believe that strings in django had to be limited to a certain number of chars for better performance, but recently I read arguments against doing this (e.g. see https://www.postgresql.org/docs/9.0/datatype-character.html). Therefore, I will use TextField instead of CharField for string fields.

Since I'm using TextField instead of CharField, the text fields in the admin are too big. This should be fixed, ideally in a way that doesn't bloat the code.

### Get rid of hard-coded weather forecasting URL

I would like to make it easy for a dev-ops person to see what the incoming and outcoming traffic is. Therefore, it would help to add the weather forecast URL as an environment variable that must be injected into the system (since you are forced to provide this environment variable, dev-ops will notice it).

### Make fetching the weather forecast async

Currently, the internal request to fetch the weather forecast blocks to wait for the result. If we use an async GET function then performance should be better. The adrf package could be used for this.

### Documentation

I usually only document when it's necessary (if the code speaks for itself, that's better). But I would document ModelIO, and explain how it's used.

### Split api/urls.py

I placed all urls in api/urls.py. If this file gets too big, I would split it up.

### Exclude "personal" files such as docker-compose.dev.override.yml from the repo

I included the docker-compose.dev.override.yml file to show how I map directories to the host computer. Normally, this file would not be included in the repo. Similarly, I left in the vandelay-py.js file (that contains a hard-coded path).
I also committed some files that are supposed to stay outside of git (i.e. ` dev.injected.env`), for convenience
(this files are created when `make compile-env` is run).

### Use GET for the weather endpoint

The weather endpoint currently uses POST so that it's easy to pass JSON data to the endpoint. But afaik a GET endpoint can also receive data. I should rewrite the /weather endpoint so that it uses GET.

### Fix warning

When running the tests, there is a warning about USE_L10N that should be fixed.

### Use newer postgres version

I noticed that by mistake I'm using an old postgres version (14).

## Other notes

In the docker-compose file, I'm using `sleep infinity` to always keep the backend container running. Then I will go into the container to do any development work there that is necessary (e.g. run the tests, or start the development server, etc).

The backend service can be initialized by running `make init-dev` in the backend container.

I used simple APIViews instead of ModelViewSet because I think the latter option is too opaque (it requires you to override methods in a base-class, which tends to get messy). To reduce boilerplate, I created the validate_or_400 helper function. The IO classes such as PlanIO still have some boilerplate but they are easy to understand, and they give you a lot of control over validation (it's easy to add custom validation steps) and serialization (it's easy to customize the JSON output).

Since I used a skaffolding tool (Moonleap) to create the docker-compose environment, there are some extra tools installed (e.g. pip-compile, compile-env, vandelay, and isort). The skaffolding tool also installs the user-module. For this test, I could have left it out, but on the other hand, I think it's always a good idea to add a users module from the start (since adding it later can cause problems).

## Example run

The [example run](./example-run.md) file shows some curl calls that target the endpoints.

## Time spent

Sorry, I didn't track the time, but I spent much more than 3 hours. At the same time, I tried to keep the code minimal (and not add unnecessary stuff, except for the few tools that my skaffolding tool installed automatically).

In general, I have no problem with aiming for a minimal solution (in fact, I love simple solutions that can take you far), but I'm terrible at rushing to get something done in a suboptimal way (I feel a strong resistance against doing so, and I find it hard to make myself do it). When I want to save time, I will look for a cheap solution that still gives an acceptable result, but then I will try to implement that cheap solution in a satisfactory way, even if that means I have to spend a few hours more.
