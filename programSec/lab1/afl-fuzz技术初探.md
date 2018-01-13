# afl-fuzz技术初探

> 转载请注明出处:http://www.cnblogs.com/WangAoBo/p/8280352.html
>
> 参考了:
>
> http://pwn4.fun/2017/09/21/AFL%E6%8A%80%E6%9C%AF%E4%BB%8B%E7%BB%8D/
>
> http://blog.csdn.net/youkawa/article/details/45696317
>
> https://stfpeak.github.io/2017/06/12/AFL-Cautions/
>
> http://blog.csdn.net/abcdyzhang/article/details/53487683

在计算机领域,Fuzz Testing(模糊测试)是一种很有效的测试方法,主要原理为构造一系列“坏”数据传入应用程序,通过判断程序是否发生异常发现和检测潜在的bug.而在安全领域引入fuzz技术,无疑可以使安全研究员效率倍增,更有效的挖掘和防护漏洞。

AFL(American Fuzzy Lop)是目前最高级的Fuzzing测试工具之一,由lcamtu开发.当需要测试的程序有源码时,AFL通过对源码重新编译时插桩(插入分析代码)的方法来探测程序内部的执行路径.相对于其他fuzzer,AFL-Fuzz具有更低的性能消耗,更有效的fuzzing策略和tricks最小化技巧,只需简单的配置即可处理复杂的程序.当然,对于没有源码的可执行程序,AFL也可进行处理,但需要QEUM模拟器的支持.

本次实验将介绍AFL的安装和使用方法,以有源码的upx为例进行展示,也会简要介绍AFL处理无源码程序的情况.

## 安装afl

> 听学长介绍,afl会烧ssd,不建议在本地安装

