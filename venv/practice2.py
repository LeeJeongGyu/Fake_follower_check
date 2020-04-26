from InstagramAPI import InstagramAPI



users_list = []
following_users = []
follower_users = []

InstagramAPI = InstagramAPI("01096458519","skek8641!@#")
InstagramAPI.login()
InstagramAPI.getSelfUserFollowers()
InstagramAPI.getSelfUsernameInfo()
print(InstagramAPI.LastJson['orinalda1']['follower_count'])
