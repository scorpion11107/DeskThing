# Instalation

Simply clone the repository or download the latest release and copy the files in your prefered directory.

**Launching**

You need to have Python installed.
- On Windows, simply launch the Main.pyw file
- On Linux, open a terminal in the directory which holds the main files and run ```python3 Main.pyw```

# Adding modules

**Adding any module is quite simple:**
- download any files necessary from the module's github page / website
- move the DTM file and the main directory to the *'modules'* directory
- folow any other instalation process specified by the module's editor

*Remember that we do not provide any waranty of 'working as intended' or of security for installed modules.*

# Creating a module

DeskThing offers a simple way of creating basic modules, but more complex ones may require a consequent amount of work.

The basic file structure is as follows:
```
Modules
├── module_name.dtm
│   module_name
│   ├── name_of_main_file.py
│   └── any other files of the module
```

The main DTM file should look like this, with a JSON syntax:
``` json
{
    "name": "", // the name of the module
    "description": "", // a shot description of the module
    "path": "" // the relative path to the main python file
}
```
