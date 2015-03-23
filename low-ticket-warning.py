tweets = ["@blackcatdc LOW TICKET ALERT: Big Data (3/27) and Twin Shadow (3/30). Get your tix ASAP!", "@blackcatdc LOW TICKET ALERT for @PerfumeGenius w/ @JennyHval TOMORROW!", "@blackcatdc Correction: TONIGHT: Perfect Pussy (10:15), Skating Polly (9:15), Baby Bry Bry & The Apologists (8:15). Doors 7:30PM. SOLD OUT"] #Eventually, we'll use tweepy to check @blackcatdc, @930club, @dc9nightclub, @uhalldc, @rocknrollhotel (and any other venues we want) tweets and store them as a list like this one
#It might actually have to be a dictionary (so we can keep track of who sent the tweet, not just the contents of it the tweet), but for now let's assume it's a list!

#Loop through each tweet in the list "tweets" and check for the phrase "lower ticket warning"
for tweet in tweets:
	if “low ticket warning” in tweet.lower() or "low ticket alert" in tweet.lower(): #make sure to make the tweet all lowercase because some venues tweet in all upper case, some use sentence case. By making them all lowercase we can make sure capital letters don't throw off the matching/conditional
		print tweet #Eventually we can use some program to text us the tweet - that command will go on this line!
	else:
		exit()
