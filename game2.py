with open("story.txt", mode = 'r' ) as f: 
    story = f.read() # to read the file content 
    # python automatically closes the file according to indentation
start = -1 
start_target = '['
end_target = ']'
words = [] #list of words that occur in story 
for ind, val in enumerate(story): #enumerate is a good concept
    if val == start_target:
        start = ind
    
    if val == end_target and start != -1 :
        word = story[start : ind+1 ]
        words.append(word)
        start = -1 
words = list(set(words)) #we convert the list to set then back to list 
# this removes the duplicates, we have stored the words that user needs to input       
inputs = []
map = dict()
for word in words: 
    replace = input(f"Enter the {word}")
    map[word] = replace

print(map)

for word in words: 
    story = story.replace(word, map[word])

print(story)