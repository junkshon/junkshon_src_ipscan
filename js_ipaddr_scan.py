'''
    junkshon IP address scan of source code files. 
'''
import os
import re
import json

'''
    read config file
'''
def read_config():

    config_file = "junkshon_ipscan.json"
    try:
        with open (config_file) as json_file:
            json_config = json.load(json_file)
            return json_config
    except:
        print ('Error reading configuration file')
        
'''
    get a list of directories 
'''
def getListOfFiles(dirName):

    listOfFile = os.listdir(dirName)
    allFiles = list()

    for entry in listOfFile:

        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles     

'''
    parse source files
'''
def parse_file(file):

    file_ext_list = ['dyalog', 'apl', 'pgp', 'asn', 'asn1', 'b', 'bf', 'c', 'h', 'cpp', 'c++', 'cc', 'cxx', 'hpp', 'h++', 'hh', 'hxx', 
                     'cob', 'cpy', 'cs', 'clj', 'cljc', 'cljx', 'cljs', 'gss', 'cmake', 'cmake.in', 'coffee', 'cl', 'lisp', 'el', 'cyp', 'cypher', 
                     'pyx', 'pxd', 'pxi', 'cr', 'css', 'cql', 'd', 'dart', 'diff', 'patch', 'dtd', 'dylan', 'dyl', 'intr', 
                      'ecl', 'edn', 'e', 'elm', 'ejs', 'erb', 'erl', 'factor', 'forth', 'fth', '4th', 'f', 'for', 'f77', 
                     'f90', 'fs', 's', 'feature', 'go', 'groovy', 'gradle', 'haml', 'hs', 'lhs', 'hx', 'hxml', 'aspx', 'html', 'htm', 
                     'pro', 'jade', 'pug', 'java', 'jsp', 'js', 'json', 'map', 'jsonld', 'jsx', 'jl', 'kt', 'less', 'ls', 
                     'lua', 'markdown', 'md', 'mkd', 'm', 'nb', 'mo', 'mps',  'mbox', 
                     'nsh', 'nsi', 'nt', 'm', 'mm', 'ml', 'mli', 'mll', 'mly', 'm', 'oz', 'p', 'pas', 'jsonld', 'pl', 'pm', 'php', 'php3', 'php4', 'php5', 
                     'phtml', 'pig', 'txt', 'text', 'conf', 'def', 'list', 'log', 'pls', 'ps1', 'psd1', 'psm1', 'properties', 'ini', 'in', 'proto', 'BUILD', 
                     'bzl', 'py', 'pyw', 'pp', 'q', 'r', 'R', 'rst',  'spec', 'rb', 'rs', 'sas', 'sass', 'scala', 'scm', 'ss', 'scss', 'sh', 'ksh', 
                     'bash', 'siv', 'sieve', 'slim', 'st', 'tpl', 'soy', 'rq', 'sparql',  'sql',  'nut', 'styl', 'swift',  
                     'text', 'ltx', 'v', 'tcl', 'textile', 'toml', 'ttcn', 'ttcn3', 'ttcnpp', 'cfg', 'ttl', 'ts', 'tsx',
                     'webidl', 'vb', 'vbs', 'vtl', 'v', 'vhd', 'vhdl', 'vue', 'xml', 'xsl', 'xsd', 'xy', 'xquery', 'ys', 'yaml', 'yml', 'z80', 'mscgen', 'mscin', 
                     'msc', 'xu', 'msgenny']

    try:
        for file_ext in file_ext_list:
            if file.endswith("."+file_ext):
                f = open(file, 'r') 
                o = f.read()             
                ipaddr = re.findall( r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", o )    
                return ipaddr
    except:
            return 'Binary File'

'''
    main rountine
'''
def main():

    json_config = read_config()
    ip_scan_output = json_config['scan_output_file']
    srcDirName = json_config['source_directory']

    file_bin = 'Binary File'
    scan_result = []
    
    try:
        listOfFiles = getListOfFiles(srcDirName)
    except:
        print ('Error listing targeting directory')
        
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(srcDirName):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]

    try:       
        print ('Scanning source directory:' + srcDirName)
        for elem in listOfFiles:
            parse_ip_addr = parse_file(elem)
            if parse_ip_addr == file_bin:
                continue                    
            if not parse_ip_addr:
                continue
            else:
                payload = {
                    "filepath": elem, 
                    "result": parse_ip_addr
                }
            scan_result.append(payload)        
    except:
        print ('Error parsing source file')

    try:
        with open(ip_scan_output, 'w') as outfile:
            json.dump(scan_result, outfile)
    except:
        print ('Error creating IP scan output file')

if __name__ == '__main__':
    try:
        main()
    except:
       print ('Error starting junkshon IP scan')