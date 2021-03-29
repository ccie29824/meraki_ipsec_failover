import requests
import json
import sys
import os
import time

class Meraki():
    def __init__(self):
        self.IP = "1.1.1.1"
        self.ipList = ["1.1.1.1", "2.2.2.2"]
        self.url = "https://api.meraki.com/api/v0/organizations/XXXXX/thirdPartyVPNPeers"
        self.header = {'X-Cisco-Meraki-API-Key':'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy',
                       'Content-Type': 'application/json',
                       'cache-control': "no-cache",}

    @staticmethod
    def getIP(url, header):
        try:
            getResponse = requests.get(url = url, headers=header)
            if getResponse.status_code == 200:
                data = json.loads(getResponse.text)
                return(data)
        except requests.exceptions.ConnectionError:
            print("Connection Error")
        except requests.exceptions.ConnectTimeout:
            print("Connection Timeout")
        except Exception as e:
            print(e)

    @staticmethod
    def updateIP(IP, url, header, ipList):
        data = Meraki.getIP(url, header)
#       print(data)
#       print(len(data))
        flag = False
        for k in data:
            if 'mcd' in k.values():
                if IP == k['publicIp']:
                    flag = True
                    for ip in ipList:
                      if IP != ip:
                          newIP = ip
                          k['publicIp'] = newIP
                          break

            else:
                print('Public IP not found')
#       print(data)

        if flag:
            payload = data
            payload = json.dumps(payload)
            getResponse = requests.request('PUT', url = url, headers=header, data=payload)
            if getResponse.status_code == 200:
                print('IP updated successfully')
            else:
                print('Failed to update IP')
        else:
            print('No need to update IP')

    def ping(self):
        try:
            response = os.system("ping -n 2 " + self.IP)
            print(response)
            if response !=0:
                Meraki.updateIP(self.IP, self.url, self.header, self.ipList)
            else:
                data = Meraki.getIP(self.url, self.header)
#               print(data)
#               print(len(data))
                print('IP is UP')
                flag = False
                for k in data:
                    if 'mcd' in k.values():
                        if self.IP != k['publicIp']:
                            flag = True
                            k['publicIp'] = self.IP
                    else:
                        print('Public IP not found')
                if flag:
                    payload = data
                    payload = json.dumps(payload)
                    getResponse = requests.request('PUT', url = self.url, headers=self.header, data=payload)
                    if getResponse.status_code == 200:
                        print('IP updated successfully')
                    else:
                        print('Failed to update IP')
                else:
                    print('No need to update IP')
        except Exception as e:
            print(e)

if __name__ == "__main__":
    merakiobj = Meraki()
    while True:
        merakiobj.ping()
        print('sleeping for 30s....')
        time.sleep(30)