'''
Assignment 2 - Hash Tables in Python

Overview:
    This file covers Assignment 2 of the Python DSA course by Jovian.ai. To maintain academic integrety, the entire assignment 
    notebook will not be posted here. Instead, only code relevant to the concept of hash tables will be written below. 

Problem Statement:
    - Recreate Python dictionaries from scratch using Hash Tables. Python dictionaries are used to store key-value pairs, where
    key are used to store and retrieve values.
    - The HashTable class should support the following intructions:
        1. Insert (insert new key-value pair)
        2. Find (find value corresponding to a given key)
        3. Update (update the value associated with a given key)
        4. List (list all the keys stored in the hash table)

    Example of a Python dictionary for storing and retrieving phone numbers using names:
        phone_numbers = {'Aakash':'9489484949', 'Hemanth:'9595949494', 'Siddhant':'9231325312'}
        phone_numbers['Aakash']     # returns '9489484949'
        phone_numbers['Aakash'] = '7878787878'      # updates value corresponding to key 'Aakash'
        phone_numbers['Vishal'] = '8787878787'      # adds a new key-value pair into the dictionary

Hash Tables:
    - Uses lists or arrays to store key-value pairs, and uses a "hashing function" to determine the index for storing and retrieving
    data associated to a given key.

Hashing Function:
    - Converts strings and other non-numeric data into numbers that are, hence, used are list indices.
    - Example hashing function (implemented in this project):
        1. Iterate over the string per character
        2. Covert each character to a number using Python's built-in ord function (returns the unicode representation of the character)
        3. Sum the resulting numbers to obtain the hash for the string
        4. Return the remainder of the above sum with the size of the data_list 

'''

MAX_HASH_TABLE_SIZE = 4096      # maximum size of the hash table
# data_list = [None]*MAX_HASH_TABLE_SIZE      # list containing None value of maximum size

def get_index(data_list, string):
    result = 0  # initializing a variable to store the sum
    
    for char in string:
        result += ord(char)     # looping through the string to convert each character to an integer and perform summation
    
    list_index = result % len(data_list)        # obtaining an index position as the remainder of the result and data length
    return list_index




class HashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        self.data_list = [None] * max_size

    def insert(self, key, value):
        idx = get_index(self.data_list, key)
        self.data_list[idx] = (key, value)

    def find(self, key):
        idx = get_index(self.data_list, key)
        kv = self.data_list[idx]        # returns the key-value pair
        
        if kv == None:
            return None
        else:
            key, value = kv
            return value

    def update(self, key, value):
        idx = get_index(self.data_list, key)
        self.data_list[idx] = (key, value)      # storing a tuple since data_list stores a key-value pair

    def list_all(self):
        return [kv[0] for kv in self.data_list if kv is not None]