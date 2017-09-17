from datetime import datetime
import logging
import sys

FILE = "cli-count.txt"
UNIT = 1
log = logging.getLogger('cli-count')


def help():
    print """
    cli-count ACTION TAG_NAME VALUE             :: general format
    cli-count new tag_name (start_value)        :: default start_value is 0
    cli-count add tag_name (value)              :: default value is 1
    cli-count total tag_name (start_date)       :: date format: dd.mm.year
    cli-count list (tag_name) (start_date)      :: date format: dd.mm.year
    cli-count help                              :: examples on github
    """


def now():
    """ Return formatted now time. Example: Sun/17.09.2017/09:00:22
    """
    return datetime.now().strftime("%a/%d.%m.%Y/%H:%M:%S")


def new(action=None, tag_name=None, start_value=None):
    """ Create new tag and assign a start value
    """
    log.info("Tag %s created." % tag_name)


def add(action=None, tag_name=None, value=None):
    """ Add value for given tag
    """
    if value is None:
        value = UNIT
    if tag_name is None:
        log.error("Missing tag name.")
        return

    # [TODO] Check if tag exist or it must be created.

    line = now() + " " + tag_name + " " + str(value) + "\n"
    with open(FILE, "a") as f:
        f.write(line)
    log.info("Added %s" % line)


def total(action=None, tag_name=None, start_date=None):
    """ Show total value for a given tag
    """
    log.info("The total is...")


def list(action=None, tag_name=None, start_date=None):
    """ List records for a given tag (optional: starting from a given date)
    """
    log.info("Listing records...")
    if tag_name is not None:
        log.warning("[TODO] Implement tag filter.")
    if start_date is not None:
        log.warning("[TODO] Implement date filter.")
    with open(FILE, 'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            print line


def create_file_if_missing():
    """ All records are added in this file. Make sure it exists.
    """
    try:
        f = open(FILE, 'r')
    except IOError:
        log.warning("Missing %s file." % FILE)
        f = open(FILE, 'w')
        log.info("Created %s file used to store everything." % FILE)

    f.close()


def do_operations(action=None, tag_name=None, value=None):
    """ Redirect to complete an action
    """
    if action == "new":
        new(action=action, tag_name=tag_name, start_value=value)
    elif action == "add":
        add(action=action, tag_name=tag_name, value=value)
    elif action == "total":
        total(action=action, tag_name=tag_name, start_date=value)
    elif action == "list":
        list(action=action, tag_name=tag_name, start_date=value)
    else:
        help()


def set_log():
    """ Settings related to logging
    """
    log.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    log.addHandler(ch)


def init():
    """ Initialize first.
    """
    set_log()
    create_file_if_missing()


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

    init()
    do_operations(action=action, tag_name=tag_name, value=value)
