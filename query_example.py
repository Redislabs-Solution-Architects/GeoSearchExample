from redisearch import Client, Query, TextField, GeoField, NumericField, GeoFilter, NumericFilter


client = Client(
   'attractions',
   host='127.0.0.1',
   password='',
   port=6379
   )



print("Full text search for a 'ball string':")
q = Query("ball string").verbatim()
res = client.search(q)
for doc in res.docs:
   print("\t", doc.description)

print("Full text search for a 'ball string' search within 300 miles of Kansas City that is verified")
q = Query("ball string").add_filter(
   GeoFilter('geo', -94.5786, 39.0997, 300, unit='mi')
   ).add_filter(NumericFilter('verified', 1, 1)).verbatim()
res = client.search(q)
for doc in res.docs:
   print("\t", doc.description)