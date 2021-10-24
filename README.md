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
- [x] Develop and apply autoamted tests to validate the correctness of the server configuration.
Express everything in code
- [x] Provide your code in an https://github.com repo named <YOUR_FIRSTNAME>_Challenge

## Deployment


Use the AWS console or [AWS](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html#cliv2-linux-install) CLI to deploy template.

## Usage

```bash
aws cloudformation create-stack --stack-name MyStack --template-body file://your_template.json --parameters \
ParameterKey=KeyName,ParameterValue=<your_key> \
ParameterKey=Subnets,ParameterValue=subnet-xxxxxxxx\\,subnet-xxxxxxxx\\,subnet-xxxxxxxx \
ParameterKey=VpcId,ParameterValue=vpc-xxxxxxxx
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
