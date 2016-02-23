import sys
import json

scores={}
new_words_scores={}

def hw():
    print 'Hello, world!'

def creat_dict():
  fp = open(sys.argv[1])
  for line in fp:
    term,score=line.split("\t")
    scores[term]=int(score)
	
def lines(fp):
    print str(len(fp.readlines()))

def cal_sentiment_score(tweetwords):
  tweet_score=0
  for each in tweetwords:
    if each in scores:
	  tweet_score=tweet_score+scores[each]
  return tweet_score    

def read_tweets():
  tweet={}
  tweet_score=0
  fp = open(sys.argv[2])
  for line in fp:
    tweet=json.loads(line)
    if 'text' in tweet:
      ttext=tweet['text'].encode('utf-8')
      tweetwords=ttext.split()	  
      tweet_score=cal_sentiment_score(tweetwords)
      for word in tweetwords:
	    if not word in scores.keys():
		  if not word in new_words_scores.keys():
		    new_words_scores[word]=float(tweet_score)/len(tweetwords)
		  else:
		    new_words_scores[word]+=float(tweet_score)/len(tweetwords)
	
  for word,value in new_words_scores.items():
      if value:
	    print str(word)+" "+str(value)

	
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    creat_dict()
    read_tweets()
#    lines(sent_file)
#    lines(tweet_file)

if __name__ == '__main__':
    main()
