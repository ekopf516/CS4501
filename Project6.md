# Project 6 Documentation 

## Hosting on Digital Ocean

## Continuous Integration 
Travis CI Status Image: ![alt text](https://travis-ci.org/ekopf516/CS4501.svg?branch=master) <br>
We used Travis CI to automate builds of our project. The script we wrote runs the unit tests in the models layer as well as the end to end selenium tests we wrote.
To implement this, we started out by writing some before_install scripts that started the proper containers and created a 
database with the proper user login. We then called "docker-compose up" to run the app and then ran the script before calling "docker-compose down" and removing the temporary database.

## Integration Tests

## Load Balancing
Note: All code done for load balancing is done in the haproxy folder. <br>

