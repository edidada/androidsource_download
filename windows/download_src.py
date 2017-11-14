import xml.dom.minidom  
import os  
from subprocess import call  

rootdir = "G:/android_android-6.0.1-r9_source"  

git = "C:/Program Files/Git/bin/git.exe"  

dom = xml.dom.minidom.parse("G:/manifest/default.xml")  
root = dom.documentElement  

prefix = git + " clone https://aosp.tuna.tsinghua.edu.cn/"  
suffix = ".git"  
      
if not os.path.exists(rootdir):  
    os.mkdir(rootdir)  
      
for node in root.getElementsByTagName("project"):  
    os.chdir(rootdir)  
    d = node.getAttribute("path")  
    last = d.rfind("/")  
    if last != -1:  
        d = rootdir + "/" + d[:last]  
        if not os.path.exists(d):  
            os.makedirs(d)  
        os.chdir(d)  
    cmd = prefix + node.getAttribute("name") + suffix  
    call(cmd)  