#!/bin/bash

declare -i arg; sum=0;

case $1 in
	S)
		for arg in ${@:2}; do
			((sum+=$arg))
		done
		echo $sum
		;;
	P)
	sum=1;
	for arg in ${@:2}; do
		((sum=$arg*sum))
	done
	echo $sum
	;;

	M)
	sum=$2;
	for arg in ${@:3}; do
		if [ $sum -lt $arg ]; then
		((sum=$arg))
		fi
	done
	echo $sum
	;;
	m)
	sum=$2;
	for arg in ${@:3}; do
		if [ $sum -gt $arg ]; then
		((sum=$arg))
		fi
	done
	echo $sum
	;;
	*)
	echo "error, Use s S for sum, P for product, M for
maximum and m for minimum"
;;

esac
