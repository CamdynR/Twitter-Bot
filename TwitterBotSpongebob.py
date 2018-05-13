import tweepy, time
import random
from time import sleep

#Normally this is filled in, but these are essentially the 
#username and password for the bot so I removed them
access_token = 
acces_token_secret = 
consumer_key = 
consumer_secret = 

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,acces_token_secret)
auth.secure = True
api = tweepy.API(auth, wait_on_rate_limit=True)


#It's easier to have it loop X numner of times than to
#create another processes that will run the file X number of times
i = 0
while i < 700:
	w = random.randint(1,18)
	x = random.randint(1,15)

	handle1 = "";
	handle2 = "";

	sourceHandle1 = "@garyfromteenmom"
	sourceHandle2 = "@aayylmao"
	sourceHandle3 = "@dubstep4dads"
	sourceHandle4 = "@imskytrash"
	sourceHandle5 = "@yung_gravy"
	sourceHandle6 = "@richchigga"
	sourceHandle7 = "@dril"

	randNum1 = random.randint(1,4)
	if randNum1==1:
		handle1 = sourceHandle1
	elif randNum1==2:
		handle1 = sourceHandle2
	elif randNum1==3:
		handle1 = sourceHandle3
	elif randNum1==4:
		handle1 = sourceHandle4
	elif randNum1==5:
		handle1 = sourceHandle5
	else:
		handle1 = sourceHandle6

	randNum2 = random.randint(1,4)
	if randNum2==1:
		handle2 = sourceHandle1
	elif randNum2==2:
		handle2 = sourceHandle2
	elif randNum2==3:
		handle2 = sourceHandle3
	elif randNum2==4:
		handle2 = sourceHandle4
	elif randNum2==5:
		handle2 = sourceHandle5
	else:
		handle2 = sourceHandle6

	timeline = api.user_timeline(screen_name=handle1, include_rts=True, count=w, page=x)
	for tweet in timeline:
		string1 = tweet.text

	nString1 = string1.split()[0:int(len(string1.split())/2)]
	space = ' '
	my_new_list1 = [x + space for x in nString1]

	y = random.randint(1,18)
	z = random.randint(1,15)

	timeline = api.user_timeline(screen_name=handle2, include_rts=True, count=y, page=z)
	for tweet in timeline:
		string2 = tweet.text

	nString2 = string2.split()[int(len(string2.split())/2):len(string2.split())+1]
	my_new_list2 = [y + space for y in nString2]

	my_new_list3 = my_new_list1 + my_new_list2
	my_new_list3 = [x for x in my_new_list3 if "@" not in x]
	newString3 = ''.join(my_new_list3)

	if len(newString3) > 140:
		newString3 = newString3[0:140]
    
  api.update_status(newString3)
    
	i += 1
	time.sleep(900)
