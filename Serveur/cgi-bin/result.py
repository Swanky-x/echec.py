#!/usr/bin/python3
#coding:UTF-8
import cgi
import psycopg2

import cgitb
cgitb.enable()

print("Content-Type: text/html")
print()
html = """<!DOCTYPE html>
<head> 
    <meta charset="UTF-8">
    <title>soumission pseudo</title>
</head>
<body>
</body>
</html>"""
print(html)

# form = cgi.FieldStorage()
# try:
#     if form.getvalue("pseudo","password"):
#         pseudo = form.getvalue("pseudo")   
#         password = form.getvalue("password")
        
#         print(f"<p>Bonjour {pseudo} !</p>") 
#         print(f"<p>Votre mot de passe : {password} </p>")

#     else :
#         raise Exception ("Pseudo et/ou MDP non transmis")
# except:
#     print("Pseudo et/ou MDP non transmis")        


form = cgi.FieldStorage()
f_pseudo = form.getvalue("pseudo")
f_password = form.getvalue("password")
######################################
# Tunnel de connexion LOGIN

if "pseudo" not in form or "password" not in form:
    print(f"<H1>Erreur</H1>")
    print(f"<p>Donnez un pseudo et un mot de passe.</p>")

else :
    conn = psycopg2.connect (
        database = "jeuxechec",
        user = "echec",
        password = "echec",
        host = "127.0.0.1",
        port = "5432"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * from joueurs WHERE pseudo ='"+f_pseudo+"'")
    cursor.fetchone()

    if f_password == cursor.fetchone()[2]:
        # ICI LE CODE POUR DÉMARRER UNE PARTIE
        print (f"<p>Vous êtes connectés</p>")

    else:
        print(f"<p>Identifiant/MDP incorect, ré-essayer !</p>")
    
    cursor.close()
    conn.close()

# print(f"<p>pseudo:", form["pseudo"].value)
# print(f"<p>password:", form["password"].value)

# EO - Tunnel de connexion LOGIN
######################################




c_pseudo = form.getvalue("c_pseudo")
c_password = form.getvalue("c_password")
c_email = form.getvalue("c_email")
######################################
# Tunnel de création de compte
if "c_pseudo" not in form or "c_password" not in form or "c_email" not in form: 
    print(f"<H1>Erreur</H1>")
    print(f"<p>Tous les champs sont obligatoires à la création du compte.</p>")

else :
    conn = psycopg2.connect (
        database = "jeuxechec",
        user = "echec",
        password = "echec",
        host = "127.0.0.1",
        port = "5432"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM joueurs WHERE pseudo = '"+c_pseudo+"'")
    cursor.fetchall()
    result = (cursor.rowcount)

    if result < 1 :
        cursor.execute("INSERT INTO joueurs (pseudo, mdp, email) VALUES ('"+c_pseudo+"','"+c_password+"','"+c_email+"')")
        conn.commit()
        cursor.close()
        conn.close()
        print(f"<p>Votre comte à bien été créé</p>")
    
    else:
        print(f"<p>le pseudo existe déjà.</p>")
        