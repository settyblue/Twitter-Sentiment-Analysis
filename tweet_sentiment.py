import sys
import json

scores={}

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def create_dict():
  fp = open(sys.argv[1])
  for line in fp:
    term,score=line.split("\t")
    scores[term]=int(score)
  first_few=scores.items()
  scores.items()  
  print "first few word scores"
  for item in first_few[:20]:
    print item[0],item[1]

def cal_sentiment_score(tweetwords):
  tweet_score=0
  for each in tweetwords:
    if each in scores:
	  tweet_score=tweet_score+scores[each]
  print tweet_score
	
def read_output(fp):
  tweet={}
  fp = open(sys.argv[2])
  for line in fp:
    tweet=json.loads(line)
    if 'text' in tweet:
      ttext=tweet['text'].encode('utf-8')
      tweetwords=ttext.split()	  
      cal_sentiment_score(tweetwords)
	  
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    lines(sent_file)
    lines(tweet_file)
    create_dict()
    read_output(tweet_file)
	
	
if __name__ == '__main__':
    main()
