
#%%
import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time

import pandas as pd
import mysql.connector as mydb
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

todaydetail = datetime.datetime.today()#210921
todaydetail_str=todaydetail.strftime('%Y%m%d')#211119
todaydetail_str='20220214'

from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']

# rootメインウィンドウの設定
root = tk.Tk()
root.title("tkinter:Toplevel")
root.geometry("600x300")

# sub_winを定義する
sub_win = None
sub_win2 = None
sub_win3 = None
sub_win4 = None
fig = plt.figure()
fig2 = plt.figure()
fig3 = plt.figure()
fig4 = plt.figure()

sub_win_id = None
sub_win2_id = None
sub_win3_id = None
sub_win4_id = None
def stop_func(after_id,win):
    #global root
    #global sub_win_id
    print(after_id)
    root.after_cancel(after_id)
    win.destroy()

def sub_window():
    global sub_win,sub_win_id
    if sub_win == None or not sub_win.winfo_exists():
        sub_win = tk.Toplevel()#(master=root)いらない
        sub_win.geometry("600x300")
        
        #(1)figを生成します。
        #fig = plt.figure()#これを外で宣言したほうがいいかも？ 
        #(2) 実際のグラフを描画するAxesインスタスを生成
        ax1 = fig.add_subplot(1, 1, 1)
        #label_sub = tk.Label(sub_win, text="サブウィンドウ")
        #label_sub.pack()
        canvas = FigureCanvasTkAgg(fig, master=sub_win)#(fig, master=root)
        plot_widget = canvas.get_tk_widget()

        def func_1():
            global sub_win,sub_win_id
            fig.clf()# Clear figure グラフを消している

            conn = mydb.connect(
                    host='127.0.0.1',
                    port='3306',
                    user='root',
                    password='tkroyc123',
                    database='draw3'
                )
            cur = conn.cursor()
            tablename10='drawtable_'+todaydetail_str
            sql_1 = 'SELECT time,gaikei_value,naikei_value from '+tablename10
            sql_2=' order by id desc limit %s'
            sql_3 = sql_1+sql_2
            data = (int(5),)
            data=b1_0
            if b1_0=='':            
                data = (int(5),)
            else:
                data=(int(b1_0),)
            cur.execute(sql_3,data)
            result_g = cur.fetchall()
            cur.close()
            conn.close()
            
            boxpd = pd.DataFrame(result_g)
            x = pd.to_datetime(boxpd[0])
            x = x.sort_index(ascending=False)
            
            y1 = boxpd[1]
            y1 = y1.sort_index(ascending=False)
            y2 = boxpd[2]
            y2 = y2.sort_index(ascending=False)

            #更新した値をグラフに代入
            ax1 = fig.add_subplot(2, 1, 1)
            #ax1.set_ylim(89990,90020)
            ax1.xaxis.set_major_formatter(mdates.DateFormatter('%y/%m/%d\n%H:%M:%S'))
            ax1.plot(x,y1,label="gaikei_value")
            ax1.legend(loc='lower left')
            ax1.grid(which='major',axis='y',color='black',
                    linestyle='-',linewidth=0.2)
            ax2 = fig.add_subplot(2, 1, 2)
            ax2.xaxis.set_major_formatter(mdates.DateFormatter('%y/%m/%d\n%H:%M:%S'))
            ax2.plot(x,y2,label="naikei_value")
            ax2.legend(loc='lower left')
            ax2.grid(which='major',axis='y',color='black',
                    linestyle='-',linewidth=0.2)
            try:
                if b1_1=='' and b1_2=='' and b1_3=='' and b1_4=='':
                    # ax1.set_ylim(min(y1),max(y1))
                    # ax2.set_ylim(min(y2),max(y2))
                    ax1.set_ylim(0,100)
                    ax2.set_ylim(0,100)
                elif b1_1!='' and b1_2!='' and b1_3=='' and b1_4=='':
                    ax1.set_ylim(int(b1_1),int(b1_2))
                    ax2.set_ylim(0,100)
                elif b1_1=='' and b1_2=='' and b1_3!='' and b1_4!='':
                    ax1.set_ylim(0,100)
                    ax2.set_ylim(int(b1_3),int(b1_4))
                else:
                    ax1.set_ylim(int(b1_1),int(b1_2))
                    ax2.set_ylim(int(b1_3),int(b1_4))
            except:
                ax1.set_ylim(0,100)
                ax2.set_ylim(0,100)
            #Canvasのグラフに再描写する　1秒おきに以上を繰り返す
            fig.canvas.draw()
            print(1)
            
            sub_win_id=root.after(1000,func_1)
        #plot_widget.grid()
        plot_widget.pack(side=tk.TOP,fill=tk.BOTH,expand=1)
        #button_sub = tk.Button(master=sub_win, text="閉じる", font=(None,24), command=stop_func)
        #button_sub.pack(pady=20)
        sub_win.protocol('WM_DELETE_WINDOW', lambda:stop_func(sub_win_id,sub_win))
        sub_win_id=root.after(1000,func_1)    

