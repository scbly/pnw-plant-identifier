class Plant():
    def __init__(self):
        self.leaf_type = False
        self.plant_height = False
        self.bark_type = False
        self.leaf_pattern = False
        self.leaf_shape = False
        self.needle_type = False
        self.needle_pattern = False
        self.leaf_size = False
        self.toothiness = False
        self.leaf_size_uniformity = False
        self.plant_shape = False
        self.stem_texture = False
        self.leaf_growth_pattern = False
        self.fuzziness = False
        self.thorniness = False
        self.hairiness = False
        self.leaf_texture = False
        self.smelliness = False
        self.serration = False
        self.plant_structure = False 
        self.stem_color = False
        self.identity = False
    
    def identify_plant(self):
        while self.identity == False: 
                self.step_one()
        else:
            print(f"You have successfully identified your plant! You have a {self.identity}.")
 
    def step_ten(self):
        while (self.identity == False and self.thorniness == False):
            thorniness = input('Thorniness: thorns or no thorns?')
            if thorniness == 'thorns':
                self.thorniness = 'thorns'
                self.identity = 'Salmonberry'
            elif thorniness == 'no thorns':
                self.thorniness = 'no thorns'
                while (self.identity == False and self.leaf_texture == False):
                    leaf_texture = input('Leaf texture: not waxy or waxy?')
                    if leaf_texture == 'waxy':
                        self.leaf_texture = 'waxy'
                        self.identity = 'Salal'
                    elif leaf_texture == 'not waxy':
                        self.leaf_texture = 'not waxy'
                        while (self.identity == False and self.stem_color == False):
                            stem_color = input('Stem color: green or brown?')
                            if stem_color == 'green':
                                self.stem_color = 'green'
                                while (self.identity == False and self.leaf_growth_pattern == False):
                                    leaf_growth_pattern = input('Leaf growth pattern: not clustered or clustered?')
                                    if leaf_growth_pattern == 'clustered':
                                        self.leaf_growth_pattern = 'clustered'
                                        self.identity = 'Scotch Broom'
                                    elif leaf_growth_pattern == 'not clustered':
                                        self.leaf_growth_pattern = 'not clustered'
                                        self.identity = 'Red Huckleberry'
                                    else:
                                        print('Please type one of the two options exactly as shown.')
                            elif stem_color == 'brown':
                                self.stem_color = 'brown'
                                while (self.identity == False and self.serration == False):
                                    serration = input('Serration: serrated or not serrated?')
                                    if serration == 'serrated':
                                        self.serration = 'serrated'
                                        self.identity = 'Hardhack'
                                    elif serration == 'not serrated':
                                        self.serration = 'not serrated'
                                        self.identity = 'Snowberry'
                                    else:
                                        print('Please type one of the two options exactly as shown.')
                            else:
                                print('Please type one of the two options exactly as shown.')
                    else:
                        print('Please type one of the two options exactly as shown.')
            else:
                print('Please type one of the two options exactly as shown.')


    def step_nine(self):
        while (self.identity == False and self.hairiness == False):
            hairiness = input('Hairiness: hairy or hairless?')
            if hairiness == 'hairy':
                self.hairiness = 'hairy'
                while (self.identity == False and self.fuzziness == False):
                    fuzziness = input('Fuzziness: fuzzy both sides or fuzzy one side?')
                    if fuzziness == 'fuzzy both sides':
                        self.fuzziness = 'fuzzy both sides'
                        self.identity = 'Thimbleberry'
                    elif fuzziness == 'fuzzy one side':
                        self.fuzziness = 'fuzzy one side'
                        while (self.identity == False and self.thorniness == False):
                            thorniness = input('Thorniness: thorns or no thorns?')
                            if thorniness == 'thorns':
                                self.thorniness = 'thorns'
                                self.identity = 'Himalayan Blackberry'
                            elif thorniness == 'no thorns':
                                self.thorniness = 'no thorns'
                                self.identity = 'Stinging Nettle'
                            else:
                                print('Please type one of the two options exactly as shown.')
                    else:
                        print('Please type one of the two options exactly as shown.')       
            elif hairiness == 'hairless':
                self.hairiness = 'hairless'
            else:
                print('Please type one of the two options exactly as shown.')


    def step_eight(self):
        while (self.identity == False and self.plant_structure == False and self.leaf_growth_pattern == False and self.stem_texture == False):
            plant_structure = input('Plant Structure: trailing or erect?')
            if plant_structure == 'erect':
                self.plant_structure = 'erect'
            elif plant_structure == 'trailing':
                self.plant_structure = 'trailing'
                while (self.identity == False and self.leaf_growth_pattern == False and self.stem_texture == False):
                    leaf_growth_pattern = input('Leaf growth pattern: not clustered or clustered?')
                    if leaf_growth_pattern == 'clustered':
                        self.leaf_growth_pattern = 'clustered'
                        self.identity = 'Trillium'
                    elif leaf_growth_pattern == 'not clustered':
                        self.leaf_growth_pattern = 'not clustered'
                        while (self.identity == False and self.stem_texture == False):
                            stem_texture = input('Stem texture: waxy and smooth or prickly?')
                            if stem_texture == 'waxy and smooth':
                                self.stem_texture = 'waxy and smooth'
                                self.identity = 'English Ivy'
                            elif stem_texture == 'prickly':
                                self.stem_texture = 'prickly'
                                self.identity = 'Trailing Blackberry'
                            else:
                                print('Please type one of the two options exactly as shown.')
                    else:
                        print('Please type one of the two options exactly as shown.')
            else:
                print('Please type one of the two options exactly as shown.')


    def step_seven(self):
        while (self.identity == False and self.leaf_size == False and self.smelliness == False and self.hairiness == False):
            leaf_size = input('Leaf Size: >1 ft. or <1 ft.?')
            if leaf_size == '>1 ft.':
                self.leaf_size = '>1 ft.'
                self.identity = 'Skunk Cabbage'
            elif leaf_size == '<1 ft.':
                self.leaf_size = '<1 ft.'
                while (self.identity == False and self.hairiness == False and self.smelliness == False):
                    smelliness = input('Smelliness: not smelly or smelly?')
                    if smelliness == 'not smelly':
                        self.smelliness = 'not smelly'
                    elif smelliness == 'smelly':
                        self.smelliness = 'smelly'
                        while self.identity == False:
                            hairiness = input('Hairiness: hairy or hairless?')
                            if hairiness == 'hairy':
                                self.hairiness = 'hairy'
                                self.identity = 'Stinky Bob (Herb Robert)'
                            elif hairiness == 'hairless':
                                self.hairiness = 'hairless'
                                self.identity = 'Poison Hemlock'
                            else:
                                print('Please type one of the two options exactly as shown.')
                    else:
                        print('Please type one of the two options exactly as shown.')          
            else:
                print('Please type one of the two options exactly as shown.')


    def step_six(self):
        while (self.identity == False and self.toothiness == False and self.leaf_size_uniformity == False and self.plant_shape == False):
            toothiness = input('Toothiness: without teeth or teeth?')   
            if toothiness == 'without teeth':
                self.toothiness = 'without teeth'
                while (self.identity == False and self.leaf_size_uniformity == False):
                    leaf_size_uniformity = input('Leaf Size Uniformity: uniform or not uniform (triangular)?')
                    if leaf_size_uniformity == 'uniform':
                        self.leaf_size_uniformity = 'uniform'
                        while self.identity == False:
                            plant_shape = input('Plant shape: open center or upright center?')
                            if plant_shape == 'open center':
                                self.plant_shape = 'open center'
                                self. identity = 'Sword Fern'
                            elif plant_shape == 'upright center':
                                self.plant_shape = 'upright center'
                                self.identity = 'Deer Fern'
                            else:
                                print('Please type one of the two options exactly as shown.')
                    elif leaf_size_uniformity == 'not uniform (triangular)':
                        self.leaf_size_uniformity = 'not uniform (triangular)'
                        self.identity = 'Bracken Fern'
                    else:
                        print('Please type one of the two options exactly as shown.')
            elif toothiness == 'teeth':
                self.toothiness = 'teeth'
                self.identity = 'Oregon Grape'
            else:
                print('Please type one of the two options exactly as shown.')
    
    def step_five(self):
        while (self.identity == False and self.leaf_pattern == False):
            leaf_pattern = input('Leaf Pattern: compound or single?')
            if leaf_pattern == 'compound':
                self.leaf_pattern = 'compound'
            elif leaf_pattern == 'single':
                self.leaf_pattern = 'single'
            else: 
                print('Please type one of the two options exactly as shown.')
    
            
    def step_four(self):
        while (self.identity == False and self.bark_type == False and self.leaf_pattern == False and self.leaf_shape == False):
            bark_type = input('Bark Type: multicolored or not multicolored?')
            if bark_type == 'multicolored':
                self.bark_type = 'multicolored'
                self.identity = 'Madrone'
            elif bark_type == 'not multicolored':
                self.bark_type = 'not multicolored'
                while (self.leaf_pattern == False and self.leaf_shape == False):
                    leaf_pattern = input('Leaf Pattern: compound or single?')
                    if leaf_pattern == 'compound':
                        self.leaf_pattern = 'compound'
                        self.identity = 'Red Elderberry'
                    elif leaf_pattern == 'single':
                        while self.leaf_shape == False:
                            leaf_shape = input('Leaf Shape: lobed or elliptical?')
                            if leaf_shape == 'lobed':
                                self.leaf_shape = 'lobed'
                                self.identity = 'Big Leaf Maple'
                            elif leaf_shape == 'elliptical':
                                self.leaf_shape = 'elliptical'
                                self.identity = 'Red Alder'
                            else:
                                print('Please type one of the two options exactly as shown.')
                    else:
                        print('Please type one of the two options exactly as shown.')
            else:
                print('Please type one of the two options exactly as shown.')
            

    def step_three(self):
        while (self.identity == False and self.needle_pattern == False and self.plant_height == False):
            needle_pattern = input('Needle Pattern: orderly or chaotic?')
            if needle_pattern == 'orderly':
                self.needle_pattern = 'orderly'
                while (self.identity == False and self.plant_height == False):
                    plant_height = input('Plant height: <10 ft. or >10 ft.')
                    if plant_height == '<10 ft.':
                        self.plant_height = '<10 ft.'
                        self.identity = 'Horsetail'
                    elif plant_height == '>10 ft.':
                        self.plant_height = '>10 ft.'
                        self.identity = 'Douglas Fir'
                    else:
                        print('Please type one of the two options exactly as shown.')
            elif needle_pattern == 'chaotic':
                self.needle_pattern = 'chaotic'
                self.identity = 'Western Hemlock'
            else:
                print('Please type one of the two options exactly as shown.')
                                     
    
    def step_two(self):
        while (self.identity == False and self.needle_type == False and self.plant_height == False):
                if self.leaf_type == 'broad and flat':
                    while (self.identity == False and self.plant_height == False):
                        plant_height = input('Plant Height: <10 ft. or >10 ft.?')
                        if plant_height == '<10 ft.':
                            self.plant_height = '<10 ft.'
                        elif plant_height == '>10 ft.':
                            self.plant_height = '>10 ft.'
                        else:
                            print('Please type one of the two options exactly as shown.')
                elif self.leaf_type == 'needle-like':
                    while self.needle_type == False:
                        needle_type = input('Needle Type: single needle or branchlets?')
                        if needle_type == 'single needle':
                            self.needle_type = 'single needle'
                        elif needle_type == 'branchlets':
                            self.needle_type = 'branchlets'
                            self.identity = 'Western Red Cedar'
                        else:
                            print('Please type one of the two options exactly as shown.')
    
    
    def step_one(self):
        while (self.leaf_type == False and self.identity == False):
            leaf_type = input('Leaf Type: needle-like or broad and flat?')
            if leaf_type == 'broad and flat':
                self.leaf_type = 'broad and flat'
                self.step_two()
                if (self.identity == False and self.plant_height == '>10 ft.'):
                    self.step_four()
                elif (self.identity == False and self.plant_height == '<10 ft.'):
                    self.step_five()
                    if self.leaf_pattern == 'compound':
                        self.step_six()
                    elif self.leaf_pattern == 'single':
                        self.step_seven()
                        if self.identity == False:
                            self.step_eight()
                            if (self.identity == False and self.plant_structure == 'erect'):
                                self.step_nine()
                                if (self.identity == False and self.hairiness == 'hairless'):
                                    self.step_ten()
            elif leaf_type == 'needle-like':
                self.leaf_type = 'needle-like'
                self.step_two()
                if self.identity == False:
                    self.step_three()
            else:
                print('Please type one of the two options exactly as shown.')

#Actually running the code:

myPlant = Plant()
myPlant.identify_plant()


