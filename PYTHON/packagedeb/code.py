'''Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.
Try the new cross-platform PowerShell https://aka.ms/pscore6

PS D:\packagedeb> & C:/Users/This_PC/AppData/Local/Programs/Python/Python310/python.exe 
d:/packagedeb/packagedeb/__init__.py
PS D:\packagedeb> python setup.py sdist bdist_wheel
usage: setup.py [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
   or: setup.py --help [cmd1 cmd2 ...]
   or: setup.py --help-commands
   or: setup.py cmd --help

error: invalid command 'bdist_wheel'
PS D:\packagedeb> pip install wheel
Collecting wheel
  Downloading wheel-0.37.1-py2.py3-none-any.whl (35 kB)
Installing collected packages: wheel
Successfully installed wheel-0.37.1
PS D:\packagedeb> python setup.py sdist bdist_wheel
running sdist
running egg_info
creating packagedeb.egg-info
writing packagedeb.egg-info\PKG-INFO
writing dependency_links to packagedeb.egg-info\dependency_links.txt
writing top-level names to packagedeb.egg-info\top_level.txt
writing manifest file 'packagedeb.egg-info\SOURCES.txt'
reading manifest file 'packagedeb.egg-info\SOURCES.txt'
adding license file 'licence.txt'
writing manifest file 'packagedeb.egg-info\SOURCES.txt'
running check
warning: check: missing required meta-data: url

warning: check: missing meta-data: if 'author' supplied, 'author_email' should be supplied too

creating packagedeb-0.1
creating packagedeb-0.1\packagedeb
creating packagedeb-0.1\packagedeb.egg-info
copying files to packagedeb-0.1...
copying licence.txt -> packagedeb-0.1
copying setup.py -> packagedeb-0.1
copying packagedeb\__init__.py -> packagedeb-0.1\packagedeb
copying packagedeb.egg-info\PKG-INFO -> packagedeb-0.1\packagedeb.egg-info
copying packagedeb.egg-info\SOURCES.txt -> packagedeb-0.1\packagedeb.egg-info
copying packagedeb.egg-info\dependency_links.txt -> packagedeb-0.1\packagedeb.egg-info
copying packagedeb.egg-info\top_level.txt -> packagedeb-0.1\packagedeb.egg-info
Writing packagedeb-0.1\setup.cfg
creating dist
Creating tar archive
removing 'packagedeb-0.1' (and everything under it)
running bdist_wheel
running build
running build_py
creating build
creating build\lib
creating build\lib\packagedeb
copying packagedeb\__init__.py -> build\lib\packagedeb
installing to build\bdist.win-amd64\wheel
running install
running install_lib
creating build\bdist.win-amd64
creating build\bdist.win-amd64\wheel
running install_egg_info
Copying packagedeb.egg-info to build\bdist.win-amd64\wheel\.\packagedeb-0.1-py3.10.egg-info
running install_scripts
adding license file "licence.txt" (matched pattern "LICEN[CS]E*")
creating build\bdist.win-amd64\wheel\packagedeb-0.1.dist-info\WHEEL
creating 'dist\packagedeb-0.1-py3-none-any.whl' and adding 'build\bdist.win-amd64\wheel' to it
adding 'packagedeb/__init__.py'
adding 'packagedeb-0.1.dist-info/METADATA'
adding 'packagedeb-0.1.dist-info/WHEEL'
adding 'packagedeb-0.1.dist-info/top_level.txt'
adding 'packagedeb-0.1.dist-info/RECORD'
removing build\bdist.win-amd64\wheel
PS D:\packagedeb> cd .\dist\
PS D:\packagedeb\dist> ls


    Directory: D:\packagedeb\dist


Mode                 LastWriteTime         Length Name
-a----        10-06-2022  09:30 AM           1470 packagedeb-0.1-py3-none-any.whl       
-a----        10-06-2022  09:30 AM           1025 packagedeb-0.1.tar.gz


PS D:\packagedeb\dist> pip install .\packagedeb-0.1.tar.gz
Processing d:\packagedeb\dist\packagedeb-0.1.tar.gz
  Preparing metadata (setup.py) ... done
Building wheels for collected packages: packagedeb
  Building wheel for packagedeb (setup.py) ... done
  Created wheel for packagedeb: filename=packagedeb-0.1-py3-none-any.whl size=1470 sha256=3140e63db85e73dde28ecfebc1c27ab9ddb55f1eec3300cb3fcff08eb5e5f67d
  Stored in directory: c:\users\this_pc\appdata\local\pip\cache\wheels\68\01\47\7476458b658fec5c38b665887a2d02bf0ccbe5330864343321
Successfully built packagedeb
Installing collected packages: packagedeb
Successfully installed packagedeb-0.1
PS D:\packagedeb\dist> cd ../
PS D:\packagedeb> '''