def sub_window2():
    global sub_win2,sub_win2_id
    if sub_win2 == None or not sub_win2.winfo_exists():
        sub_win2 = tk.Toplevel()#(master=root)いらない
        sub_win2.geometry("600x300")
        
        #(1)figを生成します。
        #fig = plt.figure()#これを外で宣言したほうがいいかも？ 
        #(2) 実際のグラフを描画するAxesインスタスを生成
        ax1 = fig2.add_subplot(1, 1, 1)
        #label_sub = tk.Label(sub_win, text="サブウィンドウ")
        #label_sub.pack()
        canvas = FigureCanvasTkAgg(fig2, master=sub_win2)#(fig, master=root)
        #plot_widget = canvas.get_tk_widget(side=tk.TOP,fill=tk.BOTH,expand=1)
        #plot_widget = canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=1)
        plot_widget = canvas.get_tk_widget()
        def func_2():
            global sub_win2,sub_win2_id
            fig2.clf()# Clear figure グラフを消している

            conn = mydb.connect(
                    host='127.0.0.1',
                    port='3306',
                    user='root',
                    password='tkroyc123',
                    database='draw3'
                )
            cur = conn.cursor()
            tablename10='drawtable_'+todaydetail_str
            sql_1 = 'SELECT time,okuri_velocity,hiki_velocity from '+tablename10
            sql_2=' order by id desc limit %s'
            sql_3 = sql_1+sql_2
            data = (int(5),)
            data=b2_0
            if b2_0=='':            
                data = (int(5),)
            else:
                data=(int(b2_0),)
            #print(sql_3)
            cur.execute(sql_3,data)
            result_g = cur.fetchall()
            cur.close()
            conn.close()
            
            boxpd = pd.DataFrame(result_g)
            x = pd.to_datetime(boxpd[0])
            x = x.sort_index(ascending=False)
            
            y1 = boxpd[1]
            y1 = y1.sort_index(ascending=False)
            y2 = boxpd[2]
            y2 = y2.sort_index(ascending=False)
            
            #更新した値をグラフに代入
            ax1 = fig2.add_subplot(2, 1, 1)
            #ax1.set_ylim(89990,90020)
            ax1.xaxis.set_major_formatter(mdates.DateFormatter('%y/%m/%d\n%H:%M:%S'))
            ax1.plot(x,y1,label="okuri_velocity")
            ax1.legend(loc='lower left')
            ax1.grid(which='major',axis='y',color='black',
                    linestyle='-',linewidth=0.2)
            ax2 = fig2.add_subplot(2, 1, 2)
            ax2.xaxis.set_major_formatter(mdates.DateFormatter('%y/%m/%d\n%H:%M:%S'))
            ax2.plot(x,y2,label="hiki_velocity")
            ax2.legend(loc='lower left')
            ax2.grid(which='major',axis='y',color='black',
                    linestyle='-',linewidth=0.2)
            try:
                if b2_1=='' and b2_2=='' and b2_3=='' and b2_4=='':
                    ax1.set_ylim(0,100)
                    ax2.set_ylim(0,100)
                elif b2_1!='' and b2_2!='' and b2_3=='' and b2_4=='':
                    ax1.set_ylim(int(b2_1),int(b2_2))
                    ax2.set_ylim(0,100)
                elif b2_1=='' and b2_2=='' and b2_3!='' and b2_4!='':
                    ax1.set_ylim(0,100)
                    ax2.set_ylim(int(b2_3),int(b2_4))
                else:
                    ax1.set_ylim(int(b2_1),int(b2_2))
                    ax2.set_ylim(int(b2_3),int(b2_4))
            except:
                ax1.set_ylim(0,100)
                ax2.set_ylim(0,100)
                

            #Canvasのグラフに再描写する　1秒おきに以上を繰り返す
            fig2.canvas.draw()
            #print('test')
            print(2)
            sub_win2_id=root.after(1000,func_2)
        #plot_widget.grid()
        #plot_widget.grid(column=0,row=0)
        plot_widget.pack(side=tk.TOP,fill=tk.BOTH,expand=1)
        sub_win2.protocol('WM_DELETE_WINDOW', lambda:stop_func(sub_win2_id,sub_win2))
        sub_win2_id=root.after(1000,func_2)

