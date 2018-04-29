#include <Python.h>

/* One module with Two functions calls are shown here.

import helloworld

print helloworld.helloworld()

print helloworld.helloworld_two()

*/


static PyObject* helloworld(PyObject* self) {
   return Py_BuildValue("s", "Hello, Python extensions!!");
}

static PyObject* helloworld_two(PyObject* self) {
   return Py_BuildValue("s", "Hello From hello world_two Python C extension !!");
}

static char helloworld_docs[] =
   "helloworld( ): Any message you want to put here!!\n";

//Notice the second function declared here. All in one line
//helloworld.helloworld_two()


static PyMethodDef helloworld_funcs[] = {
   {"helloworld", (PyCFunction)helloworld, METH_NOARGS, helloworld_docs},
   {"helloworld_two", (PyCFunction)helloworld_two, METH_NOARGS, helloworld_docs},
      {NULL}
};

void inithelloworld(void) {
   Py_InitModule3("helloworld", helloworld_funcs,
      "Extension module example!");
}