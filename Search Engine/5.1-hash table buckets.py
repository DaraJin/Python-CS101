def make_hashtable(nbuckets): #empty hash table
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table
def hash_string(keyword,buckets):
	out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out
def hashtable_get_bucket(htable,keyword):
	return htable[hash_string(keyword,len(htable))]
def hashtable_add(htable,key,value):
	hashtable_get_bucket(htable,keyword).append([keyword,value])
	return hashtable
def hashtable_lookup(htable,key):
	the_buckets=hashtable_get_bucket(htable,key)
		for i in the_buckets:
			if i[0]==key:
				return i[1]
		return None
def hashtable_update(htable,key,value):
	bucket=hashtable_get_bucket(htable,key)
	for i in bucket:
		if i[0]==key:
			i[1]=value
			return htable
	bucket.append([key,value])
	return htable
	
# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

def make_hashtable(nbuckets):
    i=0
    rst=[]
    while i<nbuckets:
        rst.append([])
        i+=1
    return rst


#inputs: keyword, numbers of buckets
#output: the buckets
def hash_string(keyword,buckets):
	bucket=[]
	n=0
	for cha in keyword:
		n=n+ord(cha)
	rst=n%buckets
	return rst
	
# Define a function, hash_string,
# that takes as inputs a keyword
# (string) and a number of buckets,
# and returns a number representing
# the bucket for that keyword.

#def hash_string(keyword,buckets):
	bucket=[]
	n=0
	for cha in keyword:
		n=n+ord(cha)
	rst=n%buckets
	return rst


	
#print hash_string('a',12)
#>>> 1

#print hash_string('b',12)
#>>> 2

#print hash_string('a',13)
#>>> 6

#print hash_string('au',12)
#>>> 10

#print hash_string('udacity',12)
#>>> 11
