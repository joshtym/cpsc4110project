#!/bin/python

import sys
from random import randint
import glpk

def getInputValues():
    with open(sys.argv[1]) as file:
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

def fillLinearProgramCredentials():
    # Create our Linear Program. Vertex Cover is a minimizing problem
    lp = glpk.LPX()
    lp.name = "Unweighted Vertex Cover Problem"
    lp.obj.maximize = False
    lp.rows.add(len(edgeEndpoints1))

    # Set the bounded constraints
    for r in lp.rows:
       lp.rows[r.index].bounds = 1.0, None

    # Add in our vertices and create the lower bound for the relaxation
    lp.cols.add(len(vertices))
    for c in lp.cols:
        c.name = 'x%d' % (c.index + 1)
        c.bounds = 0.0, None

    # Create our objective function 
    temp = []
    for vertex in vertices:
        temp.append(1.0)
    lp.obj[:] = temp

    # Reset temp and fill in our constraint matrix
    temp = []
    i = 0
    while i != len(vertices) * len(edgeEndpoints1):
        temp.append(0)
        i += 1
    i = 0
    while i != len(edgeEndpoints1):
        temp[(len(vertices) * i) + (int(edgeEndpoints1[i]) - 1)] = 1
        temp[(len(vertices) * i) + (int(edgeEndpoints2[i]) - 1)] = 1
        i += 1

    # Set our constraint matrix
    lp.matrix = temp

    # Solve using the simplex method
    lp.simplex()

    # Print out our results
    print('Optimal Number of Vertices from Linear Program = ' + str(int(lp.obj.value)))
    print("Linear Program Vertices Chosen are:"),
    for c in lp.cols:
        if c.primal == 1:
            print(c.name + ','),
    print('')

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

# Ensure we have enough arguments
if len(sys.argv) < 2:
    print("Not enough arguments. Command is python vertexCover.py yourGraph.txt")
    sys.exit()

if len(sys.argv) > 2:
    print("Too many arguments. Command is python vertexCover.py yourGraph.txt")
    sys.exit()

# Variable declarations
vertices = []
edgeEndpoints1 = []
edgeEndpoints2 = []
verticesChosen = []

# Get our input values
getInputValues()
fillLinearProgramCredentials()
findVertexCover()

# Print our chosen vertices
print("Vertices chosen by Greedy are: " + ', '.join(verticesChosen))