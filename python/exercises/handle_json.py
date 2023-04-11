import requests  as req
import json
from datetime import datetime

'''
 launch_date_utc, launch_success, rocket/rocket_name, rocket/second_stage/payloads/payload_id. 
 Be aware, that rocket/second_stage/payloads is a list, that can have multiple items!

09/03/2020 (893 days ago): Falcon 9 - Starlink-11
'''
def getDetails(l):
    result = []
    for launch in l:
        result.append({
            'date':launch['launch_date_utc'],
            'launch_success': launch['launch_success'],
            'rocket_name': launch['rocket']['rocket_name'],
            'payloads': [s['payload_id'] for s in launch['rocket']['second_stage']['payloads']]
            })
    return result

def formatDetails(launches):
    for l in launches:
        line = f"{l['date']} ({l['diffDays']} days ago): {l['rocketName']} - {(', ').join(l['payloads'])}"
        writeAndClose('space_x_launches', 'txt', line)
        print(line)

def writeAndClose(fileName, ext, item):
    f = open(f"{fileName}.{ext}", 'a')
    f.write(item + '\n')
    f.close()

# def openAndReadLine(fileName, ext, nrOfLine):
#     f = open(f"{fileName}.{ext}", 'r')
#     line = f.readlines()[nrOfLine]
#     f.close()
#     return line

r = req.get('https://api.spacexdata.com/v3/launches')
data = json.dumps(r.json(), indent=2)
launches=json.loads(data)
details = getDetails(launches)
okLaunches = []
badLaunches = []
# print(launches)
for launch in details:
    d = launch['date'][:10]
    date_format = '%Y-%m-%d'
    date_object = datetime.strptime(d, date_format)
    new_format = '%d/%m/%Y'
    formated = date_object.strftime(new_format)
    diffDays = datetime.now().__sub__(date_object).days
   
    if launch['launch_success'] == True:
        okLaunches.append({
            'date': formated,
            'diffDays': diffDays,
            'rocketName':launch['rocket_name'],
            'payloads': launch['payloads']
        })
    else:
        badLaunches.append({
            'date': formated,
            'diffDays': diffDays,
            'rocketName':launch['rocket_name'],
            'payloads': launch['payloads']
        })
writeAndClose('space_x_launches', 'txt', 'Successful launches: \n')
formatDetails(okLaunches)
writeAndClose('space_x_launches', 'txt', '\n Failed launches: \n ')
formatDetails(badLaunches)
