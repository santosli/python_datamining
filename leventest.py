s = raw_input("First string:")
t = raw_input("Second string:")

def lev(s,t):
	s,t,d=' '+s,' '+t,{}

	for i in xrange(len(s)):
		d[i,0]=i

	for j in xrange(len(t)):
		d[0,j]=j

	for j in xrange(1,len(t)):
		for i in range(1,len(s)):
			if s[i] == t[j]:
				d[i,j]=d[i-1,j-1]
			else:
				d[i,j]=min(d[i-1,j],d[i,j-1],d[i-1,j-1])+1
	return d[len(s)-1,len(t)-1]

distance = lev(s,t)
print 'The levenshtein-distance of',s,'and',t,'is',distance



