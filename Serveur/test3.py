liste = [[1,'blanc',11,'tourb1','tour'],
[2,'blanc',21,'cavalierb1','cavalier'],
[3,'blanc',31,'foub1','fou'],
[4,'blanc',41,'reineb','queen'],
[5,'blanc',51,'roib','king'],
[6,'blanc',61,'foub2','fou'],
[7,'blanc',71,'cavalierb2','cavalier'],
[8,'blanc',81,'tourb2','tour'],
[9,'blanc',12,'pionb1','pion'],
[10,'blanc',22,'pionb2','pion'],
[11,'blanc',32,'pionb3','pion'],
[12,'blanc',42,'pionb4','pion'],
[13,'blanc',52,'pionb5','pion'],
[14,'blanc',62,'pionb6','pion'],
[15,'blanc',72,'pionb7','pion'],
[16,'blanc',82,'pionb8','pion'],
[17,'noir',18,'tourn1','tour'],
[18,'noir',28,'cavaliern1','cavalier'],
[19,'noir',38,'foun1','fou'],
[20,'noir',48,'reinen','queen'],
[21,'noir',58,'roin','king'],
[22,'noir',68,'foun2','fou'],
[23,'noir',78,'cavaliern2','cavalier'],
[24,'noir',88,'tourn2','tour'],
[25,'noir',17,'pionn1','pion'],
[26,'noir',27,'pionn2','pion'],
[27,'noir',37,'pionn3','pion'],
[28,'noir',47,'pionn4','pion'],
[29,'noir',57,'pionn5','pion'],
[30,'noir',67,'pionn6','pion'],
[31,'noir',77,'pionn7','pion'],
[32,'noir',87,'pionn8','pion']]

liste2 = []
for i in range(len(liste)):
    #print(f"{liste[i][2]}")
    a = str(liste[i][2])
    liste2.append([a])

col = []
ligne = []

for i in liste2:
    print(i) 
    for y in i:
        print(y)
        a = y[0]
        b = y[1]
        col.append(a)
        ligne.append(b)
        print(a)


print(col)
print(ligne)
    






