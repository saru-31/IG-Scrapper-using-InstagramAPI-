from credentials import get_api_data, call_api
import datetime

def debugToken(data):
    endpoint=dict()
    endpoint['input_token']=data['access_token']
    endpoint['access_token']=data['access_token']

    url=data['graph_domain']+'/debug_token'
    return call_api(url,endpoint,data['debug'])

data=get_api_data()
data['debug']='yes'
res=debugToken(data)
#print(res)
print("Expiring at:")
print(datetime.datetime.fromtimestamp(res['data']['data']['data_access_expires_at']))