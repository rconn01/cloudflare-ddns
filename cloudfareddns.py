import CloudFlare
import requests
import argparse
import sys



def get_public_ip():
    resp=requests.get("https://checkip.amazonaws.com")
    resp.raise_for_status()
    return resp.text.strip()



def check_record(zone_name, dns_record_name):
    ip=get_public_ip()

    print("Public ip is: " + ip)


    cf = CloudFlare.CloudFlare()

    zones = cf.zones.get(params = {'name':zone_name,'per_page':1})
    zone = zones[0]
    zone_id = zone['id']

    dns_records = cf.zones.dns_records.get(zone_id)
    record=None
    for dns_record in dns_records:
        if dns_record['name'] == dns_record_name:
            record=dns_record
            break

    if record is None:
        print("Failed to find dns record: " + dns_record_name)
        sys.exit(1)
    
    content=record['content']
    if content==ip:
        print("Record is correct, no need to update")
    else:
        print("Current record is: " + content + " updating record to: " + ip)
        record['content']=ip
        cf.zones.dns_records.put(zone_id, record['id'], data=dns_record)
        print("Update complete")

def main():
    parser = argparse.ArgumentParser(description='Dynamically update a cloudflare A record to the public ip of the host running the script')
    parser.add_argument('--zone-name', required=True, help='The zone name to update')
    parser.add_argument('--record-name', required=True, help='The FQDN of the record to update')
    args = parser.parse_args()
    check_record(args.zone_name, args.record_name)    



if __name__ == '__main__':
    main()