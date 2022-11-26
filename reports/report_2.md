# Milestone 2

## Task 2
### What is a Hash function
While transferring a file from one computer to another it is often important to ensure that the copied file is the same as the source. One method one could use is called `hashing`, which is essentially a process that translates information about the file into a code. Two hash values (of the original file and its copy) can be compared to ensure the files are equal.

`Hash function` is an algorithm that calculates a fixed-size bit string value from a file.
A file basically contains blocks of data. `Hashing` transforms this data into a far shorter fixed-length value or key which represents the original string. The `hash value` can be considered the distilled summary of everything within that file.

A good `hash function` would exhibit a property called the avalanche effect, where the resulting hash output would change significantly or entirely even when a single bit or byte of data within a file is changed. A `hash functio`n that does not do this is considered to have poor randomization, which would be easy to break by hackers.

A hash is usually a hexadecimal string of several characters. Hashing is also a unidirectional process so you can never work backwards to get back the original data.

A good `hash function` should be complex enough such that it does not produce the same hash value from two different inputs. If it does, this is known as a hash collision. A `hash function` can only be considered good and acceptable if it can offer a very low chance of collision.


### What is a Python module, package and script? How do they differ from one another?
- A `Script` is a runnable Python programs that do something when executed.
Scripts will often contain code written outside the scope of any classes or functions. 
- A `Module` is a Python file that is intended to be imported into scripts and other modules. It often defines members like classes, functions, and variables intended to be used in other files that import it.
- A `Package` is a collection of related modules that work together to provide certain functionality. These modules are contained within a folder and can be imported just like any other modules. This folder will often contain a special __init__ file that tells Python it’s a package, potentially containing more modules nested within subfolders.







## Task 5
How to create a `pip "requirements file"` for the code base and get it work within a virtualenv.

Create a virutal environment (named `venv`) for Python with a separate interpreter:
```
python3 -m venv venv
```

To activate virtual environment, use the command `source`:
```
source venv/bin/activate
```

Having installed all the necessery packages using packet manager pip, 
we use command 
``` 
pip freeze 
```
to view currently installed packages.

To add packages use
```
pip install 
```

To create requirements file use
```
pip freeze > requirements.txt
```

We have created a `requirements.txt` file with requirements for the code.

To run the code on the new machine we have to pass over the python code
and the requirements file.

The virtual einvironment with dependencies can be set up by executing following commands:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

