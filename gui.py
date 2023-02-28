import functions
import PySimpleGUI as sg

label = sg.Text("Type in a ToDo")
input_box = sg.InputText(tooltip="Enter ToDo")
add_button = sg.Button("Add")

window = sg.Window('ToDo App', 
                   layout=[[label], [input_box, add_button]], 
                   font=("Helvetica", 16))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = function.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break
window.close()