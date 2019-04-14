#!/bin/bash

# declare arg, bookmark;
book=~/.bookmarks


case $1 in
	-a)
	# add bookmark
	if [ "$#" -ne 2 ]; then
    echo "Illegal number of parameters"
		exit 1
	fi
	echo "$2|$PWD" >> $book
	# export $2="$PWD"

	# $PWD what folder I am in
	# ~/
	;;
	-r)
	# remoove
	if [ "$#" -ne 2 ]; then
    echo "Illegal number of parameters"
		exit 1
	fi
	unset $2
	sed -i "/$2|/d" $book

	;;
	*)
	echo "eror: supply the bookmarkname as an additional argument with -a or -r"

esac
# cat ~/.bookmarks
while read arg; do
	bookmark=$(echo "$arg" | sed 's/ *|.*//')
	bookmarkname=$(echo "$arg" | grep -Eo '[^|]+$')
	# echo "$bookmark     $bookmarkname"
	export $bookmark="$bookmarkname"
done <$book
