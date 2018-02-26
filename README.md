## noSNOOZ


![Service: offline](https://img.shields.io/badge/service-offline-red.svg)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

noSNOOZ for Reddit provides advance notifications about abnormally quickly rising posts.

[site](https://cbskarmory.github.io/noSNOOZ) is currently disconnected from service for security reasons


#### How to use (locally)

 - Run `./start_server.sh` or `node src/app.js`. This will host an instance of the site locally, at `localhost:8080`
 - Run `./database.py`
   - by default, this looks at news+worldnews+politics, which is configurable
   
#### Using Command Line Interface

- Run `./query.py [subreddit name]`
