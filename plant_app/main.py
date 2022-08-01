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
        'name_img': None,
        'name': None
    },

    # q01 = Node('Is the plant less than 10 feet tall', 'more than ten feet tall', q03, q04)
    1: {
        'left_attribute': 'Is the plant less than 10 feet tall',
        'right_attribute': 'more than 10 feet tall?',
        'left_index': 3,
        'right_index': 4,
        'left_img': 'https://en.wikipedia.org/wiki/Shrub#/media/File:Hortensie,_blau.jpg',
        'right_img': 'https://www.greenlawnfertilizing.com/wp-content/uploads/2017/01/oak-tree.jpg.webp',
        'name_img': None,
        'name': None
    },

    2: {
        'left_attribute': 'Do the needles attach to the branch as single needles',
        'right_attribute': 'branchlets made of many tiny needles?',
        'left_index': 5,
        'right_index': 6,
        'left_img': 'https://www.naturallywood.com/wp-content/uploads/Douglas-Fir_KCharleton_042_10474-1200x800-5b2df79-e1600100637617.jpg',
        'right_img': 'https://cdn.shopify.com/s/files/1/0089/3075/4665/products/cedar_leaf_Thuja_occidentalis_1200x.jpg?v=1569171691',
        'name_img': None,
        'name': None
    },

    3: {
        'left_attribute': 'Does the plant have a compound leaf structure made of many tiny leaves',
        'right_attribute': 'a single leaf structure?',
        'left_index': 7,
        'right_index': 8,
        'left_img': 'https://pbs.twimg.com/media/CFaLZs9WAAAtesF?format=jpg&name=small',
        'right_img': 'http://dendro.cnre.vt.edu/dendrology/images/Quercus%20velutina/leaf1.jpg',
        'name_img': None,
        'name': None
    },

    4: {
        'left_attribute': 'Is the bark multicolored green and reddish brown',
        'right_attribute': 'not multicolored?',
        'left_index': 9,
        'right_index': 10,
        'left_img': 'https://i.etsystatic.com/14438497/r/il/e6a1fa/1270238314/il_fullxfull.1270238314_oh69.jpg',
        'right_img': 'https://i.pinimg.com/564x/9f/95/29/9f9529395b1306bd4843c8fa8e034208.jpg',
        'name_img': None,
        'name': None
    },

    5: {
        'left_attribute': 'Is there an orderly spiral needle pattern',
        'right_attribute': 'chaotic spindly needle pattern?',
        'left_index': 11,
        'right_index': 12,
        'left_img': 'https://cdn.shopify.com/s/files/1/0510/9855/0461/products/hydrosol-doug-fir-botanical-second_1024x1024.jpg?v=1616627159',
        'right_img': 'https://storage.idigbio.org/portals/seinet/midwest/Pinaceae/201808/Tsuga_heterophylla_cone_er_1534286428.jpg',
        'name_img': None,
        'name': None
    },

    6: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': None,
        'right_img': None,
        'name_img': 'https://upload.wikimedia.org/wikipedia/commons/a/a3/Thuja_plicata_Vancouver.jpg',
        'name': 'Western Red Cedar'
    },

    7: {
        'left_attribute': 'Are the leaves smooth and without teeth',
        'right_attribute': 'sharp with teeth?',
        'left_index': 13,
        'right_index': 14,
        'left_img': 'https://www.thoughtco.com/thmb/sXrVxKbkw8SbiwaW0vh8Yz92_oM=/1250x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/152846652_10-56af62205f9b58b7d0182bcb.jpg',
        'right_img': 'https://images.squarespace-cdn.com/content/v1/5ab428368ab722cc4372413b/1585668188524-JOV6CYBWVAGAAHY2VBET/Mahonia+aquifolium+flower.jpg?format=1000w',
        'name_img': None,
        'name': None
    },

    8: {
        'left_attribute': 'Is the leaf size greater than one foot',
        'right_attribute': 'less than one foot?',
        'left_index': 15,
        'right_index': 16,
        'left_img': 'https://www.choicesdomatter.org/wp-content/uploads/2015/06/skunk-cabbage-closeup.jpg',
        'right_img': 'https://cdn.pixabay.com/photo/2020/04/30/21/40/green-leaves-5114700_1280.jpg',
        'name_img': None,
        'name': None
    },

    9: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': None,
        'right_img': None,
        'name_img': 'https://salishmagazine.org/wp-content/uploads/2020/05/Picture2h.jpg',
        'name': 'Madrone'
    },

    10: {
        'left_attribute': 'Does the plant have a compound leaf structure made of many tiny leaves',
        'right_attribute': 'a single leaf structure?',
        'left_index': 17,
        'right_index': 18,
        'left_img': 'https://pbs.twimg.com/media/CFaLZs9WAAAtesF?format=jpg&name=small',
        'right_img': 'http://dendro.cnre.vt.edu/dendrology/images/Quercus%20velutina/leaf1.jpg',
        'name_img': None,
        'name': None
    },

    11: {
        'left_attribute': 'Is the plant less than 10 feet tall',
        'right_attribute': 'more than ten feet tall?',
        'left_index': 19,
        'right_index': 20,
        'left_img': 'https://www.cypresscreeklandscapesupply.com/blog/wp-content/uploads/2019/11/shrubs.jpg',
        'right_img': 'https://www.greenlawnfertilizing.com/wp-content/uploads/2017/01/oak-tree.jpg.webp',
        'name_img': None,
        'name': None
    },

    12: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': None,
        'right_img': None,
        'name_img': 'https://images.squarespace-cdn.com/content/v1/550ba3ece4b003774ad9e941/1442514030401-L3U6U7B3KM631IKI1XNK/WesternHemlock14August06WesternSlopeCascades_5.jpg?format=2500w',
        'name': 'Western Hemlock'
    },

    13: {
        'left_attribute': 'Is every leaf about the same size',
        'right_attribute': 'triangular, getting much wider at the bottom?',
        'left_index': 21,
        'right_index': 22,
        'left_img': 'https://upload.wikimedia.org/wikipedia/commons/8/8d/Polystichum_munitum_%28Jami_Dwyer%29_001.jpg',
        'right_img': 'https://cdn11.bigcommerce.com/s-gp99ab/images/stencil/500x659/products/4752/11292/apivwslpm__13856.1630323659__62663.1630981312.jpg?c=3',
        'name_img': None,
        'name': None
    },

    14: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': None,
        'right_img': None,
        'name_img': 'https://i.pinimg.com/564x/9c/18/04/9c18049bc79a055e444e3fb86861be1d.jpg',
        'name': 'Oregon Grape'
    },

    15: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': None,
        'right_img': None,
        'name_img': 'https://upload.wikimedia.org/wikipedia/commons/8/81/WesternSkunkCabbage.JPG',
        'name': 'Skunk Cabbage'
    },

    16: {
        'left_attribute': 'Is the plant not smelly',
        'right_attribute': 'smelly?',
        'left_index': 23,
        'right_index': 24,
        'left_img': 'https://womenbelong.com/wp-content/uploads/2017/09/asian-girl-flower-smell-2-1.jpg',
        'right_img': 'https://www.sanluisobispo.com/news/local/education/eqmo7n/picture244132872/alternates/FREE_768/zCorpse%20flower056627',
        'name_img': None,
        'name': None
    },

    17: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': None,
        'right_img': None,
        'name_img': 'http://nativeplantspnw.com/wp-content/uploads/2017/03/Red-Elderberry-bush.png',
        'name': 'Red Elderberry'
    },

    18: {
        'left_attribute': 'Is it a lobed, finger-like leaf shape',
        'right_attribute': 'oval leaf shape?',
        'left_index': 25,
        'right_index': 26,
        'left_img': 'https://i.redd.it/7r773173jk271.jpg',
        'right_img': 'https://upload.wikimedia.org/wikipedia/commons/3/33/Rosa_canina_blatt_2005.05.26_11.50.13.jpg',
        'name_img': None,
        'name': None
    },

    19: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': None,
        'right_img': None,
        'name_img': 'http://wildfoodsandmedicines.com/wp-content/uploads/2013/07/Horsetail-hyemale.jpg',
        'name': 'Horsetail'
    },

    20: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': None,
        'right_img': None,
        'name_img': 'https://www.welton.it/photos/cascades/doug_fir.jpg',
        'name': 'Douglas Fir'
    },

    21: {
        'left_attribute': 'Does the plant have an open drooping center',
        'right_attribute': 'upright center?',
        'left_index': 27,
        'right_index': 28,
        'left_img': 'https://i0.wp.com/www.coastwildlife.org/wp-content/uploads/2020/05/fern1.png?fit=480%2C358&ssl=1',
        'right_img': 'https://www.anniesannuals.com/signs/b%20-%20c/images//blechnum_spicant.jpg',
        'name_img': None,
        'name': None
    },

    22: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': None,
        'right_img': None,
        'name_img': 'https://static.inaturalist.org/photos/12132040/large.jpeg?1512077515',
        'name': 'Bracken Fern'
    },

    23: {
        'left_attribute': 'Does the plant trail along the ground',
        'right_attribute': 'does it show upright growth of more than a few feet?',
        'left_index': 29,
        'right_index': 30,
        'left_img': 'https://i.pinimg.com/564x/fd/aa/3c/fdaa3c42a2e59a8ee8c160d9accc8955.jpg',
        'right_img': 'https://www.plantoregon.com/images/products/symphoricarposalbusLARGEnew.jpg',
        'name_img': None,
        'name': None
    },

    24: {
        'left_attribute': 'Is the plant hairy',
        'right_attribute': 'hairless?',
        'left_index': 31,
        'right_index': 32,
        'left_img': 'https://3.bp.blogspot.com/-c4lc1HfDHe8/WtJ3LvEA7PI/AAAAAAAAAdc/8fbU-inT9Porxkdduahi2JSojK71Vck1QCLcBGAs/s1600/fullsizeoutput_192.jpeg',
        'right_img': 'https://cdn.shopify.com/s/files/1/1518/7378/products/Salal.JPG?v=1531414506',
        'name_img': None,
        'name': None
    },

    25: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': None,
        'right_img': None,
        'name_img': 'https://wingtrip.files.wordpress.com/2020/05/brendan_mcgarry_200421_00008.jpg?w=2140',
        'name': 'Big Leaf Maple'
    },

    26: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': None,
        'right_img': None,
        'name_img': 'http://nativeplantspnw.com/wp-content/uploads/2014/06/Alnus-rubra-trees.jpg',
        'name': 'Red Alder'
    },

    27: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': None,
        'right_img': None,
        'name_img': 'https://animals.sandiegozoo.org/sites/default/files/2017-12/sword-fern-redwood-forest.jpg',
        'name': 'Sword Fern'
    },

    28: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': None,
        'right_img': None,
        'name_img': 'https://www.anniesannuals.com/signs/b%20-%20c/images//blechnum_spicant.jpg',
        'name': 'Deer Fern'
    },

    29: {
        'left_attribute': 'Are the leaves not clustered (attached singly to the stem)',
        'right_attribute': 'clustered?',
        'left_index': 33,
        'right_index': 34,
        'left_img': 'https://4.bp.blogspot.com/_w82lQpJ5qcE/TUWqPOdszwI/AAAAAAAACvo/LwtYFeJg74I/s1600/thimbleberry-parent-closer3-sm.jpg',
        'right_img': 'https://sussexwoodland.files.wordpress.com/2011/06/229.jpg',
        'name_img': None,
        'name': None
    },

    30: {
        'left_attribute': 'Is the plant hairy',
        'right_attribute': 'hairless?',
        'left_index': 35,
        'right_index': 36,
        'left_img': 'https://3.bp.blogspot.com/-c4lc1HfDHe8/WtJ3LvEA7PI/AAAAAAAAAdc/8fbU-inT9Porxkdduahi2JSojK71Vck1QCLcBGAs/s1600/fullsizeoutput_192.jpeg',
        'right_img': 'https://cdn.shopify.com/s/files/1/1518/7378/products/Salal.JPG?v=1531414506',
        'name_img': None,
        'name': None
    },

    31: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': None,
        'right_img': None,
        'name_img': 'https://lh6.ggpht.com/ex2xzLIOCasX9wliDmYZuOklUT2T1pjf4MvbsZo7D2DEThscAIy9MDbqoVNF7hiubyxXb7lCY9BBu5Y1M5A=s1200',
        'name': 'Stinky Bob (Herb Robert)'
    },

    32: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': None,
        'right_img': None,
        'name_img': 'https://kingcounty.gov/~/media/environment/animalsAndPlants/noxious_weeds/imagesO_R/poison-hemlock-young-plant-BHart.ashx?la=en',
        'name': 'Poison Hemlock'
    },

    33: {
        'left_attribute': 'Does the plant have a waxy stem',
        'right_attribute': 'prickly stem?',
        'left_index': 37,
        'right_index': 38,
        'left_img': 'https://images.squarespace-cdn.com/content/v1/5355817fe4b0d272a279fe8c/1557526755528-A6RZJFDPQA7W5HO9G1I5/salal-tips.jpg?format=750w',
        'right_img': 'https://i0.wp.com/twiningvinegarden.com/wp-content/uploads/2020/06/rubus-ursinus-fruit-e1593118705405.jpg?fit=498%2C600&ssl=1',
        'name_img': None,
        'name': None
    },

    34: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': None,
        'right_img': None,
        'name_img': 'https://www.degroot-inc.com/wp-content/uploads/2018/03/Trillium_White.jpg',
        'name': 'Trillium'
    },

    35: {
        'left_attribute': 'Are the leaves fuzzy on both sides',
        'right_attribute': 'fuzzy on one side?',
        'left_index': 39,
        'right_index': 40,
        'left_img': 'https://i.pinimg.com/564x/d9/54/22/d95422ecfaceca1371779c3f03649a0e.jpg',
        'right_img': 'https://www.adirondack.net/images/stinging-nettle.jpg',
        'name_img': None,
        'name': None
    },

    36: {
        'left_attribute': 'Are there thorns',
        'right_attribute': 'no thorns?',
        'left_index': 41,
        'right_index': 42,
        'left_img': 'https://www.nwcb.wa.gov/images/weeds/himalayan-blackberry/himalayanblackberry3.jpg',
        'right_img': 'https://ucanr.edu/blogs/SJVAgronomyWeedScienceBlog/blogfiles/53234_original.jpg',
        'name_img': None,
        'name': None
    },

    37: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': None,
        'right_img': None,
        'name_img': 'https://i.pinimg.com/564x/83/cb/12/83cb12c8c639606b4fb7096264a614fb.jpg',
        'name': 'English Ivy'
    },

    38: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': None,
        'right_img': None,
        'name_img': 'https://www.springbrookpark.org/wp-content/uploads/2020/04/blackberry1-scaled.jpg',
        'name': 'Trailing Blackberry'
    },

    39: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': None,
        'right_img': None,
        'name_img': 'https://i.pinimg.com/564x/78/cf/d1/78cfd13969eff2c4af24e8e602943ab7.jpg',
        'name': 'Thimbleberry'
    },

    40: {
        'left_attribute': 'Are there thorns',
        'right_attribute': 'no thorns?',
        'left_index': 43,
        'right_index': 44,
        'left_img': 'https://www.nwcb.wa.gov/images/weeds/himalayan-blackberry/himalayanblackberry3.jpg',
        'right_img': 'https://ucanr.edu/blogs/SJVAgronomyWeedScienceBlog/blogfiles/53234_original.jpg',
        'name_img': None,
        'name': None
    },

    41: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': None,
        'right_img': None,
        'name_img': 'https://i.ebayimg.com/images/g/P0gAAOSw4iVfCIoo/s-l500.jpg',
        'name': 'Salmonberry'
    },

    42: {
        'left_attribute': 'Are the leaves not waxy',
        'right_attribute': 'waxy?',
        'left_index': 45,
        'right_index': 46,
        'left_img': 'https://i.pinimg.com/564x/d9/54/22/d95422ecfaceca1371779c3f03649a0e.jpg',
        'right_img': 'https://images.squarespace-cdn.com/content/v1/5355817fe4b0d272a279fe8c/1557526755528-A6RZJFDPQA7W5HO9G1I5/salal-tips.jpg?format=750w',
        'name_img': None,
        'name': None
    },

    43: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': None,
        'right_img': None,
        'name_img': 'http://3.bp.blogspot.com/-fDJoMWx1BOc/UMi5I7u4P6I/AAAAAAAAJFY/gpqF6N5x2_k/s1600/Himalayan-Blackberry-Fruit-edited.jpg',
        'name': 'Himalayan Blackberry'
    },

    44: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': None,
        'right_img': None,
        'name_img': 'https://northernwoodlands.org/images/made/images/articles/nettle1_585_525_65.jpg',
        'name': 'Stinging Nettle'
    },

    45: {
        'left_attribute': 'Does the plant have green stems',
        'right_attribute': 'brown stems?',
        'left_index': 47,
        'right_index': 48,
        'left_img': 'https://pmcafee2013.files.wordpress.com/2014/07/cahi3_stem_001.jpg',
        'right_img': 'https://s3.amazonaws.com/eit-planttoolbox-prod/media/images/Spirea-tomentosa--Charles-Wohlers--CC-BY-NC-ND.jpg',
        'name_img': None,
        'name': None
    },

    46: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': None,
        'right_img': None,
        'name_img': 'https://thenorthwestforager.files.wordpress.com/2015/06/dsc_0805-1280x853.jpg',
        'name': 'Salal'
    },

    47: {
        'left_attribute': 'Are the leaves clustered',
        'right_attribute': 'not clustered?',
        'left_index': 49,
        'right_index': 50,
        'left_img': 'https://sussexwoodland.files.wordpress.com/2011/06/229.jpg',
        'right_img': 'https://4.bp.blogspot.com/_w82lQpJ5qcE/TUWqPOdszwI/AAAAAAAACvo/LwtYFeJg74I/s1600/thimbleberry-parent-closer3-sm.jpg',
        'name_img': None,
        'name': None
    },

    48: {
        'left_attribute': 'Are the leaves serrated',
        'right_attribute': 'not serrated?',
        'left_index': 51,
        'right_index': 52,
        'left_img': 'https://www.healthbenefitstimes.com/glossary/wp-content/uploads/2020/06/Serrated-leaf.jpg',
        'right_img': 'https://www.friendsofthewildflowergarden.org/generaljpegs/Seasons/trees/snowberryleafh.jpg',
        'name_img': None,
        'name': None
    },

    49: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': None,
        'right_img': None,
        'name_img': 'https://www.nps.gov/common/uploads/stories/images/nri/20160415/articles/0A91350B-1DD8-B71B-0B6D8DEA9FFAEFCA/0A91350B-1DD8-B71B-0B6D8DEA9FFAEFCA.jpg',
        'name': 'Scotch Broom'
    },

    50: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': None,
        'right_img': None,
        'name_img': 'https://i.pinimg.com/564x/b7/e2/54/b7e25444b32de74575215f46649d0785.jpg',
        'name': 'Red Huckleberry'
    },

    51: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': None,
        'right_img': None,
        'name_img': 'https://d2j6dbq0eux0bg.cloudfront.net/images/1681591/144097150.jpg',
        'name': 'Hardhack'
    },

    52: {
        'left_attribute': None,
        'right_attribute': None,
        'left_index': None,
        'right_index': None,
        'left_img': None,
        'right_img': None,
        'name_img': 'https://images.squarespace-cdn.com/content/v1/53b1a4ffe4b0be1ad02217c5/1561672601024-VJP9U6VSFB8ZLC8VLV51/Common+snowberry+%28Symphoricarpos+albus%29.jpg?format=1500w',
        'name': 'Snowberry'
    },
}




class Node:
    def __init__(self, left_attribute, right_attribute, left_index, right_index, left_img, right_img, name_img, name=None):
        self.left_attribute = left_attribute
        self.right_attribute = right_attribute
        self.left_index = left_index
        self.right_index = right_index
        self.left_img = left_img
        self.right_img = right_img
        self.name_img = name_img
        self.name = name
        


@app.route('/')
def index():

    node_id = int(request.args.get('node_id', 0))
    config = node_config[node_id]

    node = Node(config['left_attribute'], config['right_attribute'], config['left_index'], config['right_index'], config['left_img'], config['right_img'], config['name_img'], config['name'])

    return render_template('PNW_Plant_Flask.html', node=node)
    
# Protecting against any other files being run (I only want this one):

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)

