#!/usr/bin/env python3
#-*- encoding:utf-8 -*-
from typing import Optional, Dict
import sys
import pickle


class LynFileSystemException(Exception):
    """
    所有在使用该程序时会产生的错误
    """
    pass


class DeleteException(LynFileSystemException):
    pass


class CdPathException(LynFileSystemException):
    pass


class OpenException(LynFileSystemException):
    pass


class FNode(object):
    def __init__(self, name):
        self.name = name


class File(FNode):
    def __init__(self, name: str)->None:
        super(File, self).__init__(name)
        self.content = ""

    def read(self)->str:
        return self.content

    def write(self, content: str)->None:
        self.content = content


class DirFile(FNode):
    def __init__(
            self,
            root: Optional['DirFile'] = None,
            name: str = "/")->None:
        super(DirFile, self).__init__(name)
        self.root = root
        self.files: Dict[str, FNode] = {"..": root, ".": self}

    def mkdir(self, name: str):
        self.files[name] = DirFile(self, name)

    def rmdir(self, name: str):
        if not self.files[name]:
            print("不存在该文件")
        elif isinstance(self.files[name], DirFile):
            del self.files[name]
            print("已经删除了目录", name)
        else:
            raise DeleteException(name, "该文件类型不属于目录")

    def ls(self):
        print('filename\ttype')
        for name in self.files.keys():
            if self.files[name]:
                if isinstance(self.files[name], File):
                    print(name, "\t", "file")
                elif isinstance(self.files[name], DirFile):
                    print(name, "\t", "director")
            else:
                print(name, "\t", "director")

    def create(self, name):
        self.files[name] = File(name)

    def delete(self, name):
        del self.files[name]
        print("删除了文件", name)

    def __repr__(self)->str:
        return repr(self.files)

    def __getitem__(self, key):
        return self.files.__getitem__(key)


class FileSystem(object):
    def __init__(self, name: str)->None:
        self.name = name
        self.rootdir: DirFile = DirFile()
        self.nowdir: DirFile = self.rootdir
        self.openfile: Optional[File] = None

    @property
    def pwd(self)->str:
        tmpdir = self.nowdir
        path = ""
        while tmpdir[".."] is not None:
            path = tmpdir.name + "/" + path
            tmpdir = tmpdir[".."]
        path = "/" + path
        return path

    @property
    def nowpath(self):
        return self.nowdir.name

    def info(self):
        return self.name + "@" + self.nowdir.name + "> "

    def _absolute_cd(self, absolute_path: str)->None:
        paths = filter(lambda p: p != "", absolute_path.split("/"))
        tmpdir = self.rootdir
        try:
            for path in paths:
                tmpdir = tmpdir[path]
        except Exception:
            raise CdPathException("路径名错误")
        self.nowdir = tmpdir

    def _relatice_cd(self, relativ_path: str)->None:
        paths = filter(lambda p: p != "", relativ_path.split("/"))
        tmpdir = self.nowdir
        try:
            for path in paths:
                tmpdir = tmpdir[path]
        except Exception:
            raise CdPathException("路径名错误")
        self.nowdir = tmpdir

    def cd(self, path: str):
        if path.startswith("/"):
            self._absolute_cd(path)
        else:
            self._relatice_cd(path)

    def mkdir(self, path: str):
        self.nowdir.mkdir(path)

    def rmdir(self, path: str):
        self.nowdir.rmdir(path)

    def ls(self)->None:
        self.nowdir.ls()
        return

    def open(self, filename: str)->None:
        if self.nowdir[filename] and isinstance(self.nowdir[filename], File):
            self.openfile = self.nowdir[filename]
        else:
            raise OpenException("不存在该文件,或文件类型不为file")

    def write(self):
        number = 1
        content = ""
        while True:
            try:
                newcontent = input(str(number) + " ")
                number += 1
                content += newcontent
            except EOFError:
                self.openfile.write(content)
                return

    def close(self)->None:
        self.openfile = None

    def read(self)->None:
        print(self.openfile.read())

    def create(self, filename)->None:
        self.nowdir.create(filename)
        return

    def delete(self, filename)->None:
        self.nowdir.delete(filename)
        return

    def __repr__(self):
        return "<FileSystem " + self.name + " >"


_now_filesystem: FileSystem = None
_name: str = None
indicator = ">> "


exec_command = {}


def add_command(command: str):
    """
    decorator
    给exec_command注册命令相关的函数
    """
    def wrapper(func):
        exec_command[command] = func
        return func
    return wrapper


def sholdhavefilesystem(f):
    """
    必须拥有文件系统才可以使用
    """
    def wrapper(*args, **kwargs):
        if _now_filesystem:
            f(*args, **kwargs)
        else:
            print("没有可用的文件系统")
    return wrapper


def updateIndicator(f):
    """
    需要更新指示符的命令
    """
    def wrapper(*args, **kwargs):
        res = f(*args, **kwargs)
        global indicator
        indicator = _now_filesystem.info() if _now_filesystem else ">> "
        return res
    return wrapper


@add_command("sfs")
@updateIndicator
def sfs(systemname: str):
    global _now_filesystem
    global _name
    _name = systemname
    with open(systemname, "rb") as f:
        _now_filesystem = pickle.load(f)


@add_command("new")
@updateIndicator
def new(systemname: str):
    global _now_filesystem
    global _name
    _name = systemname
    _now_filesystem = FileSystem(systemname)


@add_command("save")
def save(systemname: str)->None:
    with open(systemname, "wb") as f:
        pickle.dump(_now_filesystem, f)


@add_command("exit")
def exit():
    if _name and _now_filesystem:
        save(_name)
    sys.exit(0)


@add_command("pwd")
@sholdhavefilesystem
@updateIndicator
def pwd():
    print(_now_filesystem.pwd)


@add_command("mkdir")
@sholdhavefilesystem
def mkdir(name: str):
    _now_filesystem.mkdir(name)


@add_command("ls")
@sholdhavefilesystem
def ls():
    _now_filesystem.ls()


@add_command("cd")
@sholdhavefilesystem
@updateIndicator
def cd(path):
    try:
        _now_filesystem.cd(path)
    except CdPathException as e:
        print("路径名错误，请输入正确的路径名")


@add_command("create")
@sholdhavefilesystem
def create(name: str):
    _now_filesystem.create(name)


@add_command("delete")
@sholdhavefilesystem
def delete(name: str):
    _now_filesystem.delete(name)


@add_command("rmdir")
@sholdhavefilesystem
def rmdir(name: str):
    _now_filesystem.rmdir(name)


@add_command("write")
@sholdhavefilesystem
def write():
    _now_filesystem.write()


@add_command("read")
@sholdhavefilesystem
def read():
    _now_filesystem.read()


@add_command("open")
@sholdhavefilesystem
def openfile(filename: str):
    _now_filesystem.open(filename)


@add_command("close")
@sholdhavefilesystem
def closefile():
    _now_filesystem.close()


def clientCommand()->None:
    while True:
        try:
            line = input(indicator)
            commands = line.split()
            if len(commands) == 1:
                exec_command[commands[0]]()
            else:
                exec_command[commands[0]](*commands[1:])
        except EOFError:
            print("error")
            sys.exit(0)
        except KeyError:
            print("请输入有效的命令")
        except TypeError:
            print("请输入正确的参数")
        except LynFileSystemException as e:
            print(e)


if __name__ == "__main__":
    clientCommand()
