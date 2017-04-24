from tkinter import *
import os.path
import shutil
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import filedialog
from uuid import getnode as get_mac
from port import brate,comp1_in
something = False
user_name_get = None
reciever_name_get = None
username_list = []#список всех зарегистрированных пользователей
Filepath_Flag = ''#путь файла(объявлен глобальной переменной для того, чтобы два раза не вызывать функцию Choose_File_Path)

def Getting_Username():
    def Kill_Bill():
        successful_registration_interface.destroy()
        Login()
    global user_name_get
    user_name_get = Login_Entry.get()
    login_interface.destroy()
    successful_registration_interface = Tk()
    successful_registration_interface.title('Success!')
    Successful_Registration_Label = Label(successful_registration_interface, text='Вы вошли как '+user_name_get).pack()
    Successful_Registration_Button = Button(successful_registration_interface, text='Ok',
                                            bg='white', fg='green', command=Kill_Bill).pack()
    successful_registration_interface.mainloop()

def Getting_Recievername():
    def Kill_Fish():
        successful_recieve_file.destroy()
        Send_File()
    global reciever_name_get
    reciever_name_get = Reciever_Name_Entry.get()
    successful_recieve_file = Tk()
    successful_recieve_file.title('Success!')
    Successful_Recieve_File_Label = Label(successful_recieve_file, text='Вы отправили файл '+reciever_name_get).pack()
    Successful_Recieve_File_Button = Button(successful_recieve_file, text='Ok',
                                            bg='white', fg='green', command=Kill_Fish).pack()
    successful_recieve_file.mainloop()

def Login():#регистрация пользователя(можно вызвать из любого места без ошибок)
    invalid_symbols = '*|:"<>?/'
    user_name = user_name_get#получение имени пользователя из строки ввода
    mac = get_mac()#получение мас адреса
    Username_Flag = ''#присваиваем значение флагу имени пользователя
    for i in range(len(username_list)):#итерация по списку username_list[i][j]
        if user_name in username_list[i]:#проверка совпадения с зарегистрированным пользователем
            same_usernames_error = Tk()#визуальная часть
            same_usernames_error.title('ERROR')
            same_usernames_error_label = Label(same_usernames_error, text='Такое имя уже зарегистрировано!!!').pack()
            same_usernames_error.mainloop()
            Username_Flag = None
            break
        elif mac in username_list[i]:#проверка совпадения мас адреса
            same_mac_error = Tk()
            same_mac_error.title('ERROR')
            same_mac_error_label = Label(same_mac_error, text='Такой МАС адрес уже есть!!!').pack()
            same_mac_error.mainloop()
            Username_Flag = None
            break
    for i in invalid_symbols:#итерация по списку username_list[i][j]
        if i in user_name:#проверка на недопустимые символы
            syntax_error = Tk()#визуальная часть
            syntax_error.title('ERROR')
            syntax_error_label = Label(syntax_error, text='Имя отправителя: Invalid syntax.').pack()
            syntax_error.mainloop()
            Username_Flag = None
            break
    if 18<len(user_name):#проверка максимальной длины имени
        length_error = Tk()#визуальная часть
        length_error.title('ERROR')
        length_error_label = Label(length_error, text='Имя отправителя: Invalid lenght.').pack()
        length_error.mainloop()
        Username_Flag = None
    elif Username_Flag != None and len(user_name)!=0:#проверка длины имени
        l = [[user_name, mac]]#создание подсписка
        username_list.extend(l)#занесение подсписка в список пользователей
        print('User',user_name,'connected.')
        print(username_list)

        Username_Flag = user_name
    elif len(user_name) == 0:#условие невведенного имени
        short_entry_error = Tk()
        short_entry_error.title('ERROR')
        short_entry_error_label = Label(short_entry_error, text='Имя отправителя: User name is too short.').pack()
        short_entry_error.mainloop()
        Username_Flag = None
    return Username_Flag


#выбор пути файла
def Choose_File_Path():
    global Filepath_Flag
    file_path = filedialog.askopenfilename(title = "Выберите файл")#вывод диалогового окна выбора файла
    File_Path_Text.delete('1.0',END)
    File_Path_Text.insert(END, file_path)#занесение имени файла
    Filepath_Flag = file_path#изменение флага флага пути файла


def Choose_Reciever():
    invalid_symbols = '*|:"<>?/'
    reciever_name = reciever_name_get
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

#выбор типа кодировки(можно вызвать из любого места без ошибок)
def Choose_CodeType():
    CodeType_Flag = None
    if CodeType_Variable.get() == '[7,4]':
        CodeType_Flag = 7
    elif CodeType_Variable.get() == '[15,11]':
        CodeType_Flag = 15
    return CodeType_Flag


#выбор скорости СОМ порта(можно вызвать из любого метса без ошибок)
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
    brate(COMspeed_Flag)
    return COMspeed_Flag

#вывод информации
def Information():
    print(comp1_in.baudrate)
    info_interface = Tk()
    info_interface.title('Information')
    info='Some useless information :).'
    Programm_info = Label(info_interface, text=info)
    Programm_info.pack()



