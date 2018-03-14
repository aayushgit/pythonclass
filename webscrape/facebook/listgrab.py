import facebook
graph = facebook.GraphAPI(access_token = "EAACEdEose0cBAGVf1RnN2S0Xy26949dhEfU508aGfHk3ZBhZCr6nmBmhT24OCZCZAGCey2ZCqft95nuUfCS6RSj0iH4jw0pwcC6OLMMydi6oRixT08jBdax3SNhg2MkTaFIKz1X5lOZAKoS8jSp9nCND4CYFbm9ixZARYDxOZARmFWhs8395PXpi8jqasl2GN5YRcZBSGS6qKcAZDZD", version ="2.7")
profile = graph.get_object("me")
friends = graph.get_connections("me", "friends")
friend_list = [friend['name'] for friend in friends['data']]
print("Hello",profile['name'],"!")
status = input('''Enter the Status You Wish to Post: ''')
graph.put_object(parent_object="me",connection_name="feed",message="Hello,World!")