import sqlite3
from netflixAPI import *


conn = sqlite3.connect('movies.db')
c = conn.cursor()


def createTable():
    try:
        c.execute("""CREATE TABLE NetflixTable (
            titles text,
            descriptions text,
            years integer
        )""")
    except sqlite3.OperationalError:
        print("SQLite3 Operational error: Table already exists")


#In here is the call that gets all the movie data, calling a function getData() in netflixAPI.py, then inserting it in db (allt detta e hårdkodat af)
def insertNetflixDB():
    movieData = getData()
    titles = movieData[0]
    descriptions = movieData[1]
    years = movieData[2]

    for i in range(len(titles)):
        c.execute("INSERT INTO NetflixTable VALUES(?,?,?)", (titles[i], descriptions[i], years[i]))

    print(titles, "\n", descriptions, "\n", years)



def searchTitle(title):
    c.execute("SELECT * FROM NetflixTable WHERE titles = ?", (title,))
    print(c.fetchall())



#Loop through files to see if there is a "movies.db" file. If there is, createTable and insertNetflixDB should not be callable
def dbExists():
    pass


#createTable()
#insertNetflixDB()
searchTitle("13: The Musical")

conn.commit()
conn.close()

#Testar github



