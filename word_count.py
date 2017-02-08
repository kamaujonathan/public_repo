def words(phrase):
	result = {}
	word_count = phrase.split()
	for word in word_count:
		if word.isdigit():
			word = int(word)
		if word in result:
			result[word] += 1
		else:
			result[word] = 1
	return result
