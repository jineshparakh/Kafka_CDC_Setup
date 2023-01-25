from couchbase.cluster import Cluster
from couchbase.auth import PasswordAuthenticator
from couchbase.options import (ClusterOptions)
from datetime import timedelta
import const

def upsertRecords(n):
    # Update this to your cluster
    username = const.COUCHBASE_USERNAME
    password = const.COUCHBASE_PASSWORD
    bucket_name = "source"
    scope_name = "_default"
    collection_name = "inputCollection"
    # User Input ends here.

    # Connect options - authentication
    auth = PasswordAuthenticator(
        username,
        password,
    )

    # Get a reference to our cluster
    # NOTE: For TLS/SSL connection use 'couchbases://<your-ip-address>' instead
    cluster = Cluster('couchbase://localhost', ClusterOptions(auth))

    # Wait until the cluster is ready for use.
    cluster.wait_until_ready(timedelta(seconds=5))

    # get a reference to our bucket
    cb = cluster.bucket(bucket_name)

    cb_coll = cb.scope(scope_name).collection(collection_name)

    # insert 100 records

    upsertedRecords = []
    for i in range(n):
        print("\nUpsert CAS: ")
        try:
            doc = {
                "id": 1,
                "name": "name_"+str(i)
            }
            key = str(doc["id"])
            upsertedRecords.append(doc)
            result = cb_coll.upsert(key, doc)
            print(result.cas)
        except Exception as e:
            print(e)

    # try:
    #     inventory_scope = cb.scope(scope_name)
    #     sql_query = 'FROM inputCollection c SELECT c.*'
    #     row_iter = inventory_scope.query(
    #         sql_query,
    #         QueryOptions(positional_parameters=[]))
    #     for row in row_iter:
    #         print(row)
    # except Exception as e:
    #     print(e)

    return upsertedRecords
