import os
import tkinter as tk
import tkinter.filedialog as fd

# Imports the Google Cloud client library
from google.cloud import storage
from tkinter import ttk, Tk, Canvas, PhotoImage, NE, Button, Label

# The ID of your GCS bucket
bucket_name = "dataproc-staging-us-central1-930057279819-vgnpaykr"


def upload_blob(bucket_name, filepaths):
    """Uploads a file to the bucket."""

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    for filepath in filepaths:
        destination_blob_name = f"data/{os.path.basename(filepath)}"
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(filepath)

        print("File {} uploaded to {}.".format(filepath, destination_blob_name))


# this is the function called when the upload button is clicked
def uploadFiles():
    filepaths = fd.askopenfilenames(parent=root, title="Choose a file")
    filesUploaded = len(filepaths)
    upload_blob(bucket_name, filepaths)
    # This is the section of code which creates the a success label
    Label(
        root,
        text=f"Uploaded {filesUploaded} file(s) successfully!",
        bg="#FFFFFF",
        fg="#007700",
        font=("arial", 16, "normal"),
    ).place(x=50, y=220)


root = Tk()

# This is the section of code which creates the main window
root.geometry("394x270")
root.configure(background="#FFFFFF")
root.title("Hadoop MapReducer Data Uploader")

# First, we create a canvas to put the picture on
hadoop = Canvas(root, width=294, height=234, bd=0, highlightthickness=0, relief="ridge")
hadoop.pack()
# Then, we actually create the image file to use (it has to be a *.gif)
picture_file = PhotoImage(file="hadoop-mapreduce.png")
# Finally, we create the image on the canvas and then place it onto the main window
hadoop.create_image(294, 0, anchor=NE, image=picture_file)
hadoop.place(x=40, y=-40)

# This is the section of code which creates a button
Button(
    root,
    text="Upload",
    bg="#009ACD",
    fg="#f8ef22",
    bd=2,
    font=("verdana", 16, "normal"),
    command=uploadFiles,
).place(x=64, y=150)

# This is the section of code which creates a button
Button(
    root,
    text="Exit",
    bg="#009ACD",
    fg="#f8ef22",
    bd=2,
    font=("verdana", 16, "normal"),
    command=exit,
).place(x=240, y=150)
root.mainloop()
