import FreeSimpleGUI as fsg
from zip_creator import make_archive

label1 = fsg.Text("Select Files to compress:")
input1 = fsg.Input()
choose_button1 = fsg.FilesBrowse("Choose")

label2 = fsg.Text("Select Destination Folder:")
input2 = fsg.Input()
choose_button2 = fsg.FolderBrowse("Choose")
compress_button = fsg.Button("Compress")
output_label = fsg.Text(key = "output", text_color = "green")

window = fsg.Window("File Compressor",
                    layout=[[label1, input1 , choose_button1],
                            [label2, input2 , choose_button2],
                            [compress_button, output_label]])

while True:
    event, values = window.read()
    print(event, values )
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(values="compression completed")

window.close()

