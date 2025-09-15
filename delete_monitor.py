from uptime_kuma_api import UptimeKumaApi
import time
import os
import sys

"""
argv_value = sys.argv[1]

print("From Jenkins (repr):", repr(argv_value))
for idx, ch in enumerate(argv_value):
    print(idx, ch, ord(ch))


def clean(s: str) -> str:
    return s.strip().replace("\u00a0", " ")  # remove extra space types
"""

value = sys.argv[1]
print("From Jenkins:", repr(value))
print("Length:", len(value))

isp_list = [
    '5 STAR-BHUBANESHWAR-TATA-ILL-10',
    '7 STAR-Mumbai-AIRTEL-ILL-100',
]

for item in isp_list:
    print(f"Compare with {repr(item)} =>", value == item)



'''
name = sys.argv[1]

github_user = os.getenv("GITHUB_USER")
github_pass = os.getenv("GITHUB_PASS")

#name = sys.argv[1]

isp_name=[]
isp_id=[]

URL='http://192.168.101.13:3001//dashboard'

with UptimeKumaApi(URL) as api:
  
  api.login(github_user, github_pass)
  
  for i in api.get_monitors():
    isp_name.append(i.get("name"))
    isp_id.append(i.get("id"))

  for i in range(len(isp_name)):
    if name==isp_name[i]:
      
      id=isp_id[i]
    else:
      print(name, isp_name[i])
      print(isp_id)
      
      print(f"ISP Name is not found in the Monitoring Tool..{sys.argv[1]}. Please double check and run again with exact name..!")
      sys.exit(0)

  api.delete_monitor(id)
  time.sleep(30)
  api.logout()
'''
