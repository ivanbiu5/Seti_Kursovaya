from tkinter import *
import os.path
import shutil
from tkinter.messagebox import *
from tkinter import filedialog
from uuid import getnode as get_mac
something = False

username_list = []
user_name = None
def Login():
    global user_name
    invalid_symbols = '*|:"<>?/'
    user_name = Login_Entry.get()
    mac = get_mac()
    Username_Flag = user_name
    for i in range(len(username_list)):
        if user_name in username_list[i]:
            same_usernames_error = Tk()
            same_usernames_error.title('ERROR')
            same_usernames_error_label = Label(same_usernames_error, text='Такое имя уже зарегистрировано!!!').pack()
            same_usernames_error.mainloop()
            Username_Flag = None
            break
        elif mac in username_list[i]:
            same_mac_error = Tk()
            same_mac_error.title('ERROR')
            same_mac_error_label = Label(same_mac_error, text='Такой МАС адрес уже есть!!!').pack()
            same_mac_error.mainloop()
            Username_Flag = None
            break
    for i in invalid_symbols:
        if i in user_name:
            syntax_error = Tk()
            syntax_error.title('ERROR')
            syntax_error_label = Label(syntax_error, text='Имя отправителя: Invalid syntax.').pack()
            syntax_error.mainloop()
            Username_Flag = None
            break
    if 18<len(user_name):
        length_error = Tk()
        length_error.title('ERROR')
        length_error_label = Label(length_error, text='Имя отправителя: Invalid lenght.').pack()
        length_error.mainloop()
        Username_Flag = None
    elif Username_Flag != None and len(user_name)!=0:
        l = [[user_name, mac]]
        username_list.extend(l)
        print('User',user_name,'connected.')
        print(username_list)
        login_interface.destroy()
        return Username_Flag
    elif len(user_name) == 0:
        short_entry_error = Tk()
        short_entry_error.title('ERROR')
        short_entry_error_label = Label(short_entry_error, text='Имя отправителя: User name is too short.').pack()
        short_entry_error.mainloop()
        Username_Flag = None


#выбор пути файла
def Choose_File_Path():
    file_path = filedialog.askopenfilename(title = "Выберите файл")
    File_Path_Text.insert(END, file_path)
    Filepath_Flag = file_path
    return Filepath_Flag


def Choose_Reciever():
    invalid_symbols = '*|:"<>?/'
    reciever_name = Reciever_Name_Entry.get()
    Recievername_Flag = ''
    if 18 < len(reciever_name):
        length_error = Tk()
        length_error.title('ERROR')
        length_error_label = Label(length_error, text='Имя получателя: Invalid lenght.').pack()
        length_error.mainloop()
        Recievername_Flag = None
    for i in invalid_symbols:
        if i in reciever_name:
            syntax_error = Tk()
            syntax_error.title('ERROR')
            syntax_error_label = Label(syntax_error, text='Имя получателя: Invalid syntax.').pack()
            syntax_error.mainloop()
            Recievername_Flag = None
            break
    if len(reciever_name) == 0:
        short_entry_error = Tk()
        short_entry_error.title('ERROR')
        short_entry_error_label = Label(short_entry_error, text='Имя получателя: Invalid syntax.').pack()
        short_entry_error.mainloop()
        Recievername_Flag = None
    if Recievername_Flag != None and len(reciever_name) != 0:
        Recievername_Flag = reciever_name
    return Recievername_Flag

#выбор типа кодировки
def Choose_CodeType():
    CodeType_Flag = None
    if CodeType_Variable.get() == '[7,4]':
        CodeType_Flag = 7
    elif CodeType_Variable.get() == '[15,11]':
        CodeType_Flag = 15
    return CodeType_Flag


#выбор скорости СОМ порта
def Choose_COMspeed():
    COMspeed_Flag = None
    if COMspeed_Variable.get() == 150:
        COMspeed_Flag = 150
    elif COMspeed_Variable.get() == 600:
        COMspeed_Flag = 600
    elif COMspeed_Variable.get() == 2400:
        COMspeed_Flag = 2400
    elif COMspeed_Variable.get() == 9600:
        COMspeed_Flag = 9600
    elif COMspeed_Variable.get() == 38400:
        COMspeed_Flag = 38400
    return COMspeed_Flag

#вывод информации
def Information():
    info_interface = Tk()
    info_interface.title('Information')
    info='Some useless information :).'
    Programm_info = Label(info_interface, text=info)
    Programm_info.pack()


#функция отключения пользователя
def Disconnect_User():
    global user_name
    print(user_name)
    for i in range(len(username_list)):
        if len(user_name)!=0 and user_name in username_list[i]:
            username_list[i].pop(0)
            username_list[i].pop(0)
            print('User ', user_name, ' disconnected.', username_list)
            Filepath_Flag = None
            Username_Flag = None
            COMnum_Entry_Flag = None
            COMnum_Exit_Flag = None
            Recievername_Flag = None
            CodeType_Flag = None
            COMspeed_Flag = None
            user_name = None
            main_interface_title.destroy()
            return Username_Flag, Filepath_Flag, COMnum_Entry_Flag, \
                   COMnum_Exit_Flag, Recievername_Flag, CodeType_Flag, COMspeed_Flag
    else:
        not_connected_error = Tk()
        not_connected_error.title('ERROR')
        not_connected_label = Label(not_connected_error, text='Вы не подключены!').pack()
        not_connected_error.mainloop()


