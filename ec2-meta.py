#!/usr/bin/python3

import requests;
import argparse;
import json

url = "http://169.254.169.254/"

def convert_to_json(result):
    res = result;

    if isinstance(res, str):
        res = res.split()

    print(res)



def query(version=None, metadata=None):
    global url

    if version is None:
        result = requests.get(url)

        if result.ok:
            convert_to_json(result.text);

        else:
            print("[*] plz set --version. eg: python3 ec2-meta.py --version latest")
    else:
        url += "{}/meta-data".format(version)

        if metadata is not None:
            url += "/{}".format(metadata)

        result = requests.get(url)

        if result.ok:

            try:
                tmp_res = result.json();
                convert_to_json(tmp_res)
            except:
                convert_to_json(result.text)
        elif result.status_code == 404:
            print("[*] 404 not found!. invalid url")
        else:
            print("[*] error: run the code from your ec2 instance")

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', help = "set version to get the metadata. eg: --version latest")
    parser.add_argument('-m', '--metadata', help = "set metadata to get the metadata. eg: --metadata ami")

    args = parser.parse_args()

    query(args.version, args.metadata);

