# ec2-meta
A python script to query AWS instance metadata

* To get help use the -h flag eg: python3 ec2-meta.py -h
* By default it shows only the available version for metadata
## To list the metadata available for the particular version:
* use --version <version> eg: python3 ec2-meta.py --version latest &nbsp;&nbsp;(This list out the available metadata for the version)
## To query a particular metadata key:
* use --metadata <metadata> eg: python3 ec2-meta.py --version latest --metadata ami-id &nbsp;&nbsp;(This will query the metadata for particular key you supply)
## For extended query:
* use --metadata <metadata/sub metadata> eg: python3 ec2-meta.py --version latest --metadata ami-id/events &nbsp;&nbsp;(This will query the metadata for particular key you supply)
