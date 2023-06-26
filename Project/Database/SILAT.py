import mysql.connector														#Imports MySQL Connector

def dtaSQL():																#dtaSQL funtion
	mydb = mysql.connector.connect(											#connect to database
		host="localhost", 
		user="root", 
		password="")
	
	myprojectdb = mydb.cursor()												#Instantiating a cursor for myprojectdb
	myprojectdb.execute("CREATE DATABASE IF NOT EXISTS smars")				#Create database if not exixts

	try:																	#try to do
		projectdatabase = mysql.connector.connect(							#connect to abc_company database
			host="localhost", 
			user="root", 
			password="", 
			database="smars")

		mydbse = projectdatabase.cursor()									#Instantiating a cursor for mydbse
		mydbse.execute("CREATE TABLE IF NOT EXISTS silat "					#Create table silat if not exixts
			"(nama VARCHAR(200), "
			"age INT, nric VARCHAR(12), gender VARCHAR(6), "
			"email VARCHAR(200), "
			"phonenum VARCHAR(15), "
			"weight VARCHAR(100), "
			"category VARCHAR(100))")
	except mysql.connector.Error as err:									#if error , do
		print("Error creating table: {}".format(err))						#print error text
		