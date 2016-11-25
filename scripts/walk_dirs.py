import os

# list = [ (a,b,c) for (a,b,c) in os.walk('/Users/vladimirsivanovs/IdeaProjects/linux-command-lines')]


all_files = [(cwd,files) for (cwd, dirs, files) in os.walk('/Users/vladimirsivanovs/IdeaProjects/linux-command-lines/scripts/renamer')]

for (cwd, f_list) in all_files:
    for f in f_list:
        file = cwd+f
        if file.endswith('.txt'):
            print(file)
