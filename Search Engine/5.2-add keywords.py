




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
