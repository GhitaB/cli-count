from datetime import datetime
from datetime import date
import logging
import sys
from cliconfig import FILE
from cliconfig import DEFAULT_UNIT
from cliconfig import DEFAULT_START_VALUE_NEW
from cliconfig import DEFAULT_TOTAL
from cliconfig import DEFAULT_DATE
from cliconfig import log
from cliconfig import ACTION_NEW
from cliconfig import ACTION_ADD
from cliconfig import OPTION_ALL
from cliconfig import OPTION_TODAY
from cliconfig import SEPARATOR
from cliconfig import RESERVED_WORDS
from cliconfig import ERROR_MISSING_DATE_USE_DEFAULT
from cliconfig import ERROR_WRONG_DATE_USE_DEFAULT
from cliconfig import ERROR_MISSING_TAG_NAME
from cliconfig import ERROR_EXISTING_TAG_NAME
from cliconfig import ERROR_WRONG_TAG_NAME
from cliconfig import ERROR_WRONG_VALUE
from cliconfig import ERROR_UNKNOWN_TAG_NAME
from cliconfig import WARNING_RENAME_WITH_EXISTING_TAG_NAME


def help():
    """ Quick help
    """
    print """
cli-count new tag_name (start_value)       > default start_value is 0
cli-count add tag_name (value) ("a story") > default value is 1
cli-count total tag_name (start_date)      > date format: dd.mm.yyyy or today
cli-count list (tag_name) (start_date)     > date format: dd.mm.yyyy or today
cli-count tags (all)                       > show tags (with all info)
cli-count rename tag_name new_tag_name     > rename given tag
    """


def is_valid(tag_name):
    """ Validate a tag name
    """
    if " " in tag_name:
        return False
    if tag_name in RESERVED_WORDS:
        return False
    return True


def write(line):
    """ Append given line to FILE
    """
    with open(FILE, "a") as f:
        f.write(line)


def now():
    """ Return formatted now time. Example: Sun/17.09.2017/09:00:22
    """
    return datetime.now().strftime("%a/%d.%m.%Y/%H:%M:%S")


def get_date(ddmmyyyy=None):
    """ Return date object
    """
    if ddmmyyyy is None:
        log.error(ERROR_MISSING_DATE_USE_DEFAULT)
        ddmmyyyy = DEFAULT_DATE

    parts = ddmmyyyy.split(".")
    try:
        res = date(int(parts[2]), int(parts[1]), int(parts[0]))
    except Exception:
        log.error(ERROR_WRONG_DATE_USE_DEFAULT)
        parts = DEFAULT_DATE.split(".")
        res = date(int(parts[2]), int(parts[1]), int(parts[0]))

    return res


def new(tag_name=None, start_value=None):
    """ Create new tag and assign a start value
    """
    if tag_name is None:
        log.error(ERROR_MISSING_TAG_NAME)
        return

    if tag_name in get_tags():
        log.error(ERROR_EXISTING_TAG_NAME)
        return

    if not is_valid(tag_name):
        log.error(ERROR_WRONG_TAG_NAME)
        return

    if start_value is None:
        start_value = DEFAULT_START_VALUE_NEW

    else:
        try:
            start_value = float(start_value)
        except Exception:
            log.error(ERROR_WRONG_VALUE)
            return

    line = '{} {} {} {} \n'.format(
        now(), ACTION_NEW, tag_name, str(start_value))
    write(line)
    log.info('{} {}'.format(ACTION_NEW, line))


def add(tag_name=None, value=None, story=None):
    """ Add value for given tag
    """
    if value is None:
        value = DEFAULT_UNIT

    if tag_name is None:
        log.error(ERROR_MISSING_TAG_NAME)
        return

    if tag_name not in get_tags():
        log.error(ERROR_UNKNOWN_TAG_NAME)
        return

    try:
        value = float(value)
    except Exception:
        log.error(ERROR_WRONG_VALUE)
        return

    if story is None:
        story = SEPARATOR
    else:
        story = "{}{}".format(SEPARATOR, story)

    line = '{} {} {} {} {} \n'.format(
        now(), ACTION_ADD, tag_name, str(value), story)
    write(line)
    log.info('{} {}'.format(ACTION_ADD, line))


