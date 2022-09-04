#%%
import tkinter

tmr=0
jobId=None

def count_up():
    global tmr,jobId
    tmr=tmr+1
    label["text"]=tmr
    label.update()
    jobId=root.after(1000,count_up)

def reset():
    global tmr,jobId
    tmr=0
    label["text"]=tmr
    label.update()
    if jobId is not None:
        root.after_cancel(jobId)
        jobId=None

root=tkinter.Tk()
root.title("タイマー")
root.resizable(False,False)
canvas=tkinter.Canvas(root, width=200,height=300)
canvas.pack()

label=tkinter.Label(font=("Times New Roman",80))
label.place(x=70,y=10)

button=tkinter.Button(root,text="起動！",font=("Times New Roman",30),command=count_up,fg="black")
button.place(x=30,y=130)

button=tkinter.Button(root,text="リセット",font=("Times New Roman",15),command=reset,fg="black")
button.place(x=70,y=220)

root.mainloop()
# %%
