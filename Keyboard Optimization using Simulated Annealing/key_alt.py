import qwerty_layout as qwerty

from collections import defaultdict
import math

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Rectangle

import pylab
cm = pylab.get_cmap('seismic')


# Function to get key position

class kdb_analysis():
    def __init__(self,layout):
        self.layout=layout
            
        self.travel=self.key_dist()
        self.freq=defaultdict(int)
        self.key_count=0
        self.count=[]
        self.let_rank=[]
        self.fig = None
        self.ax = None
        

        
    def visualise_kyb(self):
        self.fig,self.ax = plt.subplots(figsize=(13,4))
        # self.ax.pcolormesh(self.maze, cmap=cmap)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.set_xlim(-1,15)
        self.ax.set_ylim(-1,5)
        plt.tight_layout()
        
        for key in layout.keys:
            if self.freq[key]==0:
                color=cm(1.*0)
            else:
                color=cm(1.*((self.let_rank.index(self.freq[key])+1)/len(self.let_rank)))
            key_loc=self.get_key_position(key)
            rect = Rectangle(key_loc, 0.75, 0.75, facecolor=color, alpha=0.9,edgecolor='black')
            self.ax.text(key_loc[0]+0.375,key_loc[1]+0.375,key,horizontalalignment='center',verticalalignment='center')
            self.ax.add_patch(rect)
        plt.show()

    def euc_dist(self,key1,key2):
        return math.sqrt((key2[1]-key1[1])**2+(key2[0]-key1[0])**2)
    
    def get_key_position(self,key):
        return self.layout.keys[key]['pos']
    
    def key_dist(self):
        di={}
        
        for i in layout.keys:
            parent=layout.keys[i]['start']
            di[i]=self.euc_dist(layout.keys[i]['pos'],layout.keys[parent]['pos'])
        
        return di
    
    
    def travel_dist(self,seq):
        trav=0
        self.freq=defaultdict(int)
        special=0
        
        for s in seq:
            for p in layout.characters[s]:
                trav+=self.travel[p]
                self.freq[p]+=1

        self.let_rank=list(set(self.freq.values()))
        self.let_rank.sort()
        print(f"The travel distance was {trav}")
        self.visualise_kyb()
        return trav
            
    
                

if __name__=='__main__':
    layout=qwerty
    s="1234567890-=qwertyuiop[]asdfghjkl;\'\\zxcvbnm,./  "
    q="1234567890-=qwertyuiop[]\\asdfghjkl;\'zxcvbnm,./\\"
    k="~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>?"
    
    '''1In the beginning God created the heaven and the earth.

2And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters.

3And God said, Let there be light and there was light.

4And God saw the light, that it was good  and God divided the light from the darkness.

5And God called the light Day, and the darkness he called Night. And the evening and the morning were the first day.

6And God said, Let there be a firmament in the midst of the waters, and let it divide the waters from the waters.

7And God made the firmament, and divided the waters which were under the firmament from the waters which were above the firmament  and it was so.

8And God called the firmament Heaven. And the evening and the morning were the second day.

9And God said, Let the waters under the heaven be gathered together unto one place, and let the dry land appear  and it was so.

10And God called the dry land Earth; and the gathering together of the waters called he Seas  and God saw that it was good.

11And God said, Let the earth bring forth grass, the herb yielding seed, and the fruit tree yielding fruit after his kind, whose seed is in itself, upon the earth  and it was so.

12And the earth brought forth grass, and herb yielding seed after his kind, and the tree yielding fruit, whose seed was in itself, after his kind  and God saw that it was good.

13And the evening and the morning were the third day.

14And God said, Let there be lights in the firmament of the heaven to divide the day from the night; and let them be for signs, and for seasons, and for days, and years 

15And let them be for lights in the firmament of the heaven to give light upon the earth  and it was so.

16And God made two great lights; the greater light to rule the day, and the lesser light to rule the night  he made the stars also.

17And God set them in the firmament of the heaven to give light upon the earth,

18And to rule over the day and over the night, and to divide the light from the darkness  and God saw that it was good.

19And the evening and the morning were the fourth day.

20And God said, Let the waters bring forth abundantly the moving creature that hath life, and fowl that may fly above the earth in the open firmament of heaven.

21And God created great whales, and every living creature that moveth, which the waters brought forth abundantly, after their kind, and every winged fowl after his kind  and God saw that it was good.

22And God blessed them, saying, Be fruitful, and multiply, and fill the waters in the seas, and let fowl multiply in the earth.

23And the evening and the morning were the fifth day.

24And God said, Let the earth bring forth the living creature after his kind, cattle, and creeping thing, and beast of the earth after his kind  and it was so.

25And God made the beast of the earth after his kind, and cattle after their kind, and every thing that creepeth upon the earth after his kind  and God saw that it was good.

26And God said, Let us make man in our image, after our likeness  and let them have dominion over the fish of the sea, and over the fowl of the air, and over the cattle, and over all the earth, and over every creeping thing that creepeth upon the earth.

27So God created man in his own image, in the image of God created he him; male and female created he them.

28And God blessed them, and God said unto them, Be fruitful, and multiply, and replenish the earth, and subdue it  and have dominion over the fish of the sea, and over the fowl of the air, and over every living thing that moveth upon the earth.

29And God said, Behold, I have given you every herb bearing seed, which is upon the face of all the earth, and every tree, in the which is the fruit of a tree yielding seed; to you it shall be for meat.

30And to every beast of the earth, and to every fowl of the air, and to every thing that creepeth upon the earth, wherein there is life, I have given every green herb for meat  and it was so.

31And God saw every thing that he had made, and, behold, it was very good. And the evening and the morning were the sixth day.'''
    p='Charan Daddy'
    get=kdb_analysis(layout)
    # get.travel_dist(s)
    get.travel_dist(p)                                                                                                                                                                                              
    


    

#https://stackoverflow.com/questions/3016283/create-a-color-generator-from-given-colormap-in-matplotlib

#https://matplotlib.org/stable/users/explain/colors/colormaps.html

#https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html

#https://matplotlib.org/stable/users/explain/text/text_props.html#sphx-glr-users-explain-text-text-props-py

#https://matplotlib.org/stable/users/explain/colors/colormaps.html