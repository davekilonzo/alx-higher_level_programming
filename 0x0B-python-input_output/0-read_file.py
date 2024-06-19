#!/bin/python3

def read_file(filename=""):
    try:
        with open(filename, "r", encoding="UTF-8") as f:
            content = f.read()
            if content:
                print(content, end="")
            else:
                print("File is empty.")
    except FileNotFoundError:
        print("File not found.")

