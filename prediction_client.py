#!/usr/bin/env python3
import sys

def check_arguments():
    if len(sys.argv) != 3:
      print("""
        Prediction API client

        Usage:
        {} <input file> <api host>
      """.format(sys.argv[0]))
      sys.exit(1)

def execute_client():
    check_arguments()
    

if __name__ == '__main__':
    execute_client()

