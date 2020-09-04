from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from connect import Gg


class Two:
    def __init__(self, buy_win):
        self.data = Gg()
        self.buy_win = buy_win
        self.buy_win.geometry('1912x1080')
        self.buy_win.config(bg='#ffffff')
        self.frame_one = LabelFrame(buy_win, text='search', font=('arial', 12, 'bold'), padx=5, pady=5, fg='green',
                                bg='#ffffff')
        self.frame_one.pack()

        self.frame_two = LabelFrame(buy_win, text='buy', font=('arial', 12, 'bold'), padx=5, pady=5, fg='green',
                                bg='#ffffff')
        self.frame_two.pack()

        self.trv = ttk.Treeview(self.frame_two, columns=(1,2,3), show='headings', height=6)
        self.trv.grid(column=1, row=1)

        self.trv.heading(1, text='items')
        self.trv.heading(2, text='price')
        self.trv.heading(3, text='available quantity(K.G.)')
        self.bazar()

        self.cus_lb = Label(self.frame_two, text='Enter username', font=('arial', 12, 'bold'), padx=5, pady=5,
                            fg='green',
                            bg='#ffffff')
        self.cus_lb.grid(row=3, column=1, sticky='W')

        self.cus_en = Entry(self.frame_two, font=('arial', 12), fg='#ffffff', bg='green')
        self.cus_en.grid(row=3, column=1, sticky='E', pady=2)

        self.add_cus_btn = Button(self.frame_two, text='Submit', font=('arial', 12, 'bold'), bg='#ffffff',
                                  fg='green', width=10, command=self.sub_btn)
        self.add_cus_btn.grid(column=1, row=4, sticky='E')

        self.quan_lb = Label(self.frame_two, text='Enter quantity', font=('arial', 12, 'bold'), padx=5, pady=5, fg='green',
                                bg='#ffffff')
        self.quan_lb.grid(row=5, column=1, sticky='W')
        self.quan_en = Entry(self.frame_two, font=('arial', 12), fg='#ffffff', bg='green')
        self.quan_en.grid(row=5, column=1, sticky='E', pady=2)

        self.add_qun_btn = Button(self.frame_two, text='Add to cart', font=('arial', 12, 'bold'), bg='#ffffff',
                                  fg='green',width=10, command=self.buy_bazar)
        self.add_qun_btn.grid(column=1, row=6, sticky='E')

        self.trv2 = ttk.Treeview(self.frame_two, column=(1, 2, 3), show='headings', height=6)
        self.trv2.grid(column=1, row=7)
        self.trv2.heading(1, text='item')
        self.trv2.heading(2, text='price')
        self.trv2.heading(3, text='quantity')

        self.combo1 = ttk.Combobox(self.frame_two, width=20)
        self.combo1.grid(column=1, row=8, sticky='W')
        self.combo()

        self.gen_bill = Button(self.frame_two, text='Generate Bill', font=('arial', 12, 'bold'), padx=5, pady=5,
                               bg='#ffffff', fg='green', width =10, command=self.bill_gen)
        self.gen_bill.grid(column=1, row=8, sticky='E')
        self.frame_three = LabelFrame(self.buy_win, text='sell', font=('arial', 12, 'bold'), padx=5, pady=5, fg='green',
                                      bg='#ffffff')
        self.frame_three.pack()

        self.item_lb = Label(self.frame_three, text='Item name', font=('arial', 12, 'bold'), fg='green', bg='#ffffff')
        self.item_lb.grid(row=1, column=1)
        self.item_en = Entry(self.frame_three, font=('arial', 12), fg='#ffffff', bg='green')
        self.item_en.grid(row=1, column=2)

        self.price_lb = Label(self.frame_three, text='Price', font=('arial', 12, 'bold'), fg='green', bg='#ffffff')
        self.price_lb.grid(row=2, column=1)
        self.price_en = Entry(self.frame_three, font=('arial', 12), fg='#ffffff', bg='green')
        self.price_en.grid(row=2, column=2)

        self.quantity_lb = Label(self.frame_three, text='Quantity', font=('arial', 12, 'bold'), fg='green', bg='#ffffff')
        self.quantity_lb.grid(row=3, column=1)
        self.quantity_en = Entry(self.frame_three, font=('arial', 12), fg='#ffffff', bg='green')
        self.quantity_en.grid(row=3, column=2)

        self.add_btn = Button(self.frame_three, text='Add item', font=('arial', 12, 'bold'), bg='#ffffff', fg='green',
                             command=lambda:self.add_item(self.item_en.get(),self.price_en.get(), self.quantity_en.get()))
        self.add_btn.grid(row=4, column=2, sticky="E")

        self.label_data = Label(self.frame_three, text='')
        self.label_data.grid(row=5,column=1)

        self.new_frame = LabelFrame(self.frame_two, text='bill', font=('arial', 12, 'bold'), padx=5, pady=5, fg='green',
                                bg='#ffffff')
        self.new_frame.grid(row=1, column=2)

        self.n_label = Label(self.new_frame, text='total amount =', font=('arial', 12, 'bold'))
        self.n_label.grid( row=1, column=1)

        self.n_label2 = Label(self.new_frame, text='0', font=('arial', 12, 'bold'))
        self.n_label2.grid( row=1, column=2)

    def bazar(self):
        self.trv.delete(*self.trv.get_children())
        ret = Gg()
        data = ret.show_veg()
        print(data)
        for i in data:
            self.trv.insert("", "end", text=i[0], values=(i[1], i[2], i[3]))
        # self.trv.bind("<Double-1>", self.trv)
        # selected_item = self.trv.selection()[0]
        # book_data = self.book_tree.item(selected_item, 'values')
        # booking_id = book_data[0]
        # cus_name = book_data[1]
        # cus_room = book_data[2]

    def sub_btn(self):
        a = self.cus_en.get()
        ret = Gg()
        data = ret.new_cus(a)
        self.label_data.config(text=data)

    def buy_bazar(self):
        data = self.label_data.cget('text')
        print(data)
        selected_item = self.trv.selection()[0]
        book_data = self.trv.item(selected_item, 'values')
        item = book_data[0]
        price = book_data[1]
        ava_qt = self.quan_en.get()
        self.trv2.insert('', 'end', text="", values=(item, price, ava_qt))
        ll = Gg()
        vat = ll.bill(item,price,ava_qt,data)

    def add_item(self,x,y,z):
        if x == '' or y == '' or z == '':
            messagebox.showerror('error', 'enter all data')
            return False
        else:
            item = x
            price = y
            available_quantity = z
            self.data.saveitem(item, price, available_quantity)
            messagebox.showinfo('success', "data entered successfully")
            return True

    def combo(self):
        ll = Gg()
        vat = ll.com()
        self.combo1['values']=vat
        # print(vat)

    def bill_gen(self):
        ll = Gg()
        vat = ll.generate(self.combo1.get())
        self.n_label2.config(text=vat)
        print(self.combo1.get())
        print(vat)


def main():
    buy_win = Tk()
    Two(buy_win)
    buy_win.mainloop()


if __name__ == "__main__":
    main()