def sub_window3():
    global sub_win3,sub_win3_id
    if sub_win3 == None or not sub_win3.winfo_exists():
        sub_win3 = tk.Toplevel()#(master=root)いらない
        sub_win3.geometry("600x300")
        
        #(1)figを生成します。
        #fig = plt.figure()#これを外で宣言したほうがいいかも？ 
        #(2) 実際のグラフを描画するAxesインスタスを生成
        ax1 = fig3.add_subplot(1, 1, 1)
        #label_sub = tk.Label(sub_win, text="サブウィンドウ")
        #label_sub.pack()
        canvas = FigureCanvasTkAgg(fig3, master=sub_win3)#(fig, master=root)
        #plot_widget = canvas.get_tk_widget(side=tk.TOP,fill=tk.BOTH,expand=1)
        #plot_widget = canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=1)
        plot_widget = canvas.get_tk_widget()
        def func_3():
            global sub_win3,sub_win3_id
            fig3.clf()# Clear figure グラフを消している

            conn = mydb.connect(
                    host='127.0.0.1',
                    port='3306',
                    user='root',
                    password='tkroyc123',
                    database='draw3'
                )
            cur = conn.cursor()
            tablename10='drawtable_'+todaydetail_str
            sql_1 = 'SELECT time,H1PV,H2PV,H3PV,`H4-1PV`,`H4-2PV`,`H4-3PV`,`H4-4PV`,H5PV,H6PV,H7PV from '+tablename10
            #sql_1 = 'SELECT time,H1PV,H2PV,H3PV,H5-2PV from '+tablename10
            sql_2=' order by id desc limit %s'
            sql_3 = sql_1+sql_2
            data = (int(5),)
            data=b3_0
            if b3_0=='':            
                data = (int(5),)
            else:
                data=(int(b3_0),)
            #print(sql_3)
            cur.execute(sql_3,data)
            result_g = cur.fetchall()
            cur.close()
            conn.close()
            
            boxpd = pd.DataFrame(result_g)
            #print(boxpd)
            x = pd.to_datetime(boxpd[0])
            x = x.sort_index(ascending=False)
            
            y1 = boxpd[1]
            y1 = y1.sort_index(ascending=False)
            y2 = boxpd[2]
            y2 = y2.sort_index(ascending=False)
            y3 = boxpd[3]
            y3 = y3.sort_index(ascending=False)
            y4 = boxpd[4]
            y4 = y4.sort_index(ascending=False)
            y5 = boxpd[5]
            y5 = y5.sort_index(ascending=False)
            y6 = boxpd[6]
            y6 = y6.sort_index(ascending=False)
            y7 = boxpd[7]
            y7 = y7.sort_index(ascending=False)
            y8 = boxpd[8]
            y8 = y8.sort_index(ascending=False)
            y9 = boxpd[9]
            y9 = y9.sort_index(ascending=False)
            y10 = boxpd[10]
            y10 = y10.sort_index(ascending=False)
            #print(y4)
            #更新した値をグラフに代入
            ax1 = fig3.add_subplot(2, 2, 1)
            #ax1.set_ylim(89990,90020)
            ax1.xaxis.set_major_formatter(mdates.DateFormatter('%y/%m/%d\n%H:%M:%S'))
            ax1.plot(x,y1,label="H1PV")
            ax1.plot(x,y2,label="H2PV")
            ax1.plot(x,y3,label="H3PV")
            ax1.legend(loc='lower left')
            ax1.grid(which='major',axis='y',color='black',
                    linestyle='-',linewidth=0.2)
            ax2 = fig3.add_subplot(2, 2, 2)
            ax2.xaxis.set_major_formatter(mdates.DateFormatter('%y/%m/%d\n%H:%M:%S'))
            ax2.plot(x,y4,label="H4-1PV")
            ax2.plot(x,y5,label="H4-2PV")
            ax2.plot(x,y6,label="H4-3PV")
            ax2.plot(x,y7,label="H4-4PV")
            ax2.legend(loc='lower left')
            ax2.grid(which='major',axis='y',color='black',
                    linestyle='-',linewidth=0.2)
            ax3 = fig3.add_subplot(2, 2, 3)
            ax3.xaxis.set_major_formatter(mdates.DateFormatter('%y/%m/%d\n%H:%M:%S'))
            ax3.plot(x,y8,label="H5MV")
            ax3.plot(x,y9,label="H6MV")
            ax3.plot(x,y10,label="H7MV")
            ax3.legend(loc='lower left')
            ax3.grid(which='major',axis='y',color='black',
                    linestyle='-',linewidth=0.2)
            # ax4 = fig3.add_subplot(2, 2, 4)
            # ax4.xaxis.set_major_formatter(mdates.DateFormatter('%y/%m/%d\n%H:%M:%S'))
            # ax4.plot(x,y8,label="H5MV")
            # ax4.plot(x,y9,label="H6MV")
            # ax4.plot(x,y10,label="H7MV")
            # ax4.legend(loc='lower left')
            # ax4.grid(which='major',axis='y',color='black',
            #         linestyle='-',linewidth=0.2)
            try:
                if b3_1=='' and b3_2=='':
                    ax1.set_ylim((min(pd.concat([y1,y2,y3])),max(pd.concat([y1,y2,y3]))))
                    ax2.set_ylim((min(pd.concat([y4,y5,y6,y7])),max(pd.concat([y4,y5,y6,y7]))))
                    ax3.set_ylim((min(pd.concat([y8,y9,y10])),max(pd.concat([y8,y9,y10]))))
                    #ax4.set_ylim((min(pd.concat([y8,y9,y10])),max(pd.concat([y8,y9,y10]))))
                else:
                    ax1.set_ylim(int(b3_1),int(b3_2))
                    ax2.set_ylim(int(b3_1),int(b3_2))
                    ax3.set_ylim(int(b3_1),int(b3_2))
                    #ax4.set_ylim(int(b3_1),int(b3_2))
            except:
                ax1.set_ylim((min(pd.concat([y1,y2,y3])),max(pd.concat([y1,y2,y3]))))
                ax2.set_ylim((min(pd.concat([y4,y5,y6,y7])),max(pd.concat([y4,y5,y6,y7]))))
                ax3.set_ylim((min(pd.concat([y8,y9,y10])),max(pd.concat([y8,y9,y10]))))
                #ax4.set_ylim((min(pd.concat([y8,y9,y10])),max(pd.concat([y8,y9,y10]))))
                

            #Canvasのグラフに再描写する　1秒おきに以上を繰り返す
            fig3.canvas.draw()
            print(3)
            sub_win3_id=root.after(1000,func_3)
        #plot_widget.grid()
        #plot_widget.grid(column=0,row=0)
        plot_widget.pack(side=tk.TOP,fill=tk.BOTH,expand=1)
        sub_win3.protocol('WM_DELETE_WINDOW', lambda:stop_func(sub_win3_id,sub_win3))
        sub_win3_id=root.after(1000,func_3)

