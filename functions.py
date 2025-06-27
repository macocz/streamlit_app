FILEPATH = "todo.txt"

def get_todos(filepath=FILEPATH):
    """Read a tex file ane return list of
    to-do items
    """

    with open(filepath, "r") as file_local:
        list_local = file_local.readlines()
    return list_local


def write_todos(list_arg,filepath=FILEPATH,):
    
    with open(filepath, "w") as file_local_1:
        file_local_1.writelines(list_arg)

if __name__ == "__main__":

    print ("hello from functions")