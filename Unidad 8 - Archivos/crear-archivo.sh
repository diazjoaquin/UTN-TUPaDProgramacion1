#!/bin/bash

touch  productos.txt

echo "Nombre,Precio,Cantidad" >> productos.txt
echo "Lapicera,\$10,5" >> productos.txt
echo "Borrador,\$5,10" >> productos.txt
echo "Cuadernos,\$2,22" >> productos.txt
echo "Tijeras,\$7,15" >> productos.txt

cat productos.txt