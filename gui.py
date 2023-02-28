#import functions
import PySimpleGUI as sg

label = sg.Text("Type in a ToDo")
input_box = sg.InputText(tooltip="Enter ToDo")
add_button = sg.Button("Add")

window = sg.Window('ToDo App', layout=[[label], [input_box, add_button]])

window.read()
window.close()