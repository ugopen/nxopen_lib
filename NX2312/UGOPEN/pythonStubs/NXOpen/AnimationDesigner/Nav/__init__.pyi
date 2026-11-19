from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Represents a @link NXOpen::AnimationDesigner::Nav::ContainerCollection NXOpen::AnimationDesigner::Nav::ContainerCollection@endlink .  <br> To obtain an instance of this class, refer to @link NXOpen::AnimationDesigner::AnimationDesignerManager  NXOpen::AnimationDesigner::AnimationDesignerManager @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ContainerCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a <ja_class>NXOpen.AnimationDesigner.Nav.ContainerCollection</ja_class>. """


    ##  Finds the @link NXOpen::AnimationDesigner::Nav::Container NXOpen::AnimationDesigner::Nav::Container@endlink  object with the given name. 
    ##  @return folder (@link Container NXOpen.AnimationDesigner.Nav.Container@endlink):  @link NXOpen::AnimationDesigner::Nav::Container NXOpen::AnimationDesigner::Nav::Container@endlink  object with this name. .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ##  The name of the @link  NXOpen::AnimationDesigner::Nav::Container   NXOpen::AnimationDesigner::Nav::Container @endlink . 
    def FindObject(part: NXOpen.Part, name: str) -> Container:
        """
         Finds the @link NXOpen::AnimationDesigner::Nav::Container NXOpen::AnimationDesigner::Nav::Container@endlink  object with the given name. 
         @return folder (@link Container NXOpen.AnimationDesigner.Nav.Container@endlink):  @link NXOpen::AnimationDesigner::Nav::Container NXOpen::AnimationDesigner::Nav::Container@endlink  object with this name. .
        """
        pass
    
import NXOpen
##  Represents a AnimationDesigner Nav Container Class.  <br> Use @link NXOpen::AnimationDesigner::AnimationDesignerManager::Containers NXOpen::AnimationDesigner::AnimationDesignerManager::Containers@endlink  to create  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class Container(NXOpen.NXObject): 
    """ Represents a AnimationDesigner Nav Container Class. """
    pass


import NXOpen
##  Represents a @link NXOpen::AnimationDesigner::Nav::SolutionCollection NXOpen::AnimationDesigner::Nav::SolutionCollection@endlink .  <br> To obtain an instance of this class, refer to @link NXOpen::AnimationDesigner::AnimationDesignerManager  NXOpen::AnimationDesigner::AnimationDesignerManager @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class SolutionCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a <ja_class>NXOpen.AnimationDesigner.Nav.SolutionCollection</ja_class>. """


    ##  Finds the @link NXOpen::AnimationDesigner::Nav::Solution NXOpen::AnimationDesigner::Nav::Solution@endlink  object with the given name. 
    ##  @return study (@link Solution NXOpen.AnimationDesigner.Nav.Solution@endlink):  @link NXOpen::AnimationDesigner::Nav::Solution NXOpen::AnimationDesigner::Nav::Solution@endlink  object with this name. .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ##  The name of the @link  NXOpen::AnimationDesigner::Nav::Solution   NXOpen::AnimationDesigner::Nav::Solution @endlink . 
    def FindObject(part: NXOpen.Part, name: str) -> Solution:
        """
         Finds the @link NXOpen::AnimationDesigner::Nav::Solution NXOpen::AnimationDesigner::Nav::Solution@endlink  object with the given name. 
         @return study (@link Solution NXOpen.AnimationDesigner.Nav.Solution@endlink):  @link NXOpen::AnimationDesigner::Nav::Solution NXOpen::AnimationDesigner::Nav::Solution@endlink  object with this name. .
        """
        pass
    
import NXOpen
##  Represents a AnimationDesigner Nav Solution Class.  <br> Use @link NXOpen::AnimationDesigner::AnimationDesignerManager::Solutions NXOpen::AnimationDesigner::AnimationDesignerManager::Solutions@endlink  to create  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class Solution(NXOpen.NXObject): 
    """ Represents a AnimationDesigner Nav Solution Class. """
    pass


import NXOpen
##  Represents a @link NXOpen::AnimationDesigner::Nav::SubFolderCollection NXOpen::AnimationDesigner::Nav::SubFolderCollection@endlink .  <br> To obtain an instance of this class, refer to @link NXOpen::AnimationDesigner::AnimationDesignerManager  NXOpen::AnimationDesigner::AnimationDesignerManager @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class SubFolderCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a <ja_class>NXOpen.AnimationDesigner.Nav.SubFolderCollection</ja_class>. """


    ##  Finds the @link NXOpen::AnimationDesigner::Nav::SubFolder NXOpen::AnimationDesigner::Nav::SubFolder@endlink  object with the given name. 
    ##  @return folder (@link SubFolder NXOpen.AnimationDesigner.Nav.SubFolder@endlink):  @link NXOpen::AnimationDesigner::Nav::SubFolder NXOpen::AnimationDesigner::Nav::SubFolder@endlink  object with this name. .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ##  The name of the @link  NXOpen::AnimationDesigner::Nav::SubFolder   NXOpen::AnimationDesigner::Nav::SubFolder @endlink . 
    def FindObject(part: NXOpen.Part, name: str) -> SubFolder:
        """
         Finds the @link NXOpen::AnimationDesigner::Nav::SubFolder NXOpen::AnimationDesigner::Nav::SubFolder@endlink  object with the given name. 
         @return folder (@link SubFolder NXOpen.AnimationDesigner.Nav.SubFolder@endlink):  @link NXOpen::AnimationDesigner::Nav::SubFolder NXOpen::AnimationDesigner::Nav::SubFolder@endlink  object with this name. .
        """
        pass
    
import NXOpen
##  Represents a AnimationDesigner Nav SubFolder Class.  <br> Use @link NXOpen::AnimationDesigner::AnimationDesignerManager::SubFolders NXOpen::AnimationDesigner::AnimationDesignerManager::SubFolders@endlink  to create  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class SubFolder(NXOpen.NXObject): 
    """ Represents a AnimationDesigner Nav SubFolder Class. """
    pass


## @package NXOpen.AnimationDesigner.Nav
## Classes, Enums and Structs under NXOpen.AnimationDesigner.Nav namespace

