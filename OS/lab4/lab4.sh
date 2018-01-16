#!/usr/bin/env bash

set -u
# set -x #debug
echo "Welcome to M4x's fileSystem."
echo "This is a simplified fileSystem for lab4 of OS of BIT."

trap 'onCtrlC' INT
function onCtrlC () {
	echo "Something wrong occured. Your tasks won't be saved..."
	mv lab4.sh ../
	rm * -r
	mv ../lab4.sh .
	exit
}

#转化为相对路径
path=$(pwd)
len=${#path}
# echo $len
#标记是否打开了文件系统
flag=false
while true
do
	path=$(pwd)
	read -p "~""${path:len}"":" cmd
	# 字符串比较注意空格的使用
	# new,转义空格
	if [[ "$cmd" == new\ * ]]; then
		#echo "test"
		mkdir "${cmd:4}" 2>error || {
		echo "${cmd:4}"" already existed. Try another name!"
	}

	elif [[ "$cmd" == sfs\ * ]]; then
		flag=true
		cd "${cmd:4}" 2>error || {
		echo "There is no ""${cmd:4}""! Please check your fileSystem's name!"
	}

	elif [ "$flag" = true ] && ([[ "$cmd" == mkdir\ * ]] || [[ "$cmd" == rmdir\ * ]] || [[ "$cmd" == ls ]] || [[ "$cmd" == cd\ * ]]); then
		$cmd
	elif [ "$flag" = true ] && [[ "$cmd" == create\ *  ]]; then
		touch "${cmd:7}"
		# 此时文件有可读可执行权限 
		chmod 555 "${cmd:7}"
	elif [ "$flag" = true ] && [[ "$cmd" == open\ * ]]; then
		# 此时文件具只有可写权限  
		chmod 666 "${cmd:5}"
	elif [ "$flag" = true ] && [[ "$cmd" == close\ * ]]; then
		# 此时文件具有可读可执行权限
		chmod 555 "${cmd:6}"
	elif [ "$flag" = true ] && [[ "$cmd" == read\ * ]]; then
		cat "${cmd:5}"
	elif [ "$flag" = true ] && [[ "$cmd" == write\ * ]]; then
		read -p "Please input your content: " content
		echo -n "$content" > "${cmd:6}"
	elif [ "$flag" = true ] && [[ "$cmd" == delete\ * ]]; then
		rm "${cmd:7}"
	elif [[ "$cmd" == exit ]]; then
		echo "Good Bye!"
		exit
	else
		echo "Wrong command!"
	fi

done
