# SecNet Challenge

CloudFormation template to stand up a secure web server using a self signed certificate. 

## Deployment

Use the AWS console or [AWS](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html#cliv2-linux-install) CLI to deploy template.

## Usage Example

```bash
aws cloudformation create-stack --stack-name MyStack --template-body file://your_template.json --parameters \
ParameterKey=KeyName,ParameterValue=<your_key> \
ParameterKey=Subnets,ParameterValue=subnet-xxxxxxxx\\,subnet-xxxxxxxx\\,subnet-xxxxxxxx \
ParameterKey=VpcId,ParameterValue=vpc-xxxxxxxx \
ParameterKey=SSHLocation,ParameterValue=x.x.x.x/x
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
