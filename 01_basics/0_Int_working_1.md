by doing this, we got one folder with name of "__pycache__" inside "hello.cpyhton-312.pyc"

Python Inner Working:--
|----------|     
|          |         Byte Code       |------- ----------|
|          |===>  (mostly hidden)===>|Python virtual M/C|
|__________|                         |__________________| 
 (SRC file)                                 (PVM)



1)Compile to Byte Code
                 (low level code and plateform independent)
 -> Byte code runs faster
 -> .pyc =>compiled python(frozen binaries)

2)"__pycache__"
         (src change and python version)
  -> "hello.cpython-312.pyc" 
  -> Works only for "IMPORTED FILES"
      NOT For top levels files.

3)Python Virtual M/C:-
  ->code loop  to iterate byte code/directly src file
  ->Run time engine
  ->also known as "PYTHON INTERPRETER"

4)Byte code is not M/C code(which instuct directly to hardware)
 ->python specific INTERPRETER
 ->cpython(Std implentation), jpyhton, stackless, Iron pyhton, PyPy
