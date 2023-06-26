def Krt(Weight):										#Krt function with variable Weight
	if Weight <=55:										#if Weight <=55 , do
		category="55kg"									#Set category = 55kg
	elif Weight >=56 and Weight<=60:					#if Weight 56 - 60 , do
		category="60kg"									#Set category = 60kg
	elif Weight >=61 and Weight<=70:					#if Weight 61 - 70 , do
		category="70kg"									#Set category = 70kg
	elif Weight >=71 and Weight<=75:					#if Weight 71 - 75 , do
		category="75kg"									#Set category = 75kg
	elif Weight >=76 and Weight<=80:					#if Weight 76 - 80 , do
		category="80kg"									#Set category = 80kg
	else:												#if Weight >80 , do
		category="+80kg"								#Set category = +80kg
		
	return category										#return category value

def Twdo(Weight):										#Twdo function with variable Weight
	if Weight <54:										#if Weight <54 , do
		category="Fin (-54kg)"							#Set category = Fin (-54kg)
	elif Weight >=54 and Weight<=58:					#if Weight 54 - 58 , do
		category="Fly (54kg - 58kg)"					#Set category = Fly (54kg - 58kg)
	elif Weight >58 and Weight<=62:						#if Weight 58 - 62 , do
		category="Bantam (59kg - 62kg)"					#Set category = Bantam (59kg - 62kg)
	elif Weight >62 and Weight<=67:						#if Weight 62 - 67 , do
		category="Feather (63kg - 67kg)"				#Set category = Feather (63kg - 67kg)
	elif Weight >69 and Weight<=72:						#if Weight 69 - 72 , do
		category="Light (68kg - 72kg)"					#Set category = Light (68kg - 72kg)
	elif Weight >72 and Weight<=78:						#if Weight 72 - 78 , do
		category="Welter (73kg - 78kg)"					#Set category = Welter (73kg - 78kg)
	elif Weight >78 and Weight<=84:						#if Weight 78 - 84 , do
		category="Middle (79kg - 84kg)"					#Set category = Middle (79kg - 84kg)
	else:												#if Weight >84 , do
		category="Heavy (+84kg)"						#Set category = Heavy (+84kg)
		
	return category										#return category value

def Mythai(Weight):										#Mythai function with variable Weight
	if Weight >=74:										#if Weight >=74 , do
		category="Heavyweight (+74kg)"					#Set category = Heavyweight (+74kg)
	elif Weight >=68 and Weight<=73:					#if Weight 68 - 73 , do
		category="Middleweight (68kg - 73kg)"			#Set category = Middleweight (68kg - 73kg)
	elif Weight >=64 and Weight<=67:					#if Weight 64 - 67 , do
		category="Welterweight (64kg - 67kg)"			#Set category = Welterweight (64kg - 67kg)
	elif Weight >=59 and Weight<=63:					#if Weight 59 - 63 , do
		category="Lightweight (59kg - 63kg)"			#Set category = Lightweight (59kg - 63kg)
	elif Weight >=55 and Weight<=58:					#if Weight 55 - 58 , do
		category="Featherweight (55kg - 58kg)"			#Set category = Featherweight (55kg - 58kg)
	elif Weight >=52 and Weight<=54:					#if Weight 52 - 54 , do
		category="Bantamweight (52kg - 54kg)"			#Set category = Bantamweight (52kg - 54kg)
	elif Weight >=49 and Weight<=51:					#if Weight 49 - 51 , do
		category="Flyweight (49kg - 51kg)"				#Set category = Flyweight (49kg - 51kg)
	else:												#if Weight <49 , do
		category="Mini Flyweigh (-48kg)"				#Set category = Mini Flyweigh (-48kg)
		
	return category										#return category value

