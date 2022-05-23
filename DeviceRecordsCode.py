# author @ Natasha
# last updated @ October 2021
# App for IDream device inventory - w/ GUI

from tkinter import *
from datetime import datetime


window = Tk()
window.title("iDream Record Form")
window.geometry("640x620")

#display metrics and intro message
intromsg = Label(window, text="Welcome Natasha", font='default 10 bold').grid(row=0, column=1, ipady=25)
metrics = Label(window, text="Your total count is <count>").grid(row=1, column=1)
currentdate = datetime.now().strftime("%m/%d/%Y")
dateinfo = Label(window, text='Today is ' + currentdate).grid(row=2, column=1)
print(intromsg)
print(metrics)
print(dateinfo)

#date and time
filedate = datetime.now().strftime("%Y_%m_%d_at_%I_%M_%S_%p")
ext = ".txt"

#labels
labels = ['Date:', 'Brand:', 'Year:', 'Model:',
          'HDD:', 'RAM:', 'Battery:','Notes:' ]

counterlbl = 4

for i in range(len(labels)):
    current_label = 'label' + str(i) #label0, label1, etc
    current_label = Label(window, text = labels[i], font=('default 10 bold'), fg='red', width=10, anchor='e')
    current_label.grid(row=counterlbl, column=0, ipady=8)
    counterlbl += 1
    
  
#entrybox
name_var = StringVar()
user_info = {
    'Date': StringVar(),
    'Brand': StringVar(),
    'Year': StringVar(),
    'Model': StringVar(),
    'HDD': StringVar(),
    'RAM': StringVar(),
    'Battery': StringVar(),
    'Notes': StringVar()
}
counter = 4
for i in user_info:
    current_entrybox = 'entry' + i #entrydate, entrybrand
    current_entrybox = Entry(window, textvariable=user_info[i], highlightthickness=5, width=40)
    current_entrybox.grid(row=counter, column=1)
    counter += 1 



#submit
def submit():
    with open(filedate + ext, 'w') as f:
       for i in user_info:
           print(i, ':', user_info.get(i).get())
           print(i, ':', user_info.get(i).get(), file=f)
    f.close()
    return Label(window, text="Data Submitted!").grid(column=1, padx=(0,30))

           


submit_button = Button(window, text='Submit', command=submit, width=16)
submit_button.grid(row=15, column=1, pady=(40, 0), padx=(0, 30))


window.mainloop()