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
    "id": "", // the 'module_id'
    "name": "", // the name of the module
    "description": "", // a short description of the module
}
```

The main python file needs to have some important things:
- a *'get_main_screen'* function that returns a Kivy screen
- a *'MainScreen'* class that extends the Kivy screen class

**Here is an example:**

*File structure:*
```
Modules
├── example_module.dtm
│   example_module
│   └── example_module.py
```

*example_module.dtm:*
``` json
{
    "id": "example_module", // can only have lowercase letters and underscores
    "name": "Example module", // can have uppercase letters, spaces, dashes and underscores; basically a 'display name'
    "description": "An example module, made for the documentation", // same limitations as the name
}
```

*example_module.py:*
``` python
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label

def get_main_screen():
    return MainScreen()

class MainScreen (Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(Label(text="Welcome to the Example Module"))
```