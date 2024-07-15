import dns.resolver as resolver
import dns.exception as exception
from sys import argv

script,domain = argv

try:
    mx_record = resolver.resolve(domain,"MX")
    for record in mx_record :
        print(f"MX RECORD: {record} with priority: {record.preference}")

        #query A record for the mx host
        a_records = resolver.resolve(record.exchange,"A")
        for a_record in a_records :
            print(f"A RECORD : {a_record.address}")

except resolver.NoAnswer:
    print("no mx record found")
except resolver.NXDOMAIN:
    print("domain name does not exist")
except exception.Timeout:
    print("Query timed out")
except Exception as e:
    print("error occured : {e}")