def sub_window4():
    global sub_win4,sub_win4_id
    if sub_win4 == None or not sub_win4.winfo_exists():
        sub_win4 = tk.Toplevel()#(master=root)いらない
        sub_win4.geometry("600x300")
        
        #(1)figを生成します。
        #fig = plt.figure()#これを外で宣言したほうがいいかも？ 
        #(2) 実際のグラフを描画するAxesインスタスを生成
        ax1 = fig4.add_subplot(1, 1, 1)
        #label_sub = tk.Label(sub_win, text="サブウィンドウ")
        #label_sub.pack()
        canvas = FigureCanvasTkAgg(fig4, master=sub_win4)#(fig, master=root)
        #plot_widget = canvas.get_tk_widget(side=tk.TOP,fill=tk.BOTH,expand=1)
        #plot_widget = canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=1)
        plot_widget = canvas.get_tk_widget()
        def func_4():
            global sub_win4,sub_win4_id
            fig4.clf()# Clear figure グラフを消している

            conn = mydb.connect(
                    host='127.0.0.1',
                    port='3306',
                    user='root',
                    password='tkroyc123',
                    database='draw3'
                )
            cur = conn.cursor()
            tablename10='drawtable_'+todaydetail_str
            sql_1 = 'SELECT time,roshinkann_PV1,roshinkann_PV2,roshinkann_PV3,\
                roshinkann_PV4,roshinkann_PV5,roshinkann_PV6,roshinkann_PV7,\
                    roshinkann_PV8,roshinkann_PV9,roshinkann_PV10 from '+tablename10
            #sql_1 = 'SELECT time,H1PV,H2PV,H3PV,H5-2PV from '+tablename10
            sql_2=' order by id desc limit %s'
            sql_3 = sql_1+sql_2
            data = (int(5),)
            data=b4_0
            if b4_0=='':            
                data = (int(5),)
            else:
                data=(int(b4_0),)
            #print(sql_3)
            cur.execute(sql_3,data)
            result_g = cur.fetchall()
            cur.close()
            conn.close()
            
            boxpd = pd.DataFrame(result_g)
            #print(boxpd)
            x = pd.to_datetime(boxpd[0])
            x = x.sort_index(ascending=False)
            
            y1 = boxpd[1]
            y1 = y1.sort_index(ascending=False)
            y2 = boxpd[2]
            y2 = y2.sort_index(ascending=False)
            y3 = boxpd[3]
            y3 = y3.sort_index(ascending=False)
            y4 = boxpd[4]
            y4 = y4.sort_index(ascending=False)
            y5 = boxpd[5]
            y5 = y5.sort_index(ascending=False)
            y6 = boxpd[6]
            y6 = y6.sort_index(ascending=False)
            y7 = boxpd[7]
            y7 = y7.sort_index(ascending=False)
            y8 = boxpd[8]
            y8 = y8.sort_index(ascending=False)
            y9 = boxpd[9]
            y9 = y9.sort_index(ascending=False)
            y10 = boxpd[10]
            y10 = y10.sort_index(ascending=False)
            #print(y4)
            #更新した値をグラフに代入
            ax1 = fig4.add_subplot(2, 2, 1)
            #ax1.set_ylim(89990,90020)
            ax1.xaxis.set_major_formatter(mdates.DateFormatter('%y/%m/%d\n%H:%M:%S'))
            ax1.plot(x,y1,label="roshinkann_PV1")
            ax1.plot(x,y2,label="roshinkann_PV2")
            ax1.plot(x,y3,label="roshinkann_PV3")
            ax1.legend(loc='lower left')
            ax1.grid(which='major',axis='y',color='black',
                    linestyle='-',linewidth=0.2)
            ax2 = fig4.add_subplot(2, 2, 2)
            ax2.xaxis.set_major_formatter(mdates.DateFormatter('%y/%m/%d\n%H:%M:%S'))
            ax2.plot(x,y4,label="roshinkann_PV4")
            ax2.plot(x,y5,label="roshinkann_PV5")
            ax2.plot(x,y6,label="roshinkann_PV6")
            ax2.legend(loc='lower left')
            ax2.grid(which='major',axis='y',color='black',
                    linestyle='-',linewidth=0.2)
            ax3 = fig4.add_subplot(2, 2, 3)
            ax3.xaxis.set_major_formatter(mdates.DateFormatter('%y/%m/%d\n%H:%M:%S'))
            ax3.plot(x,y7,label="roshinkann_PV7")
            ax3.plot(x,y8,label="roshinkann_PV8")
            ax3.legend(loc='lower left')
            ax3.grid(which='major',axis='y',color='black',
                    linestyle='-',linewidth=0.2)
            ax4 = fig4.add_subplot(2, 2, 4)
            ax4.xaxis.set_major_formatter(mdates.DateFormatter('%y/%m/%d\n%H:%M:%S'))
            ax4.plot(x,y9,label="roshinkann_PV9")
            ax4.plot(x,y10,label="roshinkann_PV10")
            ax4.legend(loc='lower left')
            ax4.grid(which='major',axis='y',color='black',
                    linestyle='-',linewidth=0.2)
            # ax5 = fig4.add_subplot(3, 2, 5)
            # ax5.xaxis.set_major_formatter(mdates.DateFormatter('%y/%m/%d\n%H:%M:%S'))
            # ax5.plot(x,y9,label="roshinkann_PV9")
            # ax5.plot(x,y10,label="roshinkann_PV10")
            # ax5.legend(loc='lower left')
            # ax5.grid(which='major',axis='y',color='black',
            #         linestyle='-',linewidth=0.2)
            # ax6 = fig4.add_subplot(3, 2, 6)
            # ax6.xaxis.set_major_formatter(mdates.DateFormatter('%y/%m/%d\n%H:%M:%S'))
            # ax6.plot(x,y9,label="roshinkann_PV9")
            # ax6.plot(x,y10,label="roshinkann_PV10")
            # ax6.legend(loc='lower left')
            # ax6.grid(which='major',axis='y',color='black',
            #         linestyle='-',linewidth=0.2)
            try:
                if b4_1=='' and b4_2=='':
                    ax1.set_ylim((min(pd.concat([y1,y2,y3])),max(pd.concat([y1,y2,y3]))))
                    ax2.set_ylim((min(pd.concat([y4,y5,y6])),max(pd.concat([y4,y5,y6]))))
                    ax3.set_ylim((min(pd.concat([y7,y8])),max(pd.concat([y7,y8]))))
                    ax4.set_ylim((min(pd.concat([y9,y10])),max(pd.concat([y9,y10]))))
                    #ax5.set_ylim((min(pd.concat([y9,y10])),max(pd.concat([y9,y10]))))
                    # ax6.set_ylim((min(pd.concat([y9,y10])),max(pd.concat([y9,y10]))))
                else:
                    ax1.set_ylim(int(b4_1),int(b4_2))
                    ax2.set_ylim(int(b4_1),int(b4_2))
                    ax3.set_ylim(int(b4_1),int(b4_2))
                    ax4.set_ylim(int(b4_1),int(b4_2))
                    #ax5.set_ylim(int(b4_1),int(b4_2))
                    # ax6.set_ylim(int(b4_1),int(b4_2))
            except:
                ax1.set_ylim((min(pd.concat([y1,y2,y3])),max(pd.concat([y1,y2,y3]))))
                ax2.set_ylim((min(pd.concat([y4,y5,y6])),max(pd.concat([y4,y5,y6]))))
                ax3.set_ylim((min(pd.concat([y7,y8])),max(pd.concat([y7,y8]))))
                ax4.set_ylim((min(pd.concat([y9,y10])),max(pd.concat([y9,y10]))))
                #ax5.set_ylim((min(pd.concat([y9,y10])),max(pd.concat([y9,y10]))))
                # ax6.set_ylim((min(pd.concat([y9,y10])),max(pd.concat([y9,y10]))))
                

            #Canvasのグラフに再描写する　1秒おきに以上を繰り返す
            fig4.canvas.draw()
            print(4)
            sub_win4_id=root.after(1000,func_4)
        #plot_widget.grid()
        #plot_widget.grid(column=0,row=0)
        plot_widget.pack(side=tk.TOP,fill=tk.BOTH,expand=1)
        sub_win4.protocol('WM_DELETE_WINDOW', lambda:stop_func(sub_win4_id,sub_win4))
        sub_win4_id=root.after(1000,func_4)
