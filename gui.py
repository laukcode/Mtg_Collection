from tkinter import *
import pandas as pd
from PIL import ImageTk, Image
from math import ceil

df = pd.read_csv(r'DataOutput\ScryfallData.csv', sep=';')


root = Tk()
root.geometry('1800x800')

frame = Frame(root)
frame.grid(row=0, column=0, sticky='nsew')

canvas = Canvas(frame)
scrollbar = Scrollbar(frame, orient='vertical', command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

content_frame = Frame(canvas)

content_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

search_field = Entry(content_frame, width=70)
search_field.grid(row=0,column=0)




# Image Size
x = 200
y = x * 1.4
size = x, y

def LoadImage(path, i):
    

    pim = Image.open(path)
    pim.thumbnail(size)
    img = ImageTk.PhotoImage(pim)
    return img

def searchClick():
    global imgs
    imgs = []
    name_list = df['name'].tolist()
    path_list = df['local_image_path'].tolist()
    filter_list = [k for k in name_list if search_field.get().upper() in k.upper()]
    filter_str = ''
    
    # Load Card List
    for card_name in filter_list:
        
        filter_str = filter_str + card_name + '\n'
        result_text = Text(content_frame, width=70, background='#dadada')
        result_text.grid(row=3, column=0)
        result_text.insert(END, filter_str)

        i = name_list.index(card_name)
        imgs.append(LoadImage(path_list[i], i))

    # Load Card Images
    for i, img in enumerate(imgs):
        
        row_i = ceil((i+1)/5)
        column_i = i%5+1

        canvas = Canvas(content_frame, width = x, height = y)
        canvas.grid(row=2+row_i, column=column_i, padx=20, pady=20)
        canvas.create_image(size, anchor=SE ,image=img)

# Window Resizing
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

# Pack Widgets
canvas.create_window((0, 0), window=content_frame, anchor='nw')
canvas.grid(row=0, column=0, sticky='nsew')
scrollbar.grid(row=0, column=1, sticky='ns')

# Scroll on mousewheel
def on_mousewheel(event):
   canvas.yview_scroll(int(-1 * (event.delta / 120)), 'units')


   
# Bind buttons to functions
canvas.bind_all('<MouseWheel>', on_mousewheel)
canvas.bind_all('<Return>', lambda event: searchClick())

search_buttom = Button(content_frame, text='Search', command=searchClick, pady=20, padx=50)
search_buttom.grid(row=1, column=0)




root.mainloop()

