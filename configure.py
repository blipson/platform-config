import requests
import json
import getpass
import datetime
import time


def get_token(env):
    pw = getpass.getpass()
    token_payload = {
        "grant_type": "password",
        "username": "bjlipson@spscommerce.com",
        "client_id": 595,
        "password": pw
    }
    token_headers = {
        "Content-Type": "application/json;charset=UTF-8"
    }
    if env == "prod":
        token_url = f"https://id.spsc.io/identity/token/"
    else:
        token_url = f"https://{env}.id.spsc.io/identity/token/"
    r = requests.post(token_url, data=json.dumps(token_payload), headers=token_headers)
    return r.json()["access_token"]


def deploy():
    env = input("Environment: ")
    version = input("Version: ")
    token = get_token(env)

    with open("bdp.json") as data_file:
        data = json.load(data_file)

    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json;charset=UTF-8"
    }
    if env == "prod":
        url = f"https://id.spsc.io/identity/v2/applications?name={data['name']}"
        create_url = "https://id.spsc.io/identity/v2/applications/"
    else:
        url = f"https://{env}.id.spsc.io/identity/v2/applications?name={data['name']}"
        create_url = f"https://{env}.id.spsc.io/identity/v2/applications/"
    print(f"---------------------------------------URL---------------------------------------\n{url}")
    appData = requests.get(url, headers=headers).json()
    print(f"---------------------------------------RESPONSE---------------------------------------\n{appData}")
    if appData["count"] == 1:
        put_url = f"https://{env}.id.spsc.io/identity/v2/applications/{appData['results'][0]['id']}/"
        appData = appData["results"][0]
        payload = {
            "created_at": appData["created_at"],
            "id": appData["id"],
            "status": appData["status"],
            "in_maintenance_mode": appData["in_maintenance_mode"],
            "launchpad_display": appData["launchpad_display"],
            "name": appData["name"],
            "url": f"https://cdn.dev.spsc.io/web/xref/ui/{version}/index.html",
            "description": appData["description"],
            "namespace": appData["namespace"],
            "language_list": appData["language_list"],
            "version": version,
            "is_archived": appData["is_archived"],
            "is_service": appData["is_service"],
            "is_public": appData["is_public"],
            "logo": appData["logo"],
            "slug_archive": appData["slug_archive"],
            "language_version": appData["language_version"],
            "maintenance_url": appData["maintenance_url"],
            "slug": appData["slug"],
            "permissions": data["permissions"],
            "publisher_org_id": appData["publisher_org_id"],
            "publisher_user_id": appData["publisher_user_id"],
            "roles": appData["roles"],
            "updated_at": datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%dT%H:%M:%SZ")
        }
        print(f"---------------------------------------URL---------------------------------------\n{url}")
        print(f"---------------------------------------DATA---------------------------------------\n{json.dumps(payload)}")
        r = requests.put(put_url, data=json.dumps(payload), headers=headers).text
        print(f"---------------------------------------RESPONSE---------------------------------------\n{r}")
    elif appData["count"] == 0:
        if "status" not in data:
            data["status"] = "Production"
        if "version" not in data:
            data["version"] = version
        headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json;charset=UTF-8"
        }
        payload = {
            "name": data["name"],
            "namespace": data["namespace"],
            "permissions": data["permissions"],
            "status": data["status"],
            "version": data["version"],
            "url": f"https://cdn.dev.spsc.io/web/xref/ui/{version}/index.html"
        }
        print(f"---------------------------------------URL---------------------------------------\n{url}")
        print(f"---------------------------------------DATA---------------------------------------\n{json.dumps(payload)}")
        r = requests.post(create_url, data=json.dumps(payload), headers=headers).text
        print(f"---------------------------------------RESPONSE---------------------------------------\n{r}")


deploy()
