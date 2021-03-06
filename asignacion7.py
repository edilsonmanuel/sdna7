
# Comentario incluido para modificar este proyecto
import requests
from pprint import pprint

response = requests.post(
    'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token',
    headers={'Authorization':'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='})
response.raise_for_status()
payload=response.json()
pprint(payload)

response = requests.get(
    'https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device',
    headers= {'X-Auth-Token':payload['Token']})   
list=response.json()['response']
namelist=[]
for j in range(len(list)):
    namelist.append ([list[j]['family'],list[j]['hostname'],
    list[j]['managementIpAddress'],list[j]['lastUpdated'],
    list[j]['reachabilityStatus']])
pprint(namelist)