def Send_File():#отправка файла
    CodeType_Text =''
    if Choose_CodeType() == 7:
        CodeType_Text = 'Type of codding: [7,4]'
    elif Choose_CodeType() == 15:
        CodeType_Text = 'Type of codding: [15,11]'
    COMspeed_Text = 'COM port speed: ' + str(Choose_COMspeed()) + 'bit/s'
    Recievername_Text = 'You recieve file to '+str(Choose_Reciever())
    send_file_interface = Tk()
    send_file_interface.title('Отправлено!')
    CodeType_Label = Label(send_file_interface, text=CodeType_Text).pack()
    COMspeed_Label = Label(send_file_interface, text=COMspeed_Text).pack()
    Recievername_Label = Label(send_file_interface, text=Recievername_Text).pack()
    send_file_interface.mainloop()

#интерфейс получения файла
def Recieve_File(file_path):

    def Save_New_File():
        return 0
    def Open_New_File():
        return 0
    recieve_interface = Tk()
    File_Name_Label = Label(recieve_interface, text='Имя файла: ' + file_path
                            ).grid(row=0, column=0)
    Save_File_Button = Button(recieve_interface, text='Сохранить файл',
                              bg='white', fg='green', command=Save_New_File
                              ).grid(row=1, column=0)
    Open_File_Button = Button(recieve_interface, text='Открыть файл',
                              bg='white', fg='green', command=Open_New_File
                              ).grid(row=2, column=0)
    recieve_interface.title('New file')



file_name = 'Kek'
file=1
if something == False:
    Recieve_File(file_name)


login_interface = Tk()
login_interface.title('Login')
Login_Label = Label(login_interface, text='Введите имя пользователя:').grid(row=0, column=0)
Login_Entry = Entry(login_interface, width=30)
Login_Entry.grid(row=0, column=1)
Login_Button = Button(login_interface, bg='white', fg='green', text='Login', command = Login).grid(row=1, column=1)
login_interface.mainloop()


main_interface_title = Tk()
main_interface_title.title('User interface')



File_Path_Label = Label(
    main_interface_title, text='Путь файла:'
).grid(row=0, column=0)
File_Path_Text = Text(
    main_interface_title, height=1, width=22)
File_Path_Text.grid(
    row=0, column=1)
File_Path_Button = Button(
    main_interface_title, text='Обзор', bg='white', fg='green', command=Choose_File_Path
).grid(row=0, column=2)


Reciever_Name_Label = Label(
    main_interface_title, text='Имя получателя:'
).grid(row=7, column=0)
Reciever_Name_Entry = Entry(
    main_interface_title, width=30)
Reciever_Name_Entry.grid(
    row=7, column=1)


CodeType_Variable = StringVar()
CodeType_Label = Label(
    main_interface_title, text='Тип кодировки:'
).grid(row=8, column=0)
CodeType_RadioButton = Radiobutton(
    main_interface_title, text='[7,4]',
    variable=CodeType_Variable, value='[7,4]', command=Choose_CodeType
).grid(row=8, column=1)
CodeType_RadioButton = Radiobutton(
    main_interface_title, text='[15,11]',
    variable=CodeType_Variable, value='[15,11]', command=Choose_CodeType
).grid(row=9, column=1)


COMspeed_Variable = IntVar()
COM_Speed_Label = Label(
    main_interface_title, text='Скорость порта:'
).grid(row=10, column=0)
COM_Speed_RadioButton = Radiobutton(
    main_interface_title, text='150bit/s',
    variable=COMspeed_Variable, value=150, command=Choose_COMspeed
).grid(row=10, column=1)
COM_Speed_RadioButton = Radiobutton(
    main_interface_title, text='600bit/s',
    variable=COMspeed_Variable, value=600, command=Choose_COMspeed
).grid(row=11, column=1)
COM_Speed_RadioButton = Radiobutton(
    main_interface_title, text='2400bit/s',
    variable=COMspeed_Variable, value=2400, command=Choose_COMspeed
).grid(row=12, column=1)
COM_Speed_RadioButton = Radiobutton(
    main_interface_title, text='9600bit/s',
    variable=COMspeed_Variable, value=9600, command=Choose_COMspeed
).grid(row=13, column=1)
COM_Speed_RadioButton = Radiobutton(
    main_interface_title, text='38400bit/s',
    variable=COMspeed_Variable, value=38400, command=Choose_COMspeed
).grid(row=14, column=1)


button_information = Button(
    main_interface_title, text='Информация о приложении',
    bg='white', fg='green', command=Information
).grid(row=15, column=1)


button_send_file = Button(
    main_interface_title, text='Отправить файл',
    bg='white', fg='green', command=Send_File
).grid(row=16, column=1)


button_disconnect = Button(
    main_interface_title, text='Отключиться от сети',
    bg='white', fg='green', command=Disconnect_User
).grid(row=17, column=1)


main_interface_title.mainloop()

'''
os.path.split(path)
Параметры:	path (str) – путь к файлу
Возвращает кортеж из пары строк - (путь к родителской папке, название файла).

>>> os.path.split('c:\\system\\apps\\Python\\Python.app')
('c:\\system\\apps\\Python\\', 'Python.app')'''