keyword_map = {}
words_map = {}
child_map = {}
parent_map = {}
gloss_map = {}
keyword = input("Please enter a specific word to find sub-categories:\n")

#obtain wnid mappings for all words and those which contain keyword
with open("words.txt") as f:
	for line in f:
		line_split = line.split()
		wnid = line_split[0]
		words = line_split[1:]
		if keyword in words:
			keyword_map[wnid] = words
		words_map[wnid] = words
f.close()

with open("gloss.txt") as f:
	for line in f:
		line_split = line.split()
		wnid = line_split[0]
		gloss = " ".join(line_split[1:])
		gloss_map[wnid] = gloss
f.close()

#obtain wnid mappings for all parents-children
with open("is_a.txt") as f:
	for line in f:
		parent, child = line.split()
		parent_map[child] = parent
		if parent not in child_map:
			child_map[parent] = [child]
		else:
			child_map[parent].append(child)
f.close()	


#find children and parents
with open(str(keyword)+".txt", "w") as f:
	search = []
	for category in keyword_map.keys():

		f.write((" ".join(words_map[category])+" (").upper())
		f.write(gloss_map[category]+")\n")
		#list all children
		f.write("Descendants:\n")
		if category in child_map:
			search = [child for child in child_map[category]]
		while search:
			node = search.pop()
			f.write("\t"+" ".join(words_map[node])+"\n")
			if node in child_map: #has children
				for child in child_map[node]:
					search.append(child)

		#list all parents
		f.write("Ancestors:\n")
		if category in parent_map:
			node = parent_map[category]
		else:
			node = category
		while node in parent_map:
			f.write("\t"+" ".join(words_map[node])+"\n")
			node = parent_map[node]
		f.write("\n\n")
f.close()

