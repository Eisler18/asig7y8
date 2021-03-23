import requests
import os
import time
import json

FILE_NAME = 'status.json'

response = requests.post(
    'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token',
    headers={'Authorization':'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='})
response.raise_for_status()
payload=response.json()
last_time = 0

while(True):
    while(time.time()-last_time >= 5*60):
        Token = payload['Token']
        response = requests.get('https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device', headers={'X-Auth-Token': Token})
        data = response.json()['response']
        
        new_dict = {}
        i = 1
        for device in data:
            new_dict.update({'device '+str(i): {'hostname': device['hostname'], 'status': device['reachabilityStatus']}})
            i += 1

        with open(FILE_NAME, 'w') as f:
            json.dump(new_dict, f, indent=2)
        
        if FILE_NAME in os.listdir("."):
            print("\nEl archivo "+os.getcwd()+"/"+FILE_NAME+" ha sido actualizado")
    
        last_time = time.time()