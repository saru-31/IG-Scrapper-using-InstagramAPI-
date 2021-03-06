from credentials import get_api_data, call_api
from get_insta_acc import getInsta
import sys
def getinfo_hashtag(data):
    endpoint=dict()
    detail=get_api_data()
    detail['debug']='yes'
    endpoint['access_token']=data['access_token']
    endpoint['user_id']=getInsta(detail)['data']['instagram_business_account']['id']
    endpoint['q']=data['hashtag']
    url = data['endpoint_base']+'ig_hashtag_search'

    return call_api(url,endpoint,data['debug'])

def getmedia_hashtag(data):
    endpoint=dict()
    detail=get_api_data()
    detail['debug']='yes'
    endpoint['access_token']=data['access_token']
    endpoint['user_id']=getInsta(detail)['data']['instagram_business_account']['id']
    endpoint['fields'] = 'id,children,caption,comment_count,like_count,media_type,media_url,permalink'
    url = data['endpoint_base']+data['hashtag_id']+ '/' +data['type']

    return call_api(url,endpoint,data['debug'])


try:
    hashtag = sys.argv[1]

except:
    hashtag='thriller'

detail=get_api_data()
detail['debug']='yes'
detail['hashtag']=hashtag

res=getinfo_hashtag(detail)

print("Information")
print("\nhashtag :"+ hashtag)
print("\nid :"+res['data']['data'][0]['id'])

detail['hashtag_id']=res['data']['data'][0]['id']
detail['type']='top_media'
res2=getmedia_hashtag(detail)
#print(res2['data'])
print("top rated posts")
print("\nhashtag :"+ hashtag)
for post in res2['data']['data']:
    print("\nLink :"+post['permalink'])
    print("\nCaption :"+post['caption'])
    print("\nMediaType :"+post['media_type'])
    print("\nPosted at :"+post['timestamp'])
    print("\nNo of Likes :")
    print(post['like_count'])
    print("\nNo of comments :")
    print(post['comment_count'])


detail['type']='recent_media'
res2=getmedia_hashtag(detail)

print("recent posts")
print("\nhashtag :"+ hashtag)
for post in res2['data']['data']:
    print("\nLink :"+post['permalink'])
    print("\nCaption :"+post['caption'])
    print("\nMediaType :"+post['media_type'])
    print("\nPosted at :"+post['timestamp'])
    print("\nNo of Likes :")
    print(post['like_count'])
    print("\nNo of comments :")
    print(post['comment_count']) 