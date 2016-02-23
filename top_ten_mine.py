import sys
import json
import operator

def goOverTweets():
    
  tweetFile = open(sys.argv[1])
  HashtagFreq = {}

for line in tweetFile:
    tweet = json.loads(line)
    if 'entities' in tweet and 'hashtags' in tweet['entities']:
      TweetHashtags=tweet['entities']['hashtags']
        for each in TweetHashtags:
		  text=each.encode('utf-8')
          if text in HashtagFreq:
			HashtagFreq[text]+=1
	      else:
			HashtagFreq[text]=1
			  
sortedHashtags=sorted(HashtagFreq,key=operator.itemgetter(1),reverse=True)

count=0
for item in sortedHashtags:
  count+=1
  if count==10:
    break
  else:
    print item[0]+" "+str(item[1])
		  
def main():
    goOverTweets()

if __name__ == '__main__':
    main()