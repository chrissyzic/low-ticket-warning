tweets = ["@blackcatdc LOW TICKET ALERT: Big Data (3/27) and Twin Shadow (3/30). Get your tix ASAP!", "@blackcatdc LOW TICKET ALERT for @PerfumeGenius w/ @JennyHval TOMORROW!", "@blackcatdc Correction: TONIGHT: Perfect Pussy (10:15), Skating Polly (9:15), Baby Bry Bry & The Apologists (8:15). Doors 7:30PM. SOLD OUT"] #Eventually, we'll use Tweepy to check @blackcatdc, @930club, @dc9nightclub, @uhalldc, @rocknrollhotel (and any other venues we want) and store the tweets as a list like this one
#It might actually have to be a dictionary (so we can keep track of who sent the tweet, not just the contents of it), but for now let's assume it's a list because that's easier!

#Loop through each tweet in the list "tweets" and check for the phrase "lower ticket warning"
for tweet in tweets:
	if “low ticket warning” in tweet.lower() or "low ticket alert" in tweet.lower(): #make sure to make the tweet contents all lowercase because some venues tweet in all upper case, some use sentence case, etc. By making them all lowercase we can make sure capital letters don't throw off the matching/conditional
		print tweet #Eventually we will use some program (Rapid SMS, maybe) to text us the tweet username contents.
	else:
		print "No warnings - your tickets are safe for another day!"
	
#Stuff I'd like to add/figure out:
## Can we create a list of bands we care about and it'll only alert us about those shows?
### Possibly pull it from a Google Spreadsheet? Or a Spotify playlist or Bandcamp if we want to get rull complicated with APIs?
## What language do venues use in "low ticket" tweets and do they consistently use the same language? (Black Cat always says "LOW TICKET ALERT")
### Ooh, that could be a good way to determine which venue sent the tweet, if they all use different language and use it consistently (but it's actually probably easier/more reliable to just store the tweeter's handle in the dictionary with the tweet)
