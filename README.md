# SecNet Challenge

CloudFormation template to stand up a secure web server using a self signed certificate. 

## Requirements

- [x] Create and deploy a running instance of a web server using a configuration management tool of your choice. 
- [x] The web server should serve one page with the following content:
 ```html 
<html>
    <head>
        <title>We are SecNet!</title>
    </head>
    <body>
        <h1>We are SecNet!</h1>
    </body>
</html>
```
- [x] Secure this application and host such that only appropriate ports are publicly exposed and any http
requests are redirected to https. This should be automated using a configuration management tool of your choice and you should feel free to use a self-signed certificate for the web server.
- [x] Develop and apply automated tests to validate the correctness of the server configuration.
Express everything in code
- [x] Provide your code in an https://github.com repo named <YOUR_FIRSTNAME>_Challenge

## Solution
For this challenge CloudFormation was selected as the IaC management tool. The roll back capability CloudFormation offers will be helpful when performing automated smoke tests. In the template an Apache web server is stood up running on an Amazon Linux AMI. The template uses Mappings to automatically pull in the correct AMI Id for different US regions. Amazon Linux is selected because it comes with AWS agents and cli tools pre-installed. The stack will deploy into the default VPC, has 3 AZs to work with, and uses a default instance type t3.small with a fall back choice of t3a.small. A fall back choice ensures a greater pool of capacity is available. The web server sits in an ASG that utilizes a mix of Spot and On-Demand instances. This stateless application is a good fit for Spot usage. A security group is created to allow open access for Apache and SSH via an IP using a /32 bit mask. Apache has a self signed certificate and is setup to redirect HTTP to HTTPS. 

## Validation
An automated validation test is applied in the UserData section. There are two while loops that curl using HTTPS and HTTP to the index.html file. It checks every 5 seconds until a 200 success code for HTTPS and a 301 redirection code for HTTP are returned. If not received within 3 minutes the creation policy will timeout and automatically roll back the changes and signal failure. A final check is performed to look for the words "We are SecNet!" in the index.html file. If successful, we know Apache is running, that the index.html file has been created, and that redirection from HTTP to HTTPS is working. Once CloudFormation receives a success signal the deployment then completes. 

## Notes
To work around the lack of a domain with a self-signed certificate. An existing IAM role is attached to the instance to provide permission to associate an EIP. This allows a predictable IP to be applied to the virtual host configuration in httpd.conf. This enables Apache to handle HTTP to HTTPS redirection. In the original iteration iptables were used to perform that function. While it worked, it also resulted in an error from Apache when connecting to port 80 using HTTP since it was unaware of the redirection. 

```html
<VirtualHost *:80> 
    DocumentRoot "/var/www/html"
    ServerName "18.190.x.x"
    ServerAlias "18.190.x.x"
    Redirect permanent / https://18.190.x.x/
</VirtualHost>
```

## Future Scaling
To scale this application you would associate the ASG with a target group and place it behind an Elastic Load Balancer. Then utilize CloudWatch advanced tracking metrics such as Target Request Count to distribute incoming requests to individual targets. 
 
## Deployment

Use the AWS console or [AWS](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html#cliv2-linux-install) CLI to deploy template.

## Dependencies
You will need to allocate an EIP and pass in the allocation Id and Ip address as stack parameters. Also, the name of an existing IAM role with the below permissions must be passed in as a parameter. 

In the real world we would have a FQDN that would resolve to an IP using DNS. 

e.g.
```text
 "Statement": [
     {
         "Effect": "Allow",
         "Action": [
             "ec2:DescribeInstances",
             "ec2:AssociateAddress",
             "ec2:DescribeAddresses",
             "ec2:AllocateAddress"
         ],
         "Resource": "*"                            
     }
 ]
```
## Usage

```bash
aws cloudformation create-stack --stack-name MyStack --template-body file://file.json --parameters \
ParameterKey=KeyName,ParameterValue=<your_key> \
ParameterKey=Subnets,ParameterValue=subnet-xxxxxxxx\\,subnet-xxxxxxxx\\,subnet-xxxxxxxx \
ParameterKey=VpcId,ParameterValue=vpc-xxxxxxxx \
ParameterKey=SSHLocation,ParameterValue=x.x.x.x/32 
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
