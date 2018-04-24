#include <Python.h>

static PyObject* printhello(PyObject* self) {
   return Py_BuildValue("s", "Hello, Learning to build Python extensions!!");
}

static PyObject* printhello_withargs(PyObject* self, PyObject *args ) {
   return Py_BuildValue("s", "Hello, with args!!");
}

static char helloworld_docs[] =
   "helloworld( ): Any message you want to put here!!\n";

static PyMethodDef helloworld_funcs[] = {
   {"printhello", (PyCFunction)printhello, 
   "printhelloargs", (PyCFunction)printhello_withargs, 
      METH_NOARGS, helloworld_docs},
      {NULL}
};

void initmymodule(void) {
   Py_InitModule3("printhello", helloworld_funcs,
                  "Extension module example!");
}
