import os 
import json
import shutil
from subprocess import PIPE, run
import sys 

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("You must pass a source and target directory - only")