#функция отключения пользователя
def Disconnect_User():
    main_interface_title.destroy()
    user_name = user_name_get
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
        CodeType_Text = 'Тип кодировки: [7,4]'
    elif Choose_CodeType() == 15:
        CodeType_Text = 'Тип кодировки: [15,11]'
    COMspeed_Text = 'Скорость COM порта ' + str(Choose_COMspeed()) + 'bit/s'
    Recievername_Text = 'Вы отправили файл '+str(Choose_Reciever())
    send_file_interface = Tk()
    send_file_interface.title('Отправлено!')
    File_Label = Label(send_file_interface, text='Файл: '+os.path.basename(Filepath_Flag)).pack()
    CodeType_Label = Label(send_file_interface, text=CodeType_Text).pack()
    COMspeed_Label = Label(send_file_interface, text=COMspeed_Text).pack()
    Recievername_Label = Label(send_file_interface, text=Recievername_Text).pack()
    send_file_interface.mainloop()
    return Choose_Reciever(), Choose_CodeType(), Choose_COMspeed(), Filepath_Flag

#интерфейс получения файла
def Recieve_File_Interface(file_path):

    def Open_File():
        askopenfile(os.path.abspath(file_path))

    def Save_File():
        directory = os.path.normpath(askdirectory())
        path = file_path
        if os.path.isfile(os.path.normpath(file_path)) == True:
            path = os.path.normpath(file_path)
        else:
            print('Такого файла нет!')
            return 0
        print(directory+' - директория, в которую сохраняем файл.')
        print(path+' - файл, который сохраняем.')
        if os.path.isfile(os.path.normpath(os.path.join(directory,os.path.basename(path)))) == False:
            shutil.move(path, directory)
            print('Вы сохранили файл в ' + directory)
        elif os.path.isfile(os.path.normpath(os.path.join(directory,os.path.basename(path)))) == True:
            print('Файл с таким именем уже есть в директории: '+directory)
            os.remove(os.path.normpath(os.path.join(directory,os.path.basename(path))))
            shutil.copy(path, directory)
            print('Вы заменили файл',os.path.basename(path),'в директории', directory)
    def Delete_File():
        path = os.path.normpath(file_path)
        if os.path.isfile(path) == True:
            os.remove(path)
            print('Вы удалили файл: '+os.path.basename(path))
    file_name = os.path.basename(file_path)
    recieve_interface = Tk()
    File_Name_Label = Label(recieve_interface, text='Имя файла: '+file_name).pack()
    Open_File_Button = Button(recieve_interface, bg='white', fg='green',
                              text='Открыть файл', command=Open_File).pack()
    Save_File_Button = Button(recieve_interface, bg='white', fg='green',
                              text='Сохранить файл', command=Save_File).pack()
    Delete_File_Button = Button(recieve_interface, bg='white', fg='green',
                                text='Удалить файл', command=Delete_File).pack()
    recieve_interface.mainloop()



file_name = 'C:/Users/Иван/Desktop/Буфер/users.txt'
if something == 1:
    Recieve_File_Interface(file_name)


login_interface = Tk()
login_interface.title('Login')
Login_Label = Label(
    login_interface, text='Введите имя пользователя:'
).grid(row=0, column=0)
Login_Entry = Entry(login_interface, width=30)
Login_Entry.grid(row=0, column=1)
Login_Button = Button(
    login_interface, bg='white', fg='green',
    text='Login', command = Getting_Username
).grid(row=1, column=1)
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
).grid(row=1, column=0)
Reciever_Name_Entry = Entry(
    main_interface_title, width=30)
Reciever_Name_Entry.grid(
    row=1, column=1)


CodeType_Variable = StringVar()
CodeType_Label = Label(
    main_interface_title, text='Тип кодировки:'
).grid(row=2, column=0)
CodeType_RadioButton = Radiobutton(
    main_interface_title, text='[7,4]',
    variable=CodeType_Variable, value='[7,4]', command=Choose_CodeType
).grid(row=2, column=1)
CodeType_RadioButton = Radiobutton(
    main_interface_title, text='[15,11]',
    variable=CodeType_Variable, value='[15,11]', command=Choose_CodeType
).grid(row=3, column=1)


COMspeed_Variable = IntVar()
COM_Speed_Label = Label(
    main_interface_title, text='Скорость порта:'
).grid(row=4, column=0)
COM_Speed_RadioButton = Radiobutton(
    main_interface_title, text='150bit/s',
    variable=COMspeed_Variable, value=150, command=Choose_COMspeed
).grid(row=4, column=1)
COM_Speed_RadioButton = Radiobutton(
    main_interface_title, text='600bit/s',
    variable=COMspeed_Variable, value=600, command=Choose_COMspeed
).grid(row=5, column=1)
COM_Speed_RadioButton = Radiobutton(
    main_interface_title, text='2400bit/s',
    variable=COMspeed_Variable, value=2400, command=Choose_COMspeed
).grid(row=6, column=1)
COM_Speed_RadioButton = Radiobutton(
    main_interface_title, text='9600bit/s',
    variable=COMspeed_Variable, value=9600, command=Choose_COMspeed
).grid(row=7, column=1)
COM_Speed_RadioButton = Radiobutton(
    main_interface_title, text='38400bit/s',
    variable=COMspeed_Variable, value=38400, command=Choose_COMspeed
).grid(row=8, column=1)


button_information = Button(
    main_interface_title, text='Информация о приложении',
    bg='white', fg='green', command=Information
).grid(row=9, column=1)


button_send_file = Button(
    main_interface_title, text='Отправить файл',
    bg='white', fg='green', command=Getting_Recievername
).grid(row=10, column=1)


button_disconnect = Button(
    main_interface_title, text='Отключиться от сети',
    bg='white', fg='green', command=Disconnect_User
).grid(row=11, column=1)


main_interface_title.mainloop()