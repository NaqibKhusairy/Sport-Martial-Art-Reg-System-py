import tkinter as prjk																	#Use tkinter library for Python GUI
from Kategory import ktgory as ctgory													#import term in ktgory.py from Kategory file
from tkinter import messagebox															#import messagebox from tkinter library
import mysql.connector																	#Imports MySQL Connector

def karte():																			#karte function
	print("KARATE clicked!\n")															#print text
	try:																				#try to do,
		from Database import KARATE as cdatabase										#import term in KARATE.py from Database file
		cdatabase.dtaSQL()																#call function dtaSQL from cdatabase
	except:																				#if error, do
		print("Error in Database\n")													#print text
	from SMARS import KARATE as KARATE													#import term in KARATE.py from SMARS file
	KARATE.krt()																		#call krt funtion from KARATE

def twndo():																			#twndo function
	print("TAEKWONDO clicked!\n")														#print text
	try:																				#try to do,
		from Database import TAEKWONDO as cdatabase										#import term in TAEKWONDO.py from Database file
		cdatabase.dtaSQL()																#call function dtaSQL from cdatabase
	except:																				#if error, do
		print("Error in Database\n")													#print text
	from SMARS import TAEKWONDO as TAEKWONDO											#import term in TAEKWONDO.py from SMARS file
	TAEKWONDO.taekwondo()																#call taekwondo funtion from TAEKWONDO

def myt():																				#myt function
	print("MUAYTHAI clicked!\n")														#print text
	try:																				#try to do,
		from Database import MUAYTHAI as cdatabase										#import term in MUAYTHAI.py from Database file
		cdatabase.dtaSQL()																#call function dtaSQL from cdatabase
	except:																				#if error, do
		print("Error in Database\n")													#print text
	from SMARS import MUAYTHAI as MUAYTHAI												#import term in MUAYTHAI.py from SMARS file
	MUAYTHAI.mt()																		#call mt funtion from MUAYTHAI

def slt():																				#slt function
	print("SILAT clicked!\n")															#print text
	try:																				#try to do,
		from Database import SILAT as cdatabase											#import term in SILAT.py from Database file
		cdatabase.dtaSQL()																#call function dtaSQL from cdatabase
	except:																				#if error, do
		print("Error in Database\n")													#print text
	from SMARS import SILAT as SILAT													#import term in SILAT.py from SMARS file
	SILAT.silat()																		#call silat funtion from SILAT

def bxng():																				#bxng function
	print("BOXING clicked!\n")															#print text
	try:																				#try to do,
		from Database import BOXING as cdatabase										#import term in BOXING.py from Database file
		cdatabase.dtaSQL()																#call function dtaSQL from cdatabase
	except:																				#if error, do
		print("Error in Database\n")													#print text
	from SMARS import BOXING as BOXING													#import term in BOXING.py from SMARS file
	BOXING.bx()																			#call bx funtion from BOXING

def mMa():																				#mMa function
	print("MMA clicked!\n")																#print text
	try:																				#try to do,
		from Database import MMA as cdatabase											#import term in MMA.py from Database file
		cdatabase.dtaSQL()																#call function dtaSQL from cdatabase
	except:																				#if error, do
		print("Error in Database\n")													#print text
	from SMARS import MMA as MMA														#import term in MMA.py from SMARS file
	MMA.mma()																			#call mma funtion from MMA

projekwnds = prjk.Tk()																	#Create Tkinter window
projekwnds.geometry("400x650")															#Set winow size = 400 X 650
projekwnds.title("Sport Martial Arts Registration System")								#Set title

canvas = prjk.Canvas(projekwnds, width=400, height=630)									#Create canvas with size = 400 X 650
canvas.pack()																			#Displays the canvas on the screen
bground = prjk.PhotoImage(file="img_gif/bg.gif")										#Create PhotoImage use img drom file img_gif
canvas.create_image(0, 0, anchor="nw", image=bground)									#Create image background use canvas

wlcm = prjk.Label(canvas, text="***Welcome To Sport Martial Arts Registration***\n"+	#Create Label
	"Please Choose Your Sport Martial Arts :-",
                 font=("Times New Roman", 14))
wlcm.grid(row=0, column=0,columnspan=2)													#set position with grid and padding

bphoto = prjk.PhotoImage(file="img_gif/boxing.gif")										#Create PhotoImage use img drom file img_gif
kphoto = prjk.PhotoImage(file="img_gif/karate.gif")										#Create PhotoImage use img drom file img_gif
mmphoto = prjk.PhotoImage(file="img_gif/mma.gif")										#Create PhotoImage use img drom file img_gif
mtphoto = prjk.PhotoImage(file="img_gif/muaythai.gif")									#Create PhotoImage use img drom file img_gif
sphoto = prjk.PhotoImage(file="img_gif/silat.gif")										#Create PhotoImage use img drom file img_gif
tphoto = prjk.PhotoImage(file="img_gif/taekwando.gif")									#Create PhotoImage use img drom file img_gif

kbtn = prjk.Button(canvas, image=kphoto, command=karte)									#Create Button with image
kbtn.grid(row=1, column=0)																#set position with grid and padding

tbtn = prjk.Button(canvas, image=tphoto, command=twndo)									#Create Button with image
tbtn.grid(row=1, column=1)																#set position with grid and padding

kbtn = prjk.Button(canvas, text="KARATE",												#Create Button with text
                 font=("Times New Roman", 9), command=karte)
kbtn.grid(row=2, column=0)																#set position with grid and padding

tbtn = prjk.Button(canvas, text="TAEKWONDO",											#Create Button with text
                 font=("Times New Roman", 9), command=twndo)
tbtn.grid(row=2, column=1)																#set position with grid and padding

mtbtn= prjk.Button(canvas, image=mtphoto, command=myt)									#Create Button with image
mtbtn.grid(row=3, column=0)																#set position with grid and padding

sbtn = prjk.Button(canvas, image=sphoto, command=slt)									#Create Button with image
sbtn.grid(row=3, column=1)																#set position with grid and padding

mtbtn = prjk.Button(canvas, text="MUAYTHAI",											#Create Button with text
                 font=("Times New Roman", 9), command=myt)
mtbtn.grid(row=4, column=0)																#set position with grid and padding

sbtn = prjk.Button(canvas, text="SILAT",												#Create Button with text
                 font=("Times New Roman", 9), command=slt)
sbtn.grid(row=4, column=1)																#set position with grid and padding

bbtn= prjk.Button(canvas, image=bphoto, command=bxng)									#Create Button with image
bbtn.grid(row=5, column=0)																#set position with grid and padding

mmbtn = prjk.Button(canvas, image=mmphoto, command=mMa)									#Create Button with image
mmbtn.grid(row=5, column=1)																#set position with grid and padding

bbtn = prjk.Button(canvas, text="BOXING",												#Create Button with text
                 font=("Times New Roman", 9), command=bxng)
bbtn.grid(row=6, column=0)																#set position with grid and padding

mmbtn = prjk.Button(canvas, text="MMA",													#Create Button with text
                 font=("Times New Roman", 9), command=mMa)
mmbtn.grid(row=6, column=1)																#set position with grid and padding

projekwnds.mainloop()																	#Exercute projectwnds event loop