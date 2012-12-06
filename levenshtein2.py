def printMatrix(m,len1,len2):
	print ''
	for i in range(len1):
		for j in range(len2):
			print "%3i" %m[i,j],
		print
	print ''

s1 = raw_input("First string:")
s2 = raw_input("Second string:")

def levenshtein2(s1,s2):
	len1 = len(s1)
	len2 = len(s2)
	matrix = {}
	
	for i in xrange(len1 + 1):
		matrix[i,0] = i

	for j in xrange(len2 + 1):
	 	matrix[0,j] = j
		
	for j in xrange(1,len2 + 1):
		for i in xrange(1,len1 + 1):
			if s1[i - 1] == s2[j - 1]:
				matrix[i,j] = matrix[i-1,j-1]
			else:
				matrix[i,j] = min(matrix[i-1,j],matrix[i,j-1],matrix[i-1,j-1]) + 1
	printMatrix(matrix,len1 + 1,len2 + 1)
	return matrix[len1,len2]

distance = levenshtein2(s1,s2)
print 'The levenshtein-distance of',s1,'and',s2,'is',distance
