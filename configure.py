import requests
import json

def main():
    with open('test.json') as data_file:
        data = json.load(data_file)

    payload = {
        'created_at': data['created_at'],
        'id': data['id'],
        'status': data['status'],
        'in_maintenance_mode': data['in_maintenance_mode'],
        'launchpad_display': data['launchpad_display'],
        'name': data['name'],
        'url': data['url'],
        'description': data['description'],
        'namespace': data['namespace'],
        'language_list': data['language_list'],
        'version': data['version'],
        'is_archived': data['is_archived'],
        'is_service': data['is_service'],
        'is_public': data['is_public'],
        'logo': data['logo'],
        'slug_archive': data['slug_archive'],
        'language_version': data['language_version'],
        'maintenance_url': data['maintenance_url'],
        'slug': data['slug'],
        'permissions': data['permissions'],
        'publisher_org_id': data['publisher_org_id'],
        'publisher_user_id': data['publisher_user_id'],
        'roles': data['roles'],
        'updated_at': data['updated_at']
    }
    headers = {
        'AUTHORIZATION': 'Bearer <TOKEN_GOES_HERE>',
        'Content-Type': 'application/json;charset=UTF-8'
    }

    url = f"https://dev.id.spsc.io/identity/v2/applications/{data['id']}/"

    print(f"PUTTING TO: {url}")
    print(f"WITH DATA: {json.dumps(payload)}")
    print(f"WITH HEADERS: {headers}")
    r = requests.put(url, data=json.dumps(payload), headers=headers)

    print(r)

main()
