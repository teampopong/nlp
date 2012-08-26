#! /usr/bin/python3
# -*- coding: utf-8 -*-

import os, json
from glob import glob
from pprint import pprint

def importer(directory, opt, fieldname):          
 
    def printer():
        print('\n===' + fieldname.upper() + '===')
        print_filenames(opt)
        print('n(files)\t: '+ str(len(filenames)))
        print('n(items)\t: '+ str(len(fieldlist)))

    def print_filenames(opt):
        if opt != 'all':
            print('Files:')
            pprint(filenames)
        else:
            pass

    filenames = get_filenames(directory, opt)
    fieldlist = get_rawlist(filenames, fieldname)
    printer()
    return fieldlist

def get_filenames(directory, opt):
    allfilenames = all_filenames(directory)
    filenames = select_filenames(allfilenames, opt)
    return filenames

def all_filenames(directory):
    return glob(os.path.join(directory, '*'))

def select_filenames(filenames, opt):
    if isinstance(opt, int):
        filenames = [filenames[opt]]
    elif isinstance(opt, str):
        if opt == 'all':
            pass
        elif opt == 'test':
            filenames = [filenames[0], filenames[39], filenames[50]]
        else:
            raise "Error: String options should be in {'all', 'test'}"
    else:
        raise "Error: Options should either be\
                an integer in [1,82] or string in {'all', 'test'}"
    return filenames

def get_rawlist(filenames, fieldname):
    rawlist = [p[fieldname] for f in filenames for p in read_people(f)]
    return rawlist

def read_people(filename):
    with open(filename, 'r') as f:
        j = f.read()
        people = json.loads(j)
    return people
