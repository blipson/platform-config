import requests
import json
import getpass
import datetime
import time
import os

url = f"https://dev.id.spsc.io/identity/"

def get_token():
    pw = getpass.getpass()
    token_payload = {
        'grant_type': 'password',
        'username': 'bjlipson@spscommerce.com',
        'client_id': 595,
        'password': pw
    }

    token_headers = {
        'Content-Type': 'application/json;charset=UTF-8'
    }

    token_url = url + "token/"
    r = requests.post(token_url, data=json.dumps(token_payload), headers=token_headers)
    return r.json()


def main():
    res = get_token()

    with open('test.json') as data_file:
        data = json.load(data_file)
    headers = {
        'AUTHORIZATION': 'Bearer ' + res['access_token'],
        'Content-Type': 'application/json;charset=UTF-8'
    }
    url = "https://dev.id.spsc.io/identity/" + f"v2/applications/{data['id']}/"
    appData = requests.get(url, headers=headers)
    appData = appData.json()

    version = os.environ['BUILD_NUMBER']
    payload = {
        'created_at': appData['created_at'],
        'id': appData['id'],
        'status': appData['status'],
        'in_maintenance_mode': appData['in_maintenance_mode'],
        'launchpad_display': appData['launchpad_display'],
        'name': appData['name'],
        'url': data['url'].replace('*', str(version)),
        'description': appData['description'],
        'namespace': appData['namespace'],
        'language_list': appData['language_list'],
        'version': version,
        'is_archived': appData['is_archived'],
        'is_service': appData['is_service'],
        'is_public': appData['is_public'],
        'logo': appData['logo'],
        'slug_archive': appData['slug_archive'],
        'language_version': appData['language_version'],
        'maintenance_url': appData['maintenance_url'],
        'slug': appData['slug'],
        'permissions': data['permissions'],
        'publisher_org_id': appData['publisher_org_id'],
        'publisher_user_id': appData['publisher_user_id'],
        'roles': appData['roles'],
        'updated_at': datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%dT%H:%M:%SZ')
    }

    print(f"PUTTING TO: {url}")
    print(f"WITH DATA: {json.dumps(payload)}")
    print(f"WITH HEADERS: {headers}")
    r = requests.put(url, data=json.dumps(payload), headers=headers)


main()
