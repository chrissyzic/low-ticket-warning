tweets = ["LOW TICKET WARNING ", ""] #Eventually, we'll use tweepy to check @blackcatdc, @930club, @dc9nightclub, @uhalldc, @rocknrollhotel (and any other venues we want) tweets and store them as a list

#Loop through each tweet in the list "tweets" and check for the phrase "lower ticket warning"
for tweet in tweets:
	if “low ticket warning” in tweet.lower(): #make sure to make the tweet all lowercase because some venues tweet in all upper case, some use sentence case. By making them all lowercase we can make sure capital letters don't throw off the matching/conditional
		  print tweet #Eventually we can use some program to text us the tweet - that command will go on this line!
else:
  exit()
