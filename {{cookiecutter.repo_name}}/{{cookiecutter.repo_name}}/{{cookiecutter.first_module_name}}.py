#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
{{cookiecutter.first_module_name}}.py
{{cookiecutter.description}}

Handles the primary functions
"""

import argparse
import sys
from common_wrangler.common import (GOOD_RET, INPUT_ERROR, INVALID_DATA, InvalidDataError, warning)


def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


def parse_cmdline(argv):
    """
    Returns the parsed argument list and return code.
    :param argv: is a list of arguments, or `None` for ``sys.argv[1:]``.
    """
    if argv is None:
        argv = sys.argv[1:]

    # initialize the parser object:
    parser = argparse.ArgumentParser()
    # parser.add_argument("-i", "--input_rates", help="The location of the input rates file",
    #                     default=DEF_IRATE_FILE, type=read_input_rates)
    parser.add_argument("-n", "--no_attribution", help="Whether to include attribution",
                        action='store_false')
    args = None
    try:
        args = parser.parse_args(argv)
    except SystemExit as e:
        if hasattr(e, 'code') and e.code == 0:
            return args, GOOD_RET
        warning(e)
        parser.print_help()
        return args, INPUT_ERROR

    return args, GOOD_RET


def main(argv=None):
    """
    Runs the main program.
    :param argv: The command line arguments.
    :return: The return code for the program's termination.
    """
    args, ret = parse_cmdline(argv)
    if ret != GOOD_RET or args is None:
        return ret

    try:
        print(canvas(args.no_attribution))
    except InvalidDataError as e:
        warning("Problems reading data:", e)
        return INVALID_DATA

    return GOOD_RET  # success


if __name__ == "__main__":
    status = main()
    sys.exit(status)
