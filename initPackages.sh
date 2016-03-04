#!/bin/bash
COMMANDS=( 'python' 'fab' 'git' 'brackets' 'node' )
COMMANDSPACKAGES=( 'python' 'fabric' 'git' 'brackets' 'nodejs' )
comNum=${#COMMANDS[@]}
for(( i=0;i<$comNum;i++)); do
    echo "Checking if command \"${COMMANDS[${i}]}\" exists! It's package name is ${COMMANDSPACKAGES[${i}]}"
    if [ -z `which ${COMMANDS[${i}]}` ]  #if com empty
    then
        apt-get install ${COMMANDSPACKAGES[${i}]}
        echo "${COMMANDS[${i}]} already installed!"
    else
        echo "${COMMANDS[${i}]} exists!"
    fi
done
 
echo "Work of install done!"