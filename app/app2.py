#-*- coding: utf-8 -*-

import tkinter as tk  #ウィンドウを表示する
#ファイルダイアログを使用するモジュール
import tkinter.filedialog as fd
#画像を扱うモジュール
import PIL.Image
#画像ファイルを表示するモジュール
import PIL.ImageTk

def dispPhoto(path):
    #image reading
    newImage = PIL.Image.open(path).resize((300,300))
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageData

def openFile():
    filePath = fd.askopenfilename()
    if filePath:
        dispPhoto(filePath)

root = tk.Tk()
root.geometry("600x400")

btn = tk.Button(text="ファイルを開く", command=openFile)
imageLabel = tk.Label()
btn.pack()
imageLabel.pack()
tk.mainloop()