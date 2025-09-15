from uptime_kuma_api import UptimeKumaApi
import time
import os
import sys

github_user = os.getenv("GITHUB_USER")
github_pass = os.getenv("GITHUB_PASS")

name = sys.argv[1]

isp_name=[]
isp_id=[]

URL='http://192.168.101.13:3001//dashboard'

with UptimeKumaApi(URL) as api:
  
  api.login(github_user, github_pass)
  
  for i in api.get_monitors():
    isp_name.append(i.get("name"))
    isp_id.append(i.get("id"))

  for i in range(len(isp_name)):
    if isp_name[i]==sys.argv[1]:
      id=isp_id[i]
    else:
      print(sys.argv[1])
      print(isp_name)
      print(isp_id)
      
      print(f"ISP Name is not found in the Monitoring Tool..{sys.argv[1]}. Please double check and run again with exact name..!")
      sys.exit(0)

  api.delete_monitor(id)
  time.sleep(30)
  api.logout()
