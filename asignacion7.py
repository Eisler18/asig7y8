import requests
from pprint import pprint

response = requests.post(
    'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token',
    headers={'Authorization':'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='})
payload=response.json()
#pprint(payload)

Token = payload['Token']
response = requests.get('https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device', headers={'X-Auth-Token': Token})
data = response.json()['response']
#print(data)

Table = [['family', 'hostname', 'managementIpAddress', 'lastUpdated', 'reachabilityStatus']]
for device in data:
    family = device['family']
    hostname = device['hostname']
    managementIpAddress = device['managementIpAddress']
    lastUpdated = device['lastUpdated']
    reachabilityStatus = device['reachabilityStatus']
    Table.append([family, hostname, managementIpAddress, lastUpdated, reachabilityStatus])

for row in Table:
    print(row)