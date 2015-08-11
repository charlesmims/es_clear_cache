# es_clear_cache

When container is run, it checks elasticsearch memory usage at localhost:9200/_node/stats, 
and if any nodes have JVM memory utilization over 95%, it clears the cluster's cache.

Doing this may cause increased IO as new searches have to go to disk, but in the case of a write-intensive cluster, this can prevent nodes from falling over.


## usage
on a host where elasticsearch is running:
```
docker run --net=host charlesmims/es_clear_cache
```
