import requests
import json

def get_api_data():
    credential=dict()
    credential['access_token']='EAAKN9Jo38IQBANdWUaw0BkJtlZATVmrTYQuUsTIoUQyTfwkzEevV2LChOjkzNooaDPZAIHZCOVBoZAA2N4cNfftTLf7gl7kiQzsSkQZC1JTWHRoIAJJKJtf8rrXBEBlz0AgD0NltAenl8vUoIRkICCLsZARZAZATBxGlkzoZA6Ucima6WZAdxGkb7NJzPXCR09FUNRuPehoH5vyAZDZD'

    credential['app_secret']= '832a710df6067662529a7d9758fbc23e'
    credential['app_id']= '719031652315268'
    credential['graph_domain']='https://graph.facebook.com/'
    credential['graph_version']= 'v9.0'
    credential['endpoint_base']=credential['graph_domain']+credential['graph_version']+'/'
    credential['debug']='no'
    credential['page_id']='109468404515926'
    credential['ig_username']='sarvesh.pai'
    return credential

def call_api(url,endpt,debug='no'):
    data=requests.get(url,endpt)
    res=dict()
    res['url']=url
    res['endpoint'] = endpt
    res['endpoint_clean']=json.dumps(res['endpoint'],indent=4) #temp
    #json.dump(res['endpoint'],res['endpoint_clean'], indent=4)
    res['data']=json.loads(data.content)
    res['data_clean']=json.dumps(res['data'],indent=4)

    if ('yes' == debug):
        print("\nURL :"+res['url'])
        print("\nEndpoint :"+res['endpoint_clean'])
        print("\nData :"+res['data_clean'])

    return res

def show_results( res):
    print("\nURL :"+res['url'])
    print("\nEndpoint :")+res['endpoint_clean']
    print("\nData :")+res['data_clean']
