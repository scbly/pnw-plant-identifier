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
        'left_img': 'https://jakesnatureblog.com/wp-content/uploads/2017/02/aspen-leaf.jpg',
        'right_img': 'https://www.healthbenefitstimes.com/9/uploads/2016/04/Horsetail-Tea.png', 
        'name': None
    },

    # q01 = Node('Is the plant less than 10 feet tall', 'more than ten feet tall', q03, q04)
    1: {
        'left_attribute': 'Is the plant less than 10 feet tall',
        'right_attribute': 'more than 10 feet tall?',
        'left_index': 3,
        'right_index': 4,
        'left_img': 'https://www.cypresscreeklandscapesupply.com/blog/wp-content/uploads/2019/11/shrubs.jpg',
        'right_img': 'https://www.greenlawnfertilizing.com/wp-content/uploads/2017/01/oak-tree.jpg.webp',
        'name': None
    },

    2: {
        'left_attribute': 'Do the needles attach to the branch as single needles',
        'right_attribute': 'branchlets made of many tiny needles?',
        'left_index': 5,
        'right_index': 6,
        'left_img': 'https://www.naturallywood.com/wp-content/uploads/Douglas-Fir_KCharleton_042_10474-1200x800-5b2df79-e1600100637617.jpg',
        'right_img': 'https://cdn.shopify.com/s/files/1/0089/3075/4665/products/cedar_leaf_Thuja_occidentalis_1200x.jpg?v=1569171691',
        'name': None
    },

    3: {
        'left_attribute': 'Does the plant have a compound leaf structure made of many tiny leaves',
        'right_attribute': 'a single leaf structure?',
        'left_index': 7,
        'right_index': 8,
        'left_img': 'https://pbs.twimg.com/media/CFaLZs9WAAAtesF?format=jpg&name=small',
        'right_img': 'http://dendro.cnre.vt.edu/dendrology/images/Quercus%20velutina/leaf1.jpg',
        'name': None
    },

    4: {
        'left_attribute': 'Is the bark multicolored green and reddish brown',
        'right_attribute': 'not multicolored?',
        'left_index': 9,
        'right_index': 10,
        'left_img': 'https://i.etsystatic.com/14438497/r/il/e6a1fa/1270238314/il_fullxfull.1270238314_oh69.jpg',
        'right_img': 'https://i.pinimg.com/564x/9f/95/29/9f9529395b1306bd4843c8fa8e034208.jpg',
        'name': None
    },

    5: {
        'left_attribute': 'Is there an orderly spiral needle pattern',
        'right_attribute': 'chaotic spindly needle pattern?',
        'left_index': 11,
        'right_index': 12,
        'left_img': 'https://cdn.shopify.com/s/files/1/0510/9855/0461/products/hydrosol-doug-fir-botanical-second_1024x1024.jpg?v=1616627159',
        'right_img': 'https://storage.idigbio.org/portals/seinet/midwest/Pinaceae/201808/Tsuga_heterophylla_cone_er_1534286428.jpg',
        'name': None
    },

    6: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': '',
        'right_img': '',
        'name': 'Western Red Cedar'
    },

    7: {
        'left_attribute': 'Are the leaves smooth and without teeth',
        'right_attribute': 'sharp with teeth?',
        'left_index': 13,
        'right_index': 14,
        'left_img': 'https://www.thoughtco.com/thmb/sXrVxKbkw8SbiwaW0vh8Yz92_oM=/1250x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/152846652_10-56af62205f9b58b7d0182bcb.jpg',
        'right_img': 'https://images.squarespace-cdn.com/content/v1/5ab428368ab722cc4372413b/1585668188524-JOV6CYBWVAGAAHY2VBET/Mahonia+aquifolium+flower.jpg?format=1000w',
        'name': None
    },

    8: {
        'left_attribute': 'Is the leaf size greater than one foot',
        'right_attribute': 'less than one foot?',
        'left_index': 15,
        'right_index': 16,
        'left_img': 'https://www.choicesdomatter.org/wp-content/uploads/2015/06/skunk-cabbage-closeup.jpg',
        'right_img': 'https://cdn.pixabay.com/photo/2020/04/30/21/40/green-leaves-5114700_1280.jpg',
        'name': None
    },

    9: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': '',
        'right_img': '',
        'name': 'Madrone'
    },

    10: {
        'left_attribute': 'Does the plant have a compound leaf structure made of many tiny leaves',
        'right_attribute': 'a single leaf structure?',
        'left_index': 17,
        'right_index': 18,
        'left_img': 'https://pbs.twimg.com/media/CFaLZs9WAAAtesF?format=jpg&name=small',
        'right_img': 'http://dendro.cnre.vt.edu/dendrology/images/Quercus%20velutina/leaf1.jpg',
        'name': None
    },

    11: {
        'left_attribute': 'Is the plant less than 10 feet tall',
        'right_attribute': 'more than ten feet tall?',
        'left_index': 19,
        'right_index': 20,
        'left_img': 'https://www.cypresscreeklandscapesupply.com/blog/wp-content/uploads/2019/11/shrubs.jpg',
        'right_img': 'https://www.greenlawnfertilizing.com/wp-content/uploads/2017/01/oak-tree.jpg.webp',
        'name': None
    },

    12: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': '',
        'right_img': '',
        'name': 'Western Hemlock'
    },

    13: {
        'left_attribute': 'Is every leaf about the same size',
        'right_attribute': 'triangular, getting much wider at the bottom?',
        'left_index': 21,
        'right_index': 22,
        'left_img': 'https://upload.wikimedia.org/wikipedia/commons/8/8d/Polystichum_munitum_%28Jami_Dwyer%29_001.jpg',
        'right_img': 'https://cdn11.bigcommerce.com/s-gp99ab/images/stencil/500x659/products/4752/11292/apivwslpm__13856.1630323659__62663.1630981312.jpg?c=3',
        'name': None
    },

    14: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': '',
        'right_img': '',
        'name': 'Oregon Grape'
    },

    15: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': '',
        'right_img': '',
        'name': 'Skunk Cabbage'
    },

    16: {
        'left_attribute': 'Is the plant not smelly',
        'right_attribute': 'smelly?',
        'left_index': 23,
        'right_index': 24,
        'left_img': 'https://womenbelong.com/wp-content/uploads/2017/09/asian-girl-flower-smell-2-1.jpg',
        'right_img': 'https://www.sanluisobispo.com/news/local/education/eqmo7n/picture244132872/alternates/FREE_768/zCorpse%20flower056627',
        'name': None
    },

    17: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': '',
        'right_img': '',
        'name': 'Red Elderberry'
    },

    18: {
        'left_attribute': 'Is it a lobed, finger-like leaf shape',
        'right_attribute': 'oval leaf shape?',
        'left_index': 25,
        'right_index': 26,
        'left_img': 'https://i.redd.it/7r773173jk271.jpg',
        'right_img': 'https://upload.wikimedia.org/wikipedia/commons/3/33/Rosa_canina_blatt_2005.05.26_11.50.13.jpg',
        'name': None
    },

    19: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': '',
        'right_img': '',
        'name': 'Horsetail'
    },

    20: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': '',
        'right_img': '',
        'name': 'Douglas Fir'
    },

    21: {
        'left_attribute': 'Does the plant have an open drooping center',
        'right_attribute': 'upright center?',
        'left_index': 27,
        'right_index': 28,
        'left_img': 'https://i0.wp.com/www.coastwildlife.org/wp-content/uploads/2020/05/fern1.png?fit=480%2C358&ssl=1',
        'right_img': 'https://www.anniesannuals.com/signs/b%20-%20c/images//blechnum_spicant.jpg',
        'name': None
    },

    22: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': '',
        'right_img': '',
        'name': 'Bracken Fern'
    },

    23: {
        'left_attribute': 'Does the plant trail along the ground',
        'right_attribute': 'does it show upright growth of more than a few feet?',
        'left_index': 29,
        'right_index': 30,
        'left_img': 'https://i.pinimg.com/564x/fd/aa/3c/fdaa3c42a2e59a8ee8c160d9accc8955.jpg',
        'right_img': 'https://www.plantoregon.com/images/products/symphoricarposalbusLARGEnew.jpg',
        'name': None
    },

    24: {
        'left_attribute': 'Is the plant hairy',
        'right_attribute': 'hairless?',
        'left_index': 31,
        'right_index': 32,
        'left_img': 'https://3.bp.blogspot.com/-c4lc1HfDHe8/WtJ3LvEA7PI/AAAAAAAAAdc/8fbU-inT9Porxkdduahi2JSojK71Vck1QCLcBGAs/s1600/fullsizeoutput_192.jpeg',
        'right_img': 'https://cdn.shopify.com/s/files/1/1518/7378/products/Salal.JPG?v=1531414506',
        'name': None
    },

    25: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': '',
        'right_img': '',
        'name': 'Big Leaf Maple'
    },

    26: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': '',
        'right_img': '',
        'name': 'Red Alder'
    },

    27: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': '',
        'right_img': '',
        'name': 'Sword Fern'
    },

    28: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': '',
        'right_img': '',
        'name': 'Deer Fern'
    },

    29: {
        'left_attribute': 'Are the leaves not clustered (attached singly to the stem)',
        'right_attribute': 'clustered?',
        'left_index': 33,
        'right_index': 34,
        'left_img': 'https://4.bp.blogspot.com/_w82lQpJ5qcE/TUWqPOdszwI/AAAAAAAACvo/LwtYFeJg74I/s1600/thimbleberry-parent-closer3-sm.jpg',
        'right_img': 'https://sussexwoodland.files.wordpress.com/2011/06/229.jpg',
        'name': None
    },

    30: {
        'left_attribute': 'Is the plant hairy',
        'right_attribute': 'hairless?',
        'left_index': 35,
        'right_index': 36,
        'left_img': 'https://3.bp.blogspot.com/-c4lc1HfDHe8/WtJ3LvEA7PI/AAAAAAAAAdc/8fbU-inT9Porxkdduahi2JSojK71Vck1QCLcBGAs/s1600/fullsizeoutput_192.jpeg',
        'right_img': 'https://cdn.shopify.com/s/files/1/1518/7378/products/Salal.JPG?v=1531414506',
        'name': None
    },

    31: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': '',
        'right_img': '',
        'name': 'Stinky Bob (Herb Robert)'
    },

    32: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': '',
        'right_img': '',
        'name': 'Poison Hemlock'
    },

    33: {
        'left_attribute': 'Does the plant have a waxy stem',
        'right_attribute': 'prickly stem?',
        'left_index': 37,
        'right_index': 38,
        'left_img': 'https://images.squarespace-cdn.com/content/v1/5355817fe4b0d272a279fe8c/1557526755528-A6RZJFDPQA7W5HO9G1I5/salal-tips.jpg?format=750w',
        'right_img': 'https://i0.wp.com/twiningvinegarden.com/wp-content/uploads/2020/06/rubus-ursinus-fruit-e1593118705405.jpg?fit=498%2C600&ssl=1',
        'name': None
    },

    34: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': '',
        'right_img': '',
        'name': 'Trillium'
    },

    35: {
        'left_attribute': 'Are the leaves fuzzy on both sides',
        'right_attribute': 'fuzzy on one side?',
        'left_index': 39,
        'right_index': 40,
        'left_img': 'https://i.pinimg.com/564x/d9/54/22/d95422ecfaceca1371779c3f03649a0e.jpg',
        'right_img': 'https://www.adirondack.net/images/stinging-nettle.jpg',
        'name': None
    },

    36: {
        'left_attribute': 'Are there thorns',
        'right_attribute': 'no thorns?',
        'left_index': 41,
        'right_index': 42,
        'left_img': 'https://www.nwcb.wa.gov/images/weeds/himalayan-blackberry/himalayanblackberry3.jpg',
        'right_img': 'https://ucanr.edu/blogs/SJVAgronomyWeedScienceBlog/blogfiles/53234_original.jpg',
        'name': None
    },

    37: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': '',
        'right_img': '',
        'name': 'English Ivy'
    },

    38: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': '',
        'right_img': '',
        'name': 'Trailing Blackberry'
    },

    39: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': '',
        'right_img': '',
        'name': 'Thimbleberry'
    },

    40: {
        'left_attribute': 'Are there thorns',
        'right_attribute': 'no thorns?',
        'left_index': 43,
        'right_index': 44,
        'left_img': 'https://www.nwcb.wa.gov/images/weeds/himalayan-blackberry/himalayanblackberry3.jpg',
        'right_img': 'https://ucanr.edu/blogs/SJVAgronomyWeedScienceBlog/blogfiles/53234_original.jpg',
        'name': None
    },

    41: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': '',
        'right_img': '',
        'name': 'Salmonberry'
    },

    42: {
        'left_attribute': 'Are the leaves not waxy',
        'right_attribute': 'waxy?',
        'left_index': 45,
        'right_index': 46,
        'left_img': 'https://i.pinimg.com/564x/d9/54/22/d95422ecfaceca1371779c3f03649a0e.jpg',
        'right_img': 'https://images.squarespace-cdn.com/content/v1/5355817fe4b0d272a279fe8c/1557526755528-A6RZJFDPQA7W5HO9G1I5/salal-tips.jpg?format=750w',
        'name': None
    },

    43: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': '',
        'right_img': '',
        'name': 'Himalayan Blackberry'
    },

    44: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': '',
        'right_img': '',
        'name': 'Stinging Nettle'
    },

    45: {
        'left_attribute': 'Does the plant have green stems',
        'right_attribute': 'brown stems?',
        'left_index': 47,
        'right_index': 48,
        'left_img': 'https://pmcafee2013.files.wordpress.com/2014/07/cahi3_stem_001.jpg',
        'right_img': 'https://pearsonecological.com/wp-content/uploads/32175819587_f6176c043b_k.jpg',
        'name': None
    },

    46: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': '',
        'right_img': '',
        'name': 'Salal'
    },

    47: {
        'left_attribute': 'Are the leaves clustered',
        'right_attribute': 'not clustered?',
        'left_index': 49,
        'right_index': 50,
        'left_img': 'https://sussexwoodland.files.wordpress.com/2011/06/229.jpg',
        'right_img': 'https://4.bp.blogspot.com/_w82lQpJ5qcE/TUWqPOdszwI/AAAAAAAACvo/LwtYFeJg74I/s1600/thimbleberry-parent-closer3-sm.jpg',
        'name': None
    },

    48: {
        'left_attribute': 'Are the leaves serrated',
        'right_attribute': 'not serrated?',
        'left_index': 51,
        'right_index': 52,
        'left_img': 'https://www.healthbenefitstimes.com/glossary/wp-content/uploads/2020/06/Serrated-leaf.jpg',
        'right_img': 'https://www.friendsofthewildflowergarden.org/generaljpegs/Seasons/trees/snowberryleafh.jpg',
        'name': None
    },

    49: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': '',
        'right_img': '',
        'name': 'Scotch Broom'
    },

    50: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': '',
        'right_img': '',
        'name': 'Red Huckleberry'
    },

    51: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': '',
        'right_img': '',
        'name': 'Hardhack'
    },

    52: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': '',
        'right_img': '',
        'name': 'Snowberry'
    },
}




class Node:
    def __init__(self, left_attribute, right_attribute, left_index, right_index, left_img, right_img, name=None):
        self.left_attribute = left_attribute
        self.right_attribute = right_attribute
        self.left_index = left_index
        self.right_index = right_index
        self.left_img = left_img
        self.right_img = right_img
        self.name = name
        


@app.route('/')
def index():

    node_id = int(request.args.get('node_id', 0))
    config = node_config[node_id]

    node = Node(config['left_attribute'], config['right_attribute'], config['left_index'], config['right_index'], config['left_img'], config['right_img'], config['name'])

    return render_template('PNW_Plant_Flask.html', node=node)
    
# Protecting against any other files being run (I only want this one):

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)

