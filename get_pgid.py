from credentials import get_api_data,call_api

def getPgId(data):
    endpoint=dict()
    endpoint['access_token']=data['access_token']
    endpoint['client_id']=data['app_id']
    endpoint['client_secret']=data['app_secret']
    url = data['endpoint_base']+'me/accounts'
    return call_api(url,endpoint,data['debug'])

detail=get_api_data()
detail['debug']='yes'
res=getPgId(detail)
print("\nPage Id is :")
print(res['data']['data'][0]['id'])
print("Page category is :\t"  )
print(res['data']['data'][0]['category'])