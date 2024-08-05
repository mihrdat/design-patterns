# Design Patterns - Gang of Four Implementation

Welcome to the Design Patterns repository! This repository contains implementations of the 23 design patterns defined in the classic book *"Design Patterns: Elements of Reusable Object-Oriented Software"* by the Gang of Four (Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides).

## Table of Contents

- [Introduction](#introduction)
- [Design Patterns Overview](#design-patterns-overview)
- [Patterns by Category](#patterns-by-category)
- [Usage](#usage)

## Introduction

Design patterns provide solutions to common problems in software design. By using well-established patterns, developers can create more flexible, reusable, and maintainable code. This repository showcases implementations of all 23 design patterns categorized into Creational, Structural, and Behavioral patterns.

## Design Patterns Overview

The patterns are grouped into three categories:

1. **Creational Patterns**: These patterns deal with object creation mechanisms.
2. **Structural Patterns**: These patterns focus on the composition of classes and objects.
3. **Behavioral Patterns**: These patterns focus on the interaction and responsibility between objects.

## Patterns by Category

### Creational Patterns
- **Abstract Factory**: Creates an instance of several families of classes.
- **Builder**: Separates object construction from its representation.
- **Factory Method**: Creates an instance of several derived classes.
- **Prototype**: Creates a new object by copying an existing object.
- **Singleton**: Ensures a class has only one instance and provides a global point of access to it.

### Structural Patterns
- **Adapter**: Allows incompatible interfaces to work together.
- **Bridge**: Separates an object’s interface from its implementation.
- **Composite**: Composes objects into tree structures to represent part-whole hierarchies.
- **Decorator**: Adds additional responsibilities to an object dynamically.
- **Facade**: Provides a simplified interface to a complex subsystem.
- **Flyweight**: Reduces the cost of creating and manipulating a large number of similar objects.
- **Proxy**: Provides a surrogate or placeholder for another object.

### Behavioral Patterns
- **Chain of Responsibility**: Passes a request along a chain of handlers.
- **Command**: Encapsulates a request as an object.
- **Interpreter**: Implements a specialized language.
- **Iterator**: Provides a way to access elements of a collection sequentially.
- **Mediator**: Defines simplified communication between classes.
- **Memento**: Captures and restores an object’s internal state.
- **Observer**: Allows an object to notify other objects when its state changes.
- **State**: Allows an object to alter its behavior when its internal state changes.
- **Strategy**: Encapsulates an algorithm inside a class.
- **Template Method**: Defines the skeleton of an algorithm, letting subclasses fill in the details.
- **Visitor**: Represents an operation to be performed on elements of an object structure.

## Usage

Each pattern is implemented in Python and organized into its own directory. To explore a specific pattern:

1. Clone this repository to your local machine:
   ```bash
   git clone git@github.com:mihrdat/design-patterns.git
