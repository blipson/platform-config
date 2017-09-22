# Platform Config
A Python command line utility for deploying front end applications to Commerce Platform.

# Setup
Change the bdp.json file to look like the following example:
```
{
  "name": "Your Application's Name",
  "namespace": "your-apps-namespace",
  "permissions": [{
    "internal": true, // false if you want your app to be visible to the outside world
    "name": "your-role-name",
    "display_name": "role-display-name",
    "description": "Your role's description"
  }],
  "unit": "your-apps-unit",
  "product": "your-apps-product",
  "subproduct": "your-apps-subproduct"
}
```

# Usage
```
python3 deploy.py
```
You'll be asked for the environment you're deploying to, the version you want to deploy, and your user password.

It'll only work if your user has permission to the application endpoint in identity service
