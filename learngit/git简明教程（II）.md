# git简明教程（II）

> 这次主要介绍一些git的常用命令

## 添加SSH Key

注册github账号后，本地的Git仓库和Github仓库之间的传输是通过SSH加密的，所以需要进行相关的配置

### 1. 生成SSH Key

- 先查看主目录中有没有.ssh/id_rsa, .ssh/id_rsa.pub两个文件，在git bash中可通过

  ```bash
  cat ~/.ssh/id_rsa
  cat ~/.ssh/id_rsa.pub
  ```

  进行检查，如出现类似下图提示即未添加过SSH Key，否则跳到第2步

  ![](http://ww1.sinaimg.cn/large/006AWYXBly1fp0sbgl7g1j30hs05m0sv.jpg)

  运行

  ```bash
   ssh-keygen.exe -t rsa -C "your email"
  ```

  然后全都选择默认，一路回车即可

  ![](http://ww1.sinaimg.cn/large/006AWYXBly1fp0sojojxvj30ko0diwf6.jpg)

- 这时，主目录下就可以找到SSH Key的密钥对**.ssh/ida_rsa, .ssh/ida_rsa.pub**了，可以使用

  ```bash
  cat ~/.ssh/id_rsa
  cat ~/.ssh/id_rsa.pub
  ```

  进行查看

  ![](http://ww1.sinaimg.cn/large/006AWYXBly1fp0svdt7ytj311d0jfmy2.jpg)

  **==注意ida_rsa是私钥，不能泄露给其他人_==**

###2. 登陆github，添加Keys 

- 登陆账户，选择Settings

  ![](http://ww1.sinaimg.cn/large/006AWYXBly1fp0t0xuihlj309x08hglr.jpg)

- 选择SSH and GPG keys

  ![](http://ww1.sinaimg.cn/large/006AWYXBly1fp0t2sgrfpj307v0ga74g.jpg)

- 右上角New SSH key（SSH keys列表里是已添加过的key，GIthub允许添加多个key，每个key对应一台机器，把每台机器的key都添加到github，就可以在每台机器上向github提交代码了）

  ![](http://ww1.sinaimg.cn/large/006AWYXBly1fp0t7awm9tj30nj07saaf.jpg)

- title自拟，key文本框里id_rsa.pub的内容

  ![](http://ww1.sinaimg.cn/large/006AWYXBly1fp0ta6kecoj30lp0crjs3.jpg)

- Add SSH key，输入密码确认，就可以看到添加过的key了

  ![](http://ww1.sinaimg.cn/large/006AWYXBly1fp0tbassv8j30la0aot9b.jpg)

至此，我们就可以使用github来托管我们的远程仓库了

## 常用命令

常用命令可用下图表示

![](http://ww1.sinaimg.cn/large/006AWYXBly1fp0x2x3pntj30ik097q33.jpg)

### 克隆

- 对多人协作的工程，第一步首先要从远程库克隆

```bash
git clone username@host:/path/to/repository
```

- 远程库的地址可以从下图中所示获得（推荐使用git协议，速度更快）

![](http://ww1.sinaimg.cn/large/006AWYXBly1fp0tmnjf9ij30u80et0u3.jpg)

- 在合适的目录下打开git bash，clone远程库到本地（第一次远程clone时会提示将github添加到信任地址，yes即可）

  ![](http://ww1.sinaimg.cn/large/006AWYXBly1fp0vw12g9fj30g104ddgp.jpg)

- 接受完成后，远程仓库就已经被clone到本地了，可以看出本地和远程的目录结构是完全一样的

![](http://ww1.sinaimg.cn/large/006AWYXBly1fp0vyjffojj30gz0bkn19.jpg)

![](http://ww1.sinaimg.cn/large/006AWYXBly1fp0vzelz4vj30te0f1abk.jpg)



### 添加，提交和推送改动

- 使用git add将有更改的文件添加到缓存区

  ```bash
  git add <filename>
  git add *
  ```

- 使用git commit将改动提交到HEAD，为方便回顾，提交信息建议为有意义的信息

  ```bash
  git commit -m"提交信息"
  ```

- 使用git push将改动推送到远程

  ```bash
  git push origin master
  master可换成其他分支
  ```

  如果当前分支只有一个追踪分支，可简写为git push

  ![](http://ww1.sinaimg.cn/large/006AWYXBly1fp0wa500tvj30tz0jaqd8.jpg)

  此时，仓库的改动就已经推送到远程了，可以在github平台上验证

  ![](http://ww1.sinaimg.cn/large/006AWYXBly1fp0wc03li7j30u605gmxi.jpg)

### 版本回退

- 首先我们可以使用git log命令查看提交日志

  ```bash
  git log
  git log的查看方法类似vim，q退出，j下移
  ```

  ![深度截图_选择区域_20180304185347](../../../home/m4x/my_repo/learngit/Pics/深度截图_选择区域_20180304185347.png)

  git log会根据时间顺序排列提交日志，其中最重要的一条信息是**commit id**，每个commit id对应着一次提交，上图中，我们最新的一次commit是*my vimrc*，如果我们想***==回退到==***add some pics*的那个版本，只需执行

  ```bash
  git reset --hard 29043
  commit id不必写全，能起到唯一标示的作用即可
  ```

  ![](http://ww1.sinaimg.cn/large/006AWYXBly1fp0zqc06twj30cp029wes.jpg)

  此时再查看git log或者仓库内文件的内容，可以发现我们已经**回退到过去了**

  ![](http://ww1.sinaimg.cn/large/006AWYXBly1fp0zsnx34jj30m408jjvh.jpg)

  > git log --pretty=oneline
  >
  > 上条命令将以上图所示方式，每行打印一条commit信息

  ***那如果我们想==回到将来==，该怎么办呢？***

  可以先用git reflog命令查看命令执行的记录

  ```bash
  git reflog
  ```

  ![](http://ww1.sinaimg.cn/large/006AWYXBly1fp0zxm2aezj30mn089q72.jpg)

  比如我们想回到*my vimrc*这次commit，使用git reflog就找到了我们想回到的，“将来的”commit id，git reset即可

  ```bash
  git reset --hard 85cd8
  ```

  ![](http://ww1.sinaimg.cn/large/006AWYXBly1fp102ejh8oj30c102egm6.jpg)

  这样我们就又回到了将来

  #### tricks

  - 对于简单的回退到上次commit，可以直接使用

    ```bash
    git reset --hard HEAD^
    ```

  - 同理上上次可以使用

    ```bash
    git reset --hard HEAD^^
    ```

  - 往上100个版本，可以使用

    ```bash
    git reset --hard HEAD~100
    ```

    ![](http://ww1.sinaimg.cn/large/006AWYXBly1fp108j87z6j30mu0fmqaj.jpg)

### 分支

>  为了保证开发时不同程序员不相互干扰，往往需要创建多个分支（master为默认分支），在其他分支上进行开发，完成后再将他们合并到主分支上
>
> ![](http://ww1.sinaimg.cn/large/006AWYXBly1fp10s4k0kxj30rh0hbgng.jpg)

- 创建分支

  ```bash
  git checkout -b feature_x
  创建一个叫"feature_x"的分支，并切换过去
  ```

  ![](http://ww1.sinaimg.cn/large/006AWYXBly1fp10n0gw8vj30jy077go0.jpg)

  > git branch查看当前所有分支git

- 切换回主分支

  ```bash
  git checkout master
  ```

- 删除新建分支

  ```bash
  git branch -d feature_x
  ```

  ![](http://ww1.sinaimg.cn/large/006AWYXBly1fp10q9hxjpj30k7099n1i.jpg)

  不能删除当前所在的分支

  > 除非将分支推送到远程仓库，否则该分支就是不为他人所见的
  >
  > ```bash
  > git push origin <branch>
  > ```

### 更新与合并

- 在每次工作前，建议先执行

  ```bash
  git pull
  ```

  获取远程仓库的更新

- 当前分支所有任务完成后，使用

  ```bash
  git merge <branch>
  ```

  即可把branch的工作成果合并到master分支上



对配置管理这门课，以上命令已经足够使用，想要了解更多git的用法可以参考

## reference

https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000

http://marklodato.github.io/visual-git-guide/index-zh-cn.html

http://rogerdudler.github.io/git-guide/index.zh.html

http://www.ruanyifeng.com/blog/2014/06/git_remote.html

### 