def Slt(Weight):										#Slt function with variable Weight
	if Weight <=49:										#if Weight <=49 , do
		category="Class A (-49kg)"						#Set category = Class A (-49kg)
	elif Weight >=50 and Weight<=55:					#if Weight 50 - 55 , do
		category="Class B (50kg - 55kg)"				#Set category = Class B (50kg - 55kg)
	elif Weight >=56 and Weight<=60:					#if Weight 56 - 60 , do
		category="Class C (56kg - 60kg)"				#Set category = Class C (56kg - 60kg)
	elif Weight >=61 and Weight<=65:					#if Weight 61 - 65 , do
		category="Class D (61kg - 65kg)"				#Set category = Class D (61kg - 65kg)
	elif Weight >=66 and Weight<=70:					#if Weight 66 - 70 , do
		category="Class E (66kg - 70kg)"				#Set category = Class E (66kg - 70kg)
	elif Weight >=71 and Weight<=75:					#if Weight 71 - 75 , do
		category="Class F (71kg - 75kg)"				#Set category = Class F (71kg - 75kg)
	elif Weight >=76 and Weight<=80:					#if Weight 76 - 80 , do
		category="Class G (76kg - 80kg)"				#Set category = Class G (76kg - 80kg)
	elif Weight >=81 and Weight<=85:					#if Weight 81 - 85 , do
		category="Class H (81kg - 85kg)"				#Set category = Class H (81kg - 85kg)
	elif Weight >=86 and Weight<=90:					#if Weight 86 - 90 , do
		category="Class I (86kg - 90kg)"				#Set category = Class I (86kg - 90kg)
	elif Weight >=91 and Weight<=95:					#if Weight 91 - 95 , do
		category="Class J (91kg - 95kg)"				#Set category = Class J (91kg - 95kg)
	else:												#if Weight >95, do
		category="Class Open (+96kg)"						#Set category = Class Open (+96kg)

	return category										#return category value

def Bxg(Weight):										#Bxg function with variable Weight
	if Weight >=91:										#if Weight >=91 , do
		category="Heavyweight (+91kg)"					#Set category = Heavyweight (+91kg)
	elif Weight >=81 and Weight<=90:					#if Weight 81 - 90 , do
		category="Cruiserweight (81kg - 90kg)"			#Set category = Cruiserweight (81kg - 90kg)
	elif Weight >=78 and Weight<=80:					#if Weight 78 - 80 , do
		category="heavyweight (78kg - 80kg)"			#Set category = heavyweight (78kg - 80kg)
	elif Weight >=67 and Weight<=76:					#if Weight 67 - 76 , do
		category="middleweight (67kg - 76kg)"			#Set category = middleweight (67kg - 76kg)
	else:												#if Weight <67 , do
		category="Welterweight (-66kg)"					#Set category = Welterweight (-66kg)
		
	return category										#return category value

def MmA(Weight):										#MmA function with variable Weight
	if Weight<=52:										#if Weight <= 52 , do
		category="Strawweight (-52kg)"					#Set category = Strawweight (-52kg)
	elif Weight>=53 and Weight<=57:						#if Weight 53 - 57 , do
		category="Flyweight (53kg - 57kg)"				#Set category = Flyweight (53kg - 57kg)
	elif Weight>=58 and Weight<=61:						#if Weight 58 - 61 , do
		category="Bantamweight (58kg - 61kg)"			#Set category = Bantamweight (58kg - 61kg)
	elif Weight>=62 and Weight<=66:						#if Weight 62 - 66 , do
		category="Featherweight (62kg - 66kg)"			#Set category = Featherweight (62kg - 66kg)
	elif Weight>=67 and Weight<=70:						#if Weight 67 - 70 , do
		category="Lightweight (67kg - 70kg)"			#Set category = Lightweight (67kg - 70kg)
	elif Weight>=71 and Weight<=77:						#if Weight 71 - 77 , do
		category="Welterweight (71kg - 77kg)"			#Set category = Welterweight (71kg - 77kg)
	elif Weight>=78 and Weight<=89:						#if Weight 78 - 89 , do
		category="Middleweight (78kg - 89kg)"			#Set category = Middleweight (78kg - 89kg)
	elif Weight>=90 and Weight<=93:						#if Weight 90 - 93 , do
		category="Light Heavyweight (90kg - 93kg)"		#Set category = Light Heavyweight (90kg - 93kg)
	elif Weight>=94 and Weight<=120:					#if Weight 94 - 120 , do
		category="Heavyweight (94kg - 120kg)"			#Set category = Heavyweight (94kg - 120kg)
	else:												#if Weight > 120 , do
		category="Super Heavyweight (+121kg)"			#Set category = Super Heavyweight (+121kg)
		
	return category										#return category value