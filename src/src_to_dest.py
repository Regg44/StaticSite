import os, shutil

def src_to_dest(source, destiny):
    print(destiny)
    shutil.rmtree(destiny + "/.", True)
    print(source, os.listdir(source))
    for entry in os.listdir(source):
        entry_path = os.path.join(source, entry)
        destiny_path = os.path.join(destiny, entry)
        if os.path.isdir(entry_path):
            os.mkdir(destiny_path)
            src_to_dest(entry_path, destiny_path)
        else:
            shutil.copy(entry_path, destiny_path)



