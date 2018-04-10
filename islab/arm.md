# 如何在linux主机上运行/调试 arm/mips架构的binary

> 本文中用于展示的binary分别来自Jarvis OJ上pwn的add，typo两道题

写这篇教程的主要目的是因为最近想搞其他系统架构的pwn，因此第一步就是搭建环境了，网上搜索了一波，发现很多教程都是需要树莓派，芯片等硬件，然后自己编译gdb，后来实践的过程中发现可以很简单地使用qemu实现运行和调试异架构binary，因此在这里分享一下我的方法。

### 主机信息：

以一台新装的deepin虚拟机(基于debian)为例，详细信息如下：

![](http://ww1.sinaimg.cn/large/006AWYXBly1fq5av617a5j30lq0bu78m.jpg)

### 预备环境安装：

- 安装git，gdb和gdb-multiarch，同时安装binfmt用来识别文件类型

```bash
$ sudo apt-get update
$ sudo apt-get install git gdb gdb-multiarch
$ sudo apt-get install "binfmt*"
```

- 安装gdb的插件pwndbg（或者gef等支持多架构的插件）

```bash
$ git clone https://github.com/pwndbg/pwndbg
$ cd pwndbg
$ ./setup.sh
```

装好之后如图：

![](http://ww1.sinaimg.cn/large/006AWYXBly1fq5c1vzla8j30nb04t75m.jpg)

- 安装pwntools，不必要，但绝对是写exp的神器

  ```bash
  $ sudo pip install pwntools
  ```

### 安装qemu：

```bash
$ sudo apt-get install qemu-user
```

通过qemu模拟arm/mips环境，进而进行调试

### 安装共享库：

此时已经可以运行静态链接的arm/mips binary了，如下图：

![](http://ww1.sinaimg.cn/large/006AWYXBly1fq5crjvp5dj31400p0ngj.jpg)

但还不能运行动态链接的binary，如下图：

![](http://ww1.sinaimg.cn/large/006AWYXBly1fq5csjo38rj313o05i779.jpg)

这就需要我们安装对应架构的共享库，可以通过如下命令搜索：

```bash
$ apt-cache search "libc6" | grep ARCH
```

![](http://ww1.sinaimg.cn/large/006AWYXBly1fq5cudid7gj30xy0h7trd.jpg)

我们只需安装类似**libc6-ARCH-cross**形式的即可

### 运行：

静态链接的binary直接运行即可，会自动调用对应架构的qemu；

动态链接的bianry需要用对应的qemu同时指定共享库路径，如下图32位的动态链接mips binary

![](http://ww1.sinaimg.cn/large/006AWYXBly1fq5d1guaxvj313m03bq55.jpg)

使用-L指定共享库：

```bash
$ qemu-mipsel -L /usr/mipsel-linux-gnu/ ./add
```

![](http://ww1.sinaimg.cn/large/006AWYXBly1fq5d3xxmfqj30z50c4ahc.jpg)

### 调试：

可以使用qemu的-g指定端口

```bash
$ qemu-mipsel -g 1234 -L /usr/mipsel-linux-gnu/ ./add
```



然后使用gdb-multiarch进行调试，先指定架构，然后使用remote功能

```bash
pwndbg> set architecture mips
pwndbg> target remote localhost:1234
```

![](http://ww1.sinaimg.cn/large/006AWYXBly1fq5dbufgrjj31400p013o.jpg)

这样我们就能进行调试了

![](http://ww1.sinaimg.cn/large/006AWYXBly1fq5de5c26aj31400p046h.jpg)

###　效果图：

![](http://ww1.sinaimg.cn/large/006AWYXBly1fq5de5c26aj31400p046h.jpg)

![](http://ww1.sinaimg.cn/large/006AWYXBly1fq5dg64kb8j31400p0tgd.jpg)

### more：

同样，如果想要运行或者调试其他架构的binary，只需安装其他架构的qemu和共享库即可

### reference：

https://docs.pwntools.com/en/stable/qemu.html

https://reverseengineering.stackexchange.com/questions/8829/cross-debugging-for-arm-mips-elf-with-qemu-toolchain

