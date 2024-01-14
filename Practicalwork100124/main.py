print("Hello world")
input()

script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
def chwd(path):
    if os.path.exists(path):
        os.chdir(path)
chwd(script_directory)