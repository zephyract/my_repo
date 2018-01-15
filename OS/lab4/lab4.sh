#!/usr/bin/env bash
set -euo pipefail

#转化为相对路径
path=$(pwd)
len=${#path}
# echo $len
while true
do
	path=$(pwd)
	read -p "~""${path:len}"":" cmd
	# 字符串比较注意空格的使用
	# new,转义空格
	if [[ "$cmd" == new\ * ]]; then
		#echo "test"
		mkdir "${cmd:4}"
	elif [[ "$cmd" == sfs\ * ]]; then
		cd "${cmd:4}"
	elif [[ "$cmd" == mkdir\ * ]] || [[ "$cmd" == rmdir\ * ]] || [[ "$cmd" == ls ]] || [[ "$cmd" == cd\ * ]]; then
		$cmd
	elif [[ "$cmd" == create\ *  ]]; then
		touch "${cmd:7}"
		# 此时文件有可读可执行权限 
		chmod 555 "${cmd:7}"
	elif [[ "$cmd" == open\ * ]]; then
		# 此时文件具只有可写权限  
		chmod 666 "${cmd:5}"
	elif [[ "$cmd" == close\ * ]]; then
		# 此时文件具有可读可执行权限
		chmod 555 "${cmd:6}"
	elif [[ "$cmd" == read\ * ]]; then
		cat "${cmd:5}"
	elif [[ "$cmd" == write\ * ]]; then
		read -p "Please input your content: " content
		echo -n "$content" > "${cmd:6}"
	elif [[ "$cmd" == delete\ * ]]; then
		rm "${cmd:7}"
	elif [[ "$cmd" == exit ]]; then
		exit
	else
		echo "Wrong command!"
	fi

done
