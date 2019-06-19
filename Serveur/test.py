#coding:UTF-8
#!/usr/bin/env python3
import psycopg2



# Connexion
try:
    conn = psycopg2.connect (
        database = "jeuxechec",
        user = "echec",
        password = "echec",
        host = "127.0.0.1",
        port = "5432"
    )
    # Print PostgreSQL conn properties
    print ( conn.get_dsn_parameters(),"\n")

    cursor = conn.cursor()    
    # Print PostgreSQL test
    cursor.execute("SELECT * from jeux")
    test = cursor.fetchone()
    print("retour de donnée sur la table jeux", test,"\n")




except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database conn.
        if(conn):
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")
