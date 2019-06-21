#!/usr/bin/python3
#coding:UTF-8
import cgi


print("Content-Type: text/html")
print()

html =  """<!DOCTYPE html>
<head> 
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" href="../stylesheet.css" />    
    <title>Jeux déchec</title>
</head>
<body>
    <center>

    <h1>Bienvenue sur notre jeux d'échec</h1></br>
    <div>
        <span style="display:inline-block">Vous avez déjà un compte :</span> 
        <form action="result.py" method="post">   
            <p>
                <input type="text" name="pseudo" pattern="^[a-zA-Z0-9_]{3,20}$" placeholder="Votre pseudo" />
                <input type="password" name="password" pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{6,}$" placeholder="Votre mot de passe" />
                <input type="submit" name="send" value="Sign In">
            </p>
        </form>
    </div>


    <div>
        <p>
            <span style="display:inline-block;padding-top:60px">Créer un compte :</span><br />
            <span style="font-style:italic;font-size:13px;color:#6d6969">Mot de passe contient au moins 6 caractères, 1 Maj, 1 Min, 1 chiffre</span>
        </p>
        <form action="result.py" method="post">   
            <p>
                <input type="text" name="c_pseudo" pattern="^[a-zA-Z0-9_]{3,20}$" placeholder="Choisir un pseudo" />
                <input type="text" name="c_password" pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{6,}$" placeholder="Choisir un mot de passe" />
                <input type="text" name="c_email" pattern="[A-Za-z0-9](([_\.\-]?[a-zA-Z0-9]+)*)@([A-Za-z0-9]+)(([_\.\-]?[a-zA-Z0-9]+)*)\.([A-Za-z]{2,4})" placeholder="Donner votre email" />
                <input type="submit" name="send2" value="Sign Up">
            </p>
        </form>
    </div>  

    </center>
</body>
</html>"""

print(html)