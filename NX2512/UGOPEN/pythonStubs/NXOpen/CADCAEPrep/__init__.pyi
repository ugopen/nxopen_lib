from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
class BeamSectionBar(IBeamSection): 
    """ Bar sections. """
    @property
    def H(self) -> float:
        """
        Getter for property: (float) H
         Returns the height   
            
         
        """
        pass
    @property
    def W(self) -> float:
        """
        Getter for property: (float) W
         Returns the width   
            
         
        """
        pass
    def Edit(self, width: float, height: float) -> None:
        """
         Edit the section parameters 
        """
        pass
class BeamSectionBox(IBeamSection): 
    """ Box sections. """
    @property
    def H(self) -> float:
        """
        Getter for property: (float) H
         Returns the height   
            
         
        """
        pass
    @property
    def Tss(self) -> float:
        """
        Getter for property: (float) Tss
         Returns the thickness sides   
            
         
        """
        pass
    @property
    def Ttb(self) -> float:
        """
        Getter for property: (float) Ttb
         Returns the thickness top-bottom   
            
         
        """
        pass
    @property
    def W(self) -> float:
        """
        Getter for property: (float) W
         Returns the width   
            
         
        """
        pass
    def Edit(self, width: float, height: float, thicknessTopBottom: float, thicknessSides: float) -> None:
        """
         Edit the section parameters 
        """
        pass
class BeamSectionChan(IBeamSection): 
    """ Chan sections. """
    @property
    def H(self) -> float:
        """
        Getter for property: (float) H
         Returns the height   
            
         
        """
        pass
    @property
    def Tf(self) -> float:
        """
        Getter for property: (float) Tf
         Returns the flange thickness   
            
         
        """
        pass
    @property
    def Tw(self) -> float:
        """
        Getter for property: (float) Tw
         Returns the web thickness   
            
         
        """
        pass
    @property
    def W(self) -> float:
        """
        Getter for property: (float) W
         Returns the width   
            
         
        """
        pass
    def Edit(self, width: float, height: float, webThickness: float, flangeThickness: float) -> None:
        """
         Edit the section parameters 
        """
        pass
class BeamSectionHexa(IBeamSection): 
    """ Hexa sections. """
    @property
    def H(self) -> float:
        """
        Getter for property: (float) H
         Returns the height   
            
         
        """
        pass
    @property
    def W(self) -> float:
        """
        Getter for property: (float) W
         Returns the overall width   
            
         
        """
        pass
    @property
    def Ws(self) -> float:
        """
        Getter for property: (float) Ws
         Returns the side width   
            
         
        """
        pass
    def Edit(self, sideWidth: float, overallWidth: float, height: float) -> None:
        """
         Edit the section parameters 
        """
        pass
class BeamSectionI(IBeamSection): 
    """ I sections. """
    @property
    def H(self) -> float:
        """
        Getter for property: (float) H
         Returns the height   
            
         
        """
        pass
    @property
    def Tbf(self) -> float:
        """
        Getter for property: (float) Tbf
         Returns the bottom flange thickness   
            
         
        """
        pass
    @property
    def Ttf(self) -> float:
        """
        Getter for property: (float) Ttf
         Returns the top flange thickness   
            
         
        """
        pass
    @property
    def Tw(self) -> float:
        """
        Getter for property: (float) Tw
         Returns the web thickness   
            
         
        """
        pass
    @property
    def Wbf(self) -> float:
        """
        Getter for property: (float) Wbf
         Returns the bottom flange width   
            
         
        """
        pass
    @property
    def Wtf(self) -> float:
        """
        Getter for property: (float) Wtf
         Returns the top flange width   
            
         
        """
        pass
    def Edit(self, height: float, widthBottomFlange: float, widthTopFlange: float, thicknessWeb: float, thicknessBottomFlange: float, thicknessTopFlange: float) -> None:
        """
         Edit the section parameters 
        """
        pass
class BeamSectionL(IBeamSection): 
    """ L sections. """
    @property
    def Lh(self) -> float:
        """
        Getter for property: (float) Lh
         Returns the horizontal length   
            
         
        """
        pass
    @property
    def Lv(self) -> float:
        """
        Getter for property: (float) Lv
         Returns the vertical length   
            
         
        """
        pass
    @property
    def Th(self) -> float:
        """
        Getter for property: (float) Th
         Returns the horizontal thickness   
            
         
        """
        pass
    @property
    def Tv(self) -> float:
        """
        Getter for property: (float) Tv
         Returns the vertical thickness   
            
         
        """
        pass
    def Edit(self, lengthVertical: float, lengthHorizontal: float, thicknessHorizontal: float, thicknessVertical: float) -> None:
        """
         Edit the section parameters 
        """
        pass
