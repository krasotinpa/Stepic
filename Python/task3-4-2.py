D = {}
with open('input.txt') as inf:
    for line in inf:
	    for word in line.strip().split():
		    D[word] = D.get(word, 0) + 1
max_count = max(D.values())
most_frequent = [k for k, v in D.items() if v == max_count]

#print(D)
#print(most_frequent)
print(min(most_frequent), max_count)


