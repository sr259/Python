When trying to run your python code one day, your computer crashed. Hopefully all your files saved, but as you rebooted your computer,
you see that everthing you wrote has become absolutely jumbled up! Your loops are all misplaced and your variables are now instatiated wrong!
What are you to do? Instead of rebooting or redownloading the software, you decide to go along and simply get accustomed to this new language. Introducing Nothyp (pronounced Not Hype or Not Hip, because as you will see, this language is not very hip), a language that is just mildly annoying.

This language is simply python but things seem to be out of place. For loops are now variables and defining functions have now never been so confusing. Heres a rundown of the language and what it can implement.

1. Variables are defined by for loops

variable: "for" NAME "in" data_type ":"
         |"for" NAME "in" expression ":"

2. for loops are defined by if statements

for_loop: "if" NAME comparison numeric ":"
    | "if" NAME comparison string ":"
    | "if" NAME comparison list ":"

3. while loops are defined by defining functions

while_loop: "def" NAME "(" expression ")"

4. printing something is now with using the function type()

print: "type(" [NAME]+ ")"

5. defining functions are with while loops

define_func: "while" NAME comparison (NAME)+ ":"

6. calling functions are done with the list() command

call_func: "list(" NAME "," argument_list ")"

7. returns are done with continue

8. if statements are done with the print() command

9. else is done with break

10. elif is done with the abs() commmand

Comparisons are all jumbled too! True is now equal to false, '<=' is now '>=', and '!=' is now '==', and all you can think of! How annoying.

**There are some important things to note, this language is not perfect. It unfortunately cannot handle
indentation or some type of comparisons, as well as a lot of the specific syntax python has to offer.
It can handle some math expressions, comparisons, and a minimal amount of data types (numbers, strings, lists, 
and boolean values).

Nothyp.py holds the grammar.
Interpreter.py holds the interpreter.
runme.py is what you want run, it will ask for some inputs. There are input examples in the examples.txt file.