class BeamSectionRod(IBeamSection): 
    """ Rod sections. """
    @property
    def R(self) -> float:
        """
        Getter for property: (float) R
         Returns the radius   
            
         
        """
        pass
    def Edit(self, radius: float) -> None:
        """
         Edit the section parameters 
        """
        pass
import NXOpen
class BeamSectionSketch(IBeamSection): 
    """ Sketch sections. """
    @property
    def OriginBoundingBoxCenterOffset(self) -> NXOpen.Point2d:
        """
        Getter for property: ( NXOpen.Point2d) OriginBoundingBoxCenterOffset
         Returns the offset between the origin and the center of the bounding box   
            
         
        """
        pass
    @property
    def Sketch(self) -> NXOpen.Sketch:
        """
        Getter for property: ( NXOpen.Sketch) Sketch
         Returns the sketch   
            
         
        """
        pass
    def Edit(self, sketch: NXOpen.Sketch) -> None:
        """
         Edit the section parameters 
        """
        pass
class BeamSectionTube(IBeamSection): 
    """ Tube sections. """
    @property
    def Ri(self) -> float:
        """
        Getter for property: (float) Ri
         Returns the inside radius   
            
         
        """
        pass
    @property
    def Ro(self) -> float:
        """
        Getter for property: (float) Ro
         Returns the outside radius   
            
         
        """
        pass
    def Edit(self, radiusOutside: float, radiusInside: float) -> None:
        """
         Edit the section parameters 
        """
        pass
class BeamSectionT(IBeamSection): 
    """ T sections. """
    @property
    def H(self) -> float:
        """
        Getter for property: (float) H
         Returns the height   
            
         
        """
        pass
    @property
    def Tf(self) -> float:
        """
        Getter for property: (float) Tf
         Returns the flange thickness   
            
         
        """
        pass
    @property
    def Tw(self) -> float:
        """
        Getter for property: (float) Tw
         Returns the web thickness   
            
         
        """
        pass
    @property
    def W(self) -> float:
        """
        Getter for property: (float) W
         Returns the width   
            
         
        """
        pass
    def Edit(self, width: float, height: float, flangeThickness: float, webThickness: float) -> None:
        """
         Edit the section parameters 
        """
        pass
import NXOpen
class IBeamSectionCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of IBeamSections """
    pass
import NXOpen
class IBeamSection(NXOpen.NXObject): 
    """ Base abstract class for beam sections. """
    class Sectiontype(Enum):
        """
        Members Include: 
         |Unknown| 
         |Sketch| 
         |Rod| 
         |Tube| 
         |Hexa| 
         |Bar| 
         |Box| 
         |T| 
         |L| 
         |I| 
         |Chan| 

        """
        Unknown: int
        Sketch: int
        Rod: int
        Tube: int
        Hexa: int
        Bar: int
        Box: int
        T: int
        L: int
        I: int
        Chan: int
        @staticmethod
        def ValueOf(value: int) -> IBeamSection.Sectiontype:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the section name   
            
         
        """
        pass
    @property
    def Type(self) -> IBeamSection.Sectiontype:
        """
        Getter for property: ( IBeamSection.Sectiontype NXOpen.C) Type
         Returns the section type   
            
         
        """
        pass
