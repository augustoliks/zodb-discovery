# discovery-zodb

- __Date__: 04/11/2020
- __Author__: [@augustoliks](https://github.com/augustoliks) | <carlos.santos110@fatec.sp.gov.br>
- __Description__: Simple project with Python + ZODB.
- __Objective__: Explore ZODB. 

- __Actual Features__:
    - Insert objects with inherited dependencies;
    - Recovery objects.

## Introduction to the ZODB (by Michel Pelletier)

For many tasks, relational databases are clearly a good solution, but sometimes relational databases don’t fit well with your object model. If you have lots of different kinds of interconnected objects with complex relationships, and changing schemas then ZODB might be worth giving a try.

A major feature of ZODB is transparency. __You do not need to write any code to explicitly read or write your objects to or from a database__. You just put your persistent objects into a container that works just like a Python dictionary. Everything inside this dictionary is saved in the database. This dictionary is said to be the "root" of the database. It’s like a magic bag; any Python object that you put inside it becomes persistent.

Actually there are a few restrictions on what you can store in the ZODB. You can store any objects that can be "pickled' into a standard, cross-platform serial format. Objects like lists, dictionaries, and numbers can be pickled. Objects like files, sockets, and Python code objects, cannot be stored in the database because they cannot be pickled. For more information on “pickling”, see the Python pickle module documentation at http://www.python.org/doc/current/lib/module-pickle.html

## Running Example

```bash
$ git clone https://github.com/augustoliks/zodb-discovery
$ cd discovery-zodb/
$ virtualenv --python=$(which python3) venv
$ source venv/bin/activate
(venv) $ pip3 install -r requirements.txt 
```

```shell
(venv) $ python3 app.py 

[+] Add new employee: Tommie Hayes

read all employees on disk
         - Tommie Hayes contracted by Carlos Neto at 2020-11-04 22:30:59.065217
```

```shell
(venv) $ python3 app.py 

Ignoring index for /home/augustoliks/gitlab/discovery-zodb/discovery-zodb/database-employees.fs

[+] Add new employee: Emily Walt

read all employees on disk
         - Tommie Hayes contracted by Carlos Neto at 2020-11-04 22:30:59.065217
         - Emily Walt contracted by Carlos Neto at 2020-11-04 22:31:02.335004
```

```shell
(venv) $ python3 app.py 

[+] Add new employee: Naida Chavis

read all employees on disk
         - Tommie Hayes contracted by Carlos Neto at 2020-11-04 22:30:59.065217
         - Emily Walt contracted by Carlos Neto at 2020-11-04 22:31:02.335004
         - Naida Chavis contracted by Carlos Neto at 2020-11-04 22:31:04.289794
```

```shell
(venv) $ python3 app.py 

[+] Add new employee: Edna Jackson

read all employees on disk
         - Tommie Hayes contracted by Carlos Neto at 2020-11-04 22:30:59.065217
         - Emily Walt contracted by Carlos Neto at 2020-11-04 22:31:02.335004
         - Naida Chavis contracted by Carlos Neto at 2020-11-04 22:31:04.289794
         - Edna Jackson contracted by Carlos Neto at 2020-11-04 22:31:05.276756
```

## Reference

- http://www.zodb.org/en/latest/articles/ZODB1.html
