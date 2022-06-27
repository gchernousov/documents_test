documents = [
  {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
  {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
  {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
  {"type": "insurance", "number": "10855", "name": "Альберт Дроздов"},
  {"type": "invoice", "number": "15-3", "name": "Елизавета Полякова"},
  {"type": "passport", "number": "2705 621552", "name": "Анна Самойлова"},
  {"type": "passport", "number": "2512 915613", "name": "Ярослав Одинцов"},
  {"type": "paper", "number": "12", "name": "Иван Иванов"}
      ]

directories = {
  '1': ['2207 876234', '11-2', '2705 621552'],
  '2': ['10006', '15-3', '10855'],
  '3': ['2512 915613'],
  '4': []
      }


def people(number_doc: str, documents):
  """Функция для поиска человека по номеру документа"""
  result = ""
  for value in documents:
    if number_doc == value['number']:
      result = value['name']
      break
    else:
      result = 'not_found'
  return result


def show_shelf(number: str, directories):
  """Функция для поиска полки, на которой лежит искомый документ"""
  result = False
  result_id = ""
  for id_, shelf in enumerate(directories.values(), 1):
    for doc in shelf:
      if number == doc:
        result = True
        result_id = id_
        break
  if result == False:
    return result
  else:
    return result_id


def show_list(documents):
  """Функция, которая выводит список всех документов"""
  for doc in documents:
    print(f'{doc["type"]} "{doc["number"]}" "{doc["name"]}"')


def add_doc_on_shelf(new_number: str, directories):
  """Функция добавления документа на полку"""
  adding_on_shelf = False
  move_on_shelf = input('\nНа какую полку поместить ваш документ?: ')
  while adding_on_shelf == False:
    if move_on_shelf in directories.keys():
      directories[move_on_shelf].append(new_number)
      adding_on_shelf = True
    else:
      print(f'Извините, но такой полки нет')
  else:
    return move_on_shelf


def add_doc(documents, directories):
  """Функция добавления нового документа в базу документов"""
  new_type = input('\nВведите тип документа (passport, invoice, insurance, etc.): ')
  new_number = input('Введите номер документа: ')
  new_name = input('Введите имя и фамилию владельца документа: ')
  documents.append({'type': new_type, 'number': new_number, 'name': new_name})
  shelf_number = add_doc_on_shelf(new_number, directories)
  result = f'Вы добавили: {new_type} "{new_number}" {new_name} на {shelf_number} полку'
  return result


def delete_doc(number: str, documents, directories):
  """Функция удаления документа из базы и с полки"""
  del_this_doc = ""
  for document in documents:
    if number == document['number']:
      del_this_doc = document
      break
    else:
      del_this_doc = 'not_found'
  if del_this_doc == 'not_found':
    return 'Документ не найден'
  else:
    documents.remove(del_this_doc)
    for shelf in directories.values():
      for doc in shelf:
        if number == doc:
          shelf.remove(doc)
  return f'Документ с номером "{number}" успешно удален'


def move_document(doc_number: str, directories):
  """Функция для перемещения документа с одной полки на другую"""
  result_show_shelf = show_shelf(doc_number, directories)
  if result_show_shelf != False:
    directories[str(result_show_shelf)].remove(doc_number)
    new_shelf = add_doc_on_shelf(doc_number, directories)
    return f'Документ успешно перемещен с {result_show_shelf} на {new_shelf} полку'
  else:
    return 'Документ не найден'


def add_new_shelf(new_shelf, directories):
  """Функция для добавления новой полки"""
  if new_shelf in directories.keys():
    return 'Такая полка уже есть'
  else:
    directories[new_shelf] = []
    return f'Полка {new_shelf} успешно добавлена'

def start_program():
  print("""Добрый день!\n
          Список рабочих команд:\n
          p  - Узнать имя человека, которому принадлежит документ
          s  - Узнать номер полки, на которой находится документ
          l  - Вывести список всех документов
          a  - Добавить новый документ в каталог
          d  - Удалить документ из каталога
          m  - Переместить документ с одной полки на другую
          as - Добавить новую полку
          q  - Выйти
          """)

  run_program = True
  while run_program == True:
    command = input('\nЧто вы хотите сделать?: ')
    if command == 'p':
      search = input('Введите номер документа для поиска: ')
      result = people(search, documents)
      if result == 'not_found':
        print('Документ не найден')
      else:
        print(f'Владелец документа: {result}')
    elif command == 's':
      search = input('Введите номер документа для поиска: ')
      result = show_shelf(search, directories)
      if result == False:
        print("Документ не найден")
      else:
        print(f'Ваш документ на {result} полке')
    elif command == 'l':
      print('Доступные документы:\n')
      show_list(documents)
    elif command == 'a':
      print('\nВы хотите добавить документ')
      result = add_doc(documents, directories)
      print(result)
    elif command == 'd':
      search = input('Введите номер документа, который вы хотите удалить: ')
      delete_doc(search, documents, directories)
    elif command == 'm':
      doc_number = input('Введите номер документа, который хотите переместить: ')
      result = move_document(doc_number, directories)
      print(result)
    elif command == 'as':
      new_shelf = input('Введите номер новой полки: ')
      result = add_new_shelf(new_shelf, directories)
      print(result)
    elif command == 'q':
      run_program = False
    else:
      print('Такой команды нет. Попробуйте еще раз.')
  else:
    print('До свидания!')


if __name__ == "__main__":

  start_program()