import NXOpen
class IdealizedBeamCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of IdealizedBeams """
    pass
import NXOpen
class IdealizedBeamManager(NXOpen.Object): 
    """ The object containing the information about the IdealizedBeamManager to be modified."""
    @property
    def IBeamSectionCollection() -> IBeamSectionCollection:
        """
         Returns the  NXOpen::CADCAEPrep::IBeamSectionCollection  belonging to this 
        """
        pass
    @property
    def IdealizedBeamCollection() -> IdealizedBeamCollection:
        """
         Returns the  NXOpen::CADCAEPrep::IdealizedBeamCollection  belonging to this 
        """
        pass
    def AddBeamSectionBar(self, sectionName: str, width: float, height: float) -> BeamSectionBar:
        """
         Add a beam section Bar 
         Returns section ( BeamSectionBar NXOpen.C):  the new section .
        """
        pass
    def AddBeamSectionBox(self, sectionName: str, width: float, height: float, thicknessTopBottom: float, thicknessSides: float) -> BeamSectionBox:
        """
         Add a beam section Box
         Returns section ( BeamSectionBox NXOpen.C):  the new section .
        """
        pass
    def AddBeamSectionChan(self, sectionName: str, width: float, height: float, flangeThickness: float, webThickness: float) -> BeamSectionChan:
        """
         Add a beam section Chan
         Returns section ( BeamSectionChan NXOpen.C):  the new section .
        """
        pass
    def AddBeamSectionHexa(self, sectionName: str, sideWidth: float, overallWidth: float, height: float) -> BeamSectionHexa:
        """
         Add a beam section Hexa
         Returns section ( BeamSectionHexa NXOpen.C):  the new section .
        """
        pass
    def AddBeamSectionI(self, sectionName: str, height: float, widthBottomFlange: float, widthTopFlange: float, thicknessWeb: float, thicknessBottomFlange: float, thicknessTopFlange: float) -> BeamSectionI:
        """
         Add a beam section I 
         Returns section ( BeamSectionI NXOpen.C):  the new section .
        """
        pass
    def AddBeamSectionL(self, sectionName: str, lengthVertical: float, lengthHorizontal: float, thicknessVertical: float, thicknessHorizontal: float) -> BeamSectionL:
        """
         Add a beam section L 
         Returns section ( BeamSectionL NXOpen.C):  the new section .
        """
        pass
    def AddBeamSectionRod(self, sectionName: str, radius: float) -> BeamSectionRod:
        """
         Add a beam section Rod
         Returns section ( BeamSectionRod NXOpen.C):  the new section .
        """
        pass
    def AddBeamSectionSketch(self, sectionName: str, sketchTag: NXOpen.Sketch) -> BeamSectionSketch:
        """
         Add a beam section Sketch 
         Returns section ( BeamSectionSketch NXOpen.C):  the new section .
        """
        pass
    def AddBeamSectionT(self, sectionName: str, width: float, height: float, flangeThickness: float, webThickness: float) -> BeamSectionT:
        """
         Add a beam section T
         Returns section ( BeamSectionT NXOpen.C):  the new section .
        """
        pass
    def AddBeamSectionTube(self, sectionName: str, radiusOutside: float, radiusInside: float) -> BeamSectionTube:
        """
         Add a beam section Tube 
         Returns section ( BeamSectionTube NXOpen.C):  the new section .
        """
        pass
    def AddIdealizedBeam(self, curve: NXOpen.Curve) -> IdealizedBeam:
        """
         Add an idealized beam 
         Returns idealizedBeam ( IdealizedBeam NXOpen.C):  the new idealized beam .
        """
        pass
    def GetIdealizedBeam(self, curve: NXOpen.Curve) -> IdealizedBeam:
        """
         Get idealized beam from curve 
         Returns ibeam ( IdealizedBeam NXOpen.C):  the idealized beam .
        """
        pass
    def GetSection(self, sectionName: str) -> IBeamSection:
        """
         Get section by name 
         Returns section ( IBeamSection NXOpen.C):  the section .
        """
        pass
import NXOpen
class IdealizedBeam(NXOpen.NXObject): 
    """ The object containing the information about the IdealizedBeam to be modified."""
    @property
    def Curve(self) -> NXOpen.Curve:
        """
        Getter for property: ( NXOpen.Curve) Curve
         Returns the associated curve    
            
         
        """
        pass
    @property
    def Material(self) -> NXOpen.PhysicalMaterial:
        """
        Getter for property: ( NXOpen.PhysicalMaterial) Material
         Returns the physical material   
            
         
        """
        pass
    @Material.setter
    def Material(self, material: NXOpen.PhysicalMaterial):
        """
        Setter for property: ( NXOpen.PhysicalMaterial) Material
         Returns the physical material   
            
         
        """
        pass
    @property
    def MaterialBody(self) -> NXOpen.Body:
        """
        Getter for property: ( NXOpen.Body) MaterialBody
         Returns the associated body used to infer the material   
            
         
        """
        pass
    @MaterialBody.setter
    def MaterialBody(self, body: NXOpen.Body):
        """
        Setter for property: ( NXOpen.Body) MaterialBody
         Returns the associated body used to infer the material   
            
         
        """
        pass
    @property
    def MeshCollectorPrefix(self) -> str:
        """
        Getter for property: (str) MeshCollectorPrefix
         Returns the mesh collector prefix.  
           
                        The mesh collector prefix will be used to create the name of the mesh collector.
                        If several idealized beams share the same mesh collector prefix, all the resulting meshes will be put in the same collector.
                      
         
        """
        pass
    @MeshCollectorPrefix.setter
    def MeshCollectorPrefix(self, meshCollectorPrefix: str):
        """
        Setter for property: (str) MeshCollectorPrefix
         Returns the mesh collector prefix.  
           
                        The mesh collector prefix will be used to create the name of the mesh collector.
                        If several idealized beams share the same mesh collector prefix, all the resulting meshes will be put in the same collector.
                      
         
        """
        pass
    @property
    def OffsetEnd(self) -> NXOpen.Point2d:
        """
        Getter for property: ( NXOpen.Point2d) OffsetEnd
         Returns the OffsetEnd: 
                        Offset from the center of the bounding box to the curve end point, in the cross-section CSYS.  
          
                      
         
        """
        pass
    @OffsetEnd.setter
    def OffsetEnd(self, offsetEnd: NXOpen.Point2d):
        """
        Setter for property: ( NXOpen.Point2d) OffsetEnd
         Returns the OffsetEnd: 
                        Offset from the center of the bounding box to the curve end point, in the cross-section CSYS.  
          
                      
         
        """
        pass
    @property
    def OffsetStart(self) -> NXOpen.Point2d:
        """
        Getter for property: ( NXOpen.Point2d) OffsetStart
         Returns the OffsetStart: 
                        Offset from the center of the bounding box to the curve start point, in the cross-section CSYS.  
          
                      
         
        """
        pass
    @OffsetStart.setter
    def OffsetStart(self, offsetStart: NXOpen.Point2d):
        """
        Setter for property: ( NXOpen.Point2d) OffsetStart
         Returns the OffsetStart: 
                        Offset from the center of the bounding box to the curve start point, in the cross-section CSYS.  
          
                      
         
        """
        pass
    @property
    def Section(self) -> IBeamSection:
        """
        Getter for property: ( IBeamSection NXOpen.C) Section
         Returns the section   
            
         
        """
        pass
    @Section.setter
    def Section(self, section: IBeamSection):
        """
        Setter for property: ( IBeamSection NXOpen.C) Section
         Returns the section   
            
         
        """
        pass
    @property
    def XOffsetEnd(self) -> float:
        """
        Getter for property: (float) XOffsetEnd
         Returns the XOffsetEnd:
                        the offset along the curve on end point side; Positive means inside the curve, negative means outside the curve (along the tangent).  
          
                      
         
        """
        pass
    @XOffsetEnd.setter
    def XOffsetEnd(self, xOffsetEnd: float):
        """
        Setter for property: (float) XOffsetEnd
         Returns the XOffsetEnd:
                        the offset along the curve on end point side; Positive means inside the curve, negative means outside the curve (along the tangent).  
          
                      
         
        """
        pass
    @property
    def XOffsetStart(self) -> float:
        """
        Getter for property: (float) XOffsetStart
         Returns the XOffsetStart:
                        the offset along the curve on start point side; Positive means inside the curve, negative means outside the curve (along the tangent).  
          
                      
         
        """
        pass
    @XOffsetStart.setter
    def XOffsetStart(self, xOffsetStart: float):
        """
        Setter for property: (float) XOffsetStart
         Returns the XOffsetStart:
                        the offset along the curve on start point side; Positive means inside the curve, negative means outside the curve (along the tangent).  
          
                      
         
        """
        pass
    def GetOrientationByVector(self) -> Tuple[NXOpen.Vector3d, OrientationByVector.OrientAxis, bool, bool]:
        """
         The orientation by vector:
                         The section orientation is determined by the 3d vector parameter OrienVect that corresponds to either the Y axis or Z axis depending on the OrientAxis parameter.
                         The coordinate system of the section is determined as follows:
                            Its X axis correspond to the tagent to the curve
                            Its Y or Z axis direction is given by the projection of OrientVect onto the Y,Z plane. As a consequence OrientVect should not be parallel to X.
                            OrientAxis (ether Y or Z): indicates if the OrientVect is the Y or Z axis
                            IOrientation::FlipY (boolean): flips the section around the Y axis
                            IOrientation::FlipZ (boolean): flips the section around the Z axis             
         Returns A tuple consisting of (orientVect, orientAxis, flipY, flipZ). 
         - orientVect is:  NXOpen.Vector3d.
         - orientAxis is:  OrientationByVector.OrientAxis NXOpen.C.
         - flipY is: bool.
         - flipZ is: bool.

        """
        pass
    def SetOrientationByVector(self, orientVect: NXOpen.Vector3d, orientAxis: OrientationByVector.OrientAxis, flipY: bool, flipZ: bool) -> None:
        """
         Set the orientation by vector 
                         The section orientation is determined by the 3d vector parameter OrienVect that corresponds to either the Y axis or Z axis depending on the OrientAxis parameter.
                         The coordinate system of the section is determined as follows:
                            Its X axis correspond to the tagent to the curve
                            Its Y or Z axis direction is given by the projection of OrientVect onto the Y,Z plane. As a consequence OrientVect should not be parallel to X.
                            OrientAxis (ether Y or Z): indicates if the OrientVect is the Y or Z axis
                            IOrientation::FlipY (boolean): flips the section around the Y axis
                            IOrientation::FlipZ (boolean): flips the section around the Z axis             
        """
        pass
import NXOpen
class IOrientation(NXOpen.NXObject): 
    """ The object containing the information about the IOrientation. """
    pass
class OrientationByVector(IOrientation): 
    """ The object containing the information about the OrientationByVector."""
    class OrientAxis(Enum):
        """
        Members Include: 
         |Y|  Orient Axis along Y 
         |Z|  Orient Axis along Z 

        """
        Y: int
        Z: int
        @staticmethod
        def ValueOf(value: int) -> OrientationByVector.OrientAxis:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
