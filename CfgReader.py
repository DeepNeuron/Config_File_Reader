#!/usr/bin/env python
#*PLEASE NOTE * In order for the program to work, you must make sure the config file begins immediately in the following format:
#Key:Value. Starting from the very top line of the file and going down. 
#If you have other config files you would like to include, please write: incldue:additional_config_file_name
import sys
from collections import OrderedDict
script_name = sys.argv[0][:-3]
if len(sys.argv) <= 1:
    cfg_file_name = script_name + '.cfg'
else:
    cfg_file_name = sys.argv[1] 

def getConfig(directory_path):
    config_path = directory_path
    vector_cfg_file_names = [] 
    dic = dict()
    #vector_cfg_file_names, dic = loadcfg(directory_path, cfg_file_name ,vector_cfg_file_names, dic)
    loadcfg(directory_path, cfg_file_name ,vector_cfg_file_names, dic)
    return dic

        
def loadcfg(config_path, file_name,vector_cfg_file_names,dic):
    vector_cfg_file_names.append(file_name)
    abs_file_name = file_name
    current_file = open(abs_file_name) #Open the config file to be looked through 
    for line in current_file:
         lineSplit = line.split(':', 1)
        key = lineSplit[0]
        try:
            NEW_value = lineSplit[1].strip()
        except IndexError:
            continue    
        
        name = NEW_value
        if key == "include":  #This means there are other cfg files to be included
            found = 0 
            for old_file in vector_cfg_file_names:
                print "vector_cfg_file_name=", old_file
                if name == old_file: #Check if the included file is already in the list of config files to parse 
                    found = 1
                    break
                    
            if found == 1:
                print "file already included"
                print dic.items()
                continue
            else:
                print "Recursive call  ......"
                loadcfg(config_path, NEW_value ,vector_cfg_file_names ,dic) #Recursively look through each config file included otherwise
        else:
            if key in dic.keys():
                print "WARNING: already exists in dictionary <key,Old_value> and is now replaced by <key, NEW_value>"
                dic[key] = NEW_value
            else:
                 dic[key] = NEW_value
                    
                         
    return vector_cfg_file_names,dic
