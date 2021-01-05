Pruebas unitarias

1. herramienta doctest, viene con python

Ejecutar:
python3 -m doctest test.txt

para probar un archivo es:
en el caso de palindromo se ejcuta un doctest dentro docstring
python3 -m doctest -v algoritmos.py

se puede uar la librería pytest para prueba sencillas

pip install pytest

ubicarse dentro de assert
pytest test.py

unitest pruebas más complejas bd, api

python3 test_shopping_cart.py -v

método fail para hacer validaciones manuales

método saber cuánto código se cubrió con las pruebas
coverage report test_shopping_cart.py

Esto daría 0% de cover

coverage run test_shopping_cart.py

Esto daría un valor de cobertura del código

coverage report -m test_shopping_cart.py

Esto nos daría que no se cubrió

reporte en html
coverage html test_shopping_cart.py

levanta un servidor http en una línea
python3 -m http.server

Luego podemos ver el html en localhost:8000