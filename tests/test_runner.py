'''
Created on Nov 7, 2014

__author__ = rpiazza, bschmoker, gtback
__copyright__ = MITRE Corp
__version__ = 0.1
'''

from os.path import abspath, dirname
import sys
import glob

from sdv.errors import ValidationError
from sdv.validators import STIXSchemaValidator


def main():

    # this script lives under $repo/tests , so our schema lives in the parent dir
    validator = STIXSchemaValidator(dirname(abspath('../')))

#  grab all files under tests/ and subfolders

    testfiles = glob.glob("tests/*/*xml") 
    
# check valid-ness of each file 
    errors = 0
    
    for testfile in testfiles:
        try:
            validator_results = validator.validate(testfile)
    
        except ValidationError as ex:
            errors += 1
            print "ValidationError: %s - %s" % (ex, testfile)

    print '.'

    if errors:
        return 1


if __name__ == '__main__':
    sys.exit(main())
