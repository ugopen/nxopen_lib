from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
##  Component active set members scope 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## NoMembers</term><description> 
## </description> </item><item><term> 
## SelectMembers</term><description> 
## </description> </item><item><term> 
## AllMembers</term><description> 
## </description> </item></list>
class ActiveSetScope(Enum):
    """
    Members Include: <NoMembers> <SelectMembers> <AllMembers>
    """
    NoMembers: int
    SelectMembers: int
    AllMembers: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> ActiveSetScope:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
import NXOpen.GeometricUtilities
## 
##      Represents a @link NXOpen::Layout2d::AssemblyCreationSettingsBuilder NXOpen::Layout2d::AssemblyCreationSettingsBuilder@endlink 
##     
## 
##   <br>  Created in NX10.0.0  <br> 

class AssemblyCreationSettingsBuilder(NXOpen.TaggedObject): 
    """
     Represents a <ja_class>NXOpen.Layout2d.AssemblyCreationSettingsBuilder</ja_class>
    """


    ## Getter for property: (bool) AutomaticallyStartModelingApplication
    ##  Returns  the settings todetermines whether or not automatically start modeling application  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def AutomaticallyStartModelingApplication(self) -> bool:
        """
        Getter for property: (bool) AutomaticallyStartModelingApplication
         Returns  the settings todetermines whether or not automatically start modeling application  
            
         
        """
        pass
    
    ## Setter for property: (bool) AutomaticallyStartModelingApplication

    ##  Returns  the settings todetermines whether or not automatically start modeling application  
    ##     
    ##  
    ## Setter License requirements: drafting ("DRAFTING")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @AutomaticallyStartModelingApplication.setter
    def AutomaticallyStartModelingApplication(self, automaticallyStartModelingApplication: bool):
        """
        Setter for property: (bool) AutomaticallyStartModelingApplication
         Returns  the settings todetermines whether or not automatically start modeling application  
            
         
        """
        pass
    
    ## Getter for property: (bool) Transfer2dComponentAnnotation
    ##  Returns the settings to determines whether or not transfer 2d component annotation  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def Transfer2dComponentAnnotation(self) -> bool:
        """
        Getter for property: (bool) Transfer2dComponentAnnotation
         Returns the settings to determines whether or not transfer 2d component annotation  
            
         
        """
        pass
    
    ## Setter for property: (bool) Transfer2dComponentAnnotation

    ##  Returns the settings to determines whether or not transfer 2d component annotation  
    ##     
    ##  
    ## Setter License requirements: drafting ("DRAFTING")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Transfer2dComponentAnnotation.setter
    def Transfer2dComponentAnnotation(self, transfer2dComponentAnnotation: bool):
        """
        Setter for property: (bool) Transfer2dComponentAnnotation
         Returns the settings to determines whether or not transfer 2d component annotation  
            
         
        """
        pass
    
    ## Getter for property: (bool) TransferTopLevelSketchAnnotation
    ##  Returns the settings to determines whether or not transfer top level sketch annotation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def TransferTopLevelSketchAnnotation(self) -> bool:
        """
        Getter for property: (bool) TransferTopLevelSketchAnnotation
         Returns the settings to determines whether or not transfer top level sketch annotation   
            
         
        """
        pass
    
    ## Setter for property: (bool) TransferTopLevelSketchAnnotation

    ##  Returns the settings to determines whether or not transfer top level sketch annotation   
    ##     
    ##  
    ## Setter License requirements: drafting ("DRAFTING")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @TransferTopLevelSketchAnnotation.setter
    def TransferTopLevelSketchAnnotation(self, transferTopLevelSketchAnnotation: bool):
        """
        Setter for property: (bool) TransferTopLevelSketchAnnotation
         Returns the settings to determines whether or not transfer top level sketch annotation   
            
         
        """
        pass
    
    ##  Inherit Settings From Customer Default 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: drafting ("DRAFTING")
    def InheritSettingsFromCustomerDefault(self) -> None:
        """
         Inherit Settings From Customer Default 
        """
        pass
    
    ##  Inherit Settings From Preference 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: drafting ("DRAFTING")
    def InheritSettingsFromPreferences(self) -> None:
        """
         Inherit Settings From Preference 
        """
        pass
    
import NXOpen
##  Represents a Builder for create assembly from Layout functionality which will create a
##      *  new assembly from the selected Layout  <br> To create a new instance of this class, use @link NXOpen::Layout2d::ComponentCollection::CreateAssemblyFromLayout2dBuilder  NXOpen::Layout2d::ComponentCollection::CreateAssemblyFromLayout2dBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class AssemblyFromLayout2dBuilder(NXOpen.Builder): 
    """ Represents a Builder for create assembly from Layout functionality which will create a
     *  new assembly from the selected Layout """


    ## Getter for property: (@link NXOpen.Part NXOpen.Part@endlink) AssemblyPart
    ##  Returns the destination part for the Layout assembly   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.Part
    @property
    def AssemblyPart(self) -> NXOpen.Part:
        """
        Getter for property: (@link NXOpen.Part NXOpen.Part@endlink) AssemblyPart
         Returns the destination part for the Layout assembly   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Part NXOpen.Part@endlink) AssemblyPart

    ##  Returns the destination part for the Layout assembly   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @AssemblyPart.setter
    def AssemblyPart(self, assemblyPart: NXOpen.Part):
        """
        Setter for property: (@link NXOpen.Part NXOpen.Part@endlink) AssemblyPart
         Returns the destination part for the Layout assembly   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) Layout2dObject
    ##  Returns the select Layout object to create assembly   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObject
    @property
    def Layout2dObject(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) Layout2dObject
         Returns the select Layout object to create assembly   
            
         
        """
        pass
    
    ## Getter for property: (@link AssemblyCreationSettingsBuilder NXOpen.Layout2d.AssemblyCreationSettingsBuilder@endlink) Settings
    ##  Returns the settings of the assembly creation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return AssemblyCreationSettingsBuilder
    @property
    def Settings(self) -> AssemblyCreationSettingsBuilder:
        """
        Getter for property: (@link AssemblyCreationSettingsBuilder NXOpen.Layout2d.AssemblyCreationSettingsBuilder@endlink) Settings
         Returns the settings of the assembly creation   
            
         
        """
        pass
    
import NXOpen
##  Represents Assembly::Relation object <br> Instances of this class can be accessed through AssociativeAssemblyBuilder  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class AssemblyRelation(NXOpen.NXObject): 
    """ Represents Assembly::Relation object"""


    ## Getter for property: (bool) Associative
    ##  Returns a flag indicating associativity state   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
         Returns a flag indicating associativity state   
            
         
        """
        pass
    
    ## Setter for property: (bool) Associative

    ##  Returns a flag indicating associativity state   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Associative.setter
    def Associative(self, associative: bool):
        """
        Setter for property: (bool) Associative
         Returns a flag indicating associativity state   
            
         
        """
        pass
    
    ## Getter for property: (str) PrototypeFileSpec
    ##  Returns the prototype file spec   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def PrototypeFileSpec(self) -> str:
        """
        Getter for property: (str) PrototypeFileSpec
         Returns the prototype file spec   
            
         
        """
        pass
    
    ## Setter for property: (str) PrototypeFileSpec

    ##  Returns the prototype file spec   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @PrototypeFileSpec.setter
    def PrototypeFileSpec(self, fileSpec: str):
        """
        Setter for property: (str) PrototypeFileSpec
         Returns the prototype file spec   
            
         
        """
        pass
    
    ## Getter for property: (bool) SyncContent
    ##  Returns a flag indicating whether the prototype content will be syncronized   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def SyncContent(self) -> bool:
        """
        Getter for property: (bool) SyncContent
         Returns a flag indicating whether the prototype content will be syncronized   
            
         
        """
        pass
    
    ## Setter for property: (bool) SyncContent

    ##  Returns a flag indicating whether the prototype content will be syncronized   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @SyncContent.setter
    def SyncContent(self, syncContent: bool):
        """
        Setter for property: (bool) SyncContent
         Returns a flag indicating whether the prototype content will be syncronized   
            
         
        """
        pass
    
    ## Getter for property: (bool) SyncStructure
    ##  Returns a flag indicating whether the prototype structure will be syncronized   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def SyncStructure(self) -> bool:
        """
        Getter for property: (bool) SyncStructure
         Returns a flag indicating whether the prototype structure will be syncronized   
            
         
        """
        pass
    
    ## Setter for property: (bool) SyncStructure

    ##  Returns a flag indicating whether the prototype structure will be syncronized   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @SyncStructure.setter
    def SyncStructure(self, syncStructure: bool):
        """
        Setter for property: (bool) SyncStructure
         Returns a flag indicating whether the prototype structure will be syncronized   
            
         
        """
        pass
    
    ##  Returns the flag indicating whether the prototype is inferred from 2D component 
    ##  @return inferred (bool): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def GetPrototypeInferred(self) -> bool:
        """
         Returns the flag indicating whether the prototype is inferred from 2D component 
         @return inferred (bool): .
        """
        pass
    
import NXOpen
##  Represents a Builder for Layout associative assembly  <br> To create a new instance of this class, use @link NXOpen::Layout2d::ComponentCollection::CreateAssociativeAssemblyBuilder  NXOpen::Layout2d::ComponentCollection::CreateAssociativeAssemblyBuilder @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class AssociativeAssemblyBuilder(NXOpen.Builder): 
    """ Represents a Builder for Layout associative assembly """


    ##  the update direction 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## LayoutToAssembly</term><description> 
    ##  Update 3D model from 2D </description> </item><item><term> 
    ## AssemblyToLayout</term><description> 
    ##  Update 2D model from 3D </description> </item></list>
    class UpdateDirection(Enum):
        """
        Members Include: <LayoutToAssembly> <AssemblyToLayout>
        """
        LayoutToAssembly: int
        AssemblyToLayout: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AssociativeAssemblyBuilder.UpdateDirection:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link AssociativeAssemblyBuilder.UpdateDirection NXOpen.Layout2d.AssociativeAssemblyBuilder.UpdateDirection@endlink) Direction
    ##  Returns the update direction   
    ##     
    ##  
    ## Getter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return AssociativeAssemblyBuilder.UpdateDirection
    @property
    def Direction(self) -> AssociativeAssemblyBuilder.UpdateDirection:
        """
        Getter for property: (@link AssociativeAssemblyBuilder.UpdateDirection NXOpen.Layout2d.AssociativeAssemblyBuilder.UpdateDirection@endlink) Direction
         Returns the update direction   
            
         
        """
        pass
    
    ## Setter for property: (@link AssociativeAssemblyBuilder.UpdateDirection NXOpen.Layout2d.AssociativeAssemblyBuilder.UpdateDirection@endlink) Direction

    ##  Returns the update direction   
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Direction.setter
    def Direction(self, direction: AssociativeAssemblyBuilder.UpdateDirection):
        """
        Setter for property: (@link AssociativeAssemblyBuilder.UpdateDirection NXOpen.Layout2d.AssociativeAssemblyBuilder.UpdateDirection@endlink) Direction
         Returns the update direction   
            
         
        """
        pass
    
    ##  Gets the assembly relations 
    ##  @return relations (@link AssemblyRelation List[NXOpen.Layout2d.AssemblyRelation]@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def GetAssemblyRelations(self) -> List[AssemblyRelation]:
        """
         Gets the assembly relations 
         @return relations (@link AssemblyRelation List[NXOpen.Layout2d.AssemblyRelation]@endlink): .
        """
        pass
    
    ##  Resets the assembly relations to initial state 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def ResetAssemblyRelations(self) -> None:
        """
         Resets the assembly relations to initial state 
        """
        pass
    
