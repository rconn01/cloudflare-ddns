# cloudflare-dynamic dns

Simple python script that dynamically updates a cloudflare A record to the public IP of the host running the script.
This script will not create a new record and expects an existing record to exist.
The intention is to run this script in a cron tab so a record stays up to date

## Usage
The script requires [python-cloudflare](https://github.com/cloudflare/python-cloudflare#installation).

```
usage: cloudfareddns.py [-h] --zone-name ZONE_NAME --record-name RECORD_NAME

Dynamically update a cloudflare A record to the public ip of the host running the script

options:
  -h, --help            show this help message and exit
  --zone-name ZONE_NAME
                        The zone name to update
  --record-name RECORD_NAME
                        The FQDN of the record to update
 ```

 Sample:

 ```
 cloudfareddns.py --zone-name mydomain.com --record-name awesome.mydomain.com
 ```

 This sample will update the A record of `awesome.mydomain.com` to match the public ip of the host running the script

 ## Cloudflare auth
You need to provide a setup of cloudflare credientals that have permission to the `zone-name` you are looking to update.
You can use the ENV vars or config file that are documented [here](https://github.com/cloudflare/python-cloudflare#providing-cloudflare-username-and-api-key)

The most straight forward is to create an api token and export that `export CLOUDFLARE_API_TOKEN=<token>` 