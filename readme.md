# Parking-api with Fastapi
Projet Estiam - E4 API

## Importer toutes les dépendances :
```
pip install -r requirements.txt
```

### update dependencies / save new dependencies
```
pip freeze > requirements.txt
```

## start Docker
```
docker-compose up --build
```

## Lancement de l'app :
```
uvicorn main:app --reload
```


## Lancement des tests :
```
pytest -v
```
-v : Increase verbosity


## Auth : email + password (a revoir)
1 : Go to firebase > Authentication > Add Authentication
2 : Project settings > Enable email + password type auth


## Tests

```
pip install pytest
```

```
Start testing on command promp: pytest
```

```
Collect coverage data : coverage run -m pytest
Generate coverage file : coverage html
```


