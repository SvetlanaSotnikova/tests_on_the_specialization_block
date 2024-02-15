import functions as funct
from commands import Command as com
import sys

def main():
    notes = []
    file_name = 'notes.json'

    funct.print_commands()
    while True:
        user_input = input("\ncommand >> ").lower().split()

        # try:
        #     user_input = sys.argv[1]
        # except IndexError:
        #     print('command must be entered >> help')
        # else:
        if user_input:
            command = user_input[0]
            if command == com.ADD_NOTE.value:
                funct.add_note(notes)
            elif command == com.LIST_NOTES.value:
                funct.list_notes(notes)
            elif command == com.LIST_NOTES_FILE.value:
                funct.list_notes_file(file_name)
            elif command == com.SAVE_NOTES.value:
                funct.save_notes(notes, file_name)
            elif command == com.DELETE_NOTE.value:
                funct.delete_note(notes, file_name)
            elif command == com.EDIT_NOTE.value:
                funct.edit_note(notes, file_name)
            elif command == com.HELP.value:
                funct.print_commands()
            elif command == com.EXIT.value:
                print("До встречи :D")
                break
            else:
                print("\nType 'help' to see available commands")
        else:
            print('\ncommand must be entered >> help')


if __name__ == '__main__':
    main()