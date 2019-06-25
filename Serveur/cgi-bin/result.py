#!/usr/bin/python3
#coding:UTF-8
import cgi
import psycopg2
import bcrypt

import cgitb
cgitb.enable()

# Fonctions de hashage / décryptage
def get_hashed_password(plain_text_password):
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())

def check_password(plain_text_password, hashed_password):
    return bcrypt.checkpw(plain_text_password, hashed_password)


print("Content-Type: text/html")
print()
html = """<!DOCTYPE html>
<head> 
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" href="../stylesheet.css" />
    <title>Inscription/connexion</title>
</head>
<body>"""
print(html)
form = cgi.FieldStorage()


if form.getvalue("send") == "Sign In":

    ######################################
    # Tunnel de connexion LOGIN

    f_pseudo = form.getvalue("pseudo")
    f_password = form.getvalue("password")


    if "pseudo" not in form or "password" not in form:
        print(f"<H1>Erreur</H1>")
        print(f"<p>Donnez un pseudo et un mot de passe.</p>")
        html = """
        <a href="index.py">Retour</a>
        """
        print(html)


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
        a = cursor.fetchone()

        if a != None:
            h = check_password(f_password,a[2])

            if h == True:
                # ICI LE CODE POUR DÉMARRER UNE PARTIE
                print (f"<p>Vous êtes connectés</p>")
                html = """ 
                <div>
                    <form action="action_page.py" method="post">
                        <button type="submit" name="actio">Commencer nouvelle partie</button>
                    </form>                    
                </div>                
                 """
                print (html)

            else:
                print(f"<p>Login et mod de passe ne correspondent pas</p>")
                html = """
                <a href="index.py">Retour</a>
                """
                print(html)

        else:
            print(f"<p>Identifiant/MDP incorect, ré-essayer !</p>")
            html = """
            <a href="index.py">Retour</a>
            """
            print(html)            
        
        cursor.close()
        conn.close()

    # print(f"<p>pseudo:", form["pseudo"].value)
    # print(f"<p>password:", form["password"].value)

    # EO - Tunnel de connexion LOGIN
    ######################################

else:

    ######################################
    # Tunnel de création de compte
    c_pseudo = form.getvalue("c_pseudo")
    c_email = form.getvalue("c_email")
    c_password = form.getvalue("c_password")

    if "c_pseudo" not in form or "c_password" not in form or "c_email" not in form: 
        print(f"<H1>Erreur</H1>")
        print(f"<p>Tous les champs sont obligatoires à la création du compte.</p>")
        html = """
        <a href="index.py">Retour</a>
        """
        print(html)        

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
        c_password=get_hashed_password(c_password)

        if result < 1 :
            cursor.execute("INSERT INTO joueurs (pseudo, mdp, email) VALUES ('"+c_pseudo+"','"+c_password+"','"+c_email+"')")
            conn.commit()
            cursor.close()
            conn.close()
            print(f"<p>Votre comte à bien été créé</p>")
            html = """
            <a href="index.py">Se connecter</a>
            """
            print(html)            
        
        else:
            print(f"<p>le pseudo existe déjà.</p>")
            html = """
            <a href="index.py">Retour</a>
            """
            print(html)            

# EO - Tunnel de création de compte       
######################################


html="""
</body>
</html>"""
print(html)