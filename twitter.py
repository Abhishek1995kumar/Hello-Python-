
import tweepy as t
import pandas as p
cons_key = "d9511CHmwVCaNeQ0DCPuu4tAG"
cons_secret = "EjZJUngz7Dj856Vz6weMWXaqtf7VqezXsrnJrODHY4LfZX7RDN"
acc_key = "1302848229273415681-SKaxaUetHQBUCF2W4UgPqRzd1d66bA"
acc_secret = "dOgLq5MXol1l8G8WppT7eSldAbacKMiWKF2kJbXICiQeK"
auth = t.OAuthHandler(cons_key,cons_secret)
auth.set_access_token(acc_key,acc_secret)
api = t.API(auth)
twitter_list = []
for data in t.Cursor(api.search, q=str("BJP & Congress"),count=100,lang="en-us").items(30):
    try:
        if data.user.favorite_count:
            all_like = data.user.favorite_count
    except:
           all_like = data.favorite_count

    item = {
        "data" : str(data.text),
        "twitter" : str(data.created_at),
        "username" : str(data.user.name) ,
        "user_location" : str(data.user.location),
        "total_tweet" : str(data.user.statuses_count),
        "# use in twitter" : str(data.entities["hashtags"])
    }
    twitter_list.append(item)
df = twitter_list
df.to_excel("file04.xlsx")
print(twitter_list)



