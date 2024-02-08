#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as e:
        error_message = "Exception: {}\n".format(e)
        sys.stderr.write(error_message)
        return None