# メインフレームの作成と設置
#frame = tk.Frame(root)
#frame.pack(fill = tk.BOTH, padx=5, pady=10)
# 各種ウィジェットの作成
#button = ttk.Button(frame, text="サブウィンドウ生成", command=sub_window)
# 各種ウィジェットの設置
#button.pack()
#print(sub_win)
# メニューの設定
m = tk.Menu(root)
root.configure(menu = m)
m.add_command(label = '(1)naigaikei', under = 0, command = sub_window)
m.add_command(label = '(2)okurihiki', under = 0, command = sub_window2)
m.add_command(label = '(3)H1_H7', under = 0, command = sub_window3)
m.add_command(label = '(4)roshinkann', under = 0, command = sub_window4)

# ラベルの設定
tk.Label(root, text = 'メニュー選択してね').pack()

label1=tk.Label(root,text='(1)')
label1_0=tk.Label(root,text='range')
label1_1=tk.Label(root,text='ymin1')
label1_2=tk.Label(root,text='ymax1')
label1_3=tk.Label(root,text='ymin2')
label1_4=tk.Label(root,text='ymax2')
label1.place(x=20,y=30)
label1_0.place(x=110,y=30)
label1_1.place(x=230,y=30)
label1_2.place(x=350,y=30)
label1_3.place(x=470,y=30)
label1_4.place(x=590,y=30)

