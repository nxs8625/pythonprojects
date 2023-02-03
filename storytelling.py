import random

# Defining list of phrases which will help to build a story
Sentence_starter = ['About 9 years ago', 'He stood there, staring off into the distance', 'Once upon a time']

character = [' there lived a rich banker.',' there was a woman named Sarah.',
			' there lived a biology guru.']

time = [' One day', ' One summer evening']

story_plot = [' he was passing by', ' he was going for a picnic to ', ' she finished the phone call with the police']

place = [' the mountains', ' the garden']

second_character = [' he saw a man', ' she saw a young lady']

age = [' who seemed to be in late 20s', ' who seemed very old but kind']

work = [' searching something.', ' digging a well on roadside.']


# Selecting an item from each list and concatenating them.
print(random.choice(Sentence_starter)+random.choice(character)+
	random.choice(time)+random.choice(story_plot)+
	random.choice(place)+random.choice(second_character)+
	random.choice(age)+random.choice(work))


