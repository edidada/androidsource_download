#windows
* install python
* install msysgit

在git bash中执行：

<pre><code>
git clone https://android.googlesource.com/platform/manifest.git
cd manifest
git tag
git checkout android-4.4.2_r1
</code></pre>
修改download_src.py

执行download_src.py

原理，通过pythoy调用git相关等命令，安卓源码是通过多个git仓库来管理的

#Ubuntu 16.04

[java环境变量设置](http://blog.csdn.net/ameyume/article/details/14452245)
