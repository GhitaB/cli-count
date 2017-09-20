""" Configuration, settings
"""
from datetime import datetime
import logging

FILE = "cli-count.txt"
DEFAULT_UNIT = 1
DEFAULT_START_VALUE_NEW = 0
DEFAULT_TOTAL = 0
DEFAULT_DATE = datetime.now().strftime("%d.%m.%Y")
log = logging.getLogger('cli-count')
ACTION_NEW = "new"
ACTION_ADD = "add"
ACTION_TOTAL = "total"
ACTION_LIST = "list"
OPTION_ALL = "all"
OPTION_TODAY = "today"
SEPARATOR = "@@"
RESERVED_WORDS = ['today', 'all']

ERROR_MISSING_DATE_USE_DEFAULT = "Missing date. {} will be used.".format(
    DEFAULT_DATE)
ERROR_WRONG_DATE_USE_DEFAULT = "Wrong date. {} will be used.".format(
    DEFAULT_DATE)
ERROR_MISSING_TAG_NAME = "Missing tag name."
ERROR_EXISTING_TAG_NAME = "Tag name already exists."
ERROR_WRONG_TAG_NAME = "Invalid tag name. Don't use spaces or reserved words ("
"{}).".format(", ".join(RESERVED_WORDS))
ERROR_WRONG_VALUE = "Wrong value."
ERROR_UNKNOWN_TAG_NAME = "Unknown tag name."
WARNING_RENAME_WITH_EXISTING_TAG_NAME = """ New tag is an existing one. Manual
action needed. Open the file and make sure you have a single 'new' action for
this tag. Maybe ok: rename second one to 'add'. Make sure the total value
is correct."""