label2=tk.Label(root,text='(2)')
label2_0=tk.Label(root,text='range')
label2_1=tk.Label(root,text='ymin1')
label2_2=tk.Label(root,text='ymax1')
label2_3=tk.Label(root,text='ymin2')
label2_4=tk.Label(root,text='ymax2')
label2.place(x=20,y=60)
label2_0.place(x=110,y=60)
label2_1.place(x=230,y=60)
label2_2.place(x=350,y=60)
label2_3.place(x=470,y=60)
label2_4.place(x=590,y=60)

label3=tk.Label(root,text='(3)')
label3_0=tk.Label(root,text='range')
label3_1=tk.Label(root,text='ymin')
label3_2=tk.Label(root,text='ymax')
label3.place(x=20,y=90)
label3_0.place(x=110,y=90)
label3_1.place(x=230,y=90)
label3_2.place(x=350,y=90)

label4=tk.Label(root,text='(4)')
label4_0=tk.Label(root,text='range')
label4_1=tk.Label(root,text='ymin')
label4_2=tk.Label(root,text='ymax')
label4.place(x=20,y=120)
label4_0.place(x=110,y=120)
label4_1.place(x=230,y=120)
label4_2.place(x=350,y=120)

#テキストボックスを作る
tbox1_0=tk.Entry(width=4)
tbox1_1=tk.Entry(width=4)
tbox1_2=tk.Entry(width=4)
tbox1_3=tk.Entry(width=4)
tbox1_4=tk.Entry(width=4)
tbox1_0.place(x=170,y=30)
tbox1_1.place(x=290,y=30)
tbox1_2.place(x=410,y=30)
tbox1_3.place(x=530,y=30)
tbox1_4.place(x=650,y=30)

