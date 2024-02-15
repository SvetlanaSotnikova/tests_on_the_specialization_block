from fileinput import filename
import json
from datetime import datetime as dt


def add_note(notes):
    title = input('\nВведите заголовок заметки >> ')
    body = input('Введите текст заметки >> ')
    timestamp = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        "id": len(notes) + 1,
        "title" : title,
        "body": body,
        "time": timestamp
    }
    notes.append(note)


def list_notes(notes):
    if not notes:
        print("Список пуст :(")
    else:
        sort_notes = sorted(notes, key=lambda x: x['time'])
        print("\nСписок заметок:")
        for idx, note in enumerate(sort_notes, start=1):
            print(f"Заметка N{idx}")
            print(f"Заголок: {note['title']}")
            print(f"Текст: {note['body']}")
            print(f"Время записи: {note['time']}")
            print()


def list_notes_file(file_name):
    try:
        with open(file_name, "r") as f:
            notes = json.load(f)
            if not notes:
                print("\nСписок заметок из файла пуст :(")
            else:
                sort_notes = sorted(notes, key=lambda x: x['time'])
                print("\nСписок заметок из файла:")
                for idx, note in enumerate(sort_notes, start=1):
                    print(f"Заметка N{idx}")
                    print(f"Заголовок: {note['title']}")
                    print(f"Текст: {note['body']}")
                    print(f"Время записи: {note['time']}")
                    print()
    except FileNotFoundError:
        print(f"\nФайл {file_name} не найден.")
    except Exception as e:
        print(f"\nПроизошла ошибка при чтении файла: {e}")


def save_notes(notes, file_name):
    try:
        with open(file_name, "w") as f:
            json.dump(notes, f, indent=4)
        print(f"\nЗаметки успешно сохранены в файле {file_name}")
    except Exception as e:
        print("Ошибочка:", e)


def delete_note(notes, file_name):
    note_id = int(input("\nВведите id заметки для удаления >> "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes, file_name)
            print("Заметка удалена успешно :D")
            return
    print(f"Заметка с id={note_id} не найдена :(")
    

def edit_note(notes, file_name):
    note_id = int(input("\nВведите id заметки для удаления >> "))
    for note in notes:
        if note['id'] == note_id:   
            print("\nоставьте пустым, чтобы оставить без изменений")  
            new_title = input("Введите новый заголовок заметки >> ")
            new_body = input("Введите новый текст заметки >> ")
            if new_title:
                note['title'] = new_title
            if new_body:
                note['body'] = new_body
            note['time'] = dt.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes, file_name)
            print("\nЗаметка успешно отредактирована :D")
            return
    print(f"\nЗаметка с id={note_id} не найдена :(")


def print_commands():
    print('command >> add_note -- добавить заметку')
    print('command >> list_notes -- вывод заметок на экран из буфера')
    print('command >> list_note_file -- вывод заметок на экран из файла')
    print('command >> save_notes -- сохраение заметок в файл notes.json')
    print('command >> delete_note -- удаление заметки')
    print('command >> edit_note -- редактирование заметки')
    print('command >> exit -- выход из программы')