- 下载最新[源码](http://lcamtuf.coredump.cx/afl/)

  ![](https://ws1.sinaimg.cn/large/006AWYXBly1fnf3kvzqn6j30g108wmzt.jpg)

- 解压并安装:

  ```bash
  $make
  $sudo make all
  ```

  ![](https://ws1.sinaimg.cn/large/006AWYXBly1fnf3nxvxlaj30g00a0aho.jpg)

  如果不报错,则afl-fuzz就安装成功了

  ![](https://ws1.sinaimg.cn/large/006AWYXBly1fnf3qdhxluj30lc0lo12z.jpg)



## 有源码的afl-fuzz

这里以fuzz upx为例进行测试

### 编译upx

- upx项目地址([*https://github.com/upx/upx*)
- 因为afl会对有源码的程序进行重新编译,因此需要修改upx的Makefile

```bash
$git clone https://github.com/upx/upx.git
$cd upx
$vim Makefile
CC = /usr/local/bin/afl-gcc #添加此句
```

![](https://ws1.sinaimg.cn/large/006AWYXBly1fnf3x43cwvj30g109ftdr.jpg)

```bash
$cd src
$vim Makefile
CXX    ?= /usr/local/bin/afl-g++ #将CXX改成afl-g++
```

![](https://ws1.sinaimg.cn/large/006AWYXBly1fnf3ydcn84j30g109zgr0.jpg)

通过upx的文档,还需要安装三个库:

#### 安装lzma-sdk

```bash
$git submodule update --init --recursive
```

![](https://ws1.sinaimg.cn/large/006AWYXBly1fnf40cs8x2j30g103ugok.jpg)

#### 安装ucl

- 下载[ucl](http://www.oberhumer.com/opensource/ucl/#download)

  ![](https://ws1.sinaimg.cn/large/006AWYXBly1fnf42oq66dj30g10cl41c.jpg)

- 编译:

  ```bash
  $cd ucl-1.03
  $./configure
  $make 
  $sudo make install
  ```

  ![](https://ws1.sinaimg.cn/large/006AWYXBly1fnf44kxn0jj30g10910zr.jpg)

  ```bash
  $export UPX_UCCLDIR="~/ucl-1.03"
  ```

  ![](https://ws1.sinaimg.cn/large/006AWYXBly1fnf469emu3j30g101saaz.jpg)

#### 安装zlib

  ````bash
  $wget http://pkgs.fedoraproject.org/repo/pkgs/zlib/zlib-1.2.11.tar.xz/sha512/b7f50ada138c7f93eb7eb1631efccd1d9f03a5e77b6c13c8b757017b2d462e19d2d3e01c50fad60a4ae1bc86d431f6f94c72c11ff410c25121e571953017cb67/zlib-1.2.11.tar.xz
  ````

  ![](https://ws1.sinaimg.cn/large/006AWYXBly1fnf4795xuqj30g106b0y6.jpg)

  ```bash
  $cd zlib-1.2.11/
  $./configure
  $sudo make install
  ```

  ![](https://ws1.sinaimg.cn/large/006AWYXBly1fnf48z9croj30g1091n4e.jpg)

#### 编译upx

```bash
$cd ~/upx
$make all
```

若没有报错,则编译成功

![](https://ws1.sinaimg.cn/large/006AWYXBly1fnf4aw984mj30g1091jzv.jpg)

此时可在/src目录下找到upx.out文件

![](https://ws1.sinaimg.cn/large/006AWYXBly1fnf4blr0tdj30g107745i.jpg)

### 对upx进行fuzz测试

```bash
$cd ~
$mkdir afl_in afl_out
afl_in存放测试用例,afl_out存放fuzz结果
$cp /usr/bin/file afl_in
$afl-fuzz -i afl_in -o afl_out ~/upx/src/upx.out @@
@@会代替测试样本,即相当于执行了upx.out file
```

![](https://ws1.sinaimg.cn/large/006AWYXBly1fnf4fzvv1mj30g10917au.jpg)



### AFL运行界面:

![](https://ws1.sinaimg.cn/large/006AWYXBly1fnf4hakw53j30g10cldni.jpg)

### 运行结果与分析

![](https://ws1.sinaimg.cn/large/006AWYXBly1fnf4i8a9dzj30g1091q97.jpg)

可以看出,在短短的十几分钟内,已经跑出了6个crash,安全从业者可以通过分析afl_out中的文件得到更多信息,可以看出使用afl-fuzz比起人工审查效率有了极大地提高

> 对于从stdin获取输入的程序,可以使用
>
> \# afl-fuzz -i afl_in -o afl_out ./file

## 无源码的afl-fuzz

对无源码的程序进行fuzz一般有两种方法:

1. 对二进制文件进行插桩
2. 使用-n选项进行传统的fuzz测试

这里主要介绍第一种,该方法是通过afl-qemu实现的.

### 编译afl版的qemu

```bash
$ cd qemu_mode 
$ ./build_qemu_support.sh
```

在编译时,可能会遇到以下的报错:

![](https://ws1.sinaimg.cn/large/006AWYXBly1fnf5dniig5j30g103mq5k.jpg)

![](https://ws1.sinaimg.cn/large/006AWYXBly1fnf5dum0bdj30g104eq5p.jpg)



报错信息都比较明显,安装相应的库即可

> 若遇到glib2丢失,可以
>
> $sudo apt-get install libglib2*

### 对readelf进行fuzz

以readelf为例

```bash
$mkdir afl_in afl_out
$cp test afl_in
test为自己准备的测试elf
$sudo cp /usr/bin/readelf .
$afl_fuzz -i afl_in -o afl_out -Q readelf -a @@
```

![](https://ws1.sinaimg.cn/large/006AWYXBly1fnf794m6q3j31400p0qkz.jpg)

如下图,已经开始fuzz了:

![](https://ws1.sinaimg.cn/large/006AWYXBly1fnf794m6q3j31400p0qkz.jpg)

**本篇博文只对afl-fuzz的基本操作做了介绍,更多的高级用法还待以后探索**



