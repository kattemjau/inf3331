#!/bin/bash

case $1 in
	no)
		export TZ="Norway/Oslo"

		;;
	sk)
		export TZ="Asia/Seoul"
	;;
	us)
		export TZ="America/New_York"
	;;

*)
	echo "error, use program no, sk, or us for times"
;;


esac

while [ True ]; do
clear

date +%T

sleep 1

done
