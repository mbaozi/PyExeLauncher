# PyExeLauncher
一个以 exe 文件方式运行 Python 代码的开源工具，基于 Python Embed 版本，无需安装 Python 环境即可运行。

## 使用说明

运行 PyExeLauncher.exe 会使用当前目录下的 python 环境来运行 app 目录中的 python 脚本

会自动检索并执行存在的文件，优先 app.pyo，其次 app.pyc，最后 app.py

若三个文件都不存在，则提示报错

PyExeLauncher(console).exe 会显示终端窗口，适用于非 GUI 场景



## python说明

当前示例提供的 python 是基于 python-3.11.9-embed-amd64 版本，添加了标准版本的包，可以正常使用标准包，比如 tkinter。



**添加python包**

> 1. 本地环境中正常按照 python-3.11.9-amd64 版本
> 2. pip 安装自己所需要的包
> 3. 找到包所在位置，一般位于安装的 python 路径下的 Lib\site-packages 中
> 4. 拷贝需要的包到当前 python 路径的 Lib\site-packages 中



**更换python**

> 1. 下载需要 python embed 版本
>
> 2. 解压后将文件夹重命名为 python，替换当前 python 文件夹(不同版本，包会存在兼容问题，需要重新下)
>
> 3. 修改 python3xx._pth 文件(参考下方示例)
>
>    ```python
>    python311.zip
>    .
>    
>    Lib
>    DLLs
>    libs
>    tcl
>    
>    # Uncomment to run site.main() automatically
>    import site
>    ```
>
> 4. 将上方示例中涉及到的文件夹，从安装在本地环境的标准 python 版本中拷贝到当前 python 文件夹下
>
> 5. 添加其他需要的 python 包(Lib\site-packages)