tbox2_0=tk.Entry(width=4)
tbox2_1=tk.Entry(width=4)
tbox2_2=tk.Entry(width=4)
tbox2_3=tk.Entry(width=4)
tbox2_4=tk.Entry(width=4)
tbox2_0.place(x=170,y=60)
tbox2_1.place(x=290,y=60)
tbox2_2.place(x=410,y=60)
tbox2_3.place(x=530,y=60)
tbox2_4.place(x=650,y=60)

tbox3_0=tk.Entry(width=4)
tbox3_1=tk.Entry(width=4)
tbox3_2=tk.Entry(width=4)
tbox3_0.place(x=170,y=90)
tbox3_1.place(x=290,y=90)
tbox3_2.place(x=410,y=90)

tbox4_0=tk.Entry(width=4)
tbox4_1=tk.Entry(width=4)
tbox4_2=tk.Entry(width=4)
tbox4_0.place(x=170,y=120)
tbox4_1.place(x=290,y=120)
tbox4_2.place(x=410,y=120)

#ボタンクリックされた時の処理
b1_0=''
b1_1=''
b1_2=''
b1_3=''
b1_4=''
def ButtonBlick1():
    global b1_0,b1_1,b1_2,b1_3,b1_4
    b1_0=tbox1_0.get()
    b1_1=tbox1_1.get()
    b1_2=tbox1_2.get()
    b1_3=tbox1_3.get()
    b1_4=tbox1_4.get()
    print(sub_win)
    root.after_cancel(sub_win_id)
    print(sub_win_id)
    root.after_cancel(id)
    print(id)

b2_0=''    
b2_1=''
b2_2=''
b2_3=''
b2_4=''
def ButtonBlick2():
    global b2_0,b2_1,b2_2,b2_3,b2_4
    b2_0=tbox2_0.get()
    b2_1=tbox2_1.get()
    b2_2=tbox2_2.get()
    b2_3=tbox2_3.get()
    b2_4=tbox2_4.get()

b3_0=''    
b3_1=''
b3_2=''
def ButtonBlick3():
    global b3_0,b3_1,b3_2
    b3_0=tbox3_0.get()
    b3_1=tbox3_1.get()
    b3_2=tbox3_2.get()

b4_0=''    
b4_1=''
b4_2=''
def ButtonBlick4():
    global b4_0,b4_1,b4_2
    b4_0=tbox4_0.get()
    b4_1=tbox4_1.get()
    b4_2=tbox4_2.get()

#ボタンをつくる
button1=tk.Button(root,text='更新',command=ButtonBlick1)
button1.place(x=50,y=30)

button2=tk.Button(root,text='更新',command=ButtonBlick2)
button2.place(x=50,y=60)

button3=tk.Button(root,text='更新',command=ButtonBlick3)
button3.place(x=50,y=90)

button4=tk.Button(root,text='更新',command=ButtonBlick4)
button4.place(x=50,y=120)
root.mainloop()
# %%
