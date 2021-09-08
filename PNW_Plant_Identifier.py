#!/usr/bin/env python3


# This program is a dichotomous key for identifying 27 of the most common plants of the Pacific Northwest. 
# A plant is identified via a series of binary choices that force the user down a decision tree until the
# final leaf node is hit, producing a plant name and terminating the program. 


# class Node constructs the nodes of the tree

class Node:
    def __init__(self, left_attribute, right_attribute, left_index, right_index, is_leaf=False, name=None):
        self.left_attribute = left_attribute
        self.right_attribute = right_attribute
        self.left_index = left_index
        self.right_index = right_index
        self.is_leaf = is_leaf
        self.name = name


# def prompt processes user input and moves the user down the tree accordingly, repeating the prompt
# until the user answers in the correct format. If a leaf node is hit, the program returns the plant
# name and terminates.
        
    def prompt(self):
        if (self.left_index == None and self.right_index == None and self.is_leaf):
            print(f"You identified a {self.name}!")
            return self.name
        while self.is_leaf == False:
            ans = input(f"{self.left_attribute} (L) or {self.right_attribute} (R) ?")
            if ans == 'L':
                return self.left_index.prompt()
            elif ans == 'R':
                return self.right_index.prompt()
            else:
                print("Please type either L or R")


# These are the instantiated nodes that make up the tree, from bottom to top.


q52 = Node(None, None, None, None, True, 'Snowberry')
q51 = Node(None, None, None, None, True, 'Hardhack')
q50 = Node(None, None, None, None, True, 'Red Huckleberry')
q49 = Node(None, None, None, None, True, 'Scotch Broom')
q48 = Node('Are the leaves serrated', 'not serrated leaves', q51, q52)
q47 = Node('Are the leaves clustered', 'not clustered', q49, q50)
q46 = Node(None, None, None, None, True, 'Salal')
q45 = Node('Green stems', 'brown stems', q47, q48)
q44 = Node(None, None, None, None, True, 'Stinging Nettle')
q43 = Node(None, None, None, None, True, 'Himalayan Blackberry')
q42 = Node('Are the leaves not waxy', 'waxy', q45, q46)
q41 = Node(None, None, None, None, True, 'Salmonberry')
q40 = Node('Are there thorns', 'no thorns', q43, q44)
q39 = Node(None, None, None, None, True, 'Thimbleberry')
q38 = Node(None, None, None, None, True, 'Trailing Blackberry')
q37 = Node(None, None, None, None, True, 'English Ivy')
q36 = Node('Are there thorns', 'no thorns', q41, q42)
q35 = Node('Are the leaves fuzzy on both sides', 'fuzzy on one side', q39, q40)
q34 = Node(None, None, None, None, True, 'Trillium')
q33 = Node('Does the plant have a waxy stem', 'prickly stem', q37, q38)
q32 = Node(None, None, None, None, True, 'Poison Hemlock')
q31 = Node(None, None, None, None, True, 'Stinky Bob (Herb Robert)')
q30 = Node('Hairy', 'hairless', q35, q36)
q29 = Node('Leaves not clustered', 'clustered', q33, q34)
q28 = Node(None, None, None, None, True, 'Deer Fern')
q27 = Node(None, None, None, None, True, 'Sword Fern')
q26 = Node(None, None, None, None, True, 'Red Alder')
q25 = Node(None, None, None, None, True, 'Big Leaf Maple')
q24 = Node('Hairy', 'hairless', q31, q32)
q23 = Node('Trailing along the ground', 'upright growth', q29, q30)
q22 = Node(None, None, None, None, True, 'Bracken Fern')
q21 = Node('Does the plant have an open drooping center', 'upright center', q27, q28)
q20 = Node(None, None, None, None, True, 'Douglas Fir')
q19 = Node(None, None, None, None, True, 'Horsetail')
q18 = Node('Is it a lobed, finger-like leaf shape', 'oval leaf shape', q25, q26)
q17 = Node(None, None, None, None, True, 'Red Elderberry')
q16 = Node('Is the plant not smelly', 'smelly', q23, q24)
q15 = Node(None, None, None, None, True, 'Skunk Cabbage')
q14 = Node(None, None, None, None, True, 'Oregon Grape')
q13 = Node('Is every leaf about the same size', 'triangular, getting wider at the bottom', q21, q22)
q12 = Node(None, None, None, None, True, 'Western Hemlock')
q11 = Node('Is the plant less than 10 feet tall', 'more than ten feet tall', q19, q20)
q10 = Node('Does the plant have a compound leaf structure made of many tiny leaves', 'a single leaf structure', q17, q18)
q09 = Node(None, None, None, None, True, 'Madrone')
q08 = Node('>1 ft.', '<1 ft.', q15, q16)
q07 = Node('Are the leaves smooth and without teeth', 'sharp with teeth', q13, q14)
q06 = Node(None, None, None, None, True, 'Western Red Cedar')
q05 = Node('Is there an orderly spiral needle pattern', 'chaotic spindly needle pattern', q11, q12)
q04 = Node('Is the bark multicolored green and reddish brown', 'not multicolored', q09, q10)
q03 = Node('Does the plant have a compound leaf structure made of many tiny leaves', 'a single leaf structure', q07, q08)
q02 = Node('Do the needles attach to the branch as single needles', 'branchlets made of many tiny needles', q05, q06)
q01 = Node('Is the plant less than 10 feet tall', 'more than 10 feet tall', q03, q04)
q00 = Node('Does the plant have broad and flat leaves', 'needle-like leaves', q01, q02)


# A prompt at the top of the tree begins the exercise:

q00.prompt()