import NXOpen
##  Represents a Builder to edit 2D component active members set.  <br> To create a new instance of this class, use @link NXOpen::Layout2d::ComponentCollection::CreateComponentActiveSetBuilder  NXOpen::Layout2d::ComponentCollection::CreateComponentActiveSetBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class ComponentActiveSetBuilder(NXOpen.Builder): 
    """ Represents a Builder to edit 2D component active members set. """


    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) ActiveSet
    ##  Returns the select members of active set   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def ActiveSet(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) ActiveSet
         Returns the select members of active set   
            
         
        """
        pass
    
    ## Getter for property: (@link ActiveSetScope NXOpen.Layout2d.ActiveSetScope@endlink) ActiveSetScope
    ##  Returns the active members scope   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return ActiveSetScope
    @property
    def ActiveSetScope(self) -> ActiveSetScope:
        """
        Getter for property: (@link ActiveSetScope NXOpen.Layout2d.ActiveSetScope@endlink) ActiveSetScope
         Returns the active members scope   
            
         
        """
        pass
    
    ## Setter for property: (@link ActiveSetScope NXOpen.Layout2d.ActiveSetScope@endlink) ActiveSetScope

    ##  Returns the active members scope   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ActiveSetScope.setter
    def ActiveSetScope(self, scope: ActiveSetScope):
        """
        Setter for property: (@link ActiveSetScope NXOpen.Layout2d.ActiveSetScope@endlink) ActiveSetScope
         Returns the active members scope   
            
         
        """
        pass
    
    ##  Verifies whether specified object can be an active member 
    ##  @return isValid (bool): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objectTag"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink) </param>
    def IsValidActiveSetMember(self, objectTag: NXOpen.DisplayableObject) -> bool:
        """
         Verifies whether specified object can be an active member 
         @return isValid (bool): .
        """
        pass
    
import NXOpen
##  Represents a collection of @link NXOpen::Layout2d::Component NXOpen::Layout2d::Component@endlink s.    <br> To obtain an instance of this class, refer to @link NXOpen::Part  NXOpen::Part @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class ComponentCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of <ja_class>NXOpen.Layout2d.Component</ja_class>s.   """


    ##  Returns the OrderManager for part 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @link OrderManager NXOpen.Drawings.OrderManager@endlink
    @property
    def OrderManagers() -> OrderManager:
        """
         Returns the OrderManager for part 
        """
        pass
    
    ##  Creates a @link NXOpen::Layout2d::AssemblyFromLayout2dBuilder NXOpen::Layout2d::AssemblyFromLayout2dBuilder@endlink  that can create assembly from  
    ##          *  the selected layout
    ##         
    ##  @return builder (@link AssemblyFromLayout2dBuilder NXOpen.Layout2d.AssemblyFromLayout2dBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def CreateAssemblyFromLayout2dBuilder(self) -> AssemblyFromLayout2dBuilder:
        """
         Creates a @link NXOpen::Layout2d::AssemblyFromLayout2dBuilder NXOpen::Layout2d::AssemblyFromLayout2dBuilder@endlink  that can create assembly from  
                 *  the selected layout
                
         @return builder (@link AssemblyFromLayout2dBuilder NXOpen.Layout2d.AssemblyFromLayout2dBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Layout2d::AssociativeAssemblyBuilder NXOpen::Layout2d::AssociativeAssemblyBuilder@endlink  
    ##  @return builder (@link AssociativeAssemblyBuilder NXOpen.Layout2d.AssociativeAssemblyBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def CreateAssociativeAssemblyBuilder(self) -> AssociativeAssemblyBuilder:
        """
         Creates a @link NXOpen::Layout2d::AssociativeAssemblyBuilder NXOpen::Layout2d::AssociativeAssemblyBuilder@endlink  
         @return builder (@link AssociativeAssemblyBuilder NXOpen.Layout2d.AssociativeAssemblyBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Layout2d::ComponentActiveSetBuilder NXOpen::Layout2d::ComponentActiveSetBuilder@endlink  
    ##  @return builder (@link ComponentActiveSetBuilder NXOpen.Layout2d.ComponentActiveSetBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def CreateComponentActiveSetBuilder(self) -> ComponentActiveSetBuilder:
        """
         Creates a @link NXOpen::Layout2d::ComponentActiveSetBuilder NXOpen::Layout2d::ComponentActiveSetBuilder@endlink  
         @return builder (@link ComponentActiveSetBuilder NXOpen.Layout2d.ComponentActiveSetBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Layout2d::CreateComponentFrom3DBuilder NXOpen::Layout2d::CreateComponentFrom3DBuilder@endlink  that can create assembly from
    ##          *  the selected layout
    ##         
    ##  @return builder (@link CreateComponentFrom3DBuilder NXOpen.Layout2d.CreateComponentFrom3DBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ## 
    ## <param name="myView"> (@link NXOpen.View NXOpen.View@endlink) </param>
    def CreateComponentFrom3dBuilder(self, myView: NXOpen.View) -> CreateComponentFrom3DBuilder:
        """
         Creates a @link NXOpen::Layout2d::CreateComponentFrom3DBuilder NXOpen::Layout2d::CreateComponentFrom3DBuilder@endlink  that can create assembly from
                 *  the selected layout
                
         @return builder (@link CreateComponentFrom3DBuilder NXOpen.Layout2d.CreateComponentFrom3DBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Layout2d::DefineComponentAnchorPointBuilder NXOpen::Layout2d::DefineComponentAnchorPointBuilder@endlink  that can define the Anchor Point location of a
    ##          *  2D Component
    ##         
    ##  @return builder (@link DefineComponentAnchorPointBuilder NXOpen.Layout2d.DefineComponentAnchorPointBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def CreateDefineComponentAnchorPointBuilder(self) -> DefineComponentAnchorPointBuilder:
        """
         Creates a @link NXOpen::Layout2d::DefineComponentAnchorPointBuilder NXOpen::Layout2d::DefineComponentAnchorPointBuilder@endlink  that can define the Anchor Point location of a
                 *  2D Component
                
         @return builder (@link DefineComponentAnchorPointBuilder NXOpen.Layout2d.DefineComponentAnchorPointBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Layout2d::DefineComponentBuilder NXOpen::Layout2d::DefineComponentBuilder@endlink  that can create a fully defined 2D 
    ##             Component with specified content, anchor point, name and reuse library destination folder.
    ##         
    ##  @return builder (@link DefineComponentBuilder NXOpen.Layout2d.DefineComponentBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ## 
    ## <param name="component"> (@link Component NXOpen.Layout2d.Component@endlink)  Reserved for future use.  Use NULL. </param>
    def CreateDefineComponentBuilder(self, component: Component) -> DefineComponentBuilder:
        """
         Creates a @link NXOpen::Layout2d::DefineComponentBuilder NXOpen::Layout2d::DefineComponentBuilder@endlink  that can create a fully defined 2D 
                    Component with specified content, anchor point, name and reuse library destination folder.
                
         @return builder (@link DefineComponentBuilder NXOpen.Layout2d.DefineComponentBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Layout2d::ExportComponentHierarchyBuilder NXOpen::Layout2d::ExportComponentHierarchyBuilder@endlink  
    ##  @return builder (@link ExportComponentHierarchyBuilder NXOpen.Layout2d.ExportComponentHierarchyBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def CreateExportComponentHierarchyBuilder(self) -> ExportComponentHierarchyBuilder:
        """
         Creates a @link NXOpen::Layout2d::ExportComponentHierarchyBuilder NXOpen::Layout2d::ExportComponentHierarchyBuilder@endlink  
         @return builder (@link ExportComponentHierarchyBuilder NXOpen.Layout2d.ExportComponentHierarchyBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Layout2d::InheritDisplayAttributesBuilder NXOpen::Layout2d::InheritDisplayAttributesBuilder@endlink  
    ##  @return builder (@link InheritDisplayAttributesBuilder NXOpen.Layout2d.InheritDisplayAttributesBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def CreateInheritDisplayAttributesBuilder(self) -> InheritDisplayAttributesBuilder:
        """
         Creates a @link NXOpen::Layout2d::InheritDisplayAttributesBuilder NXOpen::Layout2d::InheritDisplayAttributesBuilder@endlink  
         @return builder (@link InheritDisplayAttributesBuilder NXOpen.Layout2d.InheritDisplayAttributesBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Layout2d::InsertComponentBuilder NXOpen::Layout2d::InsertComponentBuilder@endlink  that inserts a 2D Component instance in the active
    ##          *  sketch.
    ##         
    ##  @return builder (@link InsertComponentBuilder NXOpen.Layout2d.InsertComponentBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def CreateInsertComponentBuilder(self) -> InsertComponentBuilder:
        """
         Creates a @link NXOpen::Layout2d::InsertComponentBuilder NXOpen::Layout2d::InsertComponentBuilder@endlink  that inserts a 2D Component instance in the active
                 *  sketch.
                
         @return builder (@link InsertComponentBuilder NXOpen.Layout2d.InsertComponentBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Layout2d::MakeComponentUniqueBuilder NXOpen::Layout2d::MakeComponentUniqueBuilder@endlink  that can create definition
    ##          *  for the selected 2D Component instance
    ##         
    ##  @return builder (@link MakeComponentUniqueBuilder NXOpen.Layout2d.MakeComponentUniqueBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def CreateMakeComponentUniqueBuilder(self) -> MakeComponentUniqueBuilder:
        """
         Creates a @link NXOpen::Layout2d::MakeComponentUniqueBuilder NXOpen::Layout2d::MakeComponentUniqueBuilder@endlink  that can create definition
                 *  for the selected 2D Component instance
                
         @return builder (@link MakeComponentUniqueBuilder NXOpen.Layout2d.MakeComponentUniqueBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Layout2d::NewComponentBuilder NXOpen::Layout2d::NewComponentBuilder@endlink  that creates an empty 2D Component instance and stores its
    ##          *  definition in local 2D Component folder
    ##         
    ##  @return builder (@link NewComponentBuilder NXOpen.Layout2d.NewComponentBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def CreateNewComponentBuilder(self) -> NewComponentBuilder:
        """
         Creates a @link NXOpen::Layout2d::NewComponentBuilder NXOpen::Layout2d::NewComponentBuilder@endlink  that creates an empty 2D Component instance and stores its
                 *  definition in local 2D Component folder
                
         @return builder (@link NewComponentBuilder NXOpen.Layout2d.NewComponentBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Layout2d::PublishComponentBuilder NXOpen::Layout2d::PublishComponentBuilder@endlink  that can export local definitions into external storage locations
    ##         
    ##  @return builder (@link PublishComponentBuilder NXOpen.Layout2d.PublishComponentBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def CreatePublishComponentBuilder(self) -> PublishComponentBuilder:
        """
         Creates a @link NXOpen::Layout2d::PublishComponentBuilder NXOpen::Layout2d::PublishComponentBuilder@endlink  that can export local definitions into external storage locations
                
         @return builder (@link PublishComponentBuilder NXOpen.Layout2d.PublishComponentBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Layout2d::ReplaceComponentBuilder NXOpen::Layout2d::ReplaceComponentBuilder@endlink  that can reparent the selected 2D Component
    ##          *  instance with another 2D Component or sketch 
    ##  @return builder (@link ReparentComponentBuilder NXOpen.Layout2d.ReparentComponentBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def CreateReparentComponentBuilder(self) -> ReparentComponentBuilder:
        """
         Creates a @link NXOpen::Layout2d::ReplaceComponentBuilder NXOpen::Layout2d::ReplaceComponentBuilder@endlink  that can reparent the selected 2D Component
                 *  instance with another 2D Component or sketch 
         @return builder (@link ReparentComponentBuilder NXOpen.Layout2d.ReparentComponentBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Layout2d::ReplaceComponentBuilder NXOpen::Layout2d::ReplaceComponentBuilder@endlink  that can replace the selected 2D Component
    ##          *   instance with another 2D Component definition
    ##         
    ##  @return builder (@link ReplaceComponentBuilder NXOpen.Layout2d.ReplaceComponentBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def CreateReplaceComponentBuilder(self) -> ReplaceComponentBuilder:
        """
         Creates a @link NXOpen::Layout2d::ReplaceComponentBuilder NXOpen::Layout2d::ReplaceComponentBuilder@endlink  that can replace the selected 2D Component
                 *   instance with another 2D Component definition
                
         @return builder (@link ReplaceComponentBuilder NXOpen.Layout2d.ReplaceComponentBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Layout2d::SmashComponentBuilder NXOpen::Layout2d::SmashComponentBuilder@endlink  that can smash the selected 
    ##          *  2D Component instance
    ##         
    ##  @return builder (@link SmashComponentBuilder NXOpen.Layout2d.SmashComponentBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def CreateSmashComponentBuilder(self) -> SmashComponentBuilder:
        """
         Creates a @link NXOpen::Layout2d::SmashComponentBuilder NXOpen::Layout2d::SmashComponentBuilder@endlink  that can smash the selected 
                 *  2D Component instance
                
         @return builder (@link SmashComponentBuilder NXOpen.Layout2d.SmashComponentBuilder@endlink): .
        """
        pass
    
    ##  Deletes a list of 2D Components
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ## 
    ## <param name="components"> (@link Component List[NXOpen.Layout2d.Component]@endlink) </param>
    def DeleteComponents(self, components: List[Component]) -> None:
        """
         Deletes a list of 2D Components
        """
        pass
    
    ##  Finds the @link  NXOpen::Layout2d::Component   NXOpen::Layout2d::Component @endlink  with the given identifier as recorded in a journal.
    ##         An object may not return the same value as its JournalIdentifier in different versions of
    ##         the software. However newer versions of the software should find the same object when
    ##         FindObject is passed older versions of its journal identifier. In general, this method
    ##         should not be used in handwritten code and exists to support record and playback of journals.
    ##         An exception will be thrown if no object can be found with the given journal identifier. 
    ##  @return found (@link Component NXOpen.Layout2d.Component@endlink):  2D Component with this identifier .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="journal_identifier"> (str)  Identifier of the 2D Component to be found </param>
    def FindObject(self, journal_identifier: str) -> Component:
        """
         Finds the @link  NXOpen::Layout2d::Component   NXOpen::Layout2d::Component @endlink  with the given identifier as recorded in a journal.
                An object may not return the same value as its JournalIdentifier in different versions of
                the software. However newer versions of the software should find the same object when
                FindObject is passed older versions of its journal identifier. In general, this method
                should not be used in handwritten code and exists to support record and playback of journals.
                An exception will be thrown if no object can be found with the given journal identifier. 
         @return found (@link Component NXOpen.Layout2d.Component@endlink):  2D Component with this identifier .
        """
        pass
    
    ##  Verify if the object belong to this component 
    ##  @return isMember (bool):  true if the object is component member .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ## 
    ## <param name="disObject"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink) </param>
    def IsComponentMember(self, disObject: NXOpen.DisplayableObject) -> bool:
        """
         Verify if the object belong to this component 
         @return isMember (bool):  true if the object is component member .
        """
        pass
    
    ##  Updates 2D Components and propagates the changes to the hierarchy in given layout 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ## 
    ## <param name="components"> (@link Component List[NXOpen.Layout2d.Component]@endlink) </param>
    def UpdateComponentHierarchy(self, components: List[Component]) -> None:
        """
         Updates 2D Components and propagates the changes to the hierarchy in given layout 
        """
        pass
    
    ##  Updates 2D Components without propagating the changes to the hierarchy in given layout 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ## 
    ## <param name="components"> (@link Component List[NXOpen.Layout2d.Component]@endlink) </param>
    def UpdateComponents(self, components: List[Component]) -> None:
        """
         Updates 2D Components without propagating the changes to the hierarchy in given layout 
        """
        pass
    
import NXOpen
##  Represents a collection of @link NXOpen::Layout2d::ComponentDefinition NXOpen::Layout2d::ComponentDefinition@endlink  objects. <br> To obtain an instance of this class, refer to @link NXOpen::Part  NXOpen::Part @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class ComponentDefinitionCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of <ja_class>NXOpen.Layout2d.ComponentDefinition</ja_class> objects."""


    ##  Deletes definition
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ## 
    ## <param name="location"> (@link Layout2dDefinitionLocation NXOpen.Layout2d.Layout2dDefinitionLocation@endlink)  Location of the definition to delete </param>
    ## <param name="definitionPath"> (str)  Path of the definition to delete </param>
    def Delete(self, location: Layout2dDefinitionLocation, definitionPath: str) -> None:
        """
         Deletes definition
        """
        pass
    
    ##   Finds the @link  NXOpen::Layout2d::ComponentDefinition   NXOpen::Layout2d::ComponentDefinition @endlink  with the given sid. 
    ##              An exception will be thrown if no object can be found with the given sid. 
    ##              This method can only be used to find Local definitions 
    ##  @return folder (@link ComponentDefinition NXOpen.Layout2d.ComponentDefinition@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ## 
    ## <param name="sid"> (str)  The sid of the definition to find </param>
    def FindObject(self, sid: str) -> ComponentDefinition:
        """
          Finds the @link  NXOpen::Layout2d::ComponentDefinition   NXOpen::Layout2d::ComponentDefinition @endlink  with the given sid. 
                     An exception will be thrown if no object can be found with the given sid. 
                     This method can only be used to find Local definitions 
         @return folder (@link ComponentDefinition NXOpen.Layout2d.ComponentDefinition@endlink): .
        """
        pass
    
    ##   Refreshes all definition references in part to obtain the actual out-of-date status of components 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def RefreshAllReferences(self) -> None:
        """
          Refreshes all definition references in part to obtain the actual out-of-date status of components 
        """
        pass
    
    ##  Renames definition
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ## 
    ## <param name="location"> (@link Layout2dDefinitionLocation NXOpen.Layout2d.Layout2dDefinitionLocation@endlink)  Location of the definition to rename </param>
    ## <param name="definitionPath"> (str)  Path of the definition to rename </param>
    ## <param name="newName"> (str)  New definition name </param>
    def Rename(self, location: Layout2dDefinitionLocation, definitionPath: str, newName: str) -> None:
        """
         Renames definition
        """
        pass
    
    ##   Sets the automatic preview mode of definition with the given path 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ## 
    ## <param name="location"> (@link Layout2dDefinitionLocation NXOpen.Layout2d.Layout2dDefinitionLocation@endlink)  Location of the definition to set the preview mode </param>
    ## <param name="definitionPath"> (str)  Path of the definition to set the preview mode </param>
    ## <param name="isAutomatic"> (bool) </param>
    def SetAutomaticPreview(self, location: Layout2dDefinitionLocation, definitionPath: str, isAutomatic: bool) -> None:
        """
          Sets the automatic preview mode of definition with the given path 
        """
        pass
    
    ##   Updates definition with the given path 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ## 
    ## <param name="location"> (@link Layout2dDefinitionLocation NXOpen.Layout2d.Layout2dDefinitionLocation@endlink)  Location of the definition to update </param>
    ## <param name="definitionPath"> (str)  Path of the definition to update </param>
    def Update(self, location: Layout2dDefinitionLocation, definitionPath: str) -> None:
        """
          Updates definition with the given path 
        """
        pass
    
    ##  Updates definition preview 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ## 
    ## <param name="location"> (@link Layout2dDefinitionLocation NXOpen.Layout2d.Layout2dDefinitionLocation@endlink)  Location of the definition to update image </param>
    ## <param name="definitionPath"> (str)  Path of the definition to update image </param>
    ## <param name="imagePath"> (str)  Path of the image file used to update definition preview </param>
    def UpdateImage(self, location: Layout2dDefinitionLocation, definitionPath: str, imagePath: str) -> None:
        """
         Updates definition preview 
        """
        pass
    
import NXOpen
##  Represents a component definition. The definition contains sketch curves, sketch dimensions
##         and drafting annotations representing a two dimensional reusable sketch component. <br>   <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class ComponentDefinition(NXOpen.NXObject): 
    """ Represents a component definition. The definition contains sketch curves, sketch dimensions
        and drafting annotations representing a two dimensional reusable sketch component."""


    ##  Deletes definition
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ## 
    ## <param name="definitionPath"> (str)  Path of the definition to delete </param>
    def Delete(self, definitionPath: str) -> None:
        """
         Deletes definition
        """
        pass
    
    ##  Returns an array of specified members in this component definition
    ##  @return members (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ## 
    ## <param name="memberType"> (@link Layout2dComponentMemberType NXOpen.Layout2d.Layout2dComponentMemberType@endlink) </param>
    def GetMembers(self, memberType: Layout2dComponentMemberType) -> List[NXOpen.DisplayableObject]:
        """
         Returns an array of specified members in this component definition
         @return members (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink): .
        """
        pass
    
    ##  Renames definition
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ## 
    ## <param name="definitionPath"> (str)  Path of the definition to rename </param>
    ## <param name="newName"> (str)  New definition name </param>
    def Rename(self, definitionPath: str, newName: str) -> None:
        """
         Renames definition
        """
        pass
    
    ##  Updates definition preview 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ## 
    ## <param name="definitionPath"> (str)  Path of the definition to rename </param>
    ## <param name="imagePath"> (str)  Path of the image file used to update definition preview </param>
    def UpdateImage(self, definitionPath: str, imagePath: str) -> None:
        """
         Updates definition preview 
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
import NXOpen.PDM
##  This class is used to construct the component name and part file name block, if it is in
##         manage mode, we also have item number, item revision and item name . 
## 
##   <br>  Created in NX10.0.0  <br> 

class ComponentNameBuilder(NXOpen.TaggedObject): 
    """ This class is used to construct the component name and part file name block, if it is in
        manage mode, we also have item number, item revision and item name . """


    ## Getter for property: (@link Layout2dDefinitionLocation NXOpen.Layout2d.Layout2dDefinitionLocation@endlink) Location
    ##  Returns the location type of the component indicating local, native or team center    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return Layout2dDefinitionLocation
    @property
    def Location(self) -> Layout2dDefinitionLocation:
        """
        Getter for property: (@link Layout2dDefinitionLocation NXOpen.Layout2d.Layout2dDefinitionLocation@endlink) Location
         Returns the location type of the component indicating local, native or team center    
            
         
        """
        pass
    
    ## Setter for property: (@link Layout2dDefinitionLocation NXOpen.Layout2d.Layout2dDefinitionLocation@endlink) Location

    ##  Returns the location type of the component indicating local, native or team center    
    ##     
    ##  
    ## Setter License requirements: drafting ("DRAFTING")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Location.setter
    def Location(self, location: Layout2dDefinitionLocation):
        """
        Setter for property: (@link Layout2dDefinitionLocation NXOpen.Layout2d.Layout2dDefinitionLocation@endlink) Location
         Returns the location type of the component indicating local, native or team center    
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the JA method support for accessing and setting Component Name value,
    ##             NOTE: Client must free the returned TEXT_p_t* with TEXT_free
    ##            
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the JA method support for accessing and setting Component Name value,
                    NOTE: Client must free the returned TEXT_p_t* with TEXT_free
                   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the JA method support for accessing and setting Component Name value,
    ##             NOTE: Client must free the returned TEXT_p_t* with TEXT_free
    ##            
    ##     
    ##  
    ## Setter License requirements: drafting ("DRAFTING")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the JA method support for accessing and setting Component Name value,
                    NOTE: Client must free the returned TEXT_p_t* with TEXT_free
                   
            
         
        """
        pass
    
    ## Getter for property: (str) PartName
    ##  Returns the JA method support for accessing and setting Component part file mame value,
    ##             NOTE: Client must free the returned TEXT_p_t* with TEXT_free   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def PartName(self) -> str:
        """
        Getter for property: (str) PartName
         Returns the JA method support for accessing and setting Component part file mame value,
                    NOTE: Client must free the returned TEXT_p_t* with TEXT_free   
            
         
        """
        pass
    
    ## Setter for property: (str) PartName

    ##  Returns the JA method support for accessing and setting Component part file mame value,
    ##             NOTE: Client must free the returned TEXT_p_t* with TEXT_free   
    ##     
    ##  
    ## Setter License requirements: drafting ("DRAFTING")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @PartName.setter
    def PartName(self, partName: str):
        """
        Setter for property: (str) PartName
         Returns the JA method support for accessing and setting Component part file mame value,
                    NOTE: Client must free the returned TEXT_p_t* with TEXT_free   
            
         
        """
        pass
    
    ##  Sets @link NXOpen::PDM::PartOperationCreateBuilder NXOpen::PDM::PartOperationCreateBuilder@endlink  
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: drafting ("DRAFTING")
    ## 
    ## <param name="partOperationBuilder"> (@link NXOpen.PDM.PartOperationCreateBuilder NXOpen.PDM.PartOperationCreateBuilder@endlink) </param>
    def SetPartOperationBuilder(self, partOperationBuilder: NXOpen.PDM.PartOperationCreateBuilder) -> None:
        """
         Sets @link NXOpen::PDM::PartOperationCreateBuilder NXOpen::PDM::PartOperationCreateBuilder@endlink  
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents the Component Settings Button (Layout2d.ComponentSettingsBlockBuilder)
##     
## 
##   <br>  Created in NX10.0.0  <br> 

class ComponentSettingsBlockBuilder(NXOpen.TaggedObject): 
    """ Represents the Component Settings Button (Layout2d.ComponentSettingsBlockBuilder)
    """


    ## Getter for property: (@link ComponentSettingsBuilder NXOpen.Layout2d.ComponentSettingsBuilder@endlink) ComponentSettings
    ##  Returns the Component settings builder which stores the component settings   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return ComponentSettingsBuilder
    @property
    def ComponentSettings(self) -> ComponentSettingsBuilder:
        """
        Getter for property: (@link ComponentSettingsBuilder NXOpen.Layout2d.ComponentSettingsBuilder@endlink) ComponentSettings
         Returns the Component settings builder which stores the component settings   
            
         
        """
        pass
    
    ##  Inherit Settings From Customer Default 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def InheritSettingsFromCustomerDefault(self) -> None:
        """
         Inherit Settings From Customer Default 
        """
        pass
    
    ##  Inherit Settings From Preference 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def InheritSettingsFromPreferences(self) -> None:
        """
         Inherit Settings From Preference 
        """
        pass
    
    ##  Inherit Settings From Selected Objects 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ## 
    ## <param name="selectedObject"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  The selected 2C Component object. 
    ##                                                                         NULL is not allowed. </param>
    def InheritSettingsFromSelectedObject(self, selectedObject: NXOpen.NXObject) -> None:
        """
         Inherit Settings From Selected Objects 
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
## 
##     Represents a @link NXOpen::Layout2d::ComponentSettingsBuilder NXOpen::Layout2d::ComponentSettingsBuilder@endlink 
##     This builder stores the information of the 2D Component settings
##     
## 
##   <br>  Created in NX10.0.0  <br> 

class ComponentSettingsBuilder(NXOpen.TaggedObject): 
    """
    Represents a <ja_class>NXOpen.Layout2d.ComponentSettingsBuilder</ja_class>
    This builder stores the information of the 2D Component settings
    """


    ## Getter for property: (bool) AutomaticUpdate
    ##  Returns the flag to do automatic update or not   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def AutomaticUpdate(self) -> bool:
        """
        Getter for property: (bool) AutomaticUpdate
         Returns the flag to do automatic update or not   
            
         
        """
        pass
    
    ## Setter for property: (bool) AutomaticUpdate

    ##  Returns the flag to do automatic update or not   
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @AutomaticUpdate.setter
    def AutomaticUpdate(self, toggle: bool):
        """
        Setter for property: (bool) AutomaticUpdate
         Returns the flag to do automatic update or not   
            
         
        """
        pass
    
    ## Getter for property: (bool) KeepEditedPartsOpen
    ##  Returns the flag indicating whether to keep edited parts open or not   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def KeepEditedPartsOpen(self) -> bool:
        """
        Getter for property: (bool) KeepEditedPartsOpen
         Returns the flag indicating whether to keep edited parts open or not   
            
         
        """
        pass
    
    ## Setter for property: (bool) KeepEditedPartsOpen

    ##  Returns the flag indicating whether to keep edited parts open or not   
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @KeepEditedPartsOpen.setter
    def KeepEditedPartsOpen(self, toggle: bool):
        """
        Setter for property: (bool) KeepEditedPartsOpen
         Returns the flag indicating whether to keep edited parts open or not   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowAnnotations
    ##  Returns the flag to show annotations or not   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def ShowAnnotations(self) -> bool:
        """
        Getter for property: (bool) ShowAnnotations
         Returns the flag to show annotations or not   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowAnnotations

    ##  Returns the flag to show annotations or not   
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ShowAnnotations.setter
    def ShowAnnotations(self, toggle: bool):
        """
        Setter for property: (bool) ShowAnnotations
         Returns the flag to show annotations or not   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowDimensions
    ##  Returns the flag to show dimensions or not   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def ShowDimensions(self) -> bool:
        """
        Getter for property: (bool) ShowDimensions
         Returns the flag to show dimensions or not   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowDimensions

    ##  Returns the flag to show dimensions or not   
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ShowDimensions.setter
    def ShowDimensions(self, toggle: bool):
        """
        Setter for property: (bool) ShowDimensions
         Returns the flag to show dimensions or not   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowReferenceGeometry
    ##  Returns the flag to show reference geometry or not   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def ShowReferenceGeometry(self) -> bool:
        """
        Getter for property: (bool) ShowReferenceGeometry
         Returns the flag to show reference geometry or not   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowReferenceGeometry

    ##  Returns the flag to show reference geometry or not   
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ShowReferenceGeometry.setter
    def ShowReferenceGeometry(self, toggle: bool):
        """
        Setter for property: (bool) ShowReferenceGeometry
         Returns the flag to show reference geometry or not   
            
         
        """
        pass
    
import NXOpen
##  Represents the Component object.  <br> To create or edit an instance of this class, use @link NXOpen::Layout2d::DefineComponentBuilder  NXOpen::Layout2d::DefineComponentBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class Component(NXOpen.DisplayableObject): 
    """ Represents the Component object. """


    ## Getter for property: (bool) IsActive
    ##  Returns the active state of 2D Component.  
    ##      
    ##  
    ## Getter License requirements: drafting ("DRAFTING")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def IsActive(self) -> bool:
        """
        Getter for property: (bool) IsActive
         Returns the active state of 2D Component.  
             
         
        """
        pass
    
    ## Getter for property: (bool) LockUpdateStatus
    ##  Returns the lock update status of 2D Component.  
    ##     
    ##  
    ## Getter License requirements: drafting ("DRAFTING")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def LockUpdateStatus(self) -> bool:
        """
        Getter for property: (bool) LockUpdateStatus
         Returns the lock update status of 2D Component.  
            
         
        """
        pass
    
    ## Setter for property: (bool) LockUpdateStatus

    ##  Returns the lock update status of 2D Component.  
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @LockUpdateStatus.setter
    def LockUpdateStatus(self, lock: bool):
        """
        Setter for property: (bool) LockUpdateStatus
         Returns the lock update status of 2D Component.  
            
         
        """
        pass
    
    ## Getter for property: (bool) UpgradeUponActivation
    ##  Returns the flag which causes the component to be upgraded upon activation  
    ##     
    ##  
    ## Getter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def UpgradeUponActivation(self) -> bool:
        """
        Getter for property: (bool) UpgradeUponActivation
         Returns the flag which causes the component to be upgraded upon activation  
            
         
        """
        pass
    
    ## Setter for property: (bool) UpgradeUponActivation

    ##  Returns the flag which causes the component to be upgraded upon activation  
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @UpgradeUponActivation.setter
    def UpgradeUponActivation(self, upgrade: bool):
        """
        Setter for property: (bool) UpgradeUponActivation
         Returns the flag which causes the component to be upgraded upon activation  
            
         
        """
        pass
    
    ##  Activates the component. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def Activate(self) -> None:
        """
         Activates the component. 
        """
        pass
    
    ##  Activates the component while in edit in isolation task environment and
    ##             returns component internal sketch 
    ##  @return internalSketch (@link NXOpen.Sketch NXOpen.Sketch@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def ActivateInIsolation(self) -> NXOpen.Sketch:
        """
         Activates the component while in edit in isolation task environment and
                    returns component internal sketch 
         @return internalSketch (@link NXOpen.Sketch NXOpen.Sketch@endlink): .
        """
        pass
    
    ##  Add an array of specified curves from top level sketch to this component 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ## 
    ## <param name="curves"> (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink) </param>
    def AddExistingCurves(self, curves: List[NXOpen.DisplayableObject]) -> None:
        """
         Add an array of specified curves from top level sketch to this component 
        """
        pass
    
    ##  Deactivates the component. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def Deactivate(self) -> None:
        """
         Deactivates the component. 
        """
        pass
    
    ##  Exits the component active status without committing the changes. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def ExitActivate(self) -> None:
        """
         Exits the component active status without committing the changes. 
        """
        pass
    
    ##  Gets the anchor point of a component if it exist 
    ##  @return A tuple consisting of (isAnchorPointExist, anchorPoint). 
    ##  - isAnchorPointExist is: bool.
    ##  - anchorPoint is: @link NXOpen.Point3d NXOpen.Point3d@endlink.

    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def GetAnchorPoint(self) -> Tuple[bool, NXOpen.Point3d]:
        """
         Gets the anchor point of a component if it exist 
         @return A tuple consisting of (isAnchorPointExist, anchorPoint). 
         - isAnchorPointExist is: bool.
         - anchorPoint is: @link NXOpen.Point3d NXOpen.Point3d@endlink.

        """
        pass
    
    ##  Gets the component definition of a component 
    ##  @return definition (@link ComponentDefinition NXOpen.Layout2d.ComponentDefinition@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def GetDefinition(self) -> ComponentDefinition:
        """
         Gets the component definition of a component 
         @return definition (@link ComponentDefinition NXOpen.Layout2d.ComponentDefinition@endlink): .
        """
        pass
    
    ##  Gets the location of the component definition 
    ##  @return location (@link Layout2dDefinitionLocation NXOpen.Layout2d.Layout2dDefinitionLocation@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def GetDefinitionLocation(self) -> Layout2dDefinitionLocation:
        """
         Gets the location of the component definition 
         @return location (@link Layout2dDefinitionLocation NXOpen.Layout2d.Layout2dDefinitionLocation@endlink): .
        """
        pass
    
    ##  Gets the component definition name of a component 
    ##  @return definitionName (str): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def GetDefinitionName(self) -> str:
        """
         Gets the component definition name of a component 
         @return definitionName (str): .
        """
        pass
    
    ##  Gets the path of the component definition 
    ##  @return definitionPath (str): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def GetDefinitionPath(self) -> str:
        """
         Gets the path of the component definition 
         @return definitionPath (str): .
        """
        pass
    
    ##  Returns an array of specified members in this component 
    ##  @return members (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ## 
    ## <param name="memberType"> (@link Layout2dComponentMemberType NXOpen.Layout2d.Layout2dComponentMemberType@endlink) </param>
    def GetMembers(self, memberType: Layout2dComponentMemberType) -> List[NXOpen.DisplayableObject]:
        """
         Returns an array of specified members in this component 
         @return members (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink): .
        """
        pass
    
    ##  Gets the absolute transform of a component, as a rotation matrix and a translation vector
    ##  @return A tuple consisting of (rotation, translation). 
    ##  - rotation is: @link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink.
    ##  - translation is: @link NXOpen.Vector3d NXOpen.Vector3d@endlink.

    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def GetTransform(self) -> Tuple[NXOpen.Matrix3x3, NXOpen.Vector3d]:
        """
         Gets the absolute transform of a component, as a rotation matrix and a translation vector
         @return A tuple consisting of (rotation, translation). 
         - rotation is: @link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink.
         - translation is: @link NXOpen.Vector3d NXOpen.Vector3d@endlink.

        """
        pass
    
    ##  Renews component sketch to the latest solver version and updates component hierarchy for the changes to take effect. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def RenewSketch(self) -> None:
        """
         Renews component sketch to the latest solver version and updates component hierarchy for the changes to take effect. 
        """
        pass
    
    ##  Sets the absolute transform on a component, given a rotation matrix and a translation vector
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ## 
    ## <param name="rotation"> (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) </param>
    ## <param name="translation"> (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) </param>
    def SetTransform(self, rotation: NXOpen.Matrix3x3, translation: NXOpen.Vector3d) -> None:
        """
         Sets the absolute transform on a component, given a rotation matrix and a translation vector
        """
        pass
    
    ##  Transforms the component given a rotation matrix and a translation vector
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ## 
    ## <param name="rotation"> (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) </param>
    ## <param name="translation"> (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) </param>
    def Transform(self, rotation: NXOpen.Matrix3x3, translation: NXOpen.Vector3d) -> None:
        """
         Transforms the component given a rotation matrix and a translation vector
        """
        pass
    
    ##  Updates the component and all of its sub components. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def Update(self) -> None:
        """
         Updates the component and all of its sub components. 
        """
        pass
    
import NXOpen
##  Represents a Builder for converting Layout to drawing sheet  <br> To create a new instance of this class, use @link NXOpen::Layout2d::LayoutDrawingSheetCollection::CreateConvertLayoutToSheetBuilder  NXOpen::Layout2d::LayoutDrawingSheetCollection::CreateConvertLayoutToSheetBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class ConvertLayoutToSheetBuilder(NXOpen.Builder): 
    """ Represents a Builder for converting Layout to drawing sheet """


    ##  the drawing sheet projection angle 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## First</term><description> 
    ##  first angle projection </description> </item><item><term> 
    ## Third</term><description> 
    ##  third angle projection </description> </item></list>
    class SheetProjectionAngleType(Enum):
        """
        Members Include: <First> <Third>
        """
        First: int
        Third: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ConvertLayoutToSheetBuilder.SheetProjectionAngleType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) Name
    ##  Returns the name of the drawing sheet to be created   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name of the drawing sheet to be created   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the name of the drawing sheet to be created   
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name of the drawing sheet to be created   
            
         
        """
        pass
    
    ## Getter for property: (str) Number
    ##  Returns the number of the drawing sheet to be created   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def Number(self) -> str:
        """
        Getter for property: (str) Number
         Returns the number of the drawing sheet to be created   
            
         
        """
        pass
    
    ## Setter for property: (str) Number

    ##  Returns the number of the drawing sheet to be created   
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Number.setter
    def Number(self, number: str):
        """
        Setter for property: (str) Number
         Returns the number of the drawing sheet to be created   
            
         
        """
        pass
    
    ## Getter for property: (@link ConvertLayoutToSheetBuilder.SheetProjectionAngleType NXOpen.Layout2d.ConvertLayoutToSheetBuilder.SheetProjectionAngleType@endlink) ProjectionAngleType
    ##  Returns the sheet projection angle option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return ConvertLayoutToSheetBuilder.SheetProjectionAngleType
    @property
    def ProjectionAngleType(self) -> ConvertLayoutToSheetBuilder.SheetProjectionAngleType:
        """
        Getter for property: (@link ConvertLayoutToSheetBuilder.SheetProjectionAngleType NXOpen.Layout2d.ConvertLayoutToSheetBuilder.SheetProjectionAngleType@endlink) ProjectionAngleType
         Returns the sheet projection angle option   
            
         
        """
        pass
    
    ## Setter for property: (@link ConvertLayoutToSheetBuilder.SheetProjectionAngleType NXOpen.Layout2d.ConvertLayoutToSheetBuilder.SheetProjectionAngleType@endlink) ProjectionAngleType

    ##  Returns the sheet projection angle option   
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ProjectionAngleType.setter
    def ProjectionAngleType(self, type: ConvertLayoutToSheetBuilder.SheetProjectionAngleType):
        """
        Setter for property: (@link ConvertLayoutToSheetBuilder.SheetProjectionAngleType NXOpen.Layout2d.ConvertLayoutToSheetBuilder.SheetProjectionAngleType@endlink) ProjectionAngleType
         Returns the sheet projection angle option   
            
         
        """
        pass
    
    ## Getter for property: (str) Revision
    ##  Returns the revision of the drawing sheet to be created   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def Revision(self) -> str:
        """
        Getter for property: (str) Revision
         Returns the revision of the drawing sheet to be created   
            
         
        """
        pass
    
    ## Setter for property: (str) Revision

    ##  Returns the revision of the drawing sheet to be created   
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Revision.setter
    def Revision(self, revision: str):
        """
        Setter for property: (str) Revision
         Returns the revision of the drawing sheet to be created   
            
         
        """
        pass
    
    ## Getter for property: (str) SecondaryNumber
    ##  Returns the secondary number of the drawing sheet to be created   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def SecondaryNumber(self) -> str:
        """
        Getter for property: (str) SecondaryNumber
         Returns the secondary number of the drawing sheet to be created   
            
         
        """
        pass
    
    ## Setter for property: (str) SecondaryNumber

    ##  Returns the secondary number of the drawing sheet to be created   
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SecondaryNumber.setter
    def SecondaryNumber(self, secondaryNumber: str):
        """
        Setter for property: (str) SecondaryNumber
         Returns the secondary number of the drawing sheet to be created   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectView NXOpen.SelectView@endlink) SelectLayoutSheetView
    ##  Returns the select layout sheet view to convert  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.SelectView
    @property
    def SelectLayoutSheetView(self) -> NXOpen.SelectView:
        """
        Getter for property: (@link NXOpen.SelectView NXOpen.SelectView@endlink) SelectLayoutSheetView
         Returns the select layout sheet view to convert  
            
         
        """
        pass
    
    ##  Gets the sheet scale 
    ##  @return A tuple consisting of (numerator, denominator). 
    ##  - numerator is: float. the scale numerator .
    ##  - denominator is: float. the scale denominator .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    def GetScale(self) -> Tuple[float, float]:
        """
         Gets the sheet scale 
         @return A tuple consisting of (numerator, denominator). 
         - numerator is: float. the scale numerator .
         - denominator is: float. the scale denominator .

        """
        pass
    
    ##  Sets the sheet scale 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ## 
    ## <param name="numerator"> (float)  the scale numerator </param>
    ## <param name="denominator"> (float)  the scale denominator </param>
    def SetScale(self, numerator: float, denominator: float) -> None:
        """
         Sets the sheet scale 
        """
        pass
    
import NXOpen
##  Represents a Builder for converting a drawing sheet to Layout  <br> To create a new instance of this class, use @link NXOpen::Layout2d::LayoutDrawingSheetCollection::CreateConvertSheetToLayoutBuilder  NXOpen::Layout2d::LayoutDrawingSheetCollection::CreateConvertSheetToLayoutBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class ConvertSheetToLayoutBuilder(LayoutDrawingSheetBuilder): 
    """ Represents a Builder for converting a drawing sheet to Layout """


    ## Getter for property: (@link NXOpen.SelectView NXOpen.SelectView@endlink) SelectSheetView
    ##  Returns the select drawing sheet to convert  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.SelectView
    @property
    def SelectSheetView(self) -> NXOpen.SelectView:
        """
        Getter for property: (@link NXOpen.SelectView NXOpen.SelectView@endlink) SelectSheetView
         Returns the select drawing sheet to convert  
            
         
        """
        pass
    
import NXOpen
import NXOpen.Display
##  Represents a Builder that creates @link NXOpen::Layout2d::Component NXOpen::Layout2d::Component@endlink  from Assembly <br> To create a new instance of this class, use @link NXOpen::Layout2d::ComponentCollection::CreateComponentFrom3dBuilder  NXOpen::Layout2d::ComponentCollection::CreateComponentFrom3dBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## BoxExtentDelayUpdate </term> <description> 
##  
## false </description> </item> 
## 
## <item><term> 
##  
## CapColorOption </term> <description> 
##  
## Any </description> </item> 
## 
## <item><term> 
##  
## ClipType </term> <description> 
##  
## Section </description> </item> 
## 
## <item><term> 
##  
## CurveColorOption </term> <description> 
##  
## Any </description> </item> 
## 
## <item><term> 
##  
## CurveFont </term> <description> 
##  
## Solid </description> </item> 
## 
## <item><term> 
##  
## CurveWidth </term> <description> 
##  
## Two </description> </item> 
## 
## <item><term> 
##  
## LockPlanes </term> <description> 
##  
## true </description> </item> 
## 
## <item><term> 
##  
## ShowCap </term> <description> 
##  
## true </description> </item> 
## 
## <item><term> 
##  
## ShowClip </term> <description> 
##  
## true </description> </item> 
## 
## <item><term> 
##  
## ShowCurves (deprecated) </term> <description> 
##  
## false </description> </item> 
## 
## <item><term> 
##  
## ShowGrid </term> <description> 
##  
## false </description> </item> 
## 
## <item><term> 
##  
## ShowInterference </term> <description> 
##  
## false </description> </item> 
## 
## <item><term> 
##  
## ShowViewer </term> <description> 
##  
## false </description> </item> 
## 
## <item><term> 
##  
## Type </term> <description> 
##  
## OnePlane </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX11.0.0  <br> 

class CreateComponentFrom3DBuilder(NXOpen.Display.DynamicSectionBuilder): 
    """ Represents a Builder that creates <ja_class>NXOpen.Layout2d.Component</ja_class> from Assembly"""


    ##  the method to use 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Section</term><description> 
    ##  use section </description> </item><item><term> 
    ## Plane</term><description> 
    ##  use plane </description> </item></list>
    class CreateMethod(Enum):
        """
        Members Include: <Section> <Plane>
        """
        Section: int
        Plane: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CreateComponentFrom3DBuilder.CreateMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) ComponentName
    ##  Returns the component name   
    ##     
    ##  
    ## Getter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return str
    @property
    def ComponentName(self) -> str:
        """
        Getter for property: (str) ComponentName
         Returns the component name   
            
         
        """
        pass
    
    ## Setter for property: (str) ComponentName

    ##  Returns the component name   
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @ComponentName.setter
    def ComponentName(self, name: str):
        """
        Setter for property: (str) ComponentName
         Returns the component name   
            
         
        """
        pass
    
    ## Getter for property: (@link CreateComponentFrom3DBuilder.CreateMethod NXOpen.Layout2d.CreateComponentFrom3DBuilder.CreateMethod@endlink) Method
    ##  Returns the method to utilize in create Component from 3D  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return CreateComponentFrom3DBuilder.CreateMethod
    @property
    def Method(self) -> CreateComponentFrom3DBuilder.CreateMethod:
        """
        Getter for property: (@link CreateComponentFrom3DBuilder.CreateMethod NXOpen.Layout2d.CreateComponentFrom3DBuilder.CreateMethod@endlink) Method
         Returns the method to utilize in create Component from 3D  
            
         
        """
        pass
    
    ## Setter for property: (@link CreateComponentFrom3DBuilder.CreateMethod NXOpen.Layout2d.CreateComponentFrom3DBuilder.CreateMethod@endlink) Method

    ##  Returns the method to utilize in create Component from 3D  
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @Method.setter
    def Method(self, method: CreateComponentFrom3DBuilder.CreateMethod):
        """
        Setter for property: (@link CreateComponentFrom3DBuilder.CreateMethod NXOpen.Layout2d.CreateComponentFrom3DBuilder.CreateMethod@endlink) Method
         Returns the method to utilize in create Component from 3D  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) SelectedObjects
    ##  Returns the selected objects of Solid body or Component type   
    ##     
    ##  
    ## Getter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.SelectTaggedObjectList
    @property
    def SelectedObjects(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) SelectedObjects
         Returns the selected objects of Solid body or Component type   
            
         
        """
        pass
    
    ## Getter for property: (@link CreateComponentFrom3DSettingsBuilder NXOpen.Layout2d.CreateComponentFrom3DSettingsBuilder@endlink) Settings
    ##  Returns the settings of create component from 3D   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return CreateComponentFrom3DSettingsBuilder
    @property
    def Settings(self) -> CreateComponentFrom3DSettingsBuilder:
        """
        Getter for property: (@link CreateComponentFrom3DSettingsBuilder NXOpen.Layout2d.CreateComponentFrom3DSettingsBuilder@endlink) Settings
         Returns the settings of create component from 3D   
            
         
        """
        pass
    
    ## Setter for property: (@link CreateComponentFrom3DSettingsBuilder NXOpen.Layout2d.CreateComponentFrom3DSettingsBuilder@endlink) Settings

    ##  Returns the settings of create component from 3D   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @Settings.setter
    def Settings(self, settings: CreateComponentFrom3DSettingsBuilder):
        """
        Setter for property: (@link CreateComponentFrom3DSettingsBuilder NXOpen.Layout2d.CreateComponentFrom3DSettingsBuilder@endlink) Settings
         Returns the settings of create component from 3D   
            
         
        """
        pass
    
    ##  Gets the projection plane origin and orientation matrix 
    ##  @return A tuple consisting of (origin, orientation). 
    ##  - origin is: @link NXOpen.Point3d NXOpen.Point3d@endlink.
    ##  - orientation is: @link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink.

    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def GetProjectionPlane(self) -> Tuple[NXOpen.Point3d, NXOpen.Matrix3x3]:
        """
         Gets the projection plane origin and orientation matrix 
         @return A tuple consisting of (origin, orientation). 
         - origin is: @link NXOpen.Point3d NXOpen.Point3d@endlink.
         - orientation is: @link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink.

        """
        pass
    
    ##  Returns the current source part 
    ##  @return part (@link NXOpen.Part NXOpen.Part@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def GetSourcePart(self) -> NXOpen.Part:
        """
         Returns the current source part 
         @return part (@link NXOpen.Part NXOpen.Part@endlink): .
        """
        pass
    
    ##  Sets the projection plane specified by origin, y and z vectors, where z is the plane normal and
    ##             the x vector is computed.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ## 
    ## <param name="origin"> (@link NXOpen.Point3d NXOpen.Point3d@endlink) </param>
    ## <param name="yAxis"> (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) </param>
    ## <param name="zAxis"> (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) </param>
    def SetProjectionPlane(self, origin: NXOpen.Point3d, yAxis: NXOpen.Vector3d, zAxis: NXOpen.Vector3d) -> None:
        """
         Sets the projection plane specified by origin, y and z vectors, where z is the plane normal and
                    the x vector is computed.
        """
        pass
    
    ##  Sets the source part to create 2D component from. The part may be the current work part or other part loaded in session. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ## 
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def SetSourcePart(self, part: NXOpen.Part) -> None:
        """
         Sets the source part to create 2D component from. The part may be the current work part or other part loaded in session. 
        """
        pass
    
import NXOpen
import NXOpen.Display
import NXOpen.GeometricUtilities
## 
##      Represents a @link NXOpen::Layout2d::CreateComponentFrom3DSettingsBuilder NXOpen::Layout2d::CreateComponentFrom3DSettingsBuilder@endlink 
##     
## 
##   <br>  Created in NX11.0.0  <br> 

class CreateComponentFrom3DSettingsBuilder(NXOpen.TaggedObject): 
    """
     Represents a <ja_class>NXOpen.Layout2d.CreateComponentFrom3DSettingsBuilder</ja_class>
    """


    ## Getter for property: (@link ActiveSetScope NXOpen.Layout2d.ActiveSetScope@endlink) ActiveSetScope
    ##  Returns the option whether each 2D component will be created with no active set or an active set for the entire 2D component.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return ActiveSetScope
    @property
    def ActiveSetScope(self) -> ActiveSetScope:
        """
        Getter for property: (@link ActiveSetScope NXOpen.Layout2d.ActiveSetScope@endlink) ActiveSetScope
         Returns the option whether each 2D component will be created with no active set or an active set for the entire 2D component.  
             
         
        """
        pass
    
    ## Setter for property: (@link ActiveSetScope NXOpen.Layout2d.ActiveSetScope@endlink) ActiveSetScope

    ##  Returns the option whether each 2D component will be created with no active set or an active set for the entire 2D component.  
    ##      
    ##  
    ## Setter License requirements: drafting ("DRAFTING")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ActiveSetScope.setter
    def ActiveSetScope(self, scope: ActiveSetScope):
        """
        Setter for property: (@link ActiveSetScope NXOpen.Layout2d.ActiveSetScope@endlink) ActiveSetScope
         Returns the option whether each 2D component will be created with no active set or an active set for the entire 2D component.  
             
         
        """
        pass
    
    ## Getter for property: (bool) AutomaticallyStartInsert2DComponentCommand
    ##  Returns the settings to determines whether or not automatically start insert 2D component command.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def AutomaticallyStartInsert2DComponentCommand(self) -> bool:
        """
        Getter for property: (bool) AutomaticallyStartInsert2DComponentCommand
         Returns the settings to determines whether or not automatically start insert 2D component command.  
            
         
        """
        pass
    
    ## Setter for property: (bool) AutomaticallyStartInsert2DComponentCommand

    ##  Returns the settings to determines whether or not automatically start insert 2D component command.  
    ##     
    ##  
    ## Setter License requirements: drafting ("DRAFTING")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @AutomaticallyStartInsert2DComponentCommand.setter
    def AutomaticallyStartInsert2DComponentCommand(self, automaticallyStartInsert2DComponentCommand: bool):
        """
        Setter for property: (bool) AutomaticallyStartInsert2DComponentCommand
         Returns the settings to determines whether or not automatically start insert 2D component command.  
            
         
        """
        pass
    
    ## Getter for property: (int) Color
    ##  Returns  the settings to specifies the 2D component curves color.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return int
    @property
    def Color(self) -> int:
        """
        Getter for property: (int) Color
         Returns  the settings to specifies the 2D component curves color.  
            
         
        """
        pass
    
    ## Setter for property: (int) Color

    ##  Returns  the settings to specifies the 2D component curves color.  
    ##     
    ##  
    ## Setter License requirements: drafting ("DRAFTING")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @Color.setter
    def Color(self, color: int):
        """
        Setter for property: (int) Color
         Returns  the settings to specifies the 2D component curves color.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Display.DynamicSectionTypes.CurveColorOption NXOpen.Display.DynamicSectionTypes.CurveColorOption@endlink) ColorOption
    ##  Returns  the settings to specifies how the color of the 2D component curves is defined.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Display.DynamicSectionTypes.CurveColorOption
    @property
    def ColorOption(self) -> NXOpen.Display.DynamicSectionTypes.CurveColorOption:
        """
        Getter for property: (@link NXOpen.Display.DynamicSectionTypes.CurveColorOption NXOpen.Display.DynamicSectionTypes.CurveColorOption@endlink) ColorOption
         Returns  the settings to specifies how the color of the 2D component curves is defined.  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Display.DynamicSectionTypes.CurveColorOption NXOpen.Display.DynamicSectionTypes.CurveColorOption@endlink) ColorOption

    ##  Returns  the settings to specifies how the color of the 2D component curves is defined.  
    ##     
    ##  
    ## Setter License requirements: drafting ("DRAFTING")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @ColorOption.setter
    def ColorOption(self, colorOption: NXOpen.Display.DynamicSectionTypes.CurveColorOption):
        """
        Setter for property: (@link NXOpen.Display.DynamicSectionTypes.CurveColorOption NXOpen.Display.DynamicSectionTypes.CurveColorOption@endlink) ColorOption
         Returns  the settings to specifies how the color of the 2D component curves is defined.  
            
         
        """
        pass
    
    ## Getter for property: (bool) CreateSingle2DComponentDefinition
    ##  Returns the settings to determines whether or not create single 2D component definition.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def CreateSingle2DComponentDefinition(self) -> bool:
        """
        Getter for property: (bool) CreateSingle2DComponentDefinition
         Returns the settings to determines whether or not create single 2D component definition.  
            
         
        """
        pass
    
    ## Setter for property: (bool) CreateSingle2DComponentDefinition

    ##  Returns the settings to determines whether or not create single 2D component definition.  
    ##     
    ##  
    ## Setter License requirements: drafting ("DRAFTING")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @CreateSingle2DComponentDefinition.setter
    def CreateSingle2DComponentDefinition(self, createSingle2DComponentDefinition: bool):
        """
        Setter for property: (bool) CreateSingle2DComponentDefinition
         Returns the settings to determines whether or not create single 2D component definition.  
            
         
        """
        pass
    
    ##  Inherit Settings From Customer Default 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: drafting ("DRAFTING")
    def InheritSettingsFromCustomerDefault(self) -> None:
        """
         Inherit Settings From Customer Default 
        """
        pass
    
    ##  Inherit Settings From Preference 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: drafting ("DRAFTING")
    def InheritSettingsFromPreferences(self) -> None:
        """
         Inherit Settings From Preference 
        """
        pass
    
import NXOpen
##  Represents a Builder for Define Component Anchor Point functionality which will define the anchor
##      *  point location of a 2D Component instance  <br> To create a new instance of this class, use @link NXOpen::Layout2d::ComponentCollection::CreateDefineComponentAnchorPointBuilder  NXOpen::Layout2d::ComponentCollection::CreateDefineComponentAnchorPointBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class DefineComponentAnchorPointBuilder(NXOpen.Builder): 
    """ Represents a Builder for Define Component Anchor Point functionality which will define the anchor
     *  point location of a 2D Component instance """


    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) AnchorPoint
    ##  Returns the anchor point of a 2D Component   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def AnchorPoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) AnchorPoint
         Returns the anchor point of a 2D Component   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) AnchorPoint

    ##  Returns the anchor point of a 2D Component   
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @AnchorPoint.setter
    def AnchorPoint(self, anchorPoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) AnchorPoint
         Returns the anchor point of a 2D Component   
            
         
        """
        pass
    
import NXOpen
import NXOpen.Gateway
##  Represents a Builder for Define 2D component functionality which will define
##      *  a 2D Component and stores its definition in the Reuse Library              <br> To create a new instance of this class, use @link NXOpen::Layout2d::ComponentCollection::CreateDefineComponentBuilder  NXOpen::Layout2d::ComponentCollection::CreateDefineComponentBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## ImageCapture.CaptureMethod </term> <description> 
##  
## GraphicsArea </description> </item> 
## 
## <item><term> 
##  
## ImageCapture.Format </term> <description> 
##  
## Bmp </description> </item> 
## 
## <item><term> 
##  
## ImageCapture.Size </term> <description> 
##  
## Pixels64 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX10.0.0  <br> 

class DefineComponentBuilder(NXOpen.Builder): 
    """ Represents a Builder for Define 2D component functionality which will define
     *  a 2D Component and stores its definition in the Reuse Library             """


    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) ActiveSet
    ##  Returns the select members of active set   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def ActiveSet(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) ActiveSet
         Returns the select members of active set   
            
         
        """
        pass
    
    ## Getter for property: (@link ActiveSetScope NXOpen.Layout2d.ActiveSetScope@endlink) ActiveSetScope
    ##  Returns the active members scope   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return ActiveSetScope
    @property
    def ActiveSetScope(self) -> ActiveSetScope:
        """
        Getter for property: (@link ActiveSetScope NXOpen.Layout2d.ActiveSetScope@endlink) ActiveSetScope
         Returns the active members scope   
            
         
        """
        pass
    
    ## Setter for property: (@link ActiveSetScope NXOpen.Layout2d.ActiveSetScope@endlink) ActiveSetScope

    ##  Returns the active members scope   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ActiveSetScope.setter
    def ActiveSetScope(self, scope: ActiveSetScope):
        """
        Setter for property: (@link ActiveSetScope NXOpen.Layout2d.ActiveSetScope@endlink) ActiveSetScope
         Returns the active members scope   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) AnchorPoint
    ##  Returns the anchor point to define the 2D Component  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def AnchorPoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) AnchorPoint
         Returns the anchor point to define the 2D Component  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) AnchorPoint

    ##  Returns the anchor point to define the 2D Component  
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @AnchorPoint.setter
    def AnchorPoint(self, anchorPoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) AnchorPoint
         Returns the anchor point to define the 2D Component  
            
         
        """
        pass
    
    ## Getter for property: (@link ComponentNameBuilder NXOpen.Layout2d.ComponentNameBuilder@endlink) ComponentName
    ##  Returns the 2D Component Name defines the name for the new created definition   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return ComponentNameBuilder
    @property
    def ComponentName(self) -> ComponentNameBuilder:
        """
        Getter for property: (@link ComponentNameBuilder NXOpen.Layout2d.ComponentNameBuilder@endlink) ComponentName
         Returns the 2D Component Name defines the name for the new created definition   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) Contents
    ##  Returns the select objects to create a 2D Component definition  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def Contents(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) Contents
         Returns the select objects to create a 2D Component definition  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Gateway.ImageCaptureBuilder NXOpen.Gateway.ImageCaptureBuilder@endlink) ImageCapture
    ##  Returns the image capture builder used to create an image for the definition   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.Gateway.ImageCaptureBuilder
    @property
    def ImageCapture(self) -> NXOpen.Gateway.ImageCaptureBuilder:
        """
        Getter for property: (@link NXOpen.Gateway.ImageCaptureBuilder NXOpen.Gateway.ImageCaptureBuilder@endlink) ImageCapture
         Returns the image capture builder used to create an image for the definition   
            
         
        """
        pass
    
    ## Getter for property: (str) ImageName
    ##  Returns the 2D Component image name for the new created definition   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def ImageName(self) -> str:
        """
        Getter for property: (str) ImageName
         Returns the 2D Component image name for the new created definition   
            
         
        """
        pass
    
    ## Setter for property: (str) ImageName

    ##  Returns the 2D Component image name for the new created definition   
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ImageName.setter
    def ImageName(self, imageName: str):
        """
        Setter for property: (str) ImageName
         Returns the 2D Component image name for the new created definition   
            
         
        """
        pass
    
    ##  Verifies whether specified object can be an active member 
    ##  @return result (bool): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objectValue"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink) </param>
    def IsValidActiveSetMember(self, objectValue: NXOpen.DisplayableObject) -> bool:
        """
         Verifies whether specified object can be an active member 
         @return result (bool): .
        """
        pass
    
    ##  Sets the location type of the component indicating local, native or team center
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ## 
    ## <param name="locationType"> (@link Layout2dDefinitionLocation NXOpen.Layout2d.Layout2dDefinitionLocation@endlink) </param>
    def SetLocation(self, locationType: Layout2dDefinitionLocation) -> None:
        """
         Sets the location type of the component indicating local, native or team center
        """
        pass
    
    ##  Sets the path to store the 2D Component 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ## 
    ## <param name="path"> (str)  location of component </param>
    def SetPath(self, path: str) -> None:
        """
         Sets the path to store the 2D Component 
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Layout2d::EditComponentSettingsBuilder NXOpen::Layout2d::EditComponentSettingsBuilder@endlink  builder.
##         It provides an interface for editing layout2d component settings. 
##         The committed object is the component with the new settings  <br> To create a new instance of this class, use @link NXOpen::Drafting::SettingsManager::CreateLayout2dEditComponentSettingsBuilder  NXOpen::Drafting::SettingsManager::CreateLayout2dEditComponentSettingsBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class EditComponentSettingsBuilder(BaseEditSettingsBuilder): 
    """ Represents a <ja_class>NXOpen.Layout2d.EditComponentSettingsBuilder</ja_class> builder.
        It provides an interface for editing layout2d component settings. 
        The committed object is the component with the new settings """


    ## Getter for property: (@link ComponentSettingsBlockBuilder NXOpen.Layout2d.ComponentSettingsBlockBuilder@endlink) ComponentSettings
    ##  Returns the 2D Component settings block builder which holds the component settings builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return ComponentSettingsBlockBuilder
    @property
    def ComponentSettings(self) -> ComponentSettingsBlockBuilder:
        """
        Getter for property: (@link ComponentSettingsBlockBuilder NXOpen.Layout2d.ComponentSettingsBlockBuilder@endlink) ComponentSettings
         Returns the 2D Component settings block builder which holds the component settings builder   
            
         
        """
        pass
    
    ##  Inherit Settings From Customer Default 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def InheritSettingsFromCustomerDefault(self) -> None:
        """
         Inherit Settings From Customer Default 
        """
        pass
    
    ##  Inherit Settings From Preference 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def InheritSettingsFromPreferences(self) -> None:
        """
         Inherit Settings From Preference 
        """
        pass
    
    ##  Inherit Settings From Selected Objects 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ## 
    ## <param name="selectedObject"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  The selected 2D Component object. 
    ##                                                                         NULL is not allowed. </param>
    def InheritSettingsFromSelectedObject(self, selectedObject: NXOpen.NXObject) -> None:
        """
         Inherit Settings From Selected Objects 
        """
        pass
    
import NXOpen
##  Represents a Builder for export component 2D hierarchy  <br> To create a new instance of this class, use @link NXOpen::Layout2d::ComponentCollection::CreateExportComponentHierarchyBuilder  NXOpen::Layout2d::ComponentCollection::CreateExportComponentHierarchyBuilder @endlink  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class ExportComponentHierarchyBuilder(NXOpen.Builder): 
    """ Represents a Builder for export component 2D hierarchy """


    ## Getter for property: (bool) ChildComponentsForComponents
    ##  Returns the flag indicating whether to export child components for components   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def ChildComponentsForComponents(self) -> bool:
        """
        Getter for property: (bool) ChildComponentsForComponents
         Returns the flag indicating whether to export child components for components   
            
         
        """
        pass
    
    ## Setter for property: (bool) ChildComponentsForComponents

    ##  Returns the flag indicating whether to export child components for components   
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @ChildComponentsForComponents.setter
    def ChildComponentsForComponents(self, childComponentsForComponents: bool):
        """
        Setter for property: (bool) ChildComponentsForComponents
         Returns the flag indicating whether to export child components for components   
            
         
        """
        pass
    
    ## Getter for property: (bool) ChildComponentsForDefinitions
    ##  Returns the flag indicating whether to export child components for definitions   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def ChildComponentsForDefinitions(self) -> bool:
        """
        Getter for property: (bool) ChildComponentsForDefinitions
         Returns the flag indicating whether to export child components for definitions   
            
         
        """
        pass
    
    ## Setter for property: (bool) ChildComponentsForDefinitions

    ##  Returns the flag indicating whether to export child components for definitions   
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @ChildComponentsForDefinitions.setter
    def ChildComponentsForDefinitions(self, childComponentsForDefinitions: bool):
        """
        Setter for property: (bool) ChildComponentsForDefinitions
         Returns the flag indicating whether to export child components for definitions   
            
         
        """
        pass
    
    ## Getter for property: (bool) Contents
    ##  Returns the flag indicating whether to export contents for components   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def Contents(self) -> bool:
        """
        Getter for property: (bool) Contents
         Returns the flag indicating whether to export contents for components   
            
         
        """
        pass
    
    ## Setter for property: (bool) Contents

    ##  Returns the flag indicating whether to export contents for components   
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @Contents.setter
    def Contents(self, contents: bool):
        """
        Setter for property: (bool) Contents
         Returns the flag indicating whether to export contents for components   
            
         
        """
        pass
    
    ## Getter for property: (bool) DefinitionReferenceProperties
    ##  Returns the flag indicating whether to export definition reference properties for components   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def DefinitionReferenceProperties(self) -> bool:
        """
        Getter for property: (bool) DefinitionReferenceProperties
         Returns the flag indicating whether to export definition reference properties for components   
            
         
        """
        pass
    
    ## Setter for property: (bool) DefinitionReferenceProperties

    ##  Returns the flag indicating whether to export definition reference properties for components   
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @DefinitionReferenceProperties.setter
    def DefinitionReferenceProperties(self, definitionReferenceProperties: bool):
        """
        Setter for property: (bool) DefinitionReferenceProperties
         Returns the flag indicating whether to export definition reference properties for components   
            
         
        """
        pass
    
    ## Getter for property: (bool) Definitions
    ##  Returns the flag indicating whether to export definitions for components   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def Definitions(self) -> bool:
        """
        Getter for property: (bool) Definitions
         Returns the flag indicating whether to export definitions for components   
            
         
        """
        pass
    
    ## Setter for property: (bool) Definitions

    ##  Returns the flag indicating whether to export definitions for components   
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @Definitions.setter
    def Definitions(self, definitions: bool):
        """
        Setter for property: (bool) Definitions
         Returns the flag indicating whether to export definitions for components   
            
         
        """
        pass
    
    ## Getter for property: (str) OutputFileName
    ##  Returns the selected output file   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return str
    @property
    def OutputFileName(self) -> str:
        """
        Getter for property: (str) OutputFileName
         Returns the selected output file   
            
         
        """
        pass
    
    ## Setter for property: (str) OutputFileName

    ##  Returns the selected output file   
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @OutputFileName.setter
    def OutputFileName(self, outputFileName: str):
        """
        Setter for property: (str) OutputFileName
         Returns the selected output file   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Selection
    ##  Returns the selected objects which may be of @link NXOpen::Layout2d::Component NXOpen::Layout2d::Component@endlink  or @link NXOpen::Sketch NXOpen::Sketch@endlink  type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def Selection(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Selection
         Returns the selected objects which may be of @link NXOpen::Layout2d::Component NXOpen::Layout2d::Component@endlink  or @link NXOpen::Sketch NXOpen::Sketch@endlink  type   
            
         
        """
        pass
    
    ## Getter for property: (bool) SoftwareProperties
    ##  Returns the flag indicating whether to export software properties for components   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def SoftwareProperties(self) -> bool:
        """
        Getter for property: (bool) SoftwareProperties
         Returns the flag indicating whether to export software properties for components   
            
         
        """
        pass
    
    ## Setter for property: (bool) SoftwareProperties

    ##  Returns the flag indicating whether to export software properties for components   
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @SoftwareProperties.setter
    def SoftwareProperties(self, softwareProperties: bool):
        """
        Setter for property: (bool) SoftwareProperties
         Returns the flag indicating whether to export software properties for components   
            
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
## 
##     Represents a @link NXOpen::Layout2d::GeneralPreferencesBuilder NXOpen::Layout2d::GeneralPreferencesBuilder@endlink 
##     This builder stores the general layout preferences
##     
## 
##   <br>  Created in NX12.0.0  <br> 

