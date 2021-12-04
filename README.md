# Algorithms, Data Structures and Best Programming Practices

Maybe technical interviews should go beyond just algorithms and data structures and test good programming practices like designing a class with proper methods. This repo is a collection of problems that I try not only to solve but go beyond that. Some time good patterns means object-oriented programming.

# Problems

## Randomly select an array's element

### problem description

Write an algorithm that select an element of an array with probability proportional to the elements value with respect to the sum of all elements in the array. For example, in the array `[1,2,3,4]`, element 1 should be chosen with a probability of `1/(1+2+3+4)`, element 2 with a probability of `2/(1+2+3+4)`, etc.

### solution

From the algorithm to a OOP design in three steps:

- random1: an algorithm
- random2: a class with proper structure
- random3: an optimized class