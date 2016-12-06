#!/bin/python

from random import randint

def getInputValues():
    with open('graph2.txt') as file:
        while True:
            # Read the current character
            curChar = file.read(1)
            temp = ""

            # If we've reached the end of file, beam us up Scotty!
            if not curChar:
                print("File read completed")
                break

            # We only care about characters that are not spaces and newlines loop through and get the first vertex
            while curChar != ' ' and curChar != '\n':
                temp = temp + curChar
                curChar = file.read(1)

            # Add vertex to our vertices if not already in it
            if temp not in vertices:
                vertices.append(temp)

            # Append this endpoint
            edgeEndpoints1.append(temp)

            # Read ahead to the next character and reset our temp variable
            curChar = file.read(1)
            temp = ""

            # Similary, get the second vertex of our edge
            while curChar != ' ' and curChar != '\n' and curChar:
                temp = temp + curChar
                curChar = file.read(1)

            # Add vertex to vertices if not already in it
            if temp not in vertices:
                vertices.append(temp)

            # Append the endpoint
            edgeEndpoints2.append(temp)

def findVertexCover():
    while True:
        # If we've emptied our set of endpoints, end our loop
        if not edgeEndpoints1 or not edgeEndpoints2:
            break

        # Get our length of edges to properly get a random index
        endpointLength = len(edgeEndpoints1)

        # Pick an edge arbitrarily (randomly)
        randomEdgeIndex = randint(0,endpointLength - 1)

        # Store the endpoints as variables
        edgeVertex1 = edgeEndpoints1[randomEdgeIndex]
        edgeVertex2 = edgeEndpoints2[randomEdgeIndex]

        # Add in our endpoints to our chosen set
        verticesChosen.append(edgeVertex1)
        verticesChosen.append(edgeVertex2)

        # Find all edges from our endpoints and remove them from the set.
        while True:
            try:
                vertexIndex = edgeEndpoints1.index(edgeVertex1)
                del edgeEndpoints1[vertexIndex]
                del edgeEndpoints2[vertexIndex]
            except Exception, e:
                break

        while True:
            try:
                vertexIndex = edgeEndpoints1.index(edgeVertex2)
                del edgeEndpoints1[vertexIndex]
                del edgeEndpoints2[vertexIndex]
            except Exception, e:
                break

        while True:
            try:
                vertexIndex = edgeEndpoints2.index(edgeVertex1)
                del edgeEndpoints1[vertexIndex]
                del edgeEndpoints2[vertexIndex]
            except Exception, e:
                break

        while True:
            try:
                vertexIndex = edgeEndpoints2.index(edgeVertex2)
                del edgeEndpoints1[vertexIndex]
                del edgeEndpoints2[vertexIndex]
            except Exception, e:
                break

# Variable declarations
vertices = []
edgeEndpoints1 = []
edgeEndpoints2 = []
verticesChosen = []

# Get our input values
getInputValues()
findVertexCover()

# Print our chosen vertices
print("Vertices chosen are: " + ', '.join(verticesChosen))
    