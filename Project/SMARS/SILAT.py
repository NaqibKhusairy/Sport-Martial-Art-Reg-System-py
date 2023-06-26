import tkinter as prjk																		#Use tkinter library for Python GUI
from Kategory import ktgory as ctgory														#import term in ktgory.py from Kategory file
from tkinter import messagebox																#import messagebox from tkinter library
import mysql.connector																		#Imports MySQL Connector

def silat():																				#silat function
	def sltrst():																			#function sltrst
		name.delete(0,prjk.END)																#clear input in name Entry
		NrIc.delete(0,prjk.END)																#clear input in NrIc Entry
		EMail.delete(0,prjk.END)															#clear input in EMail Entry
		Phone.delete(0,prjk.END)															#clear input in Phone Entry
		Brt.delete(0,prjk.END)																#clear input in Brt Entry
		OutputFrm["text"]=""																#set text in OutputFrm to ""
		ktgotyLbl["text"]=""																#set text in ktgotyLbl to ""
		ktgotyDot["text"]=""																#set text in ktgotyDot to ""
		ktgoty["text"]=""																	#set text in ktgoty to ""
		OutputFrm.config(borderwidth=0)														#set border width to OutputFrm to 0

	def sltsbmt():																			#function sltsbmt
		OutputFrm["text"]="Your Category : "												#set text in OutputFrm
		OutputFrm.config(borderwidth=1)														#set border width to OutputFrm to 1
		ktgotyLbl["text"]="Category"														#set text in ktgotyLbl
		ktgotyDot["text"]=":"																#set text in ktgotyDot
		Nama=name.get()																		#get name from value in name Entry
		Ic=NrIc.get()																		#get Ic from value in NrIc Entry
		Mail=EMail.get()																	#get Mail from value in EMail Entry
		PhoneNum=Phone.get()																#get PhoneNum from value in Phone Entry
		Weight=float(Brt.get())																#get float Weight from value in Brt Entry
		try:																				#try to do
			Nama=Nama.upper()																#change name to upper
			year=int(Ic[0:2])																#get year from Ic parameter 0-2
			if year>=0 and year<=22:														#if year 0-22, do
				year+=2000																	#set year equal to year+2000
			else:																			#id year >22 , do
				year+=1900																	#set year equal to year+1900
			age=2023-year																	#set age = 2023 - year

			jntina=int(Ic)																	#get jntina from Ic
			jntina%=2																		#calculate jntina = jntina % 2
			if jntina == 0:																	#if jntina equal to 0, do
				gend="FEMALE"																#set gend to FEMALE
			else:																			#IF jntina not equal to 0, do
				gend="MALE"																	#set gend to MALE

			if Weight>=1000:																#if Weight > 1000, do
				Weight/=1000																#Set Weight equal to Weight/1000
			else:																			#if Weight < 1000
				Weight=Weight																#Set Weight = Weight

			category=ctgory.Slt(Weight)														#Set category and call Slt function from ctgory
			Weight="{:.2f}".format(Weight)													#Set Weight to 2 decimal point
			Weight=Weight+" kg"																#Set Weight to Weight+kg
			Ic=str(Ic)																		#Set Ic to string Ic
			age=str(age)																	#Set age to string age
			print("NAME         : "+Nama)													#print output
			print("AGE          : "+age)													#print output
			print("GENDER       : "+gend)													#print output
			print("NRIC         : "+Ic)														#print output
			print("EMAIL        : "+Mail)													#print output
			print("PHONE NUMBER : "+PhoneNum)												#print output
			print("WEIGHT       : "+Weight)													#print output
			print("CATEGORY     : "+category)												#print output
			ktgoty["text"]=category															#set text in ktgoty to value of category
			print()																			#print black space
		except:																				#if error , do
			Weight="Invalid"																#set Weight to invalid
			print("Weight "+Weight)															#print Weight invalid
			OutputFrm["text"]=""															#set text in OutputFrm to ""
			ktgotyLbl["text"]=""															#set text in ktgotyLbl to ""
			ktgotyDot["text"]=""															#set text in ktgotyDot to ""
			ktgoty["text"]=""																#set text in ktgoty to ""
			OutputFrm.config(borderwidth=0)													#set border width for OutputFrm to 0

		def cncl():																			#cncl function
			try:																			#try to do
				projectdatabase = mysql.connector.connect(									#connect to database
					host="localhost", 
					user="root", 
					password="", 
					database="smars")

				mydbse = projectdatabase.cursor()											#Instantiating a cursor for myprojectdb
				mydbse.execute("DELETE FROM silat WHERE nric=%s",							#Executing database query with parameters
					(Ic,))
				projectdatabase.commit()
				print(f"Your Registration Canceled")

			except mysql.connector.Error as err:											#if error , do
				print("Failed delete record : {}".format(err)+"\n")							#print error text

			messagebox.showinfo("Canceled","You canceled your Registration")				#show message box with text
			confwnds.withdraw()																#hide the confwnds
			wnds.withdraw()																	#hide the wnds

		def comfrm():																		#comfrm function
			def printrest():																#function printrest
				print("\n\n           ***** Recipt *****\n"+								#print text
					"***** Sports Martial Arts : "+SMA+" *****\n")
				print("\tNAME         : "+Nama)												#print output
				print("\tAGE          : "+age)												#print output
				print("\tGENDER       : "+gend)												#print output
				print("\tNRIC         : "+Ic)												#print output
				print("\tEMAIL        : "+Mail)												#print output
				print("\tPHONE NUMBER : "+PhoneNum)											#print output
				print("\tWEIGHT       : "+Weight)											#print output
				print("\tCATEGORY     : "+category)											#print output
				print("\n*****************************************\n")						#print star and new line

			def resit():																	#resit function
				rstwnds = prjk.Tk()															#Create Tkinter window
				rstwnds.geometry("315x420")													#Set winow size = 400 X 650
				rstwnds.title("Your Registration Resipt")									#Set title

				rstfrmlbl=prjk.Label(rstwnds,text="\n  *** Recipt ***\n"+					#Create Label
					"  *** Sports Martial Arts : "+SMA+" ***\n",
					font=("Times New Roman",13))
				rstfrmlbl.grid(row=0,column=0)												#set position with grid and padding

				DataFrame=prjk.LabelFrame(rstwnds,text="Your Information : ",				#Create frame with title
					padx=10,pady=10)
				DataFrame.grid(row=1,column=0,padx=10)										#set position with grid and padding

				nLbl=prjk.Label(DataFrame,text="NAME")										#Create Label for NAME
				nLbl.grid(row=0,column=0,padx=5,pady=5)										#set position with grid and padding
				nDot=prjk.Label(DataFrame,text=" : ")										#Create Label for :
				nDot.grid(row=0,column=1,padx=5,pady=5)										#set position with grid and padding
				n=prjk.Entry(DataFrame)														#Create n Entry
				n.insert(prjk.END,Nama)														#insert Nama to n Entry
				n.config(state='disable')													#make n Entrty disable
				n.grid(row=0,column=2,padx=5,pady=5)										#set position with grid and padding

				aLbl=prjk.Label(DataFrame,text="AGE")										#Create Label for AGE
				aLbl.grid(row=1,column=0,padx=5,pady=5)										#set position with grid and padding
				aDot=prjk.Label(DataFrame,text=" : ")										#Create Label for :
				aDot.grid(row=1,column=1,padx=5,pady=5)										#set position with grid and padding
				a=prjk.Entry(DataFrame)														#Create a Entry
				a.insert(prjk.END,age)														#insert age to a Entry
				a.config(state='disable')													#make a Entrty disable
				a.grid(row=1,column=2,padx=5,pady=5)										#set position with grid and padding

				gLbl=prjk.Label(DataFrame,text="GENDER")									#Create Label for GENDER
				gLbl.grid(row=2,column=0,padx=5,pady=5)										#set position with grid and padding
				gDot=prjk.Label(DataFrame,text=" : ")										#Create Label for :
				gDot.grid(row=2,column=1,padx=5,pady=5)										#set position with grid and padding
				g=prjk.Entry(DataFrame)														#Create a Entry
				g.insert(prjk.END,gend)														#insert gend to a Entry
				g.config(state='disable')													#make a Entrty disable
				g.grid(row=2,column=2,padx=5,pady=5)										#set position with grid and padding

				nLbl=prjk.Label(DataFrame,text="NRIC")										#Create Label for  NRIC
				nLbl.grid(row=3,column=0,padx=5,pady=5)										#set position with grid and padding
				nDot=prjk.Label(DataFrame,text=" : ")										#Create Label for :
				nDot.grid(row=3,column=1,padx=5,pady=5)										#set position with grid and padding
				n=prjk.Entry(DataFrame)														#Create n Entry
				n.insert(prjk.END,str(Ic))													#insert string Ic to n Entry
				n.config(state='disable')													#make n Entrty disable
				n.grid(row=3,column=2,padx=5,pady=5)										#set position with grid and padding

				eLbl=prjk.Label(DataFrame,text="E-MAIL")									#Create Label for E-MAIL
				eLbl.grid(row=4,column=0,padx=5,pady=5)										#set position with grid and padding
				eDot=prjk.Label(DataFrame,text=" : ")										#Create Label for :
				eDot.grid(row=4,column=1,padx=5,pady=5)										#set position with grid and padding
				e=prjk.Entry(DataFrame)														#Create e Entry
				e.insert(prjk.END,Mail)														#insert Mail to e Entry
				e.config(state='disable')													#make e Entrty disable
				e.grid(row=4,column=2,padx=5,pady=5)										#set position with grid and padding

				pLbl=prjk.Label(DataFrame,text="PHONE NUMBER")								#Create Label for PHONE NUMBER
				pLbl.grid(row=5,column=0,padx=5,pady=5)										#set position with grid and padding
				pDot=prjk.Label(DataFrame,text=" : ")										#Create Label for :
				pDot.grid(row=5,column=1,padx=5,pady=5)										#set position with grid and padding
				p=prjk.Entry(DataFrame)														#Create p Entry
				p.insert(prjk.END,PhoneNum)													#insert PhoneNum to p Entry
				p.config(state='disable')													#make p Entrty disable
				p.grid(row=5,column=2,padx=5,pady=5)										#set position with grid and padding

				wLbl=prjk.Label(DataFrame,text="WEIGHT")									#Create Label for WEIGHT
				wLbl.grid(row=6,column=0,padx=5,pady=5)										#set position with grid and padding
				wDot=prjk.Label(DataFrame,text=" : ")										#Create Label for :
				wDot.grid(row=6,column=1,padx=5,pady=5)										#set position with grid and padding
				w=prjk.Entry(DataFrame)														#Create w Entry
				w.insert(prjk.END,Weight)													#insert Weight to w Entry
				w.config(state='disable')													#make w Entrty disable
				w.grid(row=6,column=2,padx=5,pady=5)										#set position with grid and padding

				cLbl=prjk.Label(DataFrame,text="CATEGORY")									#Create Label for CATEGORY
				cLbl.grid(row=7,column=0,padx=5,pady=5)										#set position with grid and padding
				cDot=prjk.Label(DataFrame,text=" : ")										#Create Label for :
				cDot.grid(row=7,column=1,padx=5,pady=5)										#set position with grid and padding
				c=prjk.Entry(DataFrame)														#Create c Entry
				c.insert(prjk.END,category)													#insert category to c Entry
				c.config(state='disable')													#make c Entrty disable
				c.grid(row=7,column=2,padx=5,pady=5)										#set position with grid and padding

				rstwnds.mainloop()															#Exercute rstwnds event loop
			print("You Successfully Registered in "+SMA+"\n")								#print text
			messagebox.showinfo("Successfully","Your data inserted successfully")			#show message box with text
			confwnds.withdraw()																#hide the confwnds
			wnds.withdraw()																	#hide the wnds
			printrest()																		#call printrest function
			resit()																			#call resit function
			
		print("Please Confirm Your Data\n")													#print text
		confwnds = prjk.Tk()																#Create Tkinter window
		confwnds.geometry("375x450")														#Set winow size = 400 X 650
		confwnds.title("Confirm Your Data")													#Set title
		confwnds.configure(bg="#faf8f5")													#Set Background color

		confrmlbl=prjk.Label(confwnds,text="\n  *** Please Confirm Your Data ***\n"+		#Create Label
			"  Sports Martial Arts : Silat\n",
			bg="#faf8f5",font=("Times New Roman",18))
		confrmlbl.grid(row=0,column=0)														#set position with grid and padding

		DataFrame=prjk.LabelFrame(confwnds,text="Your Information : ",						#Create frame with title
			padx=10,pady=10,bg="#faf8f5")
		DataFrame.grid(row=1,column=0,padx=10)												#set position with grid and padding

		nLbl=prjk.Label(DataFrame,text="NAME", bg="#faf8f5")								#Create Label for NAME
		nLbl.grid(row=0,column=0,padx=5,pady=5)												#set position with grid and padding
		nDot=prjk.Label(DataFrame,text=" : ", bg="#faf8f5")									#Create Label for :
		nDot.grid(row=0,column=1,padx=5,pady=5)												#set position with grid and padding
		n=prjk.Entry(DataFrame)																#Create n Entry
		n.insert(prjk.END,Nama)																#insert Nama to n Entry
		n.config(state='disable')															#make n Entrty disable
		n.grid(row=0,column=2,padx=5,pady=5)												#set position with grid and padding

		aLbl=prjk.Label(DataFrame,text="AGE", bg="#faf8f5")									#Create Label for AGE
		aLbl.grid(row=1,column=0,padx=5,pady=5)												#set position with grid and padding
		aDot=prjk.Label(DataFrame,text=" : ", bg="#faf8f5")									#Create Label for :
		aDot.grid(row=1,column=1,padx=5,pady=5)												#set position with grid and padding
		a=prjk.Entry(DataFrame)																#Create a Entry
		a.insert(prjk.END,age)																#insert age to a Entry
		a.config(state='disable')															#make a Entrty disable
		a.grid(row=1,column=2,padx=5,pady=5)												#set position with grid and padding

		gLbl=prjk.Label(DataFrame,text="GENDER", bg="#faf8f5")								#Create Label for GENDER
		gLbl.grid(row=2,column=0,padx=5,pady=5)												#set position with grid and padding
		gDot=prjk.Label(DataFrame,text=" : ", bg="#faf8f5")									#Create Label for :
		gDot.grid(row=2,column=1,padx=5,pady=5)												#set position with grid and padding
		g=prjk.Entry(DataFrame)																#Create a Entry
		g.insert(prjk.END,gend)																#insert gend to a Entry
		g.config(state='disable')															#make a Entrty disable
		g.grid(row=2,column=2,padx=5,pady=5)												#set position with grid and padding

		nLbl=prjk.Label(DataFrame,text="NRIC", bg="#faf8f5")								#Create Label for  NRIC
		nLbl.grid(row=3,column=0,padx=5,pady=5)												#set position with grid and padding
		nDot=prjk.Label(DataFrame,text=" : ", bg="#faf8f5")									#Create Label for :
		nDot.grid(row=3,column=1,padx=5,pady=5)												#set position with grid and padding
		n=prjk.Entry(DataFrame)																#Create n Entry
		n.insert(prjk.END,str(Ic))															#insert string Ic to n Entry
		n.config(state='disable')															#make n Entrty disable
		n.grid(row=3,column=2,padx=5,pady=5)												#set position with grid and padding

		eLbl=prjk.Label(DataFrame,text="E-MAIL", bg="#faf8f5")								#Create Label for E-MAIL
		eLbl.grid(row=4,column=0,padx=5,pady=5)												#set position with grid and padding
		eDot=prjk.Label(DataFrame,text=" : ", bg="#faf8f5")									#Create Label for :
		eDot.grid(row=4,column=1,padx=5,pady=5)												#set position with grid and padding
		e=prjk.Entry(DataFrame)																#Create e Entry
		e.insert(prjk.END,Mail)																#insert Mail to e Entry
		e.config(state='disable')															#make e Entrty disable
		e.grid(row=4,column=2,padx=5,pady=5)												#set position with grid and padding

		pLbl=prjk.Label(DataFrame,text="PHONE NUMBER", bg="#faf8f5")						#Create Label for PHONE NUMBER
		pLbl.grid(row=5,column=0,padx=5,pady=5)												#set position with grid and padding
		pDot=prjk.Label(DataFrame,text=" : ", bg="#faf8f5")									#Create Label for :
		pDot.grid(row=5,column=1,padx=5,pady=5)												#set position with grid and padding
		p=prjk.Entry(DataFrame)																#Create p Entry
		p.insert(prjk.END,PhoneNum)															#insert PhoneNum to p Entry
		p.config(state='disable')															#make p Entrty disable
		p.grid(row=5,column=2,padx=5,pady=5)												#set position with grid and padding

		wLbl=prjk.Label(DataFrame,text="WEIGHT", bg="#faf8f5")								#Create Label for WEIGHT
		wLbl.grid(row=6,column=0,padx=5,pady=5)												#set position with grid and padding
		wDot=prjk.Label(DataFrame,text=" : ", bg="#faf8f5")									#Create Label for :
		wDot.grid(row=6,column=1,padx=5,pady=5)												#set position with grid and padding
		w=prjk.Entry(DataFrame)																#Create w Entry
		w.insert(prjk.END,Weight)															#insert Weight to w Entry
		w.config(state='disable')															#make w Entrty disable
		w.grid(row=6,column=2,padx=5,pady=5)												#set position with grid and padding

		cLbl=prjk.Label(DataFrame,text="CATEGORY", bg="#faf8f5")							#Create Label for CATEGORY
		cLbl.grid(row=7,column=0,padx=5,pady=5)												#set position with grid and padding
		cDot=prjk.Label(DataFrame,text=" : ", bg="#faf8f5")									#Create Label for :
		cDot.grid(row=7,column=1,padx=5,pady=5)												#set position with grid and padding
		c=prjk.Entry(DataFrame)																#Create c Entry
		c.insert(prjk.END,category)															#insert category to c Entry
		c.config(state='disable')															#make c Entrty disable
		c.grid(row=7,column=2,padx=5,pady=5)												#set position with grid and padding

		FrameBtn=prjk.Frame(confwnds,padx=10,bg="#faf8f5")									#Create frame
		FrameBtn.grid(row=2,column=0,padx=10,pady=10)										#set position with grid and padding

		BtnSub=prjk.Button(FrameBtn,text="CONFIRM",command=comfrm)							#Create Confirm button
		BtnSub.grid(row=0,column=0,padx=5)													#set position with grid and padding

		BtnCncl=prjk.Button(FrameBtn,text="CANCEL",command=cncl)							#Create Cancel button
		BtnCncl.grid(row=0,column=1,padx=5)													#set position with grid and padding

		SMA="Silat"																			#Set SMA = Muay Thai
		try:																				#try to do
			projectdatabase = mysql.connector.connect(										#connect to database
				host="localhost", 
				user="root", 
				password="", 
				database="smars")

			mydbse = projectdatabase.cursor()												#Instantiating a cursor for myprojectdb
			mydbse.execute("SELECT * FROM silat WHERE nric=%s",								#Executing database query with parameters
				(Ic,))
			sameinpt=mydbse.fetchone()														#Fetching one row from database

			if sameinpt:																	#if sameinpt, do
				print("You Already Registered in "+SMA+"\n")								#print text
				messagebox.showinfo("Registered","You Already Registered in "				#show message box with text
					+SMA)
				confwnds.withdraw()															#hide the confwnds
				wnds.withdraw()																#hide the wnds
			else:																			#if not sameinpt, do
				mydbse.execute("INSERT INTO silat"											#insert data into customers table
					"(nama,age,nric,gender,email,phonenum,weight,category)"
					"VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
					(Nama,age,Ic,gend,Mail,PhoneNum,Weight,category))
				projectdatabase.commit()													#Save changes to database
			
		except mysql.connector.Error as err:												#if error , do
			print("Failed Insert data : {}".format(err)+"\n")								#print error text

	wnds=prjk.Tk()																			#Create Tkinter window
	wnds.geometry("444x420")																#Set winow size = 400 X 650
	wnds.title("Silat Registration System")													#Set title
	wnds.configure(bg="#faf8f5")															#Set Background color

	wlcm=prjk.Label(wnds,text="\n  ***Welcome To Silat Registration System***\n",			#Create Label
		bg="#faf8f5",font=("Times New Roman",14))
	wlcm.grid(row=0,column=0)																#set position with grid and padding

	FillFrm=prjk.LabelFrame(wnds, text="Fill Your Information Here : ",						#Create frame with title
		padx=10, pady=10, bg="#faf8f5")
	FillFrm.grid(row=1,column=0,padx=10)													#set position with grid and padding

	nameLbl=prjk.Label(FillFrm,text="NAME", bg="#faf8f5")									#Create Label for NAME
	nameLbl.grid(row=0,column=0,padx=5,pady=5)												#set position with grid and padding
	nameDot=prjk.Label(FillFrm,text=" : ", bg="#faf8f5")									#Create Label for :
	nameDot.grid(row=0,column=1,padx=5,pady=5)												#set position with grid and padding
	name=prjk.Entry(FillFrm)																#Create name Entry
	name.grid(row=0,column=2,padx=5,pady=5)													#set position with grid and padding

	NrIcLbl=prjk.Label(FillFrm,text="NRIC", bg="#faf8f5")									#Create Label for  NRIC
	NrIcLbl.grid(row=1,column=0,padx=5,pady=5)												#set position with grid and padding
	NrIcDot=prjk.Label(FillFrm,text=" : ", bg="#faf8f5")									#Create Label for :
	NrIcDot.grid(row=1,column=1,padx=5,pady=5)												#set position with grid and padding
	NrIc=prjk.Entry(FillFrm)																#Create NrIc Entry
	NrIc.grid(row=1,column=2,padx=5,pady=5)													#set position with grid and padding
	NrIcex=prjk.Label(FillFrm,text="Example : 010203040506",								#Create Label for  Example
		bg="#faf8f5",font=("Times New Roman",9))
	NrIcex.grid(row=1,column=3,padx=5,pady=5)												#set position with grid and padding

	EMailLbl=prjk.Label(FillFrm,text="E-MAIL", bg="#faf8f5")								#Create Label for E-MAIL
	EMailLbl.grid(row=2,column=0,padx=5,pady=5)												#set position with grid and padding
	EMailDot=prjk.Label(FillFrm,text=" : ", bg="#faf8f5")									#Create Label for :
	EMailDot.grid(row=2,column=1,padx=5,pady=5)												#set position with grid and padding
	EMail=prjk.Entry(FillFrm)																#Create EMail Entry
	EMail.grid(row=2,column=2,padx=5,pady=5)												#set position with grid and padding

	PhoneLbl=prjk.Label(FillFrm,text="PHONE NUMBER", bg="#faf8f5")							#Create Label for PHONE NUMBER
	PhoneLbl.grid(row=3,column=0,padx=5,pady=5)												#set position with grid and padding
	PhoneDot=prjk.Label(FillFrm,text=" : ", bg="#faf8f5")									#Create Label for :
	PhoneDot.grid(row=3,column=1,padx=5,pady=5)												#set position with grid and padding
	Phone=prjk.Entry(FillFrm)																#Create Phone Entry
	Phone.grid(row=3,column=2,padx=5,pady=5)												#set position with grid and padding

	BrtLbl=prjk.Label(FillFrm,text="WEIGHT", bg="#faf8f5")									#Create Label for WEIGHT
	BrtLbl.grid(row=4,column=0,padx=5,pady=5)												#set position with grid and padding
	BrtDot=prjk.Label(FillFrm,text=" : ", bg="#faf8f5")										#Create Label for :
	BrtDot.grid(row=4,column=1,padx=5,pady=5)												#set position with grid and padding
	Brt=prjk.Entry(FillFrm)																	#Create Brt Entry
	Brt.grid(row=4,column=2,padx=5,pady=5)													#set position with grid and padding

	BtnFrm=prjk.Frame(wnds,padx=10,bg="#faf8f5")											#Create frame
	BtnFrm.grid(row=5,column=0,padx=10,pady=10)												#set position with grid and padding

	submitBtn=prjk.Button(BtnFrm,text="SUBMIT",command=sltsbmt)								#Create Submit button
	submitBtn.grid(row=0,column=0,padx=5)													#set position with grid and padding

	rstBtn=prjk.Button(BtnFrm,text="RESET",command=sltrst)									#Create Reset button
	rstBtn.grid(row=0,column=1,padx=5)														#set position with grid and padding

	OutputFrm=prjk.LabelFrame(wnds,															#Create frame with title
	text="",borderwidth=0,
	padx=10,pady=10,bg="#faf8f5")
	OutputFrm.grid(row=6,column=0,padx=10)													#set position with grid and padding

	ktgotyLbl=prjk.Label(OutputFrm,text="",													#Create Label
	bg="#faf8f5")
	ktgotyLbl.grid(row=0,column=0,padx=5,pady=5)											#set position with grid and padding
	ktgotyDot=prjk.Label(OutputFrm,text="",													#Create Label
	bg="#faf8f5")
	ktgotyDot.grid(row=0,column=1,padx=5,pady=5)											#set position with grid and padding
	ktgoty=prjk.Label(OutputFrm,text="",													#Create Label
	bg="#faf8f5")
	ktgoty.grid(row=0,column=2,padx=5,pady=5)												#set position with grid and padding

	wnds.mainloop()																			#Exercute rstwnds event loop