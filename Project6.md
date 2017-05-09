# Project 6 Documentation 

## Hosting on Digital Ocean
http://162.243.0.109:8000/home/

## Continuous Integration 
Travis CI Status Image: ![alt text](https://travis-ci.org/ekopf516/CS4501.svg?branch=master) <br>
We used Travis CI to automate builds of our project. The script we wrote runs the unit tests in the models layer as well as the end to end selenium tests we wrote.
To implement this, we started out by writing some before_install scripts that started the proper containers and created a 
database with the proper user login. We then called "docker-compose up" to run the app and then ran the script before calling "docker-compose down" and removing the temporary database.

## Integration Tests
We used Selenium HQ to do some end to end testing. This helped us ensure that all our webpages were correctly connected and that the right information was being processed. We used a stand-alone chrome driver (selenium-chrome). All code for these tests can be found in selenium_test.py

## Load Balancing
Note: All code done for load balancing is done in the haproxy folder. <br>
We used haproxy to set up a load balancer between two web containers (web and web2). We created a new container "haproxy" and added that to our docker-compose file, so that it was brought up at run time. The haproxy.cfg file contains the set up for our load balancer; we implemented it to connect to our papertrail account so that we could see all the requests that were being sent. We used a round robin algorithm to do the load balancing requests.
