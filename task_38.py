# Задача 38: 
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал для изменения и удаления данных

def data_entry():
    with open("telephone_directory.csv","a", encoding="utf-8") as data:
        data.write("\n")
        inf=input("Введите ФИО: ")
        data.write(inf)
        data.write("-")
        inf=input("Введите телефон: ")
        data.write(inf+"\n")
        data.close()
        menu()


def search():
    with open("telephone_directory.csv", encoding="utf-8") as fin:
        obiekt=input("Введите что ищем: ")
        for line in fin.readlines():
            if obiekt in line:
                print(line,end="")
    menu()
                
    

def poiski():
    with open("telephone_directory.csv", encoding="utf-8") as fin:
        obiekt=input("Введите что ищем: ")
        for (num,line) in enumerate(fin,1):
            if obiekt in line:
                print(num)
                line=000
    menu()

def read_all_entries():
    with open("telephone_directory.csv","r", encoding="utf-8") as fin:               
        for line in fin.readlines():
            print(line,end="")
    fin.close()
    menu()


def deleting_a_file():
 with open("telephone_directory.csv", 'r', encoding="utf-8") as fin:
        X = input('Введите имя или фамилию для удаления: ')
        lines = fin.readlines()
        with open("telephone_directory.csv", 'w', encoding="utf-8") as fin:
            for line in lines:
                if X in line:
                    print('Указанные данные удалены')
                else:
                    print(line)    
                    fin.write(line)



def menu():
    delstr()
    print("\nСписок команд:\n"
            "0-выход из справочника\n"
            "1-ввод данных\n"
            "2-Поиск по введенному значнию\n"
            "3-Вывести весь справочник\n"
            "4-изменить данные\n"
            "5-удаление записи\n")
    choice=int(input("Введите команду: "))
    if choice==0:
        exit()
    elif choice==1:
        data_entry()
    elif choice==2:
        search()
    elif choice==3:
        read_all_entries()
    elif choice==4:
        edit_the_file()
    elif choice==5:
        deleting_a_file()
    
def edit_the_file():
    with open("telephone_directory.csv", "r", encoding='utf-8') as data:
        tel_book = data.read()
    print(tel_book)
    print("")
    index_delete_data = int(input("Введите номер строки для редактирования: ")) - 1
    tel_book_lines = tel_book.split("\n")
    edit_tel_book_lines = tel_book_lines[index_delete_data]
    elements = edit_tel_book_lines.split(" | ")
    fio = input("Введите ФИО: ")
    phone = input("Введите номер телефона: ")
    num = elements[0]
    if len(fio) == 0:
        fio = elements[1]
    if len(phone) == 0:
        phone = elements[2]
    edited_line = f"{num} | {fio} | {phone}"
    tel_book_lines[index_delete_data] = edited_line
    print(f"Запись - {edit_tel_book_lines}, изменена на - {edited_line}\n")
    with open("telephone_directory.csv", "w", encoding='utf-8') as f:
        f.write("\n".join(tel_book_lines))

    
def exit():
    print("вы выхли из справочника")

# menu()
def delstr():
    with open("telephone_directory.csv","r", encoding="utf-8") as f:
        lines=f.readlines()
        f.close()
        with open("telephone_directory.csv","w", encoding="utf-8") as o:
            for line in lines:
                if line.strip():
                    o.write(line)
        o.close()


menu()