from tkinter import *
import re
frame=Tk()
frame.title('Calcy')
frame.resizable(False,False)
frame.configure(bg="#1e1e1e")

#Entry_Box
e1 = Entry(width=35,bd=5,justify=RIGHT)
e1.grid(row=0, column=0, columnspan=4, padx=15, pady=15)

#for_clicking_integers_buttons
def press(number):
    e1.insert(END,number)

#for_clicking_operators
def operators(symbol):
    e1.insert(END,symbol)

#For_parenthesis
def parenthesis():
    current = e1.get()
    openn=current.count('(')
    close=current.count(')')
    if openn>close:
        e1.insert(END, ')')
    else:
        e1.insert(END, '(')

#for_calculating_percentage
def percent():
    try:
        current = e1.get()
        if current:
            value = eval(current)
            e1.delete(0, END)
            e1.insert(0, value / 100)
    except:
        e1.delete(0,END)
        e1.insert(0,"Invalid")

#For_cheking_result
def submit():
    expression = e1.get().replace('÷', '/').replace('×', '*')
    expression = re.sub(r'(?<!\d)-?0+(\d+)', r'\1', expression)
    expression = re.sub(r'(\d)\(', r'\1*(', expression)  # 2(3+4) -> 2*(3+4)
    expression = re.sub(r'\)(\d)', r')*\1', expression)  # (2+3)4 -> (2+3)*4
    try:
        result = eval(expression)
        e1.delete(0, END)
        e1.insert(0, result)
    except ZeroDivisionError:
        e1.delete(0, END)
        e1.insert(0, "Can't divide by zero")
    except Exception:
        e1.delete(0, END)
        e1.insert(0, "Invalid")
   

#For_deleting_entries
def clear():
    e1.delete(0,END)

#Buttons
b1=Button(text='C',height=3,width=6,bg="red",fg='white',font=('Arial',9,'bold'),command=clear).grid(row=1,column=0,padx=3,pady=3)
b2=Button(text='( )',height=3,width=6,bg="orange",fg='black',font=('Arial',9,'bold'),command=parenthesis).grid(row=1,column=1,padx=3,pady=3)
b3=Button(text='%',height=3,width=6,bg="orange",fg='black',font=('Arial',9,'bold'),command=percent).grid(row=1,column=2,padx=3,pady=3)
b4=Button(text='/',height=3,width=6,bg="orange",fg='black',font=('Arial',9,'bold'),command=lambda:operators('/')).grid(row=1,column=3,padx=3,pady=3)


b5=Button(text='7',height=3,width=6,bg="#222222",fg='white',font=('Arial',9,'bold'),command=lambda:press(7)).grid(row=2,column=0,padx=3,pady=3)
b6=Button(text='8',height=3,width=6,bg="#222222",fg='white',font=('Arial',9,'bold'),command=lambda:press(8)).grid(row=2,column=1,padx=3,pady=3)
b7=Button(text='9',height=3,width=6,bg="#222222",fg='white',font=('Arial',9,'bold'),command=lambda:press(9)).grid(row=2,column=2,padx=3,pady=3)
b8=Button(text='*',height=3,width=6,bg="orange",fg='black',font=('Arial',9,'bold'),command=lambda:operators('*')).grid(row=2,column=3,padx=3,pady=3)
                                                                                                                   
b9=Button(text='4',height=3,width=6,bg="#222222",fg='white',font=('Arial',9,'bold'),command=lambda:press(4)).grid(row=3,column=0,padx=3,pady=3)
b10=Button(text='5',height=3,width=6,bg="#222222",fg='white',font=('Arial',9,'bold'),command=lambda:press(5)).grid(row=3,column=1,padx=3,pady=3)
b11=Button(text='6',height=3,width=6,bg="#222222",fg='white',font=('Arial',9,'bold'),command=lambda:press(6)).grid(row=3,column=2,padx=3,pady=3)
b12=Button(text='-',height=3,width=6,bg="orange",fg='black',font=('Arial',9,'bold'),command=lambda:operators('-')).grid(row=3,column=3,padx=3,pady=3)

b13=Button(text='1',height=3,width=6,bg="#222222",fg='white',font=('Arial',9,'bold'),command=lambda:press(1)).grid(row=4,column=0,padx=3,pady=3)
b14=Button(text='2',height=3,width=6,bg="#222222",fg='white',font=('Arial',9,'bold'),command=lambda:press(2)).grid(row=4,column=1,padx=3,pady=3)
b15=Button(text='3',height=3,width=6,bg="#222222",fg='white',font=('Arial',9,'bold'),command=lambda:press(3)).grid(row=4,column=2,padx=3,pady=3)
b16=Button(text='+',height=3,width=6,bg="orange",fg='black',font=('TArial',9,'bold'),command=lambda:operators('+')).grid(row=4,column=3,padx=3,pady=3)

b17=Button(text='📠',height=3,width=6,bg="#222222",fg='white',font=('Arial',9,'bold')).grid(row=5,column=0)
b18=Button(text='0',height=3,width=6,bg="#222222",fg='white',font=('Arial',9,'bold'),command=lambda: press(0)).grid(row=5,column=1)
b19=Button(text='.',height=3,width=6,bg="#222222",fg='white',font=('Arial',9,'bold'),command=lambda:press('.')).grid(row=5,column=2)
b20=Button(text='=',height=3,width=6,bg="green",fg='white',font=('Arial',9,'bold'),command=submit).grid(row=5,column=3)


mainloop()     