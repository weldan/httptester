httptester
==========

HTTP connection tester

install required modules/program (ubuntu)
=================================
```bash
$ make
```


usage
=====

direct connection
=================
```bash
$ python httptester.py --host http://mweldan.com 
```

connect via tor
=================
```bash
$ python httptester.py --host http://mweldan.com --tor 1
```

connect via http proxy
=================
```bash
$ python httptester.py --host http://mweldan.com --proxy proxyhost:proxyport 
```

bug report and else
====================
create new ticket or email me at mweldan@gmail.com
