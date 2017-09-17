import sys

FILE = "cli-count.txt"


def help():
    print """
    cli-count ACTION TAG_NAME VALUE             :: general format
    cli-count new tag_name (start_value)        :: default start_value is 0
    cli-count add tag_name (value)              :: default value is 1
    cli-count total tag_name (start_date)       :: date format: dd.mm.year
    cli-count list (tag_name) (start_date)      :: date format: dd.mm.year
    cli-count help                              :: examples on github
    """


def new(action=None, tag_name=None, value=None):
    """ Create new tag and assign a start value
    """
    status = "New tag created."
    return status


def add(action=None, tag_name=None, value=None):
    """ Add value for given tag
    """
    status = "Tag value added."
    return status


def total(action=None, tag_name=None, value=None):
    """ Show total value for a given tag
    """
    status = "The total is..."
    return status


def list(action=None, tag_name=None, value=None):
    """ List records for a given tag (optional: starting from a given date)
    """
    status = "Listing records..."
    return status


def do_operations(action=None, tag_name=None, value=None):
    """ Redirect to complete an action
    """
    if action == "new":
        status = new(action=action, tag_name=tag_name, value=value)
        print status
    elif action == "add":
        status = add(action=action, tag_name=tag_name, value=value)
        print status
    elif action == "total":
        status = total(action=action, tag_name=tag_name, value=value)
        print status
    elif action == "list":
        status = list(action=action, tag_name=tag_name, value=value)
        print status
    else:
        status = help()
        print status


if __name__ == "__main__":
    """ Check for ACTION, TAG_NAME and VALUE as params
        then do related operations
    """
    try:
        action = sys.argv[1]
    except Exception:
        action = None
    try:
        tag_name = sys.argv[2]
    except Exception:
        tag_name = None
    try:
        value = sys.argv[3]
    except Exception:
        value = None

    do_operations(action=action, tag_name=tag_name, value=value)
