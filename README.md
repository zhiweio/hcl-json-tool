# hcl-json-tool
Tool for conversion between HCL and JSON

## Usage

Build

```shell
$ go mod init json2hcl
$ go get github.com/hashicorp/hcl/v2/hclwrite
$ go get github.com/hashicorp/hcl/v2
$ go build
```

Run

```shell
$ ./json2hcl test.json output.tf
```

Install 
```shell
$ python3 -m pip install python-hcl2
```

Run
```shell
$ python3 json2tfvars.py test.json output.tfvars
```
