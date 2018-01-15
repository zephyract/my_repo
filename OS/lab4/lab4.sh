#!/usr/bin/env bash

while true
do
	echo -n "当前目录:"
	pwd
	read -p "> " cmd
	#字符串比较注意空格的使用
	#new,转义空格
	if [[ "$cmd" == new\ * ]]; then
		#echo "test"
		mkdir ${cmd:4}
	elif [[ "$cmd" == sfs\ * ]]; then
		cd ${cmd:4}
	elif [[ "$cmd" == mkdir\ * ]] || [[ "$cmd" == rmdir\ * ]] || [[ "$cmd" == ls ]];then
		$cmd
	fi

done
