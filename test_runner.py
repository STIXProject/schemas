'''
Created on Nov 7, 2014

@author: rpiazza
'''

import argparse
from os.path import abspath, dirname
import sys

from sdv.errors import ValidationError
from sdv.validators import STIXSchemaValidator


class ArgumentError(Exception):
    """An exception to be raised when invalid or incompatible arguments are
    passed into the application via the command line.

    Args:
        show_help (bool): If true, the help/usage information should be printed
            to the screen.

    Attributes:
        show_help (bool): If true, the help/usage information should be printed
            to the screen.

    """
    def __init__(self, msg=None, show_help=False):
        super(ArgumentError, self).__init__(msg)
        self.show_help = show_help


def _validate_args(args):
    """Checks that valid and compatible command line arguments were passed into
    the application.

    Args:
        args (argparse.Namespace): The arguments parsed and returned from
            ArgumentParser.parse_args().

    Raises:
        ArgumentError: If invalid or incompatible command line arguments were
            passed into the application.

    """

    if len(sys.argv) == 1:
        raise ArgumentError("Invalid arguments", show_help=True)

    if (args.LIST_FILE is None):
        raise ArgumentError("No test case list file given", show_help=True)


def _get_arg_parser():
    """Initializes and returns an argparse.ArgumentParser instance for this
    application.

    Returns:
        Instance of ``argparse.ArgumentParser``

    """
    parser = argparse.ArgumentParser(
        description="STIX Regression Tester v%s" % "0.1"
    )

    parser.add_argument(
        "--verbose",
        dest="verbose",
        action="store_true",
        default=False,
        help="More detailed output."
    )

    parser.add_argument(
        "--test-case-repository",
        dest="test_case_repository",
        default=None,
        help="Directory to prepend to all listed test case file paths"
    )

    parser.add_argument(
        "LIST_FILE",
        help="A file containing the list of STIX files to validate."
    )

    return parser


def main():
    parser = _get_arg_parser()
    args = parser.parse_args()

    try:
        # Validate the input command line arguments
        _validate_args(args)
    except ArgumentError as ex:
        if ex.show_help:
            parser.print_help()
        print ex
        return 1

    # This test script should be in the root directory of the schema
    # repository.
    schema_dir = dirname(abspath(__file__))
    validator = STIXSchemaValidator(schema_dir)

    with open(args.LIST_FILE, 'r') as testCaseListFile:
        numTestCases = 0
        numPosTestCasesFail = 0
        numNegTestCasesFail = 0
        errors = 0

        for line in testCaseListFile:
            line = line.strip()
            # Allow premature exiting of test manifest. This makes testing one
            # or two test cases much quicker (though the "--end--" should be
            # removed before committing).
            if line == "--end--":
                break
            if line.startswith("#"):
                continue
            testCaseFileName, posOrNeg = [x.strip() for x in line.split(',')]
            if args.test_case_repository is not None:
                testCaseFileName = args.test_case_repository + "/" + testCaseFileName
            if args.verbose:
                print "-" * 64
                print testCaseFileName
            numTestCases += 1
            try:
                validator_results = validator.validate(testCaseFileName)

                if posOrNeg == "pos" and not validator_results.is_valid:
                    numPosTestCasesFail += 1
                    print "FAIL - didn't pass positive case " + testCaseFileName
                    for e in validator_results.errors:
                        print e
                elif posOrNeg == "neg" and validator_results.is_valid:
                    numNegTestCasesFail += 1
                    print "FAIL - passed negative case " + testCaseFileName
                elif not posOrNeg == "neg" and not posOrNeg == "pos":
                    errors += 1
                    print "FAIL case not supported " + posOrNeg
            except ValidationError as ex:
                errors += 1
                print "ValidationError: %s - %s" % (ex, testCaseFileName)

    totalNumFailed = numPosTestCasesFail + numNegTestCasesFail + errors

    print "Total: " + str(numTestCases)
    print "Failed: " + str(totalNumFailed)

    if totalNumFailed:
        return 1


if __name__ == '__main__':
    sys.exit(main())
