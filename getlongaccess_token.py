from credentials import get_api_data , call_api

def getLongAccessToken(data):
    endpoint=dict()
    endpoint['grant_type']='fb_exchange_token'
    endpoint['client_id']=data['app_id']
    endpoint['client_secret']=data['app_secret']
    endpoint['fb_exchange_token']=data['access_token']
    url = data['endpoint_base']+'oauth/access_token'
    
    return call_api(url,endpoint,data['debug'])

detail=get_api_data()
detail['debug']='yes'
res=getLongAccessToken(detail)
#print(res)
print("-----Access Token----- \n" + res['data']['access_token'])

