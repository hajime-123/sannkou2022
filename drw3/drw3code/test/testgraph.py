#%%
import tkinter

# 秒数をカウントする変数
count = 0

after_id = None

def stop_func():
    global app
    global after_id
    print(after_id)
    app.after_cancel(after_id)

# 定期的に実行する関数
def repeat_func():
    global app
    global label
    global count
    global after_id

    # 定期的に行いたい処理
    count += 1
    label.config(
        text=str(count)
    )

    # 再度repeat_funcが実行されるようにafter実行
    after_id = app.after(1000, repeat_func)

# メインウィンドウの作成
app = tkinter.Tk()
app.geometry("300x200")

# ラベルウィジェット作成
label = tkinter.Label(
    app,
    width=15,
    height=1,
    text="0",
    font=("", 50)
)
label.pack()

# ボタンウィジェット作成
button = tkinter.Button(
    app,
    text="STOP",
    font=("", 50),
    command=stop_func
)
button.pack()

# 1000ms後にrepeat_func関数を実行
after_id = app.after(1000, repeat_func)

# メインループ
app.mainloop()
# %%
