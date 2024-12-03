# Instalation

Simply clone the repository or download the latest release and copy the files in your prefered folder.

**Launching**

You need to have Python installed.
- On Windows, simply launch the Main.pyw file
- On linux, open a terminal in the directory which holds the main files and run ```python3 Main.pyw```

# Adding modules

**Adding any module is quite simple:**
- download any files necessary from the module's github page / website
- move the DTM file to the 'modules' folder
- folow any other instalation process specified by the module's editor

*Remember that we do not provide any waranty of security for installed modules.*

# Creating a module

DeskThing offers a simple way of creating basic modules, but more complex ones may require a consequent amount of work.

Modules should be published under the MIT License.

The basic file structure is as follows:
```
Modules
├── module_id.dtm
│   module_id
│   ├── module_id.py
│   └── any other files of the module
```

The main DTM file should look like this, with a JSON syntax:
``` json
{
    "name": "", // the name of the module
    "id": "", // the 'module ID'
    "description": "", // a shot description of the module
    "path": "" // the relative path to the main python file
}
```

Here is an example:
``` json
{
    "name": "Example module", // can have capital letters, spaces, dashes and underscores
    "id": "example_module", // can only have lowercase letters and underscores
    "description": "An example module, made for the documentation",
    "path": "modules/example_module/example_module.py"
}
```