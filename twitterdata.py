import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#Open JSON file
tweet_json = open("twitter_jsonfile.json", "r") # the r means you are JUST reading and nothing more

#Get data from JSON file
tweet_data = json.load(tweet_json)

#Close JSON file
tweet_json.close()

#Pront DATA of on tweet
print("Tweet id:", tweet_data[0]['id']) #index is there because you want to call something specific in the key of id

#print the text of the first tweet
print("Tweet text:", tweet_data[0]['text']) 

for t in range(len(tweet_data)): #the length only goes to the number that you put. Let's say that the length of the list is 3, it would go automatically to 3. 
                                 #With range you go through every single index.
    print("Tweet text: ", tweet_data[t]['text']) #the t goes there so that you go through the 'text' and over since t is not a number but a concept 
    
# Textblob sample:
#tb = TextBlob("You are a brilliant computer scientist.")
#print(tb.polarity)

polarity = []
subjectivity = []
tweets = "" # there are only two quotation marks because we want to make tweets a string

for e in range(len(tweet_data)): #irate through the text
    tweet_blob = TextBlob(tweet_data[e]['text']) #text to be set to a textblob
    polarity.append(tweet_blob.polarity) #will add the text blob and polarize it at the same time. That's why .polarity is inside the parameter.
    subjectivity.append(tweet_blob.subjectivity) # will add the text blob and subjectivize it  at the same time.
    tweets = tweets + tweet_data[e]['text'] #convine all your string or tweets, will be used later in WordCloud function
    
textbird_tb = TextBlob(tweets)

undesired_words = ["hi", "bye", "interesting", "goodnight", "spider", "fear"]
filtered_dictionary = {}
filtered_words[words] = count
    
for word in textbird_tb.words:
    if(len(word) < 2):
        continue
    elif( not word.isalpha()):
        continue
    elif(word in undesired_words): #the continue means that if the condition is not met, the elif condition will be broken and it will go back to the beginning of the for loop.
        continue
    filtered_dictionary['word'] = textbird_tb.word_counts(word)
    
    
#Set up you HISTOGRAM
plt.his(polarity, bins = [-1.1, -.75, -.5, -.25, 0,  .25, .5, .75, 1.1])
plt.xlabel('Polarity')
plt.ylabel('Frequency')
plt.title('Polarity vs Frequency')
plt.axis([-1.1, 1.1, 0, 100]) #describes how high the x and y axis will go. X is first and Y is after. 
plt.grid(True)
plt.show()
    
word_Cloud = WordCloud().generate_from_frequencies(filtered_dictionary)
plt.imshow(word_Cloud, interpolation = "bilinear")
plt.axis("off")
plt.show


