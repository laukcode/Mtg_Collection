from tkinter import *
import pandas as pd


df = pd.read_csv(r'DataOutput\ScryfallData.csv', sep=';')

root = Tk()


search_field = Entry(root, width=80)
search_field.grid(row=0,column=0)

def searchClick():
    name_list = df['name'].tolist()
    filter_list = [k for k in name_list if search_field.get() in k]
    filter_str = ''
    
    for card_name in filter_list:
        
        filter_str = filter_str + card_name + '\n'
        result_text = Text(root)
        result_text.grid(row=3, column=0)

        result_text.insert(END, filter_str)
    

search_buttom = Button(root, text='Search', command=searchClick, pady=20, padx=50)
search_buttom.grid(row=1, column=0)




root.mainloop()

