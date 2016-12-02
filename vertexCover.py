#!/bin/python

def getInputValues():
    with open('graph.txt') as file:
        while True:
            # Read the current character
            curChar = file.read(1)

            # If we've reached the end of file, beam us up Scotty!
            if not curChar:
                print("File read completed")
                break

            # We only care about characters that are not spaces and newlines
            if curChar != ' ' and curChar != '\n':
                # The set of vertices should be unique and not a space or newline
                if curChar not in vertices and curChar != ' ' and curChar != '\n':
                    vertices.append(curChar)

                # Append our first character as the first endpoint
                edgeEndpoints1.append(curChar)

                # Read two more characters to get to the next endpoint
                curChar = file.read(1)
                curChar = file.read(1)

                # Check to see if this endpoint is in our set of verticies
                if curChar not in vertices and curChar != ' ' and curChar != '\n':
                    vertices.append(curChar)

                # Append the second character of the line to the second endpoint
                edgeEndpoints2.append(curChar)

# Variable declarations
vertices = []
edgeEndpoints1 = []
edgeEndpoints2 = []
verticesChosen = []

# Get our input values
getInputValues()