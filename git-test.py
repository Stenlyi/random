#zamestnanec1=["Petr", "Novák", "Olomouc", 779 00, True]
#zamestnanec2=["Pavel", "Malý", "prostějov", 775 44, True]
#zamestnanec3=["Jan", "Velký", "Přerov", False]
#
#zamestnanci = [zamestnanec1, zamestnanec2, zamestnanec3]
#
#for zamestnanci in zamestnanci:
#    print(zamestnanec[1])

#key-valuue-pair
#zamestnanec1={"name": "Jon", "age": 30, "city": "NY"}
#zamestnanec2={
#    "name": "Marry",
#    "age": 16,
#    "city": "Paris",
#}

#založení slovníků
muj_novy_slovnik={}
muj_novy_slovnik_2=dict()
#zalozeni mnoziny
moje_mnozina=set()

print(muj_novy_slovnik)
muj_novy_slovnik["jmeno"]="Lukas"
print(muj_novy_slovnik)
muj_novy_slovnik["ridicak"]=True
muj_novy_slovnik["hobby"]=("fotbal", "hry", " spánek")
muj_novy_slovnik["vek"]=22
muj_novy_slovnik["jmeno"]="Matěj"

print(muj_novy_slovnik)

print(muj_novy_slovnik["jmeno"])

print(muj_novy_slovnik["hobby"])
print(muj_novy_slovnik["hobby"][0])

#ZÁKLADNÍ SLOVNÍKOVÉ METODY
print(muj_novy_slovnik.keys())
print(muj_novy_slovnik.values())
print(muj_novy_slovnik.items())

student={
    "name": "Jon",
    "age": 25,
    "courses": ["Math", "Compsci"]
}

for keys in student.keys():
    print(keys)