def total(tag_name=None, start_date=None):
    """ Show total value for a given tag
    """
    if tag_name is None:
        log.error(ERROR_MISSING_TAG_NAME)
        return

    if tag_name not in get_tags():
        log.error(ERROR_UNKNOWN_TAG_NAME)
        return

    if start_date is not None:
        if start_date == OPTION_TODAY:
            start_date = get_date(DEFAULT_DATE)
        else:
            start_date = get_date(start_date)

    total = DEFAULT_TOTAL

    with open(FILE, 'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            parts = line.split(" ")
            if parts[2] == tag_name:
                if start_date is not None:
                    if get_date(parts[0].split("/")[1]) >= start_date:
                        print line
                        total += float(parts[3])
                else:
                    print line
                    total += float(parts[3])

    log.info("TOTAL: {}".format(total))


def list(tag_name=None, start_date=None):
    """ List records for a given tag (optional: starting from a given date)
    """
    if tag_name is not None:
        if tag_name not in get_tags():
            log.error(ERROR_UNKNOWN_TAG_NAME)
            return

        if start_date is not None:
            if start_date == OPTION_TODAY:
                start_date = get_date(DEFAULT_DATE)
            else:
                start_date = get_date(start_date)

            with open(FILE, 'r') as f:
                lines = f.read().splitlines()
                for line in lines:
                    parts = line.split(" ")
                    if parts[2] == tag_name:
                        if start_date is not None:
                            if get_date(parts[0].split("/")[1]) >= start_date:
                                print line

        else:
            with open(FILE, 'r') as f:
                lines = f.read().splitlines()
                for line in lines:
                    parts = line.split(" ")
                    if parts[2] == tag_name:
                        print line

    else:
        with open(FILE, 'r') as f:
            lines = f.read().splitlines()
            for line in lines:
                print line


def get_tags():
    """ Return the list of tags
    """
    tags = []

    with open(FILE, 'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            parts = line.split(" ")
            if parts[1] == ACTION_NEW:
                tags.append(parts[2])
    return tags


def tags(option=None):
    """ Show existing tag names.  option: all, for all info
    """
    tags = []
    show_all = True if option == OPTION_ALL else False

    with open(FILE, 'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            parts = line.split(" ")
            if parts[1] == ACTION_NEW:
                if show_all is True:
                    print line
                tags.append(parts[2])
    print tags


def rename(tag_name=None, new_tag_name=None):
    """ Replace tag_name with new_tag_name
    """
    if tag_name is None:
        log.error(ERROR_MISSING_TAG_NAME)
        return

    tags = get_tags()

    if tag_name not in tags:
        log.error(ERROR_UNKNOWN_TAG_NAME)
        return

    if new_tag_name is None:
        log.error(ERROR_MISSING_TAG_NAME)
        return
    else:
        if not is_valid(new_tag_name):
            log.error(ERROR_WRONG_TAG_NAME)
            return

        if new_tag_name in tags:
            log.warning(WARNING_RENAME_WITH_EXISTING_TAG_NAME)

    with open(FILE, 'r+') as f:
        lines = f.read().splitlines()
        new_lines = []
        for line in lines:
            new_line = line
            parts = line.split(" ")
            if parts[2] == tag_name:
                parts[2] = new_tag_name
                new_line = " ".join(parts)
                log.info("Renamed: {}".format(new_line))
            new_lines.append(new_line)

    with open(FILE, 'w') as f:
        f.write("\n".join(new_lines))


def create_file_if_missing():
    """ All records are added in this file. Make sure it exists.
    """
    try:
        f = open(FILE, 'r')
    except IOError:
        f = open(FILE, 'w')

    f.close()


def do_operations(val1=None, val2=None, val3=None, val4=None):
    """ Redirect to complete an action
    """
    if val1 == "new":
        new(tag_name=val2, start_value=val3)
    elif val1 == "add":
        add(tag_name=val2, value=val3, story=val4)
    elif val1 == "total":
        total(tag_name=val2, start_date=val3)
    elif val1 == "list":
        list(tag_name=val2, start_date=val3)
    elif val1 == "tags":
        tags(option=val2)
    elif val1 == "rename":
        rename(tag_name=val2, new_tag_name=val3)
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
    """ Check for ACTION, TAG_NAME and VALUE as vals
        then do related operations
    """
    try:
        val1 = sys.argv[1]
    except Exception:
        val1 = None
    try:
        val2 = sys.argv[2]
    except Exception:
        val2 = None
    try:
        val3 = sys.argv[3]
    except Exception:
        val3 = None
    try:
        val4 = sys.argv[4]
    except Exception:
        val4 = None

    init()
    do_operations(val1=val1, val2=val2, val3=val3, val4=val4)
