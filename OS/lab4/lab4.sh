#!/usr/bin/env bash

#转化为相对路径
path=`pwd`
len=${#path}
# echo $len
while true
do
	path=`pwd`
	read -p "~/"${path:len}":" cmd
	# 字符串比较注意空格的使用
	# new,转义空格
	if [[ "$cmd" == new\ * ]]; then
		#echo "test"
		mkdir ${cmd:4}
	elif [[ "$cmd" == sfs\ * ]]; then
		cd ${cmd:4}
	elif [[ "$cmd" == mkdir\ * ]] || [[ "$cmd" == rmdir\ * ]] || [[ "$cmd" == ls ]];then
		$cmd
	fi

done
