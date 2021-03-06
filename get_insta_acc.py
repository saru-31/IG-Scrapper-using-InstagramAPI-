from credentials import get_api_data,call_api

def getInsta(data):
    endpoint=dict()
    endpoint['access_token']=data['access_token']
    endpoint['fields']='instagram_business_account'
    url = data['endpoint_base']+data['page_id']
    return call_api(url,endpoint,data['debug'])

detail=get_api_data()
detail['debug']='yes'
res=getInsta(detail)
print("\nPage Id is :")
print(res['data']['id'])
print("Instagram id :\t"  )
print(res['data']['instagram_business_account']['id'])