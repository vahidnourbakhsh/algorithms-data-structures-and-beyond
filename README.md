# Algorithms, Data Structures and Best Programming Practices

Maybe technical interviews should go beyond just algorithms and data structures and test good programming practices like designing a class with proper methods. This repo is a collection of problems that I try not only to solve but go beyond that. Some time good patterns means object-oriented programming.

# Problems

## Randomly select an array's element

### problem description

Write an algorithm that select an element of an array with probability proportional to the elements value with respect to the sum of all elements in the array. For example, in the array `[1,2,3,4]`, element 1 should be chosen with a probability of `1/(1+2+3+4)`, element 2 with a probability of `2/(1+2+3+4)`, etc. For a full discussion on this problem and the following solutions, you can read the [Medium Article](https://vahidn.medium.com/evolving-from-an-interview-answer-code-toward-a-production-code-8c393ccee3ea)

### solutions

We show three stpes.

- step 1: an algorithm that simply solves the problem. This is what you would expect in a technical interview.
- step 2: a class with proper structure. In this step we define a class with methods we should use to solve the problem.
- step 3: a unit test. In this step we add a unit test to test what we built in step 2.
