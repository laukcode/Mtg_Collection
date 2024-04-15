from tkinter import *
import pandas as pd
from PIL import ImageTk, Image
from math import ceil

df = pd.read_csv(r'DataOutput\ScryfallData.csv', sep=';')


root = Tk()
root.geometry("1800x800")



search_field = Entry(root, width=80)
search_field.grid(row=0,column=0)




# Image Size
x = 200
y = x * 1.4
size = x, y

def LoadImage(path, i):
    

    pim = Image.open(path)
    pim.thumbnail(size)
    img = ImageTk.PhotoImage(pim)

    canvas = Canvas(root, width = 300, height = 300)
    canvas.grid(row=3, column=i)
    return img

def searchClick():
    global imgs
    imgs = []
    name_list = df['name'].tolist()
    path_list = df['local_image_path'].tolist()
    filter_list = [k for k in name_list if search_field.get() in k]
    filter_str = ''
    
    # Load Card List
    for card_name in filter_list:
        
        filter_str = filter_str + card_name + '\n'
        result_text = Text(root)
        result_text.grid(row=3, column=0)
        result_text.insert(END, filter_str)

        i = name_list.index(card_name)
        imgs.append(LoadImage(path_list[i], i))
    # Load Card Images
    for i, img in enumerate(imgs):
        row_i = ceil((i+1)/5)
        column_i = i%5+1

        canvas = Canvas(root, width = x, height = y, bg='black')
        canvas.grid(row=2+row_i, column=column_i)
        canvas.create_image(size, anchor=SE ,image=img )

search_buttom = Button(root, text='Search', command=searchClick, pady=20, padx=50)
search_buttom.grid(row=1, column=0)




root.mainloop()

