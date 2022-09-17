#!/bin/bash
#key = 7985be91e6644668b31c8830a4f6e3c9

function pwned()
{
echo 'Introduzca su ApiKey '
read -s Apikey
curl -H "hibp-api-key:$Apikey" https://haveibeenpwned.com/api/v3/breachedaccount/$Correo
}
echo '*********** BIENVENDIDO ***********'
read Correo
if [$Correo == 'null'];
then
echo 'Correo Vacio'
else
pwned
