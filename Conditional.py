def main():
    required_service = "Lambdak"

    if required_service == 'file storage':
        aws_service = "s3"
    elif required_service == 'compute':
        aws_service = 'ec2'
    elif required_service == 'database':
        aws_service = 'RDS'
    elif required_service == 'Lambda':
        aws_service =" serverless"
    else :
        aws_service = 'unknown'
    

    if required_service != 'unknown':
         print (f" The required stuff: {aws_service}")
    else:
        print(f" Error: {aws_service}")

   # weather = 'cold'

    #if weather == 'cold':
     # drink = " Hot cofee"
    #else:
     #drink = "Cold Cofee"

    #print(f"what cofee would you like to have?: {drink}")













if __name__ == '__main__':
    main()