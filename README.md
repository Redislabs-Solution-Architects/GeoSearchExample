## Downloading Data

Download All_States_Offbeat_Tourist_Attractions.gpx

from http://www.poi-factory.com/node/29228

You will need to register

## Running Locally

### Starup docker container

```
docker run --rm -p 6379:6379 redislabs/redisearch:latest
```


### Install python requirements

```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

### Dump database and load example data

```
redis-cli flushdb && python3 load_data.py 
```

### Example command line search

Find me all balls of string withing 300 miles of Kansas City that are verified 

```
127.0.0.1:6379> FT.SEARCH attractions "@description:'ball string' @verified: [1 1] @geo:[-94.5786 39.0997 300 mi]" 
```

### Example search in python

```
python3 query_example.py 
```