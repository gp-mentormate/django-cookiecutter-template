# The `helpers.py` file is commonly used to store helper functions
# that provide utility or reusable functionality throughout the application.
# In our project, we have chosen to use the filename `helpers.py`
# instead of `utils.py`.

def strtobool(val: str) -> bool:
    """
    Convert a string representation of truth to True or False.
    True values are 'y', 'yes', 't', 'true', 'on', and '1'; false values
    are 'n', 'no', 'f', 'false', 'off', and '0'.  Raises ValueError if
    'val' is anything else.
    """

    val = val.lower()
    if val in ('y', 'yes', 't', 'true', 'on', '1'):
        return True
    elif val in ('n', 'no', 'f', 'false', 'off', '0'):
        return False
    else:
        raise ValueError(f"invalid truth value {val}")
