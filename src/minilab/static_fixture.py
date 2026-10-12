"""Static-analysis fixture.

Every finding below is planted. Nothing here is imported or executed, and the
file is left out of the coverage measure (see pyproject.toml). Do not "fix" it:
a clean report against this file means the tool did not look.
"""
import hashlib
import json          # unused import
import subprocess

DB_PASSWORD = "hunter2-prod-primary"         # hardcoded secret


def BadName(value, bucket=[]):               # bad name, mutable default
    unused_local = value * 2                 # unused variable
    bucket.append(value)
    return bucket


def swallow(path):
    try:
        with open(path) as handle:
            return handle.read()
    except:                                  # bare except
        pass
    return None


def run_report(name):
    return subprocess.check_output("cat /var/reports/" + name, shell=True)   # shell injection


def evaluate(expression):
    return eval(expression)                  # arbitrary code execution


def checksum(payload):
    return hashlib.md5(payload.encode("utf-8")).hexdigest()                  # weak hash


def never_called(value):                     # dead code
    return value * 2
    return value * 3                         # unreachable


def classify(weight, region, hazardous, express, zone):
    """Deliberately over a cyclomatic-complexity limit of 10."""
    band = "parcel"
    if weight <= 0:
        return "invalid"
    if hazardous:
        if region == "EU":
            if weight > 30:
                band = "haz-heavy-eu"
            elif weight > 5:
                band = "haz-mid-eu"
            else:
                band = "haz-light-eu"
        elif region == "US":
            if zone in (7, 8, 9):
                band = "haz-remote-us"
            elif weight > 20:
                band = "haz-heavy-us"
            else:
                band = "haz-std-us"
        else:
            band = "haz-intl"
    elif express:
        band = "express"
    elif weight > 50:
        band = "freight"
    elif weight > 10:
        band = "parcel-heavy"
    if zone > 6 and band != "freight":
        band += "-remote"
    return band
