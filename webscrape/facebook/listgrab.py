import facebook
graph = facebook.GraphAPI(access_token = "EAACEdEose0cBADaPqH7gnc2jrax9BOEXAsUHoWc26M3c3TjESOKmkVwjr5OGvqmnSLv5DiGBEyjMaJlAoLaYEmJhK8jvbHeBGn6ZC28UOSsGQHPVobBCvOVJXZCYMZBUzbi9fDU5wza9Ett4mnBg64HKUe1A68GZADohjQHZCpyxPj4gRZAyBTqtucbodaM8wZD", version ="2.7")
profile = graph.get_object("me")
friends = graph.get_connections("me", "friends")
friend_list = [friend['name'] for friend in friends['data']]
print(friend_list)
