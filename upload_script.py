import requests
import sys
import json

args = sys.argv[1]
row = args.split('#')
headers = {'Content-Type': 'application/json',
           "Authorization": "af-pEJaygALr3ony0WkVv18JtOKccwCn7sj"}
data = {
    "card_html": row[-2],
    "link": row[2],
    "private": False,
    "metadata"  : {
        "Message-ID": row[1],
        "Date": row[3],
        "From": row[4][12:-2],
        "To": row[5][12:-2],
        "Subject": row[6],
        "X-From": row[7],
        "X-To": row[8],
        "X-CC": row[9],
        "X-BCC": row[10],
        "X-Folder": row[11],
        "X-Origin": row[12],
        "X-FileName": row[13],
        "User": row[15],
    }
}
data = requests.post("http://localhost:8090/api/card", data=json.dumps(data), headers=headers)
print(row[0])
if data.status_code != 200:
    print("Error: " + data.text)