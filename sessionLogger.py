from tkinter import *
from tkinter import simpledialog
from time import time
import pandas as pd
"""
def printOption():
	label_var.set(str(var.get()))
    label_.pack(anchor='center')
    root.qitr+=1
"""
session_time = 0
local_time = 0
local_times = []
answers = []

def startGlobal():
	root.global_timer_s = time()
	root.local_timer_s = time()
	root.qitr = 1 	
def stopGlobal():
	root.global_timer_e = time()
	session_time = round((root.global_timer_e-root.global_timer_s),2)
	print(session_time)
	session_df = pd.DataFrame({"Answers":answers,"Time":local_times,"Total_Time":local_times})
	session_df["Total_Time"] = (session_time/60)
	answer = simpledialog.askstring("Input", "Session Name?",parent=root)
	session_df.to_csv("session_logs/"+answer+".csv")
def logQuestion():
    ques_label_var.set(str(root.qitr))
    ques_label.pack(anchor='w')
    root.qitr+=1
	
def getOptions():
	lb_index_tuple = list_button.curselection()
	selected_options = []
	for item in lb_index_tuple:
		selected_options.append(options[item])
	print(selected_options)
	answers.append(selected_options)
	root.local_timer_e = time()
	print("TIME")
	local_time = round((root.local_timer_e-root.local_timer_s),2)
	if local_time>60:
		local_time=local_time/60
	local_times.append(local_time)
	print(local_time)
	root.local_timer_s = time()
	list_button.selection_clear(0, 'end')
	logQuestion()

root =Tk()
root.local_timer_s = time()
root.local_timer_e = 0 
root.global_timer_s = time()
root.global_Timer_e = 0 

root.qitr = 1
ques_label_var=StringVar()
root.grid()
#root.geometry('500x800')
root.title('GRE Session')
var=StringVar()


ques_label = Label(root, textvariable=ques_label_var)
start_button = Button(root,text="START",command=startGlobal)
start_button.pack(anchor='w')
stop_button = Button(root,text="STOP",command=stopGlobal)
stop_button.pack(anchor='w')	
list_button = Listbox(root, selectmode = "multiple",height=7)
list_button.pack(anchor='e') 
options = ["A","B","C","D","E","F","NumEntry"]
for each_item in range(len(options)): 
    list_button.insert('end', options[each_item]) 
  

submit = Button(root,text="SUBMIT",command=getOptions)
submit.pack(anchor="e")
print(root.qitr)
root.mainloop()
print(var)

