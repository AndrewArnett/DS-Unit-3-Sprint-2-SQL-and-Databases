# Total amount of each passenger that survived
SELECT COUNT(*) FROM titanic_data WHERE survived = 1;
342
# Total amount of each passenger that died
SELECT COUNT(*) FROM titanic_data WHERE survived = 0;
545
# Amount of each sub class that survived
SELECT COUNT(*) FROM titanic_data WHERE survived = 1 AND pclass =1;
136
SELECT COUNT(*) FROM titanic_data WHERE survived = 1 AND pclass =2;
87
SELECT COUNT(*) FROM titanic_data WHERE survived = 1 AND pclass =3;
119
# Total amound of each sub class that died
SELECT COUNT(*) FROM titanic_data WHERE survived = 0 AND pclass =1;
80
SELECT COUNT(*) FROM titanic_data WHERE survived = 0 AND pclass =2;
97
SELECT COUNT(*) FROM titanic_data WHERE survived = 0 AND pclass =3;
368
# Average age of survivors
SELECT AVG(age) FROM titanic_data WHERE survived = 1;
28.4083918128272
# Average age of those who died
SELECT AVG(age) FROM titanic_data WHERE survived = 0;
30.1385321100917
# Average age of pclass 1
SELECT AVG(age) FROM titanic_data WHERE pclass = 1;
38.7889814815587
# Average age of pclass 2
SELECT AVG(age) FROM titanic_data WHERE pclass = 2;
29.8686413042571
# Average age of pclass 3
SELECT AVG(age) FROM titanic_data WHERE pclass = 3;
25.188747433238
# Average fare of survivors
SELECT AVG(fare) FROM titanic_data WHERE survived = 1;
48.3954076976107
# Average fare of those who died
SELECT AVG(fare) FROM titanic_data WHERE survived = 0;
22.2085840951412
# Average fare of pclass 1
SELECT AVG(fare) FROM titanic_data WHERE pclass = 1;
84.154687528257
# Average fare of pclass 2
SELECT AVG(fare) FROM titanic_data WHERE pclass = 2;
20.6621831810993
# Average fare of pclass 3
SELECT AVG(fare) FROM titanic_data WHERE pclass = 3;
13.7077075010452