# Simple To-Do List App
# by TokyoEdtech
# Python 3.8 using Geany Editor
# Ubuntu Linux (Mac and Windows Compatible)
# Topics: tkinter, grid geometry manager
# Topics: Listbox Widget, Scrollbar widget, tkinter.messagebox, Try/Except Block, pickle
import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()


class joke:
    def jok_class():
        root = tkinter.Tk()
        root['bg'] = '#fafafa'
        # Указываем название окна
        root.title('Погодное приложение')
        # Указываем размеры окна
        root.geometry('300x250')
        # Делаем невозможным менять размеры окна
        root.resizable(width=False, height=False)

        # Создаем фрейм (область для размещения других объектов)
        # Указываем к какому окну он принадлежит, какой у него фон и какая обводка
        frame_top = tkinter.Frame(root, bg='#ffb700', bd=5)
        # Также указываем его расположение
        frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

        # Все то-же самое, но для второго фрейма
        frame_bottom = tkinter.Frame(root, bg='#42aaff', bd=5)
        frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)

        # Создаем текстовое поле для получения данных от пользователя
        cityField = tkinter.Entry(frame_top, bg='white', font=30)
        city = cityField.get()
        cityField.pack()  # Размещение этого объекта, всегда нужно прописывать

        # Создаем кнопку и при нажатии будет срабатывать метод "get_weather"
        btn = tkinter.Button(frame_top, text='Посмотреть погоду', command=joke.get_weather)
        btn.pack()

        # Создаем текстовую надпись, в которую будет выводиться информация о погоде
        info = tkinter.Label(frame_bottom, text='Погодная информация', bg='#42aaff', font=40)
        info.pack()

        # Запускаем постоянный цикл, чтобы программа работала
        root.mainloop()

    def get_weather():
        # Получаем данные от пользователя

        city = cityField.get()
        # данные о погоде будем брать с сайта openweathermap.org
        # ниже пропишите свой API ключ, который получите в кабинете пользователя на сайте openweathermap.org
        key = '1a09d9352710b4c25d8fc3f9cae5a7f4'
        # ссылка, с которой мы получим все данные в формате JSON
        url = 'http://api.openweathermap.org/data/2.5/weather'
        # Дополнительные парамтеры (Ключ, город введенный пользователем и единицины измерения - metric означает Цельсий)
        params = {'APPID': key, 'q': city, 'units': 'metric'}
        # Отправляем запрос по определенному URL
        result = requests.get(url, params=params)
        # Получаем JSON ответ по этому URL
        weather = result.json()

        # Полученные данные добавляем в текстовую надпись для отображения пользователю
        info['text'] = f'{str(weather["name"])}: {weather["main"]["temp"]}'


def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")


def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")


def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat.")


def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))


def open_second_form():
    root.destroy()
    jokeform = joke
    jokeform.jok_class()


# Create GUI
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

button_add_task = tkinter.Button(root, text="Add task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = tkinter.Button(root, text="Delete task", width=48, command=delete_task)
button_delete_task.pack()

button_load_tasks = tkinter.Button(root, text="Load tasks", width=48, command=load_tasks)
button_load_tasks.pack()

button_save_tasks = tkinter.Button(root, text="Save tasks", width=48, command=save_tasks)
button_save_tasks.pack()
button_wather = tkinter.Button(root, text="Погода", width=48, command=open_second_form)
button_wather.pack()
root.mainloop()
