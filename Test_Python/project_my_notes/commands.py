from enum import Enum

class Command(Enum):
    ADD_NOTE = 'add_note'
    LIST_NOTES = 'list_notes'
    LIST_NOTES_FILE = 'list_notes_file'
    SAVE_NOTES = 'save_notes'
    DELETE_NOTE = 'delete_note'
    EDIT_NOTE = 'edit_note'
    HELP = 'help'
    EXIT = 'exit'