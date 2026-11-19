from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class ContainerCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a NXOpen.AnimationDesigner.Nav.ContainerCollection. """
    def FindObject(part: NXOpen.Part, name: str) -> Container:
        """
         Finds the NXOpen.AnimationDesigner.Nav.Container object with the given name. 
         Returns folder ( Container NXOpen.Animat):  NXOpen.AnimationDesigner.Nav.Container object with this name. .
        """
        pass
import NXOpen
class Container(NXOpen.NXObject): 
    """ Represents a AnimationDesigner Nav Container Class. """
    pass
import NXOpen
class SolutionCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a NXOpen.AnimationDesigner.Nav.SolutionCollection. """
    def FindObject(part: NXOpen.Part, name: str) -> Solution:
        """
         Finds the NXOpen.AnimationDesigner.Nav.Solution object with the given name. 
         Returns study ( Solution NXOpen.Animat):  NXOpen.AnimationDesigner.Nav.Solution object with this name. .
        """
        pass
import NXOpen
class Solution(NXOpen.NXObject): 
    """ Represents a AnimationDesigner Nav Solution Class. """
    pass
import NXOpen
class SubFolderCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a NXOpen.AnimationDesigner.Nav.SubFolderCollection. """
    def FindObject(part: NXOpen.Part, name: str) -> SubFolder:
        """
         Finds the NXOpen.AnimationDesigner.Nav.SubFolder object with the given name. 
         Returns folder ( SubFolder NXOpen.Animat):  NXOpen.AnimationDesigner.Nav.SubFolder object with this name. .
        """
        pass
import NXOpen
class SubFolder(NXOpen.NXObject): 
    """ Represents a AnimationDesigner Nav SubFolder Class. """
    pass
