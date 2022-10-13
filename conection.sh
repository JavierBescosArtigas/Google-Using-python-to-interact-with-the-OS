#!/usr/bin/bash


#Colours
declare -r greenColour="\e[0;32m\033[1m"
declare -r endColour="\033[0m\e[0m"
declare -r redColour="\e[0;31m\033[1m"
declare -r blueColour="\e[0;34m\033[1m"
declare -r yellowColour="\e[0;33m\033[1m"
declare -r purpleColour="\e[0;35m\033[1m"
declare -r turquoiseColour="\e[0;36m\033[1m"
declare -r grayColour="\e[0;37m\033[1m"


echo -e "\n\e[0;32m\033[1m [*]funcionamiento : \033[0m\e[0m conection.sh \e[0;33m\033[1m archivo.pem \e[0;34m\033[1m user_nam \e[0;35m\033[1m ip_machin \033[0m\e[0m"
echo
echo
sleep 0.5
if [ $# -gt 2 ]; then
  echo -e "\e[0;32m\033[1m [+] Cambiando permiso a 600 a $1 ... \033[0m\e[0m"
  var1=$1
  chmod 600 $var1
  error=$?
  echo "ssh -i $var1 $2@$3" |xclip -selection clipboard
  echo "ssh -i $var1 $2@$3"
  exit $error
else
  echo -e "\e[0;31m\033[1m [!] Dígame \e[0;33m\033[1m archivo.pem user_name \e[0;33m\033[1m ip_machine \033[0m\e[0m"
  read -a nombres -t 100
  if [ ${#nombres[@]} -lt 3 ];then
    echo -e "\n [x]\e[0;31m\033[1m No suficientes variables, mire el funcionamiento del programa al ejecutarlo \033[0m\e[0m"
    exit 1
    fi
  for i in ${nombres[@]}
  do
    echo $i
  done
fi
chmod 600 ${nombres[0]}
error=$?
echo "ssh -i ${nombres[0]} ${nombres[1]}@${nombres[2]}" |xclip -selection clipboard
echo "ssh -i ${nombres[0]} ${nombres[1]}@${nombres[2]}"
exit $error
