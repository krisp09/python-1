def main():
#Dictionaries
 aws_services = {
    's3' : "Storage Services",
    'ec2' : "Compute Services",
    'RDS' : "Database Services",
    'IAM' : "Identity Services"

 }

 aws_services['ec2'] = {
    'type ' : "t2 medicume",
    'description' : "type of ec2 service"
 }

 print(f"Data from aws_services: {aws_services}")
 print(f"data one by one : {aws_services['ec2']}")
 print(f"\n print data by Keys : {aws_services.keys()}")
 print(f"print data by Keys : {aws_services.values()}")
 print(f"print data by Keys : {aws_services.items()}")

 print(f"\n Nested Strcture: {aws_services['ec2']}")











if __name__ == "__main__":
    main()