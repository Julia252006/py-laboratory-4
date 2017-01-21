# Create function that write some info
# into file object and flash data in decorator part

data_lst = ["index.php", "main.py", "__init__.py", "core.py", "data.bin"]


def mydecor(func):
    def my_decor(item):
        data_file = open("config.data", "r+")
        func(data_file, item)
        data_file.close()

    return my_decor


@mydecor
def writeConfig(file, line):
    if "Configuration file! Do not modify!" in file.read():
        file.write("%s;\n" % (line))
    else:
        file.write("Configuration file! Do not modify!\n" + \
                   "%s;\n" % (line))


for item in data_lst:
    writeConfig(item)
