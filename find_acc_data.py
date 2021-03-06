from credentials import get_api_data, call_api
#from get_insta_acc import getInsta
def siphon_acc( data ) :
	
	endpt = dict()
	data['ig_username']=input('Enter the user name you want to search: ') 
	endpt['fields'] = 'business_discovery.username(' + data['ig_username'] + '){username,website,name,ig_id,id,profile_picture_url,biography,follows_count,followers_count,media_count}' # string of fields to get back with the request for the account
	endpt['access_token'] = data['access_token'] # access token
	url = data['endpoint_base'] + '17841446049286885' # endpoint url

	return call_api( url, endpt, data['debug'] ) # make the api call

detail = get_api_data() 
detail['debug'] = 'no' 
response = siphon_acc( detail ) 

print ("\n---- ACCOUNT INFO -----\n") 
print ("username:") 
print (response['data']['business_discovery']['username']) 
#print ("\nwebsite:") 
#print (response['data']['business_discovery']['website'] )
print ("\nnumber of posts:") 
print (response['data']['business_discovery']['media_count']) 
print ("\nfollowers:") # label
print (response['data']['business_discovery']['followers_count']) 
print ("\nfollowing:") # label
print (response['data']['business_discovery']['follows_count']) 
print ("\nprofile picture url:") # label
print (response['data']['business_discovery']['profile_picture_url']) 
print ("\nbiography:") 
#   ['data']['instagram_business_account']['id']print response['data']['business_discovery']['biography']

