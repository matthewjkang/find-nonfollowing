# Get instance
import instaloader
import datetime
import getpass

L = instaloader.Instaloader()

# Login or load session
username = input('username : ')
password = getpass.getpass()
L.login(username, password)  # (login)

# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, username)

# Print list of followers
follow_list = []
for followee in profile.get_followers():
    follow_list.append(followee.username)

# Print list of followees
following_list = []
for following in profile.get_followees():
    following_list.append(following.username)

unfollow = []
for i in following_list:
    if i not in follow_list:
        unfollow.append(i)


textfile = open(str(datetime.date.today())+" unfollowers.txt", "w")
for element in unfollow:
    textfile.write(element + "\n")
textfile.close

