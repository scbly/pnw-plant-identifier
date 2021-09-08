# This is my attempt at Flask.

from flask import Flask, render_template, request

# Creating the app!

app = Flask(__name__)

node_config = {

    # q00 = Node('Does the plant have broad and flat leaves', 'needle-like leaves', q01, q02)
    0: {
        'left_attribute': 'Does the plant have broad and flat leaves',
        'right_attribute': 'needle-like leaves?',
        'left_index': 1,
        'right_index': 2,
        'is_leaf': False,
        'name': None
    },

    # q01 = Node('Is the plant less than 10 feet tall', 'more than ten feet tall', q03, q04)
    1: {
        'left_attribute': 'Is the plant less than 10 feet tall',
        'right_attribute': 'more than 10 feet tall?',
        'left_index': 3,
        'right_index': 4,
        'is_leaf': False,
        'name': None
    },

    # etc etc etc...
    2: {
        'left_attribute': 'Do the needles attach to the branch as single needles',
        'right_attribute': 'branchlets made of many tiny needles?',
        'left_index': 5,
        'right_index': 6,
        'is_leaf': False,
        'name': None
    },

    3: {
        'left_attribute': 'Does the plant have a compound leaf structure made of many tiny leaves',
        'right_attribute': 'a single leaf structure?',
        'left_index': 7,
        'right_index': 8,
        'is_leaf': False,
        'name': None
    },

    4: {
        'left_attribute': 'Is the bark multicolored green and reddish brown',
        'right_attribute': 'not multicolored?',
        'left_index': 9,
        'right_index': 10,
        'is_leaf': False,
        'name': None
    },

    5: {
        'left_attribute': 'Is there an orderly spiral needle pattern',
        'right_attribute': 'chaotic spindly needle pattern?',
        'left_index': 11,
        'right_index': 12,
        'is_leaf': False,
        'name': None
    },

    6: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'is_leaf': True,
        'name': 'Western Red Cedar'
    },

    7: {
        'left_attribute': 'Are the leaves smooth and without teeth',
        'right_attribute': 'sharp with teeth?',
        'left_index': 13,
        'right_index': 14,
        'is_leaf': False,
        'name': None
    },

    8: {
        'left_attribute': 'Is the leaf size greater than one foot',
        'right_attribute': 'less than one foot?',
        'left_index': 15,
        'right_index': 16,
        'is_leaf': False,
        'name': None
    },

    9: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'is_leaf': True,
        'name': 'Madrone'
    },

    10: {
        'left_attribute': 'Does the plant have a compound leaf structure made of many tiny leaves',
        'right_attribute': 'a single leaf structure?',
        'left_index': 17,
        'right_index': 18,
        'is_leaf': False,
        'name': None
    },

    11: {
        'left_attribute': 'Is the plant less than 10 feet tall',
        'right_attribute': 'more than ten feet tall?',
        'left_index': 19,
        'right_index': 20,
        'is_leaf': False,
        'name': None
    },

    12: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'is_leaf': True,
        'name': 'Western Hemlock'
    },

    13: {
        'left_attribute': 'Is every leaf about the same size',
        'right_attribute': 'triangular, getting wider at the bottom?',
        'left_index': 21,
        'right_index': 22,
        'is_leaf': False,
        'name': None
    },

    14: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'is_leaf': True,
        'name': 'Oregon Grape'
    },

    15: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'is_leaf': True,
        'name': 'Skunk Cabbage'
    },

    16: {
        'left_attribute': 'Is the plant not smelly',
        'right_attribute': 'smelly?',
        'left_index': 23,
        'right_index': 24,
        'is_leaf': False,
        'name': None
    },

    17: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'is_leaf': True,
        'name': 'Red Elderberry'
    },

    18: {
        'left_attribute': 'Is it a lobed, finger-like leaf shape',
        'right_attribute': 'oval leaf shape?',
        'left_index': 25,
        'right_index': 26,
        'is_leaf': False,
        'name': None
    },

    19: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'is_leaf': True,
        'name': 'Horsetail'
    },

    20: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'is_leaf': True,
        'name': 'Douglas Fir'
    },

    21: {
        'left_attribute': 'Does the plant have an open drooping center',
        'right_attribute': 'upright center?',
        'left_index': 27,
        'right_index': 28,
        'is_leaf': False,
        'name': None
    },

    22: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'is_leaf': True,
        'name': 'Bracken Fern'
    },

    23: {
        'left_attribute': 'Does the plant trail along the ground',
        'right_attribute': 'does it show upright growth of more than a foot?',
        'left_index': 29,
        'right_index': 30,
        'is_leaf': False,
        'name': None
    },

    24: {
        'left_attribute': 'Is the plant hairy',
        'right_attribute': 'hairless?',
        'left_index': 31,
        'right_index': 32,
        'is_leaf': False,
        'name': None
    },

    25: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'is_leaf': True,
        'name': 'Big Leaf Maple'
    },

    26: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'is_leaf': True,
        'name': 'Red Alder'
    },

    27: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'is_leaf': True,
        'name': 'Sword Fern'
    },

    28: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'is_leaf': True,
        'name': 'Deer Fern'
    },

    29: {
        'left_attribute': 'Are the leaves not clustered (attached singly to the stem)',
        'right_attribute': 'clustered?',
        'left_index': 33,
        'right_index': 34,
        'is_leaf': False,
        'name': None
    },

    30: {
        'left_attribute': 'Is the plant hairy',
        'right_attribute': 'hairless?',
        'left_index': 35,
        'right_index': 36,
        'is_leaf': False,
        'name': None
    },

    31: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'is_leaf': True,
        'name': 'Stinky Bob (Herb Robert)'
    },

    32: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'is_leaf': True,
        'name': 'Poison Hemlock'
    },

    33: {
        'left_attribute': 'Does the plant have a waxy stem',
        'right_attribute': 'prickly stem?',
        'left_index': 37,
        'right_index': 38,
        'is_leaf': False,
        'name': None
    },

    34: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'is_leaf': True,
        'name': 'Trillium'
    },

    35: {
        'left_attribute': 'Are the leaves fuzzy on both sides',
        'right_attribute': 'fuzzy on one side?',
        'left_index': 39,
        'right_index': 40,
        'is_leaf': False,
        'name': None
    },

    36: {
        'left_attribute': 'Are there thorns',
        'right_attribute': 'no thorns?',
        'left_index': 41,
        'right_index': 42,
        'is_leaf': False,
        'name': None
    },

    37: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'is_leaf': True,
        'name': 'English Ivy'
    },

    38: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'is_leaf': True,
        'name': 'Trailing Blackberry'
    },

    39: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'is_leaf': True,
        'name': 'Thimbleberry'
    },

    40: {
        'left_attribute': 'Are there thorns',
        'right_attribute': 'no thorns?',
        'left_index': 43,
        'right_index': 44,
        'is_leaf': False,
        'name': None
    },

    41: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'is_leaf': True,
        'name': 'Salmonberry'
    },

    42: {
        'left_attribute': 'Are the leaves not waxy',
        'right_attribute': 'waxy?',
        'left_index': 45,
        'right_index': 46,
        'is_leaf': False,
        'name': None
    },

    43: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'is_leaf': True,
        'name': 'Himalayan Blackberry'
    },

    44: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'is_leaf': True,
        'name': 'Stinging Nettle'
    },

    45: {
        'left_attribute': 'Does the plant have green stems',
        'right_attribute': 'brown stems?',
        'left_index': 47,
        'right_index': 48,
        'is_leaf': False,
        'name': None
    },

    46: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'is_leaf': True,
        'name': 'Salal'
    },

    47: {
        'left_attribute': 'Are the leaves clustered',
        'right_attribute': 'not clustered?',
        'left_index': 49,
        'right_index': 50,
        'is_leaf': False,
        'name': None
    },

    48: {
        'left_attribute': 'Are the leaves serrated',
        'right_attribute': 'not serrated?',
        'left_index': 51,
        'right_index': 52,
        'is_leaf': False,
        'name': None
    },

    49: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'is_leaf': True,
        'name': 'Scotch Broom'
    },

    50: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'is_leaf': True,
        'name': 'Red Huckleberry'
    },

    51: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'is_leaf': True,
        'name': 'Hardhack'
    },

    52: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'is_leaf': True,
        'name': 'Snowberry'
    },
}




class Node:
    def __init__(self, left_attribute, right_attribute, left_index, right_index, is_leaf=False, name=None):
        self.left_attribute = left_attribute
        self.right_attribute = right_attribute
        self.left_index = left_index
        self.right_index = right_index
        self.is_leaf = is_leaf
        self.name = name


@app.route('/')
def index():

    node_id = int(request.args.get('node_id', 0))
    config = node_config[node_id]

    node = Node(config['left_attribute'], config['right_attribute'], config['left_index'], config['right_index'], config['is_leaf'], config['name'])

    return render_template('PNW_Plant_Flask.html', node=node)
# Protecting against any other files being run (I only want this one):

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)