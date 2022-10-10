#!/usr/bin/python

def safe_function(fct,*args):
    try:
      return fct(*args)
    except BaseException as re:
        print("Exception: {}".format(re.args[0]))
        return None