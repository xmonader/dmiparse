# dmiparse
parse dmidecode with python
=======
[![Build Status](https://api.travis-ci.org/xmonader/dmiparse.svg?branch=master)](https://travis-ci.org//xmonader/dmiparse)
[![codecov](https://codecov.io/gh/xmonader/dmiparse/badge.svg)](https://codecov.io/gh//xmonader/dmiparse)


# dmiparse
Convert dmidecode output into clean queryable structure

## Installation
pip3 install dmiparse

## Example
```ipython
In [7]: print(sample1)

# dmidecode 3.1
Getting SMBIOS data from sysfs.
SMBIOS 2.6 present.

Handle 0x0001, DMI type 1, 27 bytes
System Information
		Manufacturer: LENOVO
		Product Name: 20042
		Version: Lenovo G560
		Serial Number: 2677240001087
		UUID: CB3E6A50-A77B-E011-88E9-B870F4165734
		Wake-up Type: Power Switch
		SKU Number: Calpella_CRB
		Family: Intel_Mobile



In [8]: from dmiparse import parse_dmi

In [9]: parse_dmi(sample1)
Out[9]: {'System Information': <dmiparse.Section at 0x7f88b0a5add8>}

In [10]: from json import dumps

In [11]: print(dumps(parse_dmi(sample1), default=lambda o: o.__dict__, indent=4))
{
    "System Information": {
        "props": {
            "Manufacturer": {
                "val": "LENOVO",
                "items": []
            },
            "Product Name": {
                "val": "20042",
                "items": []
            },
            "Version": {
                "val": "Lenovo G560",
                "items": []
            },
            "Serial Number": {
                "val": "2677240001087",
                "items": []
            },
            "UUID": {
                "val": "CB3E6A50-A77B-E011-88E9-B870F4165734",
                "items": []
            },
            "Wake-up Type": {
                "val": "Power Switch",
                "items": []
            },
            "SKU Number": {
                "val": "Calpella_CRB",
                "items": []
            },
            "Family": {
                "val": "Intel_Mobile",
                "items": []
            }
        },
        "title": "System Information",
        "handleline": "Handle 0x0001, DMI type 1, 27 bytes"
    }
}

```

## running tests
`tox` or `pytest`
