from datetime import date

annee = int(input("année de naissance? "))
mois = int(input("mois de naissance? "))
jour = int(input("jour de naissance? "))

def calculateAge(birthDate):
	days_in_year = 365.2425
	age = int((date.today() - birthDate).days / days_in_year)
	return age

print(calculateAge(date(annee, mois, jour)), "years")

