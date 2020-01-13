# Play_with_python following the plural site python skill path
pluralsight course: 
>```https://app.pluralsight.com/library/courses/python-big-picture```
>```https://app.pluralsight.com/library/courses/python-getting-started```
>```https://app.pluralsight.com/library/courses/python-fundamentals/table-of-contents```

##Python-big-picture
Python is a high level programming language. 
You won't have to deal with a low level assembly instructions, machine specific details, or other minute things. 
With Python you get to enjoy all the benefits that using any high level programming language brings you. 

Python is a language with a <b>dynamic</b> type system. 
This means that any type checks in the programming language happen at runtime instead of compile time. 

Programmers that prefer a dynamically type language often discuss how dynamic languages are usually simple, have smaller source footprints due to the lack of type annotations spread throughout the code. 
They're quicker to read due to less type clutter. 
And with the lack of a compiler phase, they can lead to a quicker turnaround when making software changes. 
Python and the culture of Python programmers plays a huge emphasis on <b>readability</b>. 
So after you know Python, it can be a very pleasant experience reading and learning other Python code. 

Fundamentally Python is usually used as an <b>interpreted language</b>. 
This provides very powerful prototyping and live coding opportunities and can also aid in live debugging efforts. 
It does mean the code can be slower than compiled code, but engineering is always a game of trade-offs. 

Python is also a <b>multi-paradigm programming language</b>. Python directly supports both object-oriented and structure-oriented programming.
It also embraces many functional programming concepts, especially when working with groups of things. 
Overall Python is a very powerful language that can be used in many different ways and in many different areas. 

###When to use Python
Linux scripting and administration
* Files 
* Configurations
* Processes 
* Application

Web Development 
###Flask
* ```set FLASK_APP=web_development\service.py```
* ```flash run```
* ```curl http://127.0.0.1:5000/``` 
* ```curl http://127.0.0.1:5000/user/sharon```
###django
* ```python -m pip install Django```
* ```django-admin startproject mysite```
* ```python manage.py runserver```
* ```curl http://127.0.0.1:8000```

 ##Python-getting-started
###Prereq to install flask
Flask is a lightweight WSGI(Web Server Gateway Interface) web application framework. 
It is designed to make getting started quick and easy, with the ability to scale up to complex applications. 
It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.
https://pypi.org/project/Flask/
>```pip install flask```


##Beyond the basics
###Packages
module is one source file that can be loaded using 'import' 
a package is a special type module to add structure, can contain multiple modules and gives them a hierarchical structure. 
grouping modules in a logical way 
packages are represented as directories in the file system but the module is a single file 

sys.path is a list of directories Python searches for modules
```
>>> import sys
>>> sys.path
['', 'C:\\Python27\\Lib\\idlelib', 'C:\\WINDOWS\\SYSTEM32\\python27.zip', 'C:\\Python27\\DLLs', 'C:\\Python27\\lib', 'C:\\Python27\\lib\\plat-win', 'C:\\Python27\\lib\\lib-tk', 'C:\\Python27', 'C:\\Python27\\lib\\site-packages']
```

adding entries to sys.path
```
>>> import sys
>>> sys.path.append('my_package')

>>> import my_package
>>> my_package.found()
Pythin found me!

```


  