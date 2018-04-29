# This is the Sample code for writing modules in C and integrating that to the Python Interpreter.

#### To build - look at the sample code, and the build file below

##### python setup.py build 
##### sudo python setup.py install 


https://www.tutorialspoint.com/python/python_further_extensions.htm

This code is built for python and not Python3 !

	sudo python setup.py install

This is the module that we want to see written using our module.


	#!/usr/bin/python
	import helloworld

	print helloworld.helloworld()

1.
The C functions:

	static PyObject *MyFunction( PyObject *self, PyObject *args );

	static PyObject *MyFunctionWithKeywords(PyObject *self,
	   PyObject *args, PyObject *kw);

	static PyObject *MyFunctionWithNoArgs( PyObject *self );

2. 
	struct PyMethodDef {
	   char *ml_name;
	   PyCFunction ml_meth;
	   int ml_flags;
	   char *ml_doc;
	};

3. Initialization Module

	initModule - where Module is the name of the module.
	
	


Sample Code : hello.c

	#include <Python.h>
	
	static PyObject* helloworld(PyObject* self) {
	   return Py_BuildValue("s", "Hello, Python extensions!!");
	}
	
	static char helloworld_docs[] =
	   "helloworld( ): Any message you want to put here!!\n";
	
	static PyMethodDef helloworld_funcs[] = {
	   {"helloworld", (PyCFunction)helloworld, 
	      METH_NOARGS, helloworld_docs},
	      {NULL}
	};
	
	void inithelloworld(void) {
	   Py_InitModule3("helloworld", helloworld_funcs,
	      "Extension module example!");
	}
	
	
Build: setup.py

	from distutils.core import setup, Extension
	setup(name = 'helloworld', version = '1.0',  \
	      ext_modules = [Extension('helloworld', ['hello.c'])])

OR another example:	
	
	from distutils.core import setup, Extension
	
	module1 = Extension('demo',
	    sources = ['demo.c'])
	
	setup (name = 'PackageName',
	       version = '1.0',
	       description = 'This is a demo package',
	       ext_modules = [module1])


	
