class Module():
    def __init__(self, id, name, description) -> None:
        self.id = id
        self.name = name
        self.desc = description
        self.path = "modules/" + self.id + "/" + self.id + ".py"
    
    def __repr__(self) -> str:
        return self.id
    
    def get_info(self):
        return self.id, self.name, self.desc
    
    def run(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location("mod", self.path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod.get_main_screen()


def load_modules():
    # Returns a list of all the modules information
    files = get_files_list()
    module_files = get_modules_files(files)
    modules = []
    for path in module_files:
        modules.append(load_module(path))
    return modules

def get_files_list():
    # Returns a list of all files in the modules directory
    from os import listdir, getcwd
    from os.path import isfile, join
    cwd = getcwd()
    path = cwd + "/modules"
    files_list = [f for f in listdir(path) if isfile(join(path, f))]
    return files_list

def get_modules_files(list):
    # Returns a list of all the module files
    mod = []
    for f in list:
        if f.split(".")[-1] == "dtm":
            mod.append(f)
    return mod

def load_module(path):
    # Creates a module from a module file's path
    from json import load
    f = load(open("modules/" + path, "r"))
    id = f["id"]
    name = f["name"]
    description = f["description"]
    return Module(id, name, description)