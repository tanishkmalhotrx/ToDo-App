import functions
import PySimpleGUI as sg
import time

sg.theme("LightGreen4")

clock = sg.Text('', key='clock')
label = sg.Text("What do you wish to do today?")
input_box = sg.InputText(tooltip="Enter ToDo", key="todo")
add_button = sg.Button("Add", size=18)
list_box = sg.Listbox(values=functions.get_todos(), key='todos', 
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit", size=8)
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit", size=10)

window = sg.Window('ToDo App', 
                   layout=[[clock],
                           [label], 
                           [input_box, add_button], 
                           [list_box, edit_button, complete_button],
                           [exit_button]], 
                   font=("Helvetica", 16))

while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S "))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first!", font=("Helvetica", 15))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first!", font=("Helvetica", 15))

        case "Exit":
            break

        case "todos":
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break
        
window.close()