class GeneralPreferencesBuilder(NXOpen.TaggedObject): 
    """
    Represents a <ja_class>NXOpen.Layout2d.GeneralPreferencesBuilder</ja_class>
    This builder stores the general layout preferences
    """


    ## Getter for property: (bool) ShowLayoutOrigin
    ##  Returns the flag controling the visibility of layout origin symbols in the session  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def ShowLayoutOrigin(self) -> bool:
        """
        Getter for property: (bool) ShowLayoutOrigin
         Returns the flag controling the visibility of layout origin symbols in the session  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowLayoutOrigin

    ##  Returns the flag controling the visibility of layout origin symbols in the session  
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ShowLayoutOrigin.setter
    def ShowLayoutOrigin(self, toggle: bool):
        """
        Setter for property: (bool) ShowLayoutOrigin
         Returns the flag controling the visibility of layout origin symbols in the session  
            
         
        """
        pass
    
import NXOpen
##  Represents a Builder to inherit geometry display attributes (color, font, width) from and to component definition.  <br> To create a new instance of this class, use @link NXOpen::Layout2d::ComponentCollection::CreateInheritDisplayAttributesBuilder  NXOpen::Layout2d::ComponentCollection::CreateInheritDisplayAttributesBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class InheritDisplayAttributesBuilder(NXOpen.Builder): 
    """ Represents a Builder to inherit geometry display attributes (color, font, width) from and to component definition. """


    ##  the inherit direction 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## DefinitionToComponent</term><description> 
    ##  Inherit from Definition </description> </item><item><term> 
    ## ComponentToDefinition</term><description> 
    ##  Inherit from Component  </description> </item></list>
    class InheritDirection(Enum):
        """
        Members Include: <DefinitionToComponent> <ComponentToDefinition>
        """
        DefinitionToComponent: int
        ComponentToDefinition: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> InheritDisplayAttributesBuilder.InheritDirection:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link SelectComponentList NXOpen.Layout2d.SelectComponentList@endlink) Components
    ##  Returns the selected 2D Components for inherit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return SelectComponentList
    @property
    def Components(self) -> SelectComponentList:
        """
        Getter for property: (@link SelectComponentList NXOpen.Layout2d.SelectComponentList@endlink) Components
         Returns the selected 2D Components for inherit   
            
         
        """
        pass
    
    ## Getter for property: (@link InheritDisplayAttributesBuilder.InheritDirection NXOpen.Layout2d.InheritDisplayAttributesBuilder.InheritDirection@endlink) Direction
    ##  Returns the inherit direction.  
    ##    The default direction is definition to component.   
    ##  
    ## Getter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return InheritDisplayAttributesBuilder.InheritDirection
    @property
    def Direction(self) -> InheritDisplayAttributesBuilder.InheritDirection:
        """
        Getter for property: (@link InheritDisplayAttributesBuilder.InheritDirection NXOpen.Layout2d.InheritDisplayAttributesBuilder.InheritDirection@endlink) Direction
         Returns the inherit direction.  
           The default direction is definition to component.   
         
        """
        pass
    
    ## Setter for property: (@link InheritDisplayAttributesBuilder.InheritDirection NXOpen.Layout2d.InheritDisplayAttributesBuilder.InheritDirection@endlink) Direction

    ##  Returns the inherit direction.  
    ##    The default direction is definition to component.   
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Direction.setter
    def Direction(self, direction: InheritDisplayAttributesBuilder.InheritDirection):
        """
        Setter for property: (@link InheritDisplayAttributesBuilder.InheritDirection NXOpen.Layout2d.InheritDisplayAttributesBuilder.InheritDirection@endlink) Direction
         Returns the inherit direction.  
           The default direction is definition to component.   
         
        """
        pass
    
import NXOpen
##  Represents a Builder for Insert Component functionality which will insert a 2D
##      *  Component instance in the active sketch   <br> To create a new instance of this class, use @link NXOpen::Layout2d::ComponentCollection::CreateInsertComponentBuilder  NXOpen::Layout2d::ComponentCollection::CreateInsertComponentBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class InsertComponentBuilder(NXOpen.Builder): 
    """ Represents a Builder for Insert Component functionality which will insert a 2D
     *  Component instance in the active sketch  """


    ## Getter for property: (float) Angle
    ##  Returns the component rotation angle, measured counterclockwise, around the anchor point, from the sketch +X direction to component's X axis   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return float
    @property
    def Angle(self) -> float:
        """
        Getter for property: (float) Angle
         Returns the component rotation angle, measured counterclockwise, around the anchor point, from the sketch +X direction to component's X axis   
            
         
        """
        pass
    
    ## Setter for property: (float) Angle

    ##  Returns the component rotation angle, measured counterclockwise, around the anchor point, from the sketch +X direction to component's X axis   
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Angle.setter
    def Angle(self, angle: float):
        """
        Setter for property: (float) Angle
         Returns the component rotation angle, measured counterclockwise, around the anchor point, from the sketch +X direction to component's X axis   
            
         
        """
        pass
    
    ## Getter for property: (@link ComponentSettingsBlockBuilder NXOpen.Layout2d.ComponentSettingsBlockBuilder@endlink) Settings
    ##  Returns the Component settings block builder which holds the component settings builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return ComponentSettingsBlockBuilder
    @property
    def Settings(self) -> ComponentSettingsBlockBuilder:
        """
        Getter for property: (@link ComponentSettingsBlockBuilder NXOpen.Layout2d.ComponentSettingsBlockBuilder@endlink) Settings
         Returns the Component settings block builder which holds the component settings builder   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Sketch NXOpen.Sketch@endlink) Sketch
    ##  Returns the sketch to insert the 2D Component   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.Sketch
    @property
    def Sketch(self) -> NXOpen.Sketch:
        """
        Getter for property: (@link NXOpen.Sketch NXOpen.Sketch@endlink) Sketch
         Returns the sketch to insert the 2D Component   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Sketch NXOpen.Sketch@endlink) Sketch

    ##  Returns the sketch to insert the 2D Component   
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Sketch.setter
    def Sketch(self, sketch: NXOpen.Sketch):
        """
        Setter for property: (@link NXOpen.Sketch NXOpen.Sketch@endlink) Sketch
         Returns the sketch to insert the 2D Component   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) SpecifyPoint
    ##  Returns the point specified to put the 2D Component instance  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def SpecifyPoint(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) SpecifyPoint
         Returns the point specified to put the 2D Component instance  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) SpecifyPoint

    ##  Returns the point specified to put the 2D Component instance  
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @SpecifyPoint.setter
    def SpecifyPoint(self, specifyPoint: NXOpen.Point3d):
        """
        Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) SpecifyPoint
         Returns the point specified to put the 2D Component instance  
            
         
        """
        pass
    
    ##  Sets the location type of the 2D Component indicating local, native or team center
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ## 
    ## <param name="locationType"> (@link Layout2dDefinitionLocation NXOpen.Layout2d.Layout2dDefinitionLocation@endlink) </param>
    def SetLocation(self, locationType: Layout2dDefinitionLocation) -> None:
        """
         Sets the location type of the 2D Component indicating local, native or team center
        """
        pass
    
    ##  Sets the path of the reuse library for the 2D Component 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ## 
    ## <param name="path"> (str)  the path of the 2D Component </param>
    def SetPath(self, path: str) -> None:
        """
         Sets the path of the reuse library for the 2D Component 
        """
        pass
    
##  Component member type 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## NotSet</term><description> 
## </description> </item><item><term> 
## SketchGeometryNonReference</term><description> 
## </description> </item><item><term> 
## SketchGeometryReference</term><description> 
## </description> </item><item><term> 
## SketchGeometry</term><description> 
## </description> </item><item><term> 
## SketchDimension</term><description> 
## </description> </item><item><term> 
## SketchConstraint</term><description> 
## </description> </item><item><term> 
## Sketch</term><description> 
## </description> </item><item><term> 
## Component</term><description> 
## </description> </item><item><term> 
## DraftingDimension</term><description> 
## </description> </item><item><term> 
## Dimension</term><description> 
## </description> </item><item><term> 
## DraftingAnnotationNonDimension</term><description> 
## </description> </item><item><term> 
## DraftingAnnotation</term><description> 
## </description> </item><item><term> 
## Annotation</term><description> 
## </description> </item><item><term> 
## MiscOthers</term><description> 
## </description> </item><item><term> 
## Misc</term><description> 
## </description> </item><item><term> 
## ExemptRelationsSet</term><description> 
## </description> </item><item><term> 
## All</term><description> 
## </description> </item></list>
class Layout2dComponentMemberType(Enum):
    """
    Members Include: <NotSet> <SketchGeometryNonReference> <SketchGeometryReference> <SketchGeometry> <SketchDimension> <SketchConstraint> <Sketch> <Component> <DraftingDimension> <Dimension> <DraftingAnnotationNonDimension> <DraftingAnnotation> <Annotation> <MiscOthers> <Misc> <ExemptRelationsSet> <All>
    """
    NotSet: int
    SketchGeometryNonReference: int
    SketchGeometryReference: int
    SketchGeometry: int
    SketchDimension: int
    SketchConstraint: int
    Sketch: int
    Component: int
    DraftingDimension: int
    Dimension: int
    DraftingAnnotationNonDimension: int
    DraftingAnnotation: int
    Annotation: int
    MiscOthers: int
    Misc: int
    ExemptRelationsSet: int
    All: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> Layout2dComponentMemberType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Definition location 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Unspecified</term><description> 
## </description> </item><item><term> 
## Local</term><description> 
## </description> </item><item><term> 
## Native</term><description> 
## </description> </item><item><term> 
## TcEng</term><description> 
## </description> </item></list>
class Layout2dDefinitionLocation(Enum):
    """
    Members Include: <Unspecified> <Local> <Native> <TcEng>
    """
    Unspecified: int
    Local: int
    Native: int
    TcEng: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> Layout2dDefinitionLocation:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Definition Status 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Unknown</term><description> 
## </description> </item><item><term> 
## Synced</term><description> 
## </description> </item><item><term> 
## NotSynced</term><description> 
## </description> </item><item><term> 
## Missing</term><description> 
## </description> </item></list>
class Layout2dDefinitionStatus(Enum):
    """
    Members Include: <Unknown> <Synced> <NotSynced> <Missing>
    """
    Unknown: int
    Synced: int
    NotSynced: int
    Missing: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> Layout2dDefinitionStatus:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents a Builder for creating @link Layout2d::LayoutDrawingSheet Layout2d::LayoutDrawingSheet@endlink s  <br> To create a new instance of this class, use @link NXOpen::Layout2d::LayoutDrawingSheetCollection::CreateLayoutDrawingSheetBuilder  NXOpen::Layout2d::LayoutDrawingSheetCollection::CreateLayoutDrawingSheetBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class LayoutDrawingSheetBuilder(DrawingSheetBuilder): 
    """ Represents a Builder for creating <ja_class>Layout2d.LayoutDrawingSheet</ja_class>s """
    pass


import NXOpen
##  Represents a collection of @link NXOpen::Layout2d::LayoutDrawingSheet NXOpen::Layout2d::LayoutDrawingSheet@endlink s.  <br> To obtain an instance of this class, refer to @link NXOpen::Part  NXOpen::Part @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class LayoutDrawingSheetCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of <ja_class>NXOpen.Layout2d.LayoutDrawingSheet</ja_class>s. """


    ## Getter for property: (@link LayoutDrawingSheet NXOpen.Layout2d.LayoutDrawingSheet@endlink) CurrentDrawingSheet
    ##  Returns the currently opened layout drawing sheet.  
    ##    This will return NULL if no layout drawing sheet is opened.   
    ##  
    ## Getter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return LayoutDrawingSheet
    @property
    def CurrentDrawingSheet(self) -> LayoutDrawingSheet:
        """
        Getter for property: (@link LayoutDrawingSheet NXOpen.Layout2d.LayoutDrawingSheet@endlink) CurrentDrawingSheet
         Returns the currently opened layout drawing sheet.  
           This will return NULL if no layout drawing sheet is opened.   
         
        """
        pass
    
    ##  Creates a @link NXOpen::Layout2d::ConvertLayoutToSheetBuilder NXOpen::Layout2d::ConvertLayoutToSheetBuilder@endlink  
    ##  @return builder (@link ConvertLayoutToSheetBuilder NXOpen.Layout2d.ConvertLayoutToSheetBuilder@endlink):  the convert layout to sheet builder .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def CreateConvertLayoutToSheetBuilder(self) -> ConvertLayoutToSheetBuilder:
        """
         Creates a @link NXOpen::Layout2d::ConvertLayoutToSheetBuilder NXOpen::Layout2d::ConvertLayoutToSheetBuilder@endlink  
         @return builder (@link ConvertLayoutToSheetBuilder NXOpen.Layout2d.ConvertLayoutToSheetBuilder@endlink):  the convert layout to sheet builder .
        """
        pass
    
    ##  Creates a @link NXOpen::Layout2d::ConvertSheetToLayoutBuilder NXOpen::Layout2d::ConvertSheetToLayoutBuilder@endlink  
    ##  @return builder (@link ConvertSheetToLayoutBuilder NXOpen.Layout2d.ConvertSheetToLayoutBuilder@endlink):  the convert sheet to layout builder .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def CreateConvertSheetToLayoutBuilder(self) -> ConvertSheetToLayoutBuilder:
        """
         Creates a @link NXOpen::Layout2d::ConvertSheetToLayoutBuilder NXOpen::Layout2d::ConvertSheetToLayoutBuilder@endlink  
         @return builder (@link ConvertSheetToLayoutBuilder NXOpen.Layout2d.ConvertSheetToLayoutBuilder@endlink):  the convert sheet to layout builder .
        """
        pass
    
    ##  Creates a @link NXOpen::Layout2d::LayoutDrawingSheetBuilder NXOpen::Layout2d::LayoutDrawingSheetBuilder@endlink  
    ##  @return builder (@link LayoutDrawingSheetBuilder NXOpen.Layout2d.LayoutDrawingSheetBuilder@endlink):  the layout drawing sheet builder .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ## 
    ## <param name="layoutDrawingSheet"> (@link LayoutDrawingSheet NXOpen.Layout2d.LayoutDrawingSheet@endlink)  reserved for future use, set to 0 </param>
    def CreateLayoutDrawingSheetBuilder(self, layoutDrawingSheet: LayoutDrawingSheet) -> LayoutDrawingSheetBuilder:
        """
         Creates a @link NXOpen::Layout2d::LayoutDrawingSheetBuilder NXOpen::Layout2d::LayoutDrawingSheetBuilder@endlink  
         @return builder (@link LayoutDrawingSheetBuilder NXOpen.Layout2d.LayoutDrawingSheetBuilder@endlink):  the layout drawing sheet builder .
        """
        pass
    
    ##  Finds the @link NXOpen::Layout2d::LayoutDrawingSheet NXOpen::Layout2d::LayoutDrawingSheet@endlink  with the given identifier 
    ##         as recorded in a journal.  An object may not return the same value as its JournalIdentifier in 
    ##         different versions of  the software. However newer versions of the software should find the same 
    ##         object when  FindObject is passed older versions of its journal identifier. In general, this method 
    ##         should not be used in handwritten code and exists to support record and playback of journals.
    ## 
    ##         An exception will be thrown if no object can be found with the given journal identifier. 
    ##  @return layoutDrawingSheet (@link LayoutDrawingSheet NXOpen.Layout2d.LayoutDrawingSheet@endlink):  Layout drawing sheet with this identifier .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ## 
    ## <param name="journalIdentifier"> (str)  Identifier of the Layout drawing sheet you want </param>
    def FindObject(self, journalIdentifier: str) -> LayoutDrawingSheet:
        """
         Finds the @link NXOpen::Layout2d::LayoutDrawingSheet NXOpen::Layout2d::LayoutDrawingSheet@endlink  with the given identifier 
                as recorded in a journal.  An object may not return the same value as its JournalIdentifier in 
                different versions of  the software. However newer versions of the software should find the same 
                object when  FindObject is passed older versions of its journal identifier. In general, this method 
                should not be used in handwritten code and exists to support record and playback of journals.
        
                An exception will be thrown if no object can be found with the given journal identifier. 
         @return layoutDrawingSheet (@link LayoutDrawingSheet NXOpen.Layout2d.LayoutDrawingSheet@endlink):  Layout drawing sheet with this identifier .
        """
        pass
    
    ##  Inserts a layout drawing sheet into a part. 
    ##  @return layoutDrawingSheet (@link LayoutDrawingSheet NXOpen.Layout2d.LayoutDrawingSheet@endlink):  the inserted layout drawing sheet .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ## 
    ## <param name="name"> (str)  Layout drawing sheet name </param>
    ## <param name="units"> (@link DrawingSheet.Unit NXOpen.Drawings.DrawingSheet.Unit@endlink)  Unit of sheet size </param>
    ## <param name="numerator"> (float)  Numerator of the scale of layout </param>
    ## <param name="denominator"> (float)  Denominator of the scale of layout </param>
    ## <param name="projectionAngle"> (@link DrawingSheet.ProjectionAngleType NXOpen.Drawings.DrawingSheet.ProjectionAngleType@endlink)  Projection angle </param>
    def InsertSheet(self, name: str, units: DrawingSheet.Unit, numerator: float, denominator: float, projectionAngle: DrawingSheet.ProjectionAngleType) -> LayoutDrawingSheet:
        """
         Inserts a layout drawing sheet into a part. 
         @return layoutDrawingSheet (@link LayoutDrawingSheet NXOpen.Layout2d.LayoutDrawingSheet@endlink):  the inserted layout drawing sheet .
        """
        pass
    
##  Represents a Layout drawing sheet.  <br> To create or edit an instance of this class, use @link NXOpen::Layout2d::LayoutDrawingSheetBuilder  NXOpen::Layout2d::LayoutDrawingSheetBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class LayoutDrawingSheet(DrawingSheet): 
    """ Represents a Layout drawing sheet. """
    pass


import NXOpen
## 
##     Represents a @link NXOpen::Layout2d::LocalDefinitionFolderBuilder NXOpen::Layout2d::LocalDefinitionFolderBuilder@endlink . A local definition folder contains 2D Component definitions stored in 
##     the current part.
##      <br> To create a new instance of this class, use @link NXOpen::Layout2d::LocalDefinitionFolderCollection::CreateLocalDefinitionFolderBuilder  NXOpen::Layout2d::LocalDefinitionFolderCollection::CreateLocalDefinitionFolderBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class LocalDefinitionFolderBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>NXOpen.Layout2d.LocalDefinitionFolderBuilder</ja_class>. A local definition folder contains 2D Component definitions stored in 
    the current part.
    """


    ## Getter for property: (str) FolderName
    ##  Returns the current folder name  
    ##     
    ##  
    ## Getter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def FolderName(self) -> str:
        """
        Getter for property: (str) FolderName
         Returns the current folder name  
            
         
        """
        pass
    
    ## Setter for property: (str) FolderName

    ##  Returns the current folder name  
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @FolderName.setter
    def FolderName(self, folderName: str):
        """
        Setter for property: (str) FolderName
         Returns the current folder name  
            
         
        """
        pass
    
    ## Getter for property: (@link LocalDefinitionFolder NXOpen.Layout2d.LocalDefinitionFolder@endlink) Parent
    ##  Returns the current folder's parent   
    ##     
    ##  
    ## Getter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return LocalDefinitionFolder
    @property
    def Parent(self) -> LocalDefinitionFolder:
        """
        Getter for property: (@link LocalDefinitionFolder NXOpen.Layout2d.LocalDefinitionFolder@endlink) Parent
         Returns the current folder's parent   
            
         
        """
        pass
    
    ## Setter for property: (@link LocalDefinitionFolder NXOpen.Layout2d.LocalDefinitionFolder@endlink) Parent

    ##  Returns the current folder's parent   
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Parent.setter
    def Parent(self, parentfolder: LocalDefinitionFolder):
        """
        Setter for property: (@link LocalDefinitionFolder NXOpen.Layout2d.LocalDefinitionFolder@endlink) Parent
         Returns the current folder's parent   
            
         
        """
        pass
    
import NXOpen
##  Represents a collection of @link NXOpen::Layout2d::LocalDefinitionFolder NXOpen::Layout2d::LocalDefinitionFolder@endlink  objects. A local definition folder contains 2D Component definitions stored in 
##     the current part  <br> To obtain an instance of this class, refer to @link NXOpen::Part  NXOpen::Part @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class LocalDefinitionFolderCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of <ja_class>NXOpen.Layout2d.LocalDefinitionFolder</ja_class> objects. A local definition folder contains 2D Component definitions stored in 
    the current part """


    ##  Creates local definition folder builder instance. The builder allows operations such as Creation, Edit and Deletion
    ##             of local definition folders. These operations are Undo/Redo supported.
    ##         
    ##  @return builder (@link LocalDefinitionFolderBuilder NXOpen.Layout2d.LocalDefinitionFolderBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ## 
    ## <param name="currentFolder"> (@link LocalDefinitionFolder NXOpen.Layout2d.LocalDefinitionFolder@endlink)  @link NXOpen::Layout2d::LocalDefinitionFolder NXOpen::Layout2d::LocalDefinitionFolder@endlink  to be set as current folder.
    ##                                                                                       If NULL, create a new folder </param>
    def CreateLocalDefinitionFolderBuilder(self, currentFolder: LocalDefinitionFolder) -> LocalDefinitionFolderBuilder:
        """
         Creates local definition folder builder instance. The builder allows operations such as Creation, Edit and Deletion
                    of local definition folders. These operations are Undo/Redo supported.
                
         @return builder (@link LocalDefinitionFolderBuilder NXOpen.Layout2d.LocalDefinitionFolderBuilder@endlink): .
        """
        pass
    
    ##   Finds the @link  NXOpen::Layout2d::LocalDefinitionFolder   NXOpen::Layout2d::LocalDefinitionFolder @endlink  with the given name. 
    ##              An exception will be thrown if no object can be found with the given name. 
    ##  @return folder (@link LocalDefinitionFolder NXOpen.Layout2d.LocalDefinitionFolder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ## 
    ## <param name="name"> (str) </param>
    def FindObject(self, name: str) -> LocalDefinitionFolder:
        """
          Finds the @link  NXOpen::Layout2d::LocalDefinitionFolder   NXOpen::Layout2d::LocalDefinitionFolder @endlink  with the given name. 
                     An exception will be thrown if no object can be found with the given name. 
         @return folder (@link LocalDefinitionFolder NXOpen.Layout2d.LocalDefinitionFolder@endlink): .
        """
        pass
    
import NXOpen
##  Represents a local definition folder. This folder contains 2D Component definitions stored in 
##     the current part  <br> To create or edit an instance of this class, use @link NXOpen::Layout2d::LocalDefinitionFolderBuilder  NXOpen::Layout2d::LocalDefinitionFolderBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class LocalDefinitionFolder(NXOpen.NXObject): 
    """ Represents a local definition folder. This folder contains 2D Component definitions stored in 
    the current part """
    pass


import NXOpen
import NXOpen.Gateway
##  Represents a Builder for Make 2D Component unique functionality which will create a
##      *  new definition of the selected 2D Component instance  <br> To create a new instance of this class, use @link NXOpen::Layout2d::ComponentCollection::CreateMakeComponentUniqueBuilder  NXOpen::Layout2d::ComponentCollection::CreateMakeComponentUniqueBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## ImageCapture.CaptureMethod </term> <description> 
##  
## GraphicsArea </description> </item> 
## 
## <item><term> 
##  
## ImageCapture.Format </term> <description> 
##  
## Bmp </description> </item> 
## 
## <item><term> 
##  
## ImageCapture.Size </term> <description> 
##  
## Pixels64 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX10.0.0  <br> 

class MakeComponentUniqueBuilder(NXOpen.Builder): 
    """ Represents a Builder for Make 2D Component unique functionality which will create a
     *  new definition of the selected 2D Component instance """


    ## Getter for property: (@link SelectComponent NXOpen.Layout2d.SelectComponent@endlink) Component
    ##  Returns the select 2D Comoponent instance to create definition   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return SelectComponent
    @property
    def Component(self) -> SelectComponent:
        """
        Getter for property: (@link SelectComponent NXOpen.Layout2d.SelectComponent@endlink) Component
         Returns the select 2D Comoponent instance to create definition   
            
         
        """
        pass
    
    ## Getter for property: (@link ComponentNameBuilder NXOpen.Layout2d.ComponentNameBuilder@endlink) ComponentName
    ##  Returns the 2D Component Name defines the name for the new created definition   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return ComponentNameBuilder
    @property
    def ComponentName(self) -> ComponentNameBuilder:
        """
        Getter for property: (@link ComponentNameBuilder NXOpen.Layout2d.ComponentNameBuilder@endlink) ComponentName
         Returns the 2D Component Name defines the name for the new created definition   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Gateway.ImageCaptureBuilder NXOpen.Gateway.ImageCaptureBuilder@endlink) ImageCapture
    ##  Returns the image capture builder used to create an image for the new definition   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.Gateway.ImageCaptureBuilder
    @property
    def ImageCapture(self) -> NXOpen.Gateway.ImageCaptureBuilder:
        """
        Getter for property: (@link NXOpen.Gateway.ImageCaptureBuilder NXOpen.Gateway.ImageCaptureBuilder@endlink) ImageCapture
         Returns the image capture builder used to create an image for the new definition   
            
         
        """
        pass
    
    ## Getter for property: (str) ImageName
    ##  Returns the 2D Component image name for the new created definition   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def ImageName(self) -> str:
        """
        Getter for property: (str) ImageName
         Returns the 2D Component image name for the new created definition   
            
         
        """
        pass
    
    ## Setter for property: (str) ImageName

    ##  Returns the 2D Component image name for the new created definition   
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ImageName.setter
    def ImageName(self, imageName: str):
        """
        Setter for property: (str) ImageName
         Returns the 2D Component image name for the new created definition   
            
         
        """
        pass
    
    ##  Sets the location type of the 2D Component indicating local, native or team center
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ## 
    ## <param name="locationType"> (@link Layout2dDefinitionLocation NXOpen.Layout2d.Layout2dDefinitionLocation@endlink) </param>
    def SetLocation(self, locationType: Layout2dDefinitionLocation) -> None:
        """
         Sets the location type of the 2D Component indicating local, native or team center
        """
        pass
    
    ##  Sets the path to store the 2D Component
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ## 
    ## <param name="path"> (str)  location of component </param>
    def SetPath(self, path: str) -> None:
        """
         Sets the path to store the 2D Component
        """
        pass
    
import NXOpen
##  Represents a Builder for New 2D Component functionality which will create an empty 2D Component 
##         instance and stores its definition in the local 2D Component folder
##      <br> To create a new instance of this class, use @link NXOpen::Layout2d::ComponentCollection::CreateNewComponentBuilder  NXOpen::Layout2d::ComponentCollection::CreateNewComponentBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class NewComponentBuilder(NXOpen.Builder): 
    """ Represents a Builder for New 2D Component functionality which will create an empty 2D Component 
        instance and stores its definition in the local 2D Component folder
    """


    ## Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) Owner
    ##  Returns the owner to create the 2D Component, can be either a drawing sheet, a drawing view
    ##             a sketch or a 2D Component 
    ##           
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.NXObject
    @property
    def Owner(self) -> NXOpen.NXObject:
        """
        Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) Owner
         Returns the owner to create the 2D Component, can be either a drawing sheet, a drawing view
                    a sketch or a 2D Component 
                  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) Owner

    ##  Returns the owner to create the 2D Component, can be either a drawing sheet, a drawing view
    ##             a sketch or a 2D Component 
    ##           
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Owner.setter
    def Owner(self, owner: NXOpen.NXObject):
        """
        Setter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) Owner
         Returns the owner to create the 2D Component, can be either a drawing sheet, a drawing view
                    a sketch or a 2D Component 
                  
            
         
        """
        pass
    
import NXOpen
##  Represents a Builder for Publish 2D Component functionality which will allow
##         local definitions to be exported into external storage locations  <br> To create a new instance of this class, use @link NXOpen::Layout2d::ComponentCollection::CreatePublishComponentBuilder  NXOpen::Layout2d::ComponentCollection::CreatePublishComponentBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class PublishComponentBuilder(NXOpen.Builder): 
    """ Represents a Builder for Publish 2D Component functionality which will allow
        local definitions to be exported into external storage locations """


    ## Getter for property: (str) DestinationPath
    ##  Returns the path of folder to publish into   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def DestinationPath(self) -> str:
        """
        Getter for property: (str) DestinationPath
         Returns the path of folder to publish into   
            
         
        """
        pass
    
    ## Setter for property: (str) DestinationPath

    ##  Returns the path of folder to publish into   
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @DestinationPath.setter
    def DestinationPath(self, destinationPath: str):
        """
        Setter for property: (str) DestinationPath
         Returns the path of folder to publish into   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsFolder
    ##  Returns the type of object to pblish.  
    ##    Can be definition or folder   
    ##  
    ## Getter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1847.0.0.  This property is no longer used. The type of object (definition or folder) is now determined by parsing <ja_pproperty>NXOpen.Layout2d.PublishComponentBuilder.OriginPath</ja_pproperty>  <br> 

    ## @return bool
    @property
    def IsFolder(self) -> bool:
        """
        Getter for property: (bool) IsFolder
         Returns the type of object to pblish.  
           Can be definition or folder   
         
        """
        pass
    
    ## Setter for property: (bool) IsFolder

    ##  Returns the type of object to pblish.  
    ##    Can be definition or folder   
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1847.0.0.  This property is no longer used. The type of object (definition or folder) is now determined by parsing <ja_pproperty>NXOpen.Layout2d.PublishComponentBuilder.OriginPath</ja_pproperty>  <br> 

    @IsFolder.setter
    def IsFolder(self, isFolder: bool):
        """
        Setter for property: (bool) IsFolder
         Returns the type of object to pblish.  
           Can be definition or folder   
         
        """
        pass
    
    ## Getter for property: (@link Layout2dDefinitionLocation NXOpen.Layout2d.Layout2dDefinitionLocation@endlink) Location
    ##  Returns the location type of folder to publish into   
    ##     
    ##  
    ## Getter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return Layout2dDefinitionLocation
    @property
    def Location(self) -> Layout2dDefinitionLocation:
        """
        Getter for property: (@link Layout2dDefinitionLocation NXOpen.Layout2d.Layout2dDefinitionLocation@endlink) Location
         Returns the location type of folder to publish into   
            
         
        """
        pass
    
    ## Setter for property: (@link Layout2dDefinitionLocation NXOpen.Layout2d.Layout2dDefinitionLocation@endlink) Location

    ##  Returns the location type of folder to publish into   
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Location.setter
    def Location(self, locationType: Layout2dDefinitionLocation):
        """
        Setter for property: (@link Layout2dDefinitionLocation NXOpen.Layout2d.Layout2dDefinitionLocation@endlink) Location
         Returns the location type of folder to publish into   
            
         
        """
        pass
    
    ## Getter for property: (str) OriginPath
    ##  Returns the path of folder or definition to publish   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def OriginPath(self) -> str:
        """
        Getter for property: (str) OriginPath
         Returns the path of folder or definition to publish   
            
         
        """
        pass
    
    ## Setter for property: (str) OriginPath

    ##  Returns the path of folder or definition to publish   
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @OriginPath.setter
    def OriginPath(self, originPath: str):
        """
        Setter for property: (str) OriginPath
         Returns the path of folder or definition to publish   
            
         
        """
        pass
    
import NXOpen
##  Represents a Builder for Reparent 2D Component functionality which will reparents
##     *   the selected 2D Component contents from another 2D Component definition.
##      <br> To create a new instance of this class, use @link NXOpen::Layout2d::ComponentCollection::CreateReparentComponentBuilder  NXOpen::Layout2d::ComponentCollection::CreateReparentComponentBuilder @endlink  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class ReparentComponentBuilder(NXOpen.Builder): 
    """ Represents a Builder for Reparent 2D Component functionality which will reparents
    *   the selected 2D Component contents from another 2D Component definition.
    """


    ## Getter for property: (@link SelectComponentList NXOpen.Layout2d.SelectComponentList@endlink) Components
    ##  Returns the select 2D Components to reparent the definitions   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return SelectComponentList
    @property
    def Components(self) -> SelectComponentList:
        """
        Getter for property: (@link SelectComponentList NXOpen.Layout2d.SelectComponentList@endlink) Components
         Returns the select 2D Components to reparent the definitions   
            
         
        """
        pass
    
    ## Getter for property: (bool) CreateCopy
    ##  Returns the flag to distinguish copy and cut operations   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def CreateCopy(self) -> bool:
        """
        Getter for property: (bool) CreateCopy
         Returns the flag to distinguish copy and cut operations   
            
         
        """
        pass
    
    ## Setter for property: (bool) CreateCopy

    ##  Returns the flag to distinguish copy and cut operations   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @CreateCopy.setter
    def CreateCopy(self, createCopy: bool):
        """
        Setter for property: (bool) CreateCopy
         Returns the flag to distinguish copy and cut operations   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink) Target
    ##  Returns the target of 2D Components reparent operation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.DisplayableObject
    @property
    def Target(self) -> NXOpen.DisplayableObject:
        """
        Getter for property: (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink) Target
         Returns the target of 2D Components reparent operation   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink) Target

    ##  Returns the target of 2D Components reparent operation   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @Target.setter
    def Target(self, target: NXOpen.DisplayableObject):
        """
        Setter for property: (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink) Target
         Returns the target of 2D Components reparent operation   
            
         
        """
        pass
    
    ##  Add a list of 2D Components
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="components"> (@link Component List[NXOpen.Layout2d.Component]@endlink) </param>
    def AddComponents(self, components: List[Component]) -> None:
        """
         Add a list of 2D Components
        """
        pass
    
import NXOpen
##  Represents a Builder for Replace 2D Component functionality which will replaces
##     *   the selected 2D Component contents from another 2D Component definition.
##      <br> To create a new instance of this class, use @link NXOpen::Layout2d::ComponentCollection::CreateReplaceComponentBuilder  NXOpen::Layout2d::ComponentCollection::CreateReplaceComponentBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class ReplaceComponentBuilder(NXOpen.Builder): 
    """ Represents a Builder for Replace 2D Component functionality which will replaces
    *   the selected 2D Component contents from another 2D Component definition.
    """


    ## Getter for property: (@link SelectComponentList NXOpen.Layout2d.SelectComponentList@endlink) Components
    ##  Returns the select 2D Components to replace the definitions   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return SelectComponentList
    @property
    def Components(self) -> SelectComponentList:
        """
        Getter for property: (@link SelectComponentList NXOpen.Layout2d.SelectComponentList@endlink) Components
         Returns the select 2D Components to replace the definitions   
            
         
        """
        pass
    
    ## Getter for property: (@link Layout2dDefinitionLocation NXOpen.Layout2d.Layout2dDefinitionLocation@endlink) Location
    ##  Returns the location type of the 2D Component definition to replace 
    ##         *   indicating local, native or team center
    ##           
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return Layout2dDefinitionLocation
    @property
    def Location(self) -> Layout2dDefinitionLocation:
        """
        Getter for property: (@link Layout2dDefinitionLocation NXOpen.Layout2d.Layout2dDefinitionLocation@endlink) Location
         Returns the location type of the 2D Component definition to replace 
                *   indicating local, native or team center
                  
            
         
        """
        pass
    
    ## Setter for property: (@link Layout2dDefinitionLocation NXOpen.Layout2d.Layout2dDefinitionLocation@endlink) Location

    ##  Returns the location type of the 2D Component definition to replace 
    ##         *   indicating local, native or team center
    ##           
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Location.setter
    def Location(self, locationType: Layout2dDefinitionLocation):
        """
        Setter for property: (@link Layout2dDefinitionLocation NXOpen.Layout2d.Layout2dDefinitionLocation@endlink) Location
         Returns the location type of the 2D Component definition to replace 
                *   indicating local, native or team center
                  
            
         
        """
        pass
    
    ## Getter for property: (str) Path
    ##  Returns the path of the 2D Component definition to replace   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def Path(self) -> str:
        """
        Getter for property: (str) Path
         Returns the path of the 2D Component definition to replace   
            
         
        """
        pass
    
    ## Setter for property: (str) Path

    ##  Returns the path of the 2D Component definition to replace   
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Path.setter
    def Path(self, path: str):
        """
        Setter for property: (str) Path
         Returns the path of the 2D Component definition to replace   
            
         
        """
        pass
    
    ## Getter for property: (bool) ReplaceAll
    ##  Returns the flag indicating whether to replace all instances of selected components   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def ReplaceAll(self) -> bool:
        """
        Getter for property: (bool) ReplaceAll
         Returns the flag indicating whether to replace all instances of selected components   
            
         
        """
        pass
    
    ## Setter for property: (bool) ReplaceAll

    ##  Returns the flag indicating whether to replace all instances of selected components   
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ReplaceAll.setter
    def ReplaceAll(self, replaceAll: bool):
        """
        Setter for property: (bool) ReplaceAll
         Returns the flag indicating whether to replace all instances of selected components   
            
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a list of objects on a selection list.

## 
##   <br>  Created in NX5.0.0  <br> 

class SelectComponentList(NXOpen.TaggedObject): 
    """ Represents a list of objects on a selection list.
"""


    ## Getter for property: (bool) DuplicatesAllowed
    ##  Returns whether duplicate objects are allowed in the selection list.  
    ##   
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def DuplicatesAllowed(self) -> bool:
        """
        Getter for property: (bool) DuplicatesAllowed
         Returns whether duplicate objects are allowed in the selection list.  
          
              
         
        """
        pass
    
    ## Getter for property: (int) Size
    ##  Returns the number of objects in the list.  
    ##   
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def Size(self) -> int:
        """
        Getter for property: (int) Size
         Returns the number of objects in the list.  
          
              
         
        """
        pass
    
    ##  Adds an object to the list
    ##     
    ##  @return added (bool):  True if successfully added to list;
    ##                                   False if the object was already a member
    ##                                   of the list and duplicates are not allowed .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectComponentList NXOpen.Layout2d.SelectComponentList@endlink) </param>
    ## <param name="objectValue"> (@link Component NXOpen.Layout2d.Component@endlink)  object to add </param>
    @overload
    def Add(self, objectValue: Component) -> bool:
        """
         Adds an object to the list
            
         @return added (bool):  True if successfully added to list;
                                          False if the object was already a member
                                          of the list and duplicates are not allowed .
        """
        pass
    
    ##  Adds a set of objects with views to the list
    ##     
    ##  @return added (bool):  True if successfully added all objects to the list;
    ##                                   False if there was at least one object that was already a
    ##                                   member of the list and duplicates are not allowed .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objects"> (@link Component List[NXOpen.Layout2d.Component]@endlink)  objects to add </param>
    ## <param name="views"> (@link NXOpen.View List[NXOpen.View]@endlink)  views for the objects </param>
    def AddWithViews(self, objects: List[Component], views: List[NXOpen.View]) -> bool:
        """
         Adds a set of objects with views to the list
            
         @return added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    
    ##  Adds a set of objects to the list
    ##     
    ##  @return added (bool):  True if successfully added all objects to the list;
    ##                                   False if there was at least one object that was already a
    ##                                   member of the list and duplicates are not allowed .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectComponentList NXOpen.Layout2d.SelectComponentList@endlink) </param>
    ## <param name="objects"> (@link Component List[NXOpen.Layout2d.Component]@endlink)  objects to add </param>
    @overload
    def Add(self, objects: List[Component]) -> bool:
        """
         Adds a set of objects to the list
            
         @return added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    
    ##  Adds the objects from a SelectionMethod to the list
    ##     
    ##  @return added (bool):  True if successfully added all objects to the list;
    ##                                   False if there was at least one object that was already a
    ##                                   member of the list and duplicates are not allowed .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectComponentList NXOpen.Layout2d.SelectComponentList@endlink) </param>
    ## <param name="input_selection_method"> (@link NXOpen.SelectionMethod NXOpen.SelectionMethod@endlink)  selection method containing objects to add </param>
    @overload
    def Add(self, input_selection_method: NXOpen.SelectionMethod) -> bool:
        """
         Adds the objects from a SelectionMethod to the list
            
         @return added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    
    ##  Adds the object with the objects view and objects point
    ##     
    ##  @return added (bool):  True if successfully added to list;
    ##                                   False if the object was already a member
    ##                                   of the list and duplicates are not allowed .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectComponentList NXOpen.Layout2d.SelectComponentList@endlink) </param>
    ## <param name="selection"> (@link Component NXOpen.Layout2d.Component@endlink)  selected object </param>
    ## <param name="view"> (@link NXOpen.View NXOpen.View@endlink)  selected object view</param>
    ## <param name="point"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  selected object point</param>
    @overload
    def Add(self, selection: Component, view: NXOpen.View, point: NXOpen.Point3d) -> bool:
        """
         Adds the object with the objects view and objects point
            
         @return added (bool):  True if successfully added to list;
                                          False if the object was already a member
                                          of the list and duplicates are not allowed .
        """
        pass
    
    ##  The object being selected with the objects view and objects point and snap information.
    ##     
    ##  @return added (bool):  True if successfully added all objects to the list;
    ##                                   False if there was at least one object that was already a
    ##                                   member of the list and duplicates are not allowed .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectComponentList NXOpen.Layout2d.SelectComponentList@endlink) </param>
    ## <param name="snap_type"> (@link NXOpen.InferSnapType.SnapType NXOpen.InferSnapType.SnapType@endlink)   snap point type</param>
    ## <param name="selection1"> (@link Component NXOpen.Layout2d.Component@endlink)  first selected object </param>
    ## <param name="view1"> (@link NXOpen.View NXOpen.View@endlink)  first selected object view</param>
    ## <param name="point1"> (@link NXOpen.Point3d NXOpen.Point3d@endlink) first  selected object point</param>
    ## <param name="selection2"> (@link Component NXOpen.Layout2d.Component@endlink)  second selected object </param>
    ## <param name="view2"> (@link NXOpen.View NXOpen.View@endlink) second  selected object view</param>
    ## <param name="point2"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  second selected object point</param>
    @overload
    def Add(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: Component, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: Component, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
        """
         The object being selected with the objects view and objects point and snap information.
            
         @return added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    
    ##  The object being selected with CAE set object information.
    ##     
    ##  @return added (bool):  True if successfully added all objects to the list;
    ##                                   False if there was at least one object that was already a
    ##                                   member of the list and duplicates are not allowed .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use other versions of @link NXOpen::SelectObjectList::Add NXOpen::SelectObjectList::Add@endlink .  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectComponentList NXOpen.Layout2d.SelectComponentList@endlink) </param>
    ## <param name="selection"> (@link Component NXOpen.Layout2d.Component@endlink)  selected object </param>
    ## <param name="cae_sub_type"> (@link NXOpen.CaeObjectType.CaeSubType NXOpen.CaeObjectType.CaeSubType@endlink)  CAE set object sub type</param>
    ## <param name="cae_sub_id"> (int)  CAE set object sub id</param>
    @overload
    def Add(self, selection: Component, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> bool:
        """
         The object being selected with CAE set object information.
            
         @return added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    
    ##  Removes all items from the list.
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def Clear(self) -> None:
        """
         Removes all items from the list.
            
        """
        pass
    
    ##  Returns whether the specified object is already in the list or not.
    ##     
    ##  @return list_contains (bool):  true if object is in the list, false otherwise .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objectValue"> (@link Component NXOpen.Layout2d.Component@endlink)  object to check </param>
    def Contains(self, objectValue: Component) -> bool:
        """
         Returns whether the specified object is already in the list or not.
            
         @return list_contains (bool):  true if object is in the list, false otherwise .
        """
        pass
    
    ##  Returns the list of objects in the selection list.
    ##     
    ##  @return objects (@link Component List[NXOpen.Layout2d.Component]@endlink):  items in list .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetArray(self) -> List[Component]:
        """
         Returns the list of objects in the selection list.
            
         @return objects (@link Component List[NXOpen.Layout2d.Component]@endlink):  items in list .
        """
        pass
    
    ##  Returns the list of SelectObjects in the selection list.
    ##     
    ##  @return objects (@link NXOpen.SelectObject List[NXOpen.SelectObject]@endlink):  items in list .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetSelectObjectArray(self) -> List[NXOpen.SelectObject]:
        """
         Returns the list of SelectObjects in the selection list.
            
         @return objects (@link NXOpen.SelectObject List[NXOpen.SelectObject]@endlink):  items in list .
        """
        pass
    
    ##  Remove specified object from list.
    ##     
    ##  @return removed (bool):  True if successfully removed from list;
    ##                                     False if the object was not a member of the list .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectComponentList NXOpen.Layout2d.SelectComponentList@endlink) </param>
    ## <param name="objectValue"> (@link Component NXOpen.Layout2d.Component@endlink)  Object to remove </param>
    @overload
    def Remove(self, objectValue: Component) -> bool:
        """
         Remove specified object from list.
            
         @return removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    
    ##  Remove specified objects from list.
    ##     
    ##  @return removed (bool):  True if successfully removed from list;
    ##                                     False if the object was not a member of the list .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objects"> (@link Component List[NXOpen.Layout2d.Component]@endlink)  Objects to remove </param>
    def RemoveArray(self, objects: List[Component]) -> bool:
        """
         Remove specified objects from list.
            
         @return removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    
    ##  Remove specified object from list.
    ##     
    ##  @return removed (bool):  True if successfully removed from list;
    ##                                     False if the object / view was not a member of the list .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectComponentList NXOpen.Layout2d.SelectComponentList@endlink) </param>
    ## <param name="objectValue"> (@link Component NXOpen.Layout2d.Component@endlink)  Object to remove </param>
    ## <param name="view"> (@link NXOpen.View NXOpen.View@endlink)  with this view</param>
    @overload
    def Remove(self, objectValue: Component, view: NXOpen.View) -> bool:
        """
         Remove specified object from list.
            
         @return removed (bool):  True if successfully removed from list;
                                            False if the object / view was not a member of the list .
        """
        pass
    
    ##  Remove specified object from list.
    ##     
    ##  @return removed (bool):  True if successfully removed from list;
    ##                                     False if the object was not a member of the list .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectComponentList NXOpen.Layout2d.SelectComponentList@endlink) </param>
    ## <param name="snap_type"> (@link NXOpen.InferSnapType.SnapType NXOpen.InferSnapType.SnapType@endlink)   snap point type</param>
    ## <param name="selection1"> (@link Component NXOpen.Layout2d.Component@endlink)  first selected object </param>
    ## <param name="view1"> (@link NXOpen.View NXOpen.View@endlink)  first selected object view</param>
    ## <param name="point1"> (@link NXOpen.Point3d NXOpen.Point3d@endlink) first  selected object point</param>
    ## <param name="selection2"> (@link Component NXOpen.Layout2d.Component@endlink)  second selected object </param>
    ## <param name="view2"> (@link NXOpen.View NXOpen.View@endlink) second  selected object view</param>
    ## <param name="point2"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  second selected object point</param>
    @overload
    def Remove(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: Component, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: Component, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
        """
         Remove specified object from list.
            
         @return removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    
    ##  Removes the objects from a SelectionMethod from the list
    ##     
    ##  @return removed (bool):  True if successfully removed all objects from the list;
    ##                                     False if there was at least one object that was not a
    ##                                     member of the list .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectComponentList NXOpen.Layout2d.SelectComponentList@endlink) </param>
    ## <param name="input_selection_method"> (@link NXOpen.SelectionMethod NXOpen.SelectionMethod@endlink)  selection method containing objects to add </param>
    @overload
    def Remove(self, input_selection_method: NXOpen.SelectionMethod) -> bool:
        """
         Removes the objects from a SelectionMethod from the list
            
         @return removed (bool):  True if successfully removed all objects from the list;
                                            False if there was at least one object that was not a
                                            member of the list .
        """
        pass
    
    ##  Sets the list of objects in the selection list. This will clear any existing
    ##     items in the list.
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objects"> (@link Component List[NXOpen.Layout2d.Component]@endlink)  items to put in the list</param>
    def SetArray(self, objects: List[Component]) -> None:
        """
         Sets the list of objects in the selection list. This will clear any existing
            items in the list.
            
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a single object selection.

## 
##   <br>  Created in NX5.0.0  <br> 

class SelectComponent(NXOpen.TaggedObject): 
    """ Represents a single object selection.
"""


    ## Getter for property: (@link Component NXOpen.Layout2d.Component@endlink) Value
    ##  Returns the object being selected
    ##       
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return Component
    @property
    def Value(self) -> Component:
        """
        Getter for property: (@link Component NXOpen.Layout2d.Component@endlink) Value
         Returns the object being selected
              
            
         
        """
        pass
    
    ## Setter for property: (@link Component NXOpen.Layout2d.Component@endlink) Value

    ##  Returns the object being selected
    ##       
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Value.setter
    def Value(self, selection: Component):
        """
        Setter for property: (@link Component NXOpen.Layout2d.Component@endlink) Value
         Returns the object being selected
              
            
         
        """
        pass
    
    ##  The object being selected with the object's view and point.
    ##     
    ##  @return A tuple consisting of (selection, view, point). 
    ##  - selection is: @link Component NXOpen.Layout2d.Component@endlink. selected object .
    ##  - view is: @link NXOpen.View NXOpen.View@endlink. selected object view.
    ##  - point is: @link NXOpen.Point3d NXOpen.Point3d@endlink. selected object point.

    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectComponent NXOpen.Layout2d.SelectComponent@endlink) </param>
    @overload
    def GetValue(self) -> Tuple[Component, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         @return A tuple consisting of (selection, view, point). 
         - selection is: @link Component NXOpen.Layout2d.Component@endlink. selected object .
         - view is: @link NXOpen.View NXOpen.View@endlink. selected object view.
         - point is: @link NXOpen.Point3d NXOpen.Point3d@endlink. selected object point.

        """
        pass
    
    ##  The object being selected with the objects view and point and snap information.
    ##     
    ##  @return A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
    ##  - snap_type is: @link NXOpen.InferSnapType.SnapType NXOpen.InferSnapType.SnapType@endlink.  snap point type.
    ##  - selection1 is: @link Component NXOpen.Layout2d.Component@endlink. first selected object .
    ##  - view1 is: @link NXOpen.View NXOpen.View@endlink. first selected object view.
    ##  - point1 is: @link NXOpen.Point3d NXOpen.Point3d@endlink. first selected object point.
    ##  - selection2 is: @link Component NXOpen.Layout2d.Component@endlink. second selected object .
    ##  - view2 is: @link NXOpen.View NXOpen.View@endlink. second selected object view.
    ##  - point2 is: @link NXOpen.Point3d NXOpen.Point3d@endlink. second selected object point.

    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectComponent NXOpen.Layout2d.SelectComponent@endlink) </param>
    @overload
    def GetValue(self) -> Tuple[NXOpen.InferSnapType.SnapType, Component, NXOpen.View, NXOpen.Point3d, Component, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the objects view and point and snap information.
            
         @return A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
         - snap_type is: @link NXOpen.InferSnapType.SnapType NXOpen.InferSnapType.SnapType@endlink.  snap point type.
         - selection1 is: @link Component NXOpen.Layout2d.Component@endlink. first selected object .
         - view1 is: @link NXOpen.View NXOpen.View@endlink. first selected object view.
         - point1 is: @link NXOpen.Point3d NXOpen.Point3d@endlink. first selected object point.
         - selection2 is: @link Component NXOpen.Layout2d.Component@endlink. second selected object .
         - view2 is: @link NXOpen.View NXOpen.View@endlink. second selected object view.
         - point2 is: @link NXOpen.Point3d NXOpen.Point3d@endlink. second selected object point.

        """
        pass
    
    ##  The object being selected with CAE set object information.
    ##     
    ##  @return A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
    ##  - selection is: @link Component NXOpen.Layout2d.Component@endlink. selected object .
    ##  - cae_sub_type is: @link NXOpen.CaeObjectType.CaeSubType NXOpen.CaeObjectType.CaeSubType@endlink. CAE set object sub type.
    ##  - cae_sub_id is: int. CAE set object sub id.

    ## 
    ##   <br>  Created in NX5.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use other versions of @link NXOpen::SelectObject::GetValue NXOpen::SelectObject::GetValue@endlink .  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectComponent NXOpen.Layout2d.SelectComponent@endlink) </param>
    @overload
    def GetValue(self) -> Tuple[Component, NXOpen.CaeObjectType.CaeSubType, int]:
        """
         The object being selected with CAE set object information.
            
         @return A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
         - selection is: @link Component NXOpen.Layout2d.Component@endlink. selected object .
         - cae_sub_type is: @link NXOpen.CaeObjectType.CaeSubType NXOpen.CaeObjectType.CaeSubType@endlink. CAE set object sub type.
         - cae_sub_id is: int. CAE set object sub id.

        """
        pass
    
    ##  The object being selected with the object's view and object's point
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectComponent NXOpen.Layout2d.SelectComponent@endlink) </param>
    ## <param name="selection"> (@link Component NXOpen.Layout2d.Component@endlink)  selected object </param>
    ## <param name="view"> (@link NXOpen.View NXOpen.View@endlink)  selected object view</param>
    ## <param name="point"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  selected object point</param>
    @overload
    def SetValue(self, selection: Component, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         The object being selected with the object's view and object's point
            
        """
        pass
    
    ##  The object being selected with the objects view and objects point and snap information.
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectComponent NXOpen.Layout2d.SelectComponent@endlink) </param>
    ## <param name="snap_type"> (@link NXOpen.InferSnapType.SnapType NXOpen.InferSnapType.SnapType@endlink)   snap point type</param>
    ## <param name="selection1"> (@link Component NXOpen.Layout2d.Component@endlink)  first selected object </param>
    ## <param name="view1"> (@link NXOpen.View NXOpen.View@endlink)  first selected object view</param>
    ## <param name="point1"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  first selected object point</param>
    ## <param name="selection2"> (@link Component NXOpen.Layout2d.Component@endlink)  second selected object </param>
    ## <param name="view2"> (@link NXOpen.View NXOpen.View@endlink)  second selected object view</param>
    ## <param name="point2"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  second selected object point</param>
    @overload
    def SetValue(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: Component, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: Component, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
        """
         The object being selected with the objects view and objects point and snap information.
            
        """
        pass
    
    ##  The object being selected with CAE set object information.
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use other versions of @link NXOpen::SelectObject::SetValue NXOpen::SelectObject::SetValue@endlink .  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectComponent NXOpen.Layout2d.SelectComponent@endlink) </param>
    ## <param name="selection"> (@link Component NXOpen.Layout2d.Component@endlink)  selected object </param>
    ## <param name="cae_sub_type"> (@link NXOpen.CaeObjectType.CaeSubType NXOpen.CaeObjectType.CaeSubType@endlink)  CAE set object sub type</param>
    ## <param name="cae_sub_id"> (int)  CAE set object sub id</param>
    @overload
    def SetValue(self, selection: Component, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> None:
        """
         The object being selected with CAE set object information.
            
        """
        pass
    
import NXOpen
##  Represents a Builder for Smash 2D Component functionality which will break instances
##      *  of 2D Components into its constituent pieces, we can have multiple committed objects  <br> To create a new instance of this class, use @link NXOpen::Layout2d::ComponentCollection::CreateSmashComponentBuilder  NXOpen::Layout2d::ComponentCollection::CreateSmashComponentBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class SmashComponentBuilder(NXOpen.Builder): 
    """ Represents a Builder for Smash 2D Component functionality which will break instances
     *  of 2D Components into its constituent pieces, we can have multiple committed objects """


    ## Getter for property: (@link SelectComponentList NXOpen.Layout2d.SelectComponentList@endlink) Components
    ##  Returns the select 2D Component instances to smash   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return SelectComponentList
    @property
    def Components(self) -> SelectComponentList:
        """
        Getter for property: (@link SelectComponentList NXOpen.Layout2d.SelectComponentList@endlink) Components
         Returns the select 2D Component instances to smash   
            
         
        """
        pass
    
## @package NXOpen.Layout2d
## Classes, Enums and Structs under NXOpen.Layout2d namespace

##  @link AssociativeAssemblyBuilderUpdateDirection NXOpen.Layout2d.AssociativeAssemblyBuilderUpdateDirection @endlink is an alias for @link AssociativeAssemblyBuilder.UpdateDirection NXOpen.Layout2d.AssociativeAssemblyBuilder.UpdateDirection@endlink
AssociativeAssemblyBuilderUpdateDirection = AssociativeAssemblyBuilder.UpdateDirection


##  @link ConvertLayoutToSheetBuilderSheetProjectionAngleType NXOpen.Layout2d.ConvertLayoutToSheetBuilderSheetProjectionAngleType @endlink is an alias for @link ConvertLayoutToSheetBuilder.SheetProjectionAngleType NXOpen.Layout2d.ConvertLayoutToSheetBuilder.SheetProjectionAngleType@endlink
ConvertLayoutToSheetBuilderSheetProjectionAngleType = ConvertLayoutToSheetBuilder.SheetProjectionAngleType


##  @link CreateComponentFrom3DBuilderCreateMethod NXOpen.Layout2d.CreateComponentFrom3DBuilderCreateMethod @endlink is an alias for @link CreateComponentFrom3DBuilder.CreateMethod NXOpen.Layout2d.CreateComponentFrom3DBuilder.CreateMethod@endlink
CreateComponentFrom3DBuilderCreateMethod = CreateComponentFrom3DBuilder.CreateMethod


##  @link InheritDisplayAttributesBuilderInheritDirection NXOpen.Layout2d.InheritDisplayAttributesBuilderInheritDirection @endlink is an alias for @link InheritDisplayAttributesBuilder.InheritDirection NXOpen.Layout2d.InheritDisplayAttributesBuilder.InheritDirection@endlink
InheritDisplayAttributesBuilderInheritDirection = InheritDisplayAttributesBuilder.InheritDirection


