from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class AdvancedFlangeBuilder(SheetmetalBaseBuilder): 
    """ Represents a Features.SheetMetal.AdvancedFlangeBuilder """
    class Insets(Enum):
        """
        Members Include: 
         |MaterialInside| 
         |MaterialOutside| 
         |BendOutside| 
         |MaterialInsideOML| 

        """
        MaterialInside: int
        MaterialOutside: int
        BendOutside: int
        MaterialInsideOML: int
        @staticmethod
        def ValueOf(value: int) -> AdvancedFlangeBuilder.Insets:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LengthReferences(Enum):
        """
        Members Include: 
         |Inside| 
         |Outside| 
         |Web| 
         |Din6935|  This represents 'Tangent' option on Advanced Flange dialog from nx12.0.2 onwards

        """
        Inside: int
        Outside: int
        Web: int
        Din6935: int
        @staticmethod
        def ValueOf(value: int) -> AdvancedFlangeBuilder.LengthReferences:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |ByValue| 
         |ToReference| 

        """
        ByValue: int
        ToReference: int
        @staticmethod
        def ValueOf(value: int) -> AdvancedFlangeBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Angle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Angle
         Returns the angle   
            
         
        """
        pass
    @property
    def BendOptions(self) -> BendOptions:
        """
        Getter for property: ( BendOptions NXOpen.Featu) BendOptions
         Returns the  Sheet Metal Bend Options   
            
         
        """
        pass
    @property
    def Edges(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) Edges
         Returns the base edge for the advanced flange.  
            
         
        """
        pass
    @property
    def EndAdjustment(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EndAdjustment
         Returns the flat pattern compensation adjustment at end of the flange   
            
         
        """
        pass
    @property
    def Faces(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) Faces
         Returns the  reference face for advanced flange   
            
         
        """
        pass
    @property
    def FlatPatternCompensationAtEnd(self) -> bool:
        """
        Getter for property: (bool) FlatPatternCompensationAtEnd
         Returns the  option to apply flat pattern compensation at end of the flange   
            
         
        """
        pass
    @FlatPatternCompensationAtEnd.setter
    def FlatPatternCompensationAtEnd(self, flatPatternCompensationAtEnd: bool):
        """
        Setter for property: (bool) FlatPatternCompensationAtEnd
         Returns the  option to apply flat pattern compensation at end of the flange   
            
         
        """
        pass
    @property
    def FlatPatternCompensationAtStart(self) -> bool:
        """
        Getter for property: (bool) FlatPatternCompensationAtStart
         Returns the  option to apply flat pattern compensation at start of the flange  
            
         
        """
        pass
    @FlatPatternCompensationAtStart.setter
    def FlatPatternCompensationAtStart(self, flatPatternCompensationAtStart: bool):
        """
        Setter for property: (bool) FlatPatternCompensationAtStart
         Returns the  option to apply flat pattern compensation at start of the flange  
            
         
        """
        pass
    @property
    def InferLength(self) -> bool:
        """
        Getter for property: (bool) InferLength
         Returns the infer length option   
            
         
        """
        pass
    @InferLength.setter
    def InferLength(self, inferLength: bool):
        """
        Setter for property: (bool) InferLength
         Returns the infer length option   
            
         
        """
        pass
    @property
    def Inset(self) -> AdvancedFlangeBuilder.Insets:
        """
        Getter for property: ( AdvancedFlangeBuilder.Insets NXOpen.Featu) Inset
         Returns the inset type   
            
         
        """
        pass
    @Inset.setter
    def Inset(self, inset: AdvancedFlangeBuilder.Insets):
        """
        Setter for property: ( AdvancedFlangeBuilder.Insets NXOpen.Featu) Inset
         Returns the inset type   
            
         
        """
        pass
    @property
    def Length(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Length
         Returns the length   
            
         
        """
        pass
    @property
    def LengthReference(self) -> AdvancedFlangeBuilder.LengthReferences:
        """
        Getter for property: ( AdvancedFlangeBuilder.LengthReferences NXOpen.Featu) LengthReference
         Returns the length reference   
            
         
        """
        pass
    @LengthReference.setter
    def LengthReference(self, lengthReference: AdvancedFlangeBuilder.LengthReferences):
        """
        Setter for property: ( AdvancedFlangeBuilder.LengthReferences NXOpen.Featu) LengthReference
         Returns the length reference   
            
         
        """
        pass
    @property
    def Plane1(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) Plane1
         Returns the first plane for the end limits   
            
         
        """
        pass
    @Plane1.setter
    def Plane1(self, plane1: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) Plane1
         Returns the first plane for the end limits   
            
         
        """
        pass
    @property
    def Plane2(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) Plane2
         Returns the second plane for the end limits   
            
         
        """
        pass
    @Plane2.setter
    def Plane2(self, plane2: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) Plane2
         Returns the second plane for the end limits   
            
         
        """
        pass
    @property
    def ReverseDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseDirection
         Returns the option to reverse length direction   
            
         
        """
        pass
    @ReverseDirection.setter
    def ReverseDirection(self, reverseDirection: bool):
        """
        Setter for property: (bool) ReverseDirection
         Returns the option to reverse length direction   
            
         
        """
        pass
    @property
    def ReverseTrimSide(self) -> bool:
        """
        Getter for property: (bool) ReverseTrimSide
         Returns the option to reverse trim side   
            
         
        """
        pass
    @ReverseTrimSide.setter
    def ReverseTrimSide(self, reverseTrimSide: bool):
        """
        Setter for property: (bool) ReverseTrimSide
         Returns the option to reverse trim side   
            
         
        """
        pass
    @property
    def StartAdjustment(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StartAdjustment
         Returns the flat pattern compensation adjustment at start of the flange   
            
         
        """
        pass
    @property
    def Type(self) -> AdvancedFlangeBuilder.Types:
        """
        Getter for property: ( AdvancedFlangeBuilder.Types NXOpen.Featu) Type
         Returns the advanced flange type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: AdvancedFlangeBuilder.Types):
        """
        Setter for property: ( AdvancedFlangeBuilder.Types NXOpen.Featu) Type
         Returns the advanced flange type   
            
         
        """
        pass
import NXOpen.Features
class AdvancedFlange(NXOpen.Features.Feature): 
    """ Represents an advanced flange feature """
    pass
import NXOpen
class AeroFlangeBuilder(SheetmetalBaseBuilder): 
    """ Represents a Aerospace Sheet Metal Flange Builder. 
        """
    class CompType(Enum):
        """
        Members Include: 
         |Automatic|  Automatic 
         |Angle|  Angle 
         |Distance|  Distance 
         |NotSet|  None 

        """
        Automatic: int
        Angle: int
        Distance: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> AeroFlangeBuilder.CompType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DimType(Enum):
        """
        Members Include: 
         |Inside|  Inside Dimension 
         |Outside|  Outside Dimension 

        """
        Inside: int
        Outside: int
        @staticmethod
        def ValueOf(value: int) -> AeroFlangeBuilder.DimType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DirType(Enum):
        """
        Members Include: 
         |Bend|  Bend Direction Type 
         |Discard|  Discard Direction Type 

        """
        Bend: int
        Discard: int
        @staticmethod
        def ValueOf(value: int) -> AeroFlangeBuilder.DirType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class EndType(Enum):
        """
        Members Include: 
         |End1|  Start of section 
         |End2|  End of section 
         |Closed|  Periodic Bend Edge 

        """
        End1: int
        End2: int
        Closed: int
        @staticmethod
        def ValueOf(value: int) -> AeroFlangeBuilder.EndType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LengthType(Enum):
        """
        Members Include: 
         |Value|  Value 
         |Infer|  Infer from face 

        """
        Value: int
        Infer: int
        @staticmethod
        def ValueOf(value: int) -> AeroFlangeBuilder.LengthType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MatType(Enum):
        """
        Members Include: 
         |MaterialInside|  Material Inside 
         |MaterialOutside|  Material Outside 
         |BendOutside|  Bend Outside 

        """
        MaterialInside: int
        MaterialOutside: int
        BendOutside: int
        @staticmethod
        def ValueOf(value: int) -> AeroFlangeBuilder.MatType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Angle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Angle
         Returns the angle expression.  
           
                      
         
        """
        pass
    @property
    def BaseEdges(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) BaseEdges
         Returns the base edge section object for the flange.  
          
                      
         
        """
        pass
    @BaseEdges.setter
    def BaseEdges(self, base_edges: NXOpen.ScCollector):
        """
        Setter for property: ( NXOpen.ScCollector) BaseEdges
         Returns the base edge section object for the flange.  
          
                      
         
        """
        pass
    @property
    def BendOptions(self) -> BendOptions:
        """
        Getter for property: ( BendOptions NXOpen.Featu) BendOptions
         Returns the base edge section object for the flange.  
          
                      
         
        """
        pass
    @property
    def RefFaces(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) RefFaces
         Returns the ref face smart collector object
                      
            
         
        """
        pass
    @RefFaces.setter
    def RefFaces(self, face_collector: NXOpen.ScCollector):
        """
        Setter for property: ( NXOpen.ScCollector) RefFaces
         Returns the ref face smart collector object
                      
            
         
        """
        pass
    def GetContourFlag(self) -> bool:
        """
         Get the flag that turns onoff the visibility of Contour Curve 
                    
         Returns show_contour (bool):  false = Hide contour curve, true = Show contour curve .
        """
        pass
    def GetDimensionType(self) -> AeroFlangeBuilder.DimType:
        """
         Get the length dimension type of the flange 
                    
         Returns dim_type ( AeroFlangeBuilder.DimType NXOpen.Featu):  insideoutside .
        """
        pass
    def GetEndCompensation(self, end_type: AeroFlangeBuilder.EndType) -> Tuple[NXOpen.Expression, AeroFlangeBuilder.CompType]:
        """
         Get end compensation.
                    
         Returns A tuple consisting of (value_expression, comp_type). 
         - value_expression is:  NXOpen.Expression. compensation expression .
         - comp_type is:  AeroFlangeBuilder.CompType NXOpen.Featu. AutomaticAngleDistanceNone .

        """
        pass
    def GetEndPlane(self, end_type: AeroFlangeBuilder.EndType) -> NXOpen.Plane:
        """
         Get the end plane 
                    
         Returns end_plane ( NXOpen.Plane):  smart plane entity .
        """
        pass
    def GetFlipDirection(self, type: AeroFlangeBuilder.DirType) -> bool:
        """
         Get flip direction. 
                    
         Returns flip_flag (bool):  flip_flag = false = do not flip, true = flip .
        """
        pass
    def GetLength(self) -> Tuple[NXOpen.Expression, AeroFlangeBuilder.LengthType]:
        """
         Get the type of length and the length expression. 
                    
         Returns A tuple consisting of (length_expression, type). 
         - length_expression is:  NXOpen.Expression. length expression .
         - type is:  AeroFlangeBuilder.LengthType NXOpen.Featu. length type ValueInfer .

        """
        pass
    def GetMaterialType(self) -> AeroFlangeBuilder.MatType:
        """
         Get the material type of the flange 
                    
         Returns mat_type ( AeroFlangeBuilder.MatType NXOpen.Featu):  material insidematerial outsidebend outside .
        """
        pass
    def SetAngle(self, angle_expression: str) -> None:
        """
         Set the angle expression. 
                        This method should be called only when there is no ref_face selection.
                    
        """
        pass
    def SetContourFlag(self, show_contour: bool) -> None:
        """
         Set the flag that turns onoff the visibility of Contour Curve 
                    
        """
        pass
    def SetDimensionType(self, dim_type: AeroFlangeBuilder.DimType) -> None:
        """
         Set the length dimension type of the flange 
                    
        """
        pass
    def SetEndCompensation(self, end_type: AeroFlangeBuilder.EndType, comp_type: AeroFlangeBuilder.CompType, value_expression: str) -> None:
        """
         Set end compensation.
                        This method sets the flange compensation for one end of a non-periodic
                        Base Edge section. The end_type input parameter denotes if the end is
                        the start of section(end1) or the end of section(end2). If the compensation
                        type( comp_type) is either Angle or Distance, an expression for the
                        value of compensation must be provided. This expression input can be NULL
                        for Automatic and None type of compensations.
                    
        """
        pass
    def SetEndPlane(self, end_type: AeroFlangeBuilder.EndType, end_plane: NXOpen.Plane) -> None:
        """
         Set the end plane 
                    
        """
        pass
    def SetFlipDirection(self, type: AeroFlangeBuilder.DirType, flip_flag: bool) -> None:
        """
         Set flip direction.
                        This method is called if either the bend direction or the
                        material direction needs to be flipped. 
                    
        """
        pass
    def SetLength(self, type: AeroFlangeBuilder.LengthType, value_expression: str) -> None:
        """
         Set the type of length and the length expression. 
                        If there are no ref_face's then the only length type 
                        possible is "Value". If there are selected ref_face's 
                        and the length type is "Infer", then the length 
                        expression should be NULL.
                    
        """
        pass
    def SetMaterialType(self, mat_type: AeroFlangeBuilder.MatType) -> None:
        """
         Set the material type of the flange 
                    
        """
        pass
class AeroFlatPatternBuilder(FlatPatternBuilder): 
    """ Represents a Flat Pattern feature builder. """
    pass
class AeroFlatSolidBuilder(FlatSolidBuilder): 
    """ Represents a Flat As Solid feature builder. """
    pass
import NXOpen
import NXOpen.Features
class AeroJoggleBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Aerospace Sheet Metal Joggle Builder. 
        """
    class SideType(Enum):
        """
        Members Include: 
         |Side1|  Side 1 (only side of single)
         |Side2|  Side 2 

        """
        Side1: int
        Side2: int
        @staticmethod
        def ValueOf(value: int) -> AeroJoggleBuilder.SideType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BendFaces(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) BendFaces
         Returns the flange 
                      
            
         
        """
        pass
    @BendFaces.setter
    def BendFaces(self, bend_faces: NXOpen.ScCollector):
        """
        Setter for property: ( NXOpen.ScCollector) BendFaces
         Returns the flange 
                      
            
         
        """
        pass
    @property
    def Depth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Depth
         Returns the depth expression.  
           
                      
         
        """
        pass
    @property
    def FlipJoggleSide(self) -> bool:
        """
        Getter for property: (bool) FlipJoggleSide
         Returns the joggle direction flag.  
           
                      
         
        """
        pass
    @FlipJoggleSide.setter
    def FlipJoggleSide(self, flip_joggle_side: bool):
        """
        Setter for property: (bool) FlipJoggleSide
         Returns the joggle direction flag.  
           
                      
         
        """
        pass
    @property
    def IsSymmetric(self) -> bool:
        """
        Getter for property: (bool) IsSymmetric
         Returns the symmetric flag.  
           
                      
         
        """
        pass
    @IsSymmetric.setter
    def IsSymmetric(self, is_symmetric: bool):
        """
        Setter for property: (bool) IsSymmetric
         Returns the symmetric flag.  
           
                      
         
        """
        pass
    @property
    def IsTwin(self) -> bool:
        """
        Getter for property: (bool) IsTwin
         Returns the is_twin flag.  
           
                      
         
        """
        pass
    @IsTwin.setter
    def IsTwin(self, is_twin: bool):
        """
        Setter for property: (bool) IsTwin
         Returns the is_twin flag.  
           
                      
         
        """
        pass
    @property
    def JoggleCompensation(self) -> bool:
        """
        Getter for property: (bool) JoggleCompensation
         Returns the joggle compensation.  
          
                      
         
        """
        pass
    @JoggleCompensation.setter
    def JoggleCompensation(self, joggle_comp: bool):
        """
        Setter for property: (bool) JoggleCompensation
         Returns the joggle compensation.  
          
                      
         
        """
        pass
    @property
    def JoggleIn(self) -> bool:
        """
        Getter for property: (bool) JoggleIn
         Returns the joggle in flag.  
           
                      
         
        """
        pass
    @JoggleIn.setter
    def JoggleIn(self, joggle_in: bool):
        """
        Setter for property: (bool) JoggleIn
         Returns the joggle in flag.  
           
                      
         
        """
        pass
    def GetClearance(self, side_type: AeroJoggleBuilder.SideType) -> NXOpen.Expression:
        """
         The clearance expression. 
                    
         Returns clearance ( NXOpen.Expression):  clearance expression .
        """
        pass
    def GetEndPlane(self) -> NXOpen.Plane:
        """
         The end plane 
                    
         Returns end_plane ( NXOpen.Plane):  datum plane feature .
        """
        pass
    def GetGlobalOffsetRadius(self, side_type: AeroJoggleBuilder.SideType) -> bool:
        """
         The Global flag for offset radius
                    
         Returns global_radius (bool):  If true use global radius .
        """
        pass
    def GetGlobalStationaryRadius(self, side_type: AeroJoggleBuilder.SideType) -> bool:
        """
         The Global flag for stationary radius 
                    
         Returns global_radius (bool):  If true use global radius .
        """
        pass
    def GetOffsetRadius(self, side_type: AeroJoggleBuilder.SideType) -> NXOpen.Expression:
        """
         The offset radius expression. 
                    
         Returns radius ( NXOpen.Expression):  offset radius expression .
        """
        pass
    def GetRunout(self, side_type: AeroJoggleBuilder.SideType) -> NXOpen.Expression:
        """
         The runout expression. 
                    
         Returns runout ( NXOpen.Expression):  runout expression .
        """
        pass
    def GetStandardRunout(self, side_type: AeroJoggleBuilder.SideType) -> bool:
        """
         The global flag for runout
                    
         Returns standard_runout (bool):  If true use standard runout .
        """
        pass
    def GetStartPlane(self) -> NXOpen.Plane:
        """
         The start plane 
                    
         Returns start_plane ( NXOpen.Plane):  datum plane feature .
        """
        pass
    def GetStationaryRadius(self, side_type: AeroJoggleBuilder.SideType) -> NXOpen.Expression:
        """
         The stationary radius expression. 
                    
         Returns radius ( NXOpen.Expression):  stationary radius expression .
        """
        pass
    def SetClearance(self, side_type: AeroJoggleBuilder.SideType, clearance_str: str) -> None:
        """
         Set the clearance expression. 
                    
        """
        pass
    def SetDepth(self, depth_str: str) -> None:
        """
         Set the depth expression. 
                    
        """
        pass
    def SetEndPlane(self, end_plane: NXOpen.Plane) -> None:
        """
         Set the end plane 
                    
        """
        pass
    def SetGlobalOffsetRadius(self, side_type: AeroJoggleBuilder.SideType, global_radius: bool) -> None:
        """
         Set the Global flag for offset radius
                    
        """
        pass
    def SetGlobalStationaryRadius(self, side_type: AeroJoggleBuilder.SideType, global_radius: bool) -> None:
        """
         Set the Global flag for stationary radius
                    
        """
        pass
    def SetOffsetRadius(self, side_type: AeroJoggleBuilder.SideType, radius_str: str) -> None:
        """
         Set the offset radius expression. 
                    
        """
        pass
    def SetRunout(self, side_type: AeroJoggleBuilder.SideType, runout_str: str) -> None:
        """
         Set the runout expression. 
                    
        """
        pass
    def SetStandardRunout(self, side_type: AeroJoggleBuilder.SideType, standard_runout: bool) -> None:
        """
         Set the Global flag for runout
                    
        """
        pass
    def SetStartPlane(self, start_plane: NXOpen.Plane) -> None:
        """
         Set the start plane 
                    
        """
        pass
    def SetStationaryRadius(self, side_type: AeroJoggleBuilder.SideType, radius_str: str) -> None:
        """
         Set the stationary radius expression. 
                    
        """
        pass
import NXOpen
import NXOpen.Features
class AeroLighteningCutoutBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a NXOpen.Features.SheetMetal.AeroLighteningCutoutBuilder 
    """
    class Types(Enum):
        """
        Members Include: 
         |Hole| 
         |UserDefined| 

        """
        Hole: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> AeroLighteningCutoutBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Angle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Angle
         Returns the angle   
            
         
        """
        pass
    @property
    def CheckClearance(self) -> bool:
        """
        Getter for property: (bool) CheckClearance
         Returns the check clearance   
            
         
        """
        pass
    @CheckClearance.setter
    def CheckClearance(self, checkClearance: bool):
        """
        Setter for property: (bool) CheckClearance
         Returns the check clearance   
            
         
        """
        pass
    @property
    def Clearance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Clearance
         Returns the clearance   
            
         
        """
        pass
    @property
    def CornerRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CornerRadius
         Returns the corner radius   
            
         
        """
        pass
    @property
    def CutoutProfile(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) CutoutProfile
         Returns the cutout profile   
            
         
        """
        pass
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Diameter
         Returns the diameter   
            
         
        """
        pass
    @property
    def DieRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DieRadius
         Returns the die radius   
            
         
        """
        pass
    @property
    def HoleCenter(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) HoleCenter
         Returns the hole center   
            
         
        """
        pass
    @HoleCenter.setter
    def HoleCenter(self, holeCenter: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) HoleCenter
         Returns the hole center   
            
         
        """
        pass
    @property
    def HoleFace(self) -> NXOpen.SelectFace:
        """
        Getter for property: ( NXOpen.SelectFace) HoleFace
         Returns the hole face   
            
         
        """
        pass
    @property
    def Length(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Length
         Returns the length   
            
         
        """
        pass
    @property
    def ReverseBendDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseBendDirection
         Returns the reverse bend direction   
            
         
        """
        pass
    @ReverseBendDirection.setter
    def ReverseBendDirection(self, reverseBendDirection: bool):
        """
        Setter for property: (bool) ReverseBendDirection
         Returns the reverse bend direction   
            
         
        """
        pass
    @property
    def StandardName(self) -> str:
        """
        Getter for property: (str) StandardName
         Returns the standard name   
            
         
        """
        pass
    @StandardName.setter
    def StandardName(self, standardName: str):
        """
        Setter for property: (str) StandardName
         Returns the standard name   
            
         
        """
        pass
    @property
    def Type(self) -> AeroLighteningCutoutBuilder.Types:
        """
        Getter for property: ( AeroLighteningCutoutBuilder.Types NXOpen.Featu) Type
         Returns the feature type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: AeroLighteningCutoutBuilder.Types):
        """
        Setter for property: ( AeroLighteningCutoutBuilder.Types NXOpen.Featu) Type
         Returns the feature type   
            
         
        """
        pass
    def GetStandards(self) -> List[str]:
        """
         Returns the standard names 
         Returns standardNames (List[str]): .
        """
        pass
import NXOpen
class AeroReformBuilder(SheetmetalBaseBuilder): 
    """ Represents a Aerospace Sheet Metal REFORM Builder. 
        """
    @property
    def UnformFaceCollector(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) UnformFaceCollector
         Returns the unformed faces smart collector object.  
          
                      
         
        """
        pass
    @UnformFaceCollector.setter
    def UnformFaceCollector(self, unform_face_collector: NXOpen.ScCollector):
        """
        Setter for property: ( NXOpen.ScCollector) UnformFaceCollector
         Returns the unformed faces smart collector object.  
          
                      
         
        """
        pass
import NXOpen
import NXOpen.Features
class AeroSheetmetalManager(NXOpen.Object): 
    """ Provides methods for manipulating the Knowledge Fusion rules in a part """
    def CreateAeroLighteningCutoutBuilder(self, aero_lightening_cutout: NXOpen.Features.Feature) -> AeroLighteningCutoutBuilder:
        """
         Creates a NXOpen.Features.SheetMetal.AeroLighteningCutoutBuilder 
         Returns builder ( AeroLighteningCutoutBuilder NXOpen.Featu):  AeroLighteningCutoutBuilder object.
        """
        pass
    def CreateFlangeBuilder(self, aerosm_flange: NXOpen.Features.Feature) -> AeroFlangeBuilder:
        """
         Create flange builder 
                    
         Returns builder ( AeroFlangeBuilder NXOpen.Featu):  AeroFlangeBuilder object .
        """
        pass
    def CreateFlatPatternBuilder(self, aerosm_unform: NXOpen.Features.Feature) -> FlatPatternBuilder:
        """
         Creates a NXOpen.Features.SheetMetal.FlatPatternBuilder 
         Returns builder ( FlatPatternBuilder NXOpen.Featu):  FlatPatternBuilder object .
        """
        pass
    def CreateFlatSolidBuilder(self, aerosm_unform: NXOpen.Features.Feature) -> FlatSolidBuilder:
        """
         Create flat solid builder 
                    
         Returns builder ( FlatSolidBuilder NXOpen.Featu):  FlatSolidBuilder object .
        """
        pass
    def CreateJoggleBuilder(self, aerosm_joggle: NXOpen.Features.Feature) -> AeroJoggleBuilder:
        """
         Create joggle builder 
                    
         Returns builder ( AeroJoggleBuilder NXOpen.Featu):  AeroJoggleBuilder object .
        """
        pass
    def CreateReformBuilder(self, aerosm_reform: NXOpen.Features.Feature) -> AeroReformBuilder:
        """
         Create reform builder 
                    
         Returns builder ( AeroReformBuilder NXOpen.Featu):  AeroReformBuilder object .
        """
        pass
    def CreateUnformBuilder(self, aerosm_unform: NXOpen.Features.Feature) -> AeroUnformBuilder:
        """
         Create unform builder 
                    
         Returns builder ( AeroUnformBuilder NXOpen.Featu):  AeroUnformBuilder object .
        """
        pass
import NXOpen
class AeroUnformBuilder(SheetmetalBaseBuilder): 
    """ Represents a Aerospace Sheet Metal UNFORM Builder. 
    """
    @property
    def BaseFace(self) -> NXOpen.Face:
        """
        Getter for property: ( NXOpen.Face) BaseFace
         Returns the Base Face for the UNFORM.  
           
                  
         
        """
        pass
    @BaseFace.setter
    def BaseFace(self, base_face: NXOpen.Face):
        """
        Setter for property: ( NXOpen.Face) BaseFace
         Returns the Base Face for the UNFORM.  
           
                  
         
        """
        pass
    @property
    def FormFaces(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FormFaces
         Returns the formed faces smart collector object
                  
            
         
        """
        pass
    @FormFaces.setter
    def FormFaces(self, face_collector: NXOpen.ScCollector):
        """
        Setter for property: ( NXOpen.ScCollector) FormFaces
         Returns the formed faces smart collector object
                  
            
         
        """
        pass
class ApplicationContext(Enum):
    """
    Members Include: 
     |NxSheetMetal|  Sheet Metal application context
     |FlexiblePrintedCircuitDesign|  Flexible Printed Circuit Design application context
     |AerospaceSheetMetal|  Aerospace Sheet Metal application context

    """
    NxSheetMetal: int
    FlexiblePrintedCircuitDesign: int
    AerospaceSheetMetal: int
    @staticmethod
    def ValueOf(value: int) -> ApplicationContext:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen.Features
class AssociateObjectBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Features.SheetMetal.AssociateObjectBuilder """
    class LinkedBodyFeatureOptions(Enum):
        """
        Members Include: 
         |OneForEachComponent|  An option to create one extracted or linked body feature for all selected bodies within same component as body collector 
         |OneForEachBody|  An option to create a separate extracted or linked body feature per single body 

        """
        OneForEachComponent: int
        OneForEachBody: int
        @staticmethod
        def ValueOf(value: int) -> AssociateObjectBuilder.LinkedBodyFeatureOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def InputList(self) -> AssociateObjectInputListItemBuilderList:
        """
        Getter for property: ( AssociateObjectInputListItemBuilderList NXOpen.Featu) InputList
         Returns the input list associated to current Associate Object Builder, containing elements of type 
                     Features::SheetMetal::AssociateObjectInputListItemBuilder .  
             
         
        """
        pass
    @property
    def LinkedBodyOption(self) -> AssociateObjectBuilder.LinkedBodyFeatureOptions:
        """
        Getter for property: ( AssociateObjectBuilder.LinkedBodyFeatureOptions NXOpen.Featu) LinkedBodyOption
         Returns the Linked Body Features option type   
            
         
        """
        pass
    @LinkedBodyOption.setter
    def LinkedBodyOption(self, featureOptionType: AssociateObjectBuilder.LinkedBodyFeatureOptions):
        """
        Setter for property: ( AssociateObjectBuilder.LinkedBodyFeatureOptions NXOpen.Featu) LinkedBodyOption
         Returns the Linked Body Features option type   
            
         
        """
        pass
    def CreateAssociateObjectInputListItemBuilder(self) -> AssociateObjectInputListItemBuilder:
        """
         Creates a new list item of type Features.SheetMetal.AssociateObjectInputListItemBuilder or 
                     will return an list item associated with current Associate Object Builder. 
         Returns listItem ( AssociateObjectInputListItemBuilder NXOpen.Featu): .
        """
        pass
import NXOpen
class AssociateObjectInputListItemBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[AssociateObjectInputListItemBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: AssociateObjectInputListItemBuilder) -> None:
        """
         Appends an object to the list
            
        """
        pass
    @overload
    def Clear(self) -> None:
        """
         Clears the entire list without deleting the objects.  The caller is responsible for 
                accounting for these objects.  If they are not used or deleted by the time the part is 
                closed (in other words, leaked) an error will occur 
        """
        pass
    def ClearIndex(self, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
               not change, but the item at this index is set to NULL.
            
        """
        pass
    @overload
    def Clear(self, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    @overload
    def Erase(self, index: int) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, obj: AssociateObjectInputListItemBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: AssociateObjectInputListItemBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: AssociateObjectInputListItemBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> AssociateObjectInputListItemBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( AssociateObjectInputListItemBuilder NXOpen.Featu):  object found at input index .
        """
        pass
    def GetContents(self) -> List[AssociateObjectInputListItemBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( AssociateObjectInputListItemBuilder List[NXOpen.Fea):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: AssociateObjectInputListItemBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    def MoveToBottom(self, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    def MoveToTop(self, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    def SetContents(self, objects: List[AssociateObjectInputListItemBuilder]) -> None:
        """
         Sets the contents of the entire list. This overwrites the previous contents of this list, 
                but does not delete any objects that were originally on the list.
             
        """
        pass
    @overload
    def Swap(self, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    @overload
    def Swap(self, object1: AssociateObjectInputListItemBuilder, object2: AssociateObjectInputListItemBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class AssociateObjectInputListItemBuilder(NXOpen.TaggedObject): 
    """ Represents a Features.SheetMetal.AssociateObjectInputListItemBuilder """
    @property
    def Bodies(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) Bodies
         Returns the body collector containing collection of bodies to be associated with faces returned by 
                     Features::SheetMetal::AssociateObjectInputListItemBuilder::Faces from the given 
                     Features::SheetMetal::AssociateObjectInputListItemBuilder    
            
         
        """
        pass
    @property
    def Faces(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) Faces
         Returns the face collector containing the face to be associated with bodies returned by
                     Features::SheetMetal::AssociateObjectInputListItemBuilder::Bodies from the given
                     Features::SheetMetal::AssociateObjectInputListItemBuilder    
            
         
        """
        pass
import NXOpen.Features
class AssociateObject(NXOpen.Features.Feature): 
    """ Represents an AssociateObject feature """
    pass
import NXOpen
import NXOpen.Features
class BeadBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Bead feature builder. """
    class CrossSectionTypeOptions(Enum):
        """
        Members Include: 
         |Circular|  
         |Ushaped|  
         |Vshaped|  

        """
        Circular: int
        Ushaped: int
        Vshaped: int
        @staticmethod
        def ValueOf(value: int) -> BeadBuilder.CrossSectionTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class EndTypeOptions(Enum):
        """
        Members Include: 
         |Punched|  
         |Lanced|  
         |Formed|  
         |Tapered|  

        """
        Punched: int
        Lanced: int
        Formed: int
        Tapered: int
        @staticmethod
        def ValueOf(value: int) -> BeadBuilder.EndTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class HeightSideOptions(Enum):
        """
        Members Include: 
         |SectionNormalSide|  Material removed on the side of the section normal. 
         |SectionReverseNormalSide|  Material removed on the side opposite to that of the section normal 

        """
        SectionNormalSide: int
        SectionReverseNormalSide: int
        @staticmethod
        def ValueOf(value: int) -> BeadBuilder.HeightSideOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Angle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Angle
         Returns the angle of the bead.  
            
         
        """
        pass
    @property
    def CrossSectionType(self) -> BeadBuilder.CrossSectionTypeOptions:
        """
        Getter for property: ( BeadBuilder.CrossSectionTypeOptions NXOpen.Featu) CrossSectionType
         Returns the bead profile type .  
          
                      
                        Specify  NXOpen::Features::SheetMetal::BeadBuilder::CrossSectionTypeOptionsCircular  to have profile of half circle.
                        Specify  NXOpen::Features::SheetMetal::BeadBuilder::CrossSectionTypeOptionsUshaped  to have profile of U shape.
                        Specify  NXOpen::Features::SheetMetal::BeadBuilder::CrossSectionTypeOptionsVshaped  to have profile of V shape.
                      
                  
         
        """
        pass
    @CrossSectionType.setter
    def CrossSectionType(self, cross_section_option: BeadBuilder.CrossSectionTypeOptions):
        """
        Setter for property: ( BeadBuilder.CrossSectionTypeOptions NXOpen.Featu) CrossSectionType
         Returns the bead profile type .  
          
                      
                        Specify  NXOpen::Features::SheetMetal::BeadBuilder::CrossSectionTypeOptionsCircular  to have profile of half circle.
                        Specify  NXOpen::Features::SheetMetal::BeadBuilder::CrossSectionTypeOptionsUshaped  to have profile of U shape.
                        Specify  NXOpen::Features::SheetMetal::BeadBuilder::CrossSectionTypeOptionsVshaped  to have profile of V shape.
                      
                  
         
        """
        pass
    @property
    def DieRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DieRadius
         Returns the bead die radius.  
            
         
        """
        pass
    @property
    def EndType(self) -> BeadBuilder.EndTypeOptions:
        """
        Getter for property: ( BeadBuilder.EndTypeOptions NXOpen.Featu) EndType
         Returns the bead end type .  
          
                      
                        Specify  NXOpen::Features::SheetMetal::BeadBuilder::EndTypeOptionsFormed   to have ends of bead feature be formed.
                        Specify  NXOpen::Features::SheetMetal::BeadBuilder::EndTypeOptionsLanced   to have ends of bead feature be Lanced.
                        Specify  NXOpen::Features::SheetMetal::BeadBuilder::EndTypeOptionsPunched  to have ends of bead feature be Punched.
                        Specify  NXOpen::Features::SheetMetal::BeadBuilder::EndTypeOptionsTapered  to have ends of bead feature be Tapered.
                      
                  
         
        """
        pass
    @EndType.setter
    def EndType(self, bead_end_options: BeadBuilder.EndTypeOptions):
        """
        Setter for property: ( BeadBuilder.EndTypeOptions NXOpen.Featu) EndType
         Returns the bead end type .  
          
                      
                        Specify  NXOpen::Features::SheetMetal::BeadBuilder::EndTypeOptionsFormed   to have ends of bead feature be formed.
                        Specify  NXOpen::Features::SheetMetal::BeadBuilder::EndTypeOptionsLanced   to have ends of bead feature be Lanced.
                        Specify  NXOpen::Features::SheetMetal::BeadBuilder::EndTypeOptionsPunched  to have ends of bead feature be Punched.
                        Specify  NXOpen::Features::SheetMetal::BeadBuilder::EndTypeOptionsTapered  to have ends of bead feature be Tapered.
                      
                  
         
        """
        pass
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Height
         Returns the height of the bead.  
            
         
        """
        pass
    @property
    def HeightSide(self) -> BeadBuilder.HeightSideOptions:
        """
        Getter for property: ( BeadBuilder.HeightSideOptions NXOpen.Featu) HeightSide
         Returns the Height side for the bead.  
          
                      
                        This is used to specify the direction in which the Bead is created. If Bead creation must happen in the
                        direction of the Section Normal (specified using the NXOpen.Features.SheetMetal.BeadBuilder.Section) then
                        pass the value of  NXOpen::Features::SheetMetal::BeadBuilder::HeightSideOptionsSectionNormalSide 
                        If Bead creation must happen in the opposite direction to that of Section Normal, set the value to be
                         NXOpen::Features::SheetMetal::BeadBuilder::HeightSideOptionsSectionReverseNormalSide 
                      
                  
         
        """
        pass
    @HeightSide.setter
    def HeightSide(self, height_side: BeadBuilder.HeightSideOptions):
        """
        Setter for property: ( BeadBuilder.HeightSideOptions NXOpen.Featu) HeightSide
         Returns the Height side for the bead.  
          
                      
                        This is used to specify the direction in which the Bead is created. If Bead creation must happen in the
                        direction of the Section Normal (specified using the NXOpen.Features.SheetMetal.BeadBuilder.Section) then
                        pass the value of  NXOpen::Features::SheetMetal::BeadBuilder::HeightSideOptionsSectionNormalSide 
                        If Bead creation must happen in the opposite direction to that of Section Normal, set the value to be
                         NXOpen::Features::SheetMetal::BeadBuilder::HeightSideOptionsSectionReverseNormalSide 
                      
                  
         
        """
        pass
    @property
    def IncludeRounding(self) -> bool:
        """
        Getter for property: (bool) IncludeRounding
         Returns the rounding type .  
          
                      
                        Specify true to Round the Sharp edges.
                        Specify false to avoid rounding.
                      
                  
         
        """
        pass
    @IncludeRounding.setter
    def IncludeRounding(self, rounding: bool):
        """
        Setter for property: (bool) IncludeRounding
         Returns the rounding type .  
          
                      
                        Specify true to Round the Sharp edges.
                        Specify false to avoid rounding.
                      
                  
         
        """
        pass
    @property
    def MinimumToolClearance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumToolClearance
         Returns 
                 the Minimum tool clearance expression.  
                     
                  
         
        """
        pass
    @property
    def PunchRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PunchRadius
         Returns the bead punch radius.  
            
         
        """
        pass
    @property
    def PunchedWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PunchedWidth
         Returns the Punched width of the bead.  
            
         
        """
        pass
    @property
    def Radius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Radius
         Returns the radius of the bead.  
            
         
        """
        pass
    @property
    def Section(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Section
         Returns the Section used by the bead.  
           section should be open.  
         
        """
        pass
    @Section.setter
    def Section(self, section: NXOpen.Section):
        """
        Setter for property: ( NXOpen.Section) Section
         Returns the Section used by the bead.  
           section should be open.  
         
        """
        pass
    @property
    def Sketch(self) -> NXOpen.Features.SketchFeature:
        """
        Getter for property: ( NXOpen.Features.SketchFeature) Sketch
         Returns the Slave Sketch used by the Bead, If one exists.  
          
                      
                        If the Sketch is created internally as part of the Bead command in the UI, then it shall be consumed by the Bead and shall not show up as a separate feature in the Part Navigator.
                        If such a behaviour is deired, then specify the Sketch here.
                      
                  
         
        """
        pass
    @Sketch.setter
    def Sketch(self, sketch: NXOpen.Features.SketchFeature):
        """
        Setter for property: ( NXOpen.Features.SketchFeature) Sketch
         Returns the Slave Sketch used by the Bead, If one exists.  
          
                      
                        If the Sketch is created internally as part of the Bead command in the UI, then it shall be consumed by the Bead and shall not show up as a separate feature in the Part Navigator.
                        If such a behaviour is deired, then specify the Sketch here.
                      
                  
         
        """
        pass
    @property
    def TaperDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TaperDistance
         Returns the taper distance of the bead.  
            
         
        """
        pass
    @property
    def Width(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Width
         Returns the width of the bead.  
            
         
        """
        pass
    def ValidateBuilderData(self) -> int:
        """
         Verify whether the builder data is valid for creating a Bead or not.
                    
                         If the Builder data is valid, returned value shall be 0
                    
                
         Returns builder_data_validity (int):  Data Validity Flag.
        """
        pass
import NXOpen
import NXOpen.Features
class BendBuilder(SheetmetalBaseBuilder): 
    """ Represents a Bend feature builder. """
    class BendDirectionOptions(Enum):
        """
        Members Include: 
         |SectionNormalSide|  Bend is created on the side of the section normal. 
         |SectionReverseNormalSide|  Bend is created on the side opposite to that of the section normal 

        """
        SectionNormalSide: int
        SectionReverseNormalSide: int
        @staticmethod
        def ValueOf(value: int) -> BendBuilder.BendDirectionOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class BendLocationOptions(Enum):
        """
        Members Include: 
         |OuterMoldLine| 
         |CenterLine| 
         |InnerMoldLine| 
         |MaterialInside| 
         |MaterialOutside| 

        """
        OuterMoldLine: int
        CenterLine: int
        InnerMoldLine: int
        MaterialInside: int
        MaterialOutside: int
        @staticmethod
        def ValueOf(value: int) -> BendBuilder.BendLocationOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FixedSideOptions(Enum):
        """
        Members Include: 
         |SectionSideLeft|  Side pointed to by the inverse of the tangent cross normal vector 
         |SectionSideRight|  Side pointed to by the tangent cross normal vector 

        """
        SectionSideLeft: int
        SectionSideRight: int
        @staticmethod
        def ValueOf(value: int) -> BendBuilder.FixedSideOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BendLocation(self) -> BendBuilder.BendLocationOptions:
        """
        Getter for property: ( BendBuilder.BendLocationOptions NXOpen.Featu) BendLocation
         Returns the Bend Location (Material Side)   
            
         
        """
        pass
    @BendLocation.setter
    def BendLocation(self, bend_location: BendBuilder.BendLocationOptions):
        """
        Setter for property: ( BendBuilder.BendLocationOptions NXOpen.Featu) BendLocation
         Returns the Bend Location (Material Side)   
            
         
        """
        pass
    @property
    def BendOptions(self) -> BendOptions:
        """
        Getter for property: ( BendOptions NXOpen.Featu) BendOptions
         Returns the Bend Options.  
           The option  Features::SheetMetal::BendOptions::CornerReliefTypeOptionsNone  is not valid for the  Features::Bend  starting NX11 onwards.
                          
                            From NX 12  Features::SheetMetal::BendOptions::SetExtendBendRelief 
                            has no effect on the Bend feature.
                          
                      
         
        """
        pass
    @property
    def Direction(self) -> BendBuilder.BendDirectionOptions:
        """
        Getter for property: ( BendBuilder.BendDirectionOptions NXOpen.Featu) Direction
         Returns the Bend Direction  
            
         
        """
        pass
    @Direction.setter
    def Direction(self, direction: BendBuilder.BendDirectionOptions):
        """
        Setter for property: ( BendBuilder.BendDirectionOptions NXOpen.Featu) Direction
         Returns the Bend Direction  
            
         
        """
        pass
    @property
    def ExtendProfile(self) -> bool:
        """
        Getter for property: (bool) ExtendProfile
         Returns the Extend Option   
            
         
        """
        pass
    @ExtendProfile.setter
    def ExtendProfile(self, extend_option: bool):
        """
        Setter for property: (bool) ExtendProfile
         Returns the Extend Option   
            
         
        """
        pass
    @property
    def FixedSide(self) -> BendBuilder.FixedSideOptions:
        """
        Getter for property: ( BendBuilder.FixedSideOptions NXOpen.Featu) FixedSide
         Returns the Fixed Side   
            
         
        """
        pass
    @FixedSide.setter
    def FixedSide(self, fixed_side: BendBuilder.FixedSideOptions):
        """
        Setter for property: ( BendBuilder.FixedSideOptions NXOpen.Featu) FixedSide
         Returns the Fixed Side   
            
         
        """
        pass
    @property
    def Section(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Section
         Returns the Section   
            
         
        """
        pass
    @Section.setter
    def Section(self, section: NXOpen.Section):
        """
        Setter for property: ( NXOpen.Section) Section
         Returns the Section   
            
         
        """
        pass
    @property
    def Sketch(self) -> NXOpen.Features.SketchFeature:
        """
        Getter for property: ( NXOpen.Features.SketchFeature) Sketch
         Returns the Sketch   
            
         
        """
        pass
    @Sketch.setter
    def Sketch(self, sketch: NXOpen.Features.SketchFeature):
        """
        Setter for property: ( NXOpen.Features.SketchFeature) Sketch
         Returns the Sketch   
            
         
        """
        pass
    @property
    def TargetFace(self) -> NXOpen.Face:
        """
        Getter for property: ( NXOpen.Face) TargetFace
         Returns the target face on which bend feature applies.  
             
         
        """
        pass
    @TargetFace.setter
    def TargetFace(self, targetFace: NXOpen.Face):
        """
        Setter for property: ( NXOpen.Face) TargetFace
         Returns the target face on which bend feature applies.  
             
         
        """
        pass
    def GetBendAngle(self) -> NXOpen.Expression:
        """
         Returns the Bend Angle 
         Returns bend_angle ( NXOpen.Expression): .
        """
        pass
    def SetBendAngle(self, bend_angle: str) -> None:
        """
         Sets the Bend Angle 
        """
        pass
    def ValidateBuilderData(self) -> int:
        """
         Verify whether the builder data is valid for creating bend or not.
                        
                             If the Builder data is valid, returned value should be 0
            
                        
                    
         Returns builder_data_validity (int):  Data Validity Flag.
        """
        pass
import NXOpen
class BendListBuilder(NXOpen.Builder): 
    """ Represents a Sheetmetal Flat Pattern bend list builder class. This builder is used to
    edit the bend sequence ID and bend name of the bends in the bend list."""
    @property
    def BendList(self) -> BendListItemBuilderList:
        """
        Getter for property: ( BendListItemBuilderList NXOpen.Featu) BendList
         Returns the bend list   
            
         
        """
        pass
    def EditBendItem(self, existingBendId: int, newBendId: int, newBendName: str) -> None:
        """
         This will edit a bend item in the list which has existing bend Id same as input id
                and assign new bend Id and bend name
        """
        pass
    def PopulateBendListFromView(self, flatPatternView: NXOpen.View) -> None:
        """
         This will populate the bend list from given flat pattern modeling view
        """
        pass
import NXOpen
class BendListItemBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[BendListItemBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: BendListItemBuilder) -> None:
        """
         Appends an object to the list
            
        """
        pass
    @overload
    def Clear(self) -> None:
        """
         Clears the entire list without deleting the objects.  The caller is responsible for 
                accounting for these objects.  If they are not used or deleted by the time the part is 
                closed (in other words, leaked) an error will occur 
        """
        pass
    def ClearIndex(self, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
               not change, but the item at this index is set to NULL.
            
        """
        pass
    @overload
    def Clear(self, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    @overload
    def Erase(self, index: int) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, obj: BendListItemBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: BendListItemBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: BendListItemBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> BendListItemBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( BendListItemBuilder NXOpen.Featu):  object found at input index .
        """
        pass
    def GetContents(self) -> List[BendListItemBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( BendListItemBuilder List[NXOpen.Fea):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: BendListItemBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    def MoveToBottom(self, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    def MoveToTop(self, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    def SetContents(self, objects: List[BendListItemBuilder]) -> None:
        """
         Sets the contents of the entire list. This overwrites the previous contents of this list, 
                but does not delete any objects that were originally on the list.
             
        """
        pass
    @overload
    def Swap(self, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    @overload
    def Swap(self, object1: BendListItemBuilder, object2: BendListItemBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class BendListItemBuilder(NXOpen.Builder): 
    """ Represents a Sheetmetal Flat Pattern bend list item builder class. This builder is used to
    edit the bend sequence ID and bend name of the bends in the bend list.
    BendListItemBuilder objects will be created and populated in the BendListBuilder when bend information of a flat pattern view is populated.
    User should never need to create or delete BendListItemBuilder object on its own."""
    @property
    def BendID(self) -> int:
        """
        Getter for property: (int) BendID
         Returns the new bend id   
            
         
        """
        pass
    @BendID.setter
    def BendID(self, bendId: int):
        """
        Setter for property: (int) BendID
         Returns the new bend id   
            
         
        """
        pass
    @property
    def BendName(self) -> str:
        """
        Getter for property: (str) BendName
         Returns the bend name   
            
         
        """
        pass
    @BendName.setter
    def BendName(self, bendName: str):
        """
        Setter for property: (str) BendName
         Returns the bend name   
            
         
        """
        pass
import NXOpen
class BendOptions(NXOpen.TaggedObject): 
    """ Represents a Sheetmetal Bend Options class. """
    class BendReliefTypeOptions(Enum):
        """
        Members Include: 
         |NotSet|   igRipBendRelief         
         |Square|   igRectangularBendRelief 
         |Round|   igFilletBendRelief      

        """
        NotSet: int
        Square: int
        Round: int
        @staticmethod
        def ValueOf(value: int) -> BendOptions.BendReliefTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CornerReliefTypeOptions(Enum):
        """
        Members Include: 
         |NotSet|   
         |BendOnly|   igBendOnlyCornerRelief 
         |BendAndFace|   igBendAndFaceCornerRelief 
         |BendAndFaceChain|   igChainedCornerRelief 

        """
        NotSet: int
        BendOnly: int
        BendAndFace: int
        BendAndFaceChain: int
        @staticmethod
        def ValueOf(value: int) -> BendOptions.CornerReliefTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BendRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BendRadius
         Returns the bend radius.  
             
         
        """
        pass
    @property
    def BendReliefDepth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BendReliefDepth
         Returns the bend relief depth.  
           Applicable only if  NXOpen::Features::SheetMetal::BendOptions::BendReliefTypeOptions  is 
                        set to a value other than  Features::SheetMetal::BendOptions::BendReliefTypeOptionsNone .
                        
         
        """
        pass
    @property
    def BendReliefType(self) -> BendOptions.BendReliefTypeOptions:
        """
        Getter for property: ( BendOptions.BendReliefTypeOptions NXOpen.Featu) BendReliefType
         Returns the bend relief type.  
          
                          
                            Specify  Features::SheetMetal::BendOptions::BendReliefTypeOptionsNone  if you do not want a bend relief.
                            Specify  Features::SheetMetal::BendOptions::BendReliefTypeOptionsSquare  for a squarerectangular bend relief.
                            Specify  Features::SheetMetal::BendOptions::BendReliefTypeOptionsRound  for a rounded bend relief.
                          
                      
         
        """
        pass
    @BendReliefType.setter
    def BendReliefType(self, type: BendOptions.BendReliefTypeOptions):
        """
        Setter for property: ( BendOptions.BendReliefTypeOptions NXOpen.Featu) BendReliefType
         Returns the bend relief type.  
          
                          
                            Specify  Features::SheetMetal::BendOptions::BendReliefTypeOptionsNone  if you do not want a bend relief.
                            Specify  Features::SheetMetal::BendOptions::BendReliefTypeOptionsSquare  for a squarerectangular bend relief.
                            Specify  Features::SheetMetal::BendOptions::BendReliefTypeOptionsRound  for a rounded bend relief.
                          
                      
         
        """
        pass
    @property
    def BendReliefWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BendReliefWidth
         Returns the bend relief width.  
           Applicable only if  NXOpen::Features::SheetMetal::BendOptions::BendReliefTypeOptions  is 
                        set to a value other than  Features::SheetMetal::BendOptions::BendReliefTypeOptionsNone .
                        
         
        """
        pass
    @property
    def CornerReliefType(self) -> BendOptions.CornerReliefTypeOptions:
        """
        Getter for property: ( BendOptions.CornerReliefTypeOptions NXOpen.Featu) CornerReliefType
         Returns the corner relief type.  
           Use one of the values from  NXOpen::Features::SheetMetal::BendOptions::CornerReliefTypeOptions .
                      
         
        """
        pass
    @CornerReliefType.setter
    def CornerReliefType(self, type: BendOptions.CornerReliefTypeOptions):
        """
        Setter for property: ( BendOptions.CornerReliefTypeOptions NXOpen.Featu) CornerReliefType
         Returns the corner relief type.  
           Use one of the values from  NXOpen::Features::SheetMetal::BendOptions::CornerReliefTypeOptions .
                      
         
        """
        pass
    @property
    def DieToolId(self) -> int:
        """
        Getter for property: (int) DieToolId
         Returns the die tool id selected   
            
         
        """
        pass
    @DieToolId.setter
    def DieToolId(self, dieToolId: int):
        """
        Setter for property: (int) DieToolId
         Returns the die tool id selected   
            
         
        """
        pass
    @property
    def DieToolIdName(self) -> str:
        """
        Getter for property: (str) DieToolIdName
         Returns the die tool id string selected   
            
         
        """
        pass
    @DieToolIdName.setter
    def DieToolIdName(self, dieToolId: str):
        """
        Setter for property: (str) DieToolIdName
         Returns the die tool id string selected   
            
         
        """
        pass
    @property
    def ExtendBendRelief(self) -> bool:
        """
        Getter for property: (bool) ExtendBendRelief
         Returns the option to extend the bend relief if required.  
           This only applies if the bend relief type
                        is set to a value other than  Features::SheetMetal::BendOptions::BendReliefTypeOptionsNone .    
                      
         
        """
        pass
    @ExtendBendRelief.setter
    def ExtendBendRelief(self, extend: bool):
        """
        Setter for property: (bool) ExtendBendRelief
         Returns the option to extend the bend relief if required.  
           This only applies if the bend relief type
                        is set to a value other than  Features::SheetMetal::BendOptions::BendReliefTypeOptionsNone .    
                      
         
        """
        pass
    @property
    def IncludeReliefInWidth(self) -> bool:
        """
        Getter for property: (bool) IncludeReliefInWidth
         Returns the option to include the bend relief within the width.  
           This only applies if the bend relief type
                    is set to a value other than  Features::SheetMetal::BendOptions::BendReliefTypeOptionsNone .    
                      
         
        """
        pass
    @IncludeReliefInWidth.setter
    def IncludeReliefInWidth(self, includeReliefInWidth: bool):
        """
        Setter for property: (bool) IncludeReliefInWidth
         Returns the option to include the bend relief within the width.  
           This only applies if the bend relief type
                    is set to a value other than  Features::SheetMetal::BendOptions::BendReliefTypeOptionsNone .    
                      
         
        """
        pass
    @property
    def NeutralFactor(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) NeutralFactor
         Returns the neutral factor.  
             
         
        """
        pass
    @property
    def OverrideToolSet(self) -> bool:
        """
        Getter for property: (bool) OverrideToolSet
         Returns the override tool set toggle value.  
             
         
        """
        pass
    @OverrideToolSet.setter
    def OverrideToolSet(self, overrideToolSet: bool):
        """
        Setter for property: (bool) OverrideToolSet
         Returns the override tool set toggle value.  
             
         
        """
        pass
    @property
    def PunchToolId(self) -> int:
        """
        Getter for property: (int) PunchToolId
         Returns the punch tool id selected   
            
         
        """
        pass
    @PunchToolId.setter
    def PunchToolId(self, punchToolId: int):
        """
        Setter for property: (int) PunchToolId
         Returns the punch tool id selected   
            
         
        """
        pass
    @property
    def PunchToolIdName(self) -> str:
        """
        Getter for property: (str) PunchToolIdName
         Returns the punch tool id string selected   
            
         
        """
        pass
    @PunchToolIdName.setter
    def PunchToolIdName(self, punchToolId: str):
        """
        Setter for property: (str) PunchToolIdName
         Returns the punch tool id string selected   
            
         
        """
        pass
    @property
    def UseGlobalBendRadius(self) -> bool:
        """
        Getter for property: (bool) UseGlobalBendRadius
         Returns the Use Global Bend Radius toggle.  
             
         
        """
        pass
    @UseGlobalBendRadius.setter
    def UseGlobalBendRadius(self, useGlobalBendRadius: bool):
        """
        Setter for property: (bool) UseGlobalBendRadius
         Returns the Use Global Bend Radius toggle.  
             
         
        """
        pass
    @property
    def UseGlobalNeutralFactor(self) -> bool:
        """
        Getter for property: (bool) UseGlobalNeutralFactor
         Returns the Use Global Neutral Factor toggle.  
             
         
        """
        pass
    @UseGlobalNeutralFactor.setter
    def UseGlobalNeutralFactor(self, useGlobalNeutralFactor: bool):
        """
        Setter for property: (bool) UseGlobalNeutralFactor
         Returns the Use Global Neutral Factor toggle.  
             
         
        """
        pass
    @property
    def UseGlobalReliefDepth(self) -> bool:
        """
        Getter for property: (bool) UseGlobalReliefDepth
         Returns the Use Global Relief Depth toggle.  
             
         
        """
        pass
    @UseGlobalReliefDepth.setter
    def UseGlobalReliefDepth(self, useGlobalReliefDepth: bool):
        """
        Setter for property: (bool) UseGlobalReliefDepth
         Returns the Use Global Relief Depth toggle.  
             
         
        """
        pass
    @property
    def UseGlobalReliefWidth(self) -> bool:
        """
        Getter for property: (bool) UseGlobalReliefWidth
         Returns the Use Global Relief Width toggle.  
             
         
        """
        pass
    @UseGlobalReliefWidth.setter
    def UseGlobalReliefWidth(self, useGlobalReliefWidth: bool):
        """
        Setter for property: (bool) UseGlobalReliefWidth
         Returns the Use Global Relief Width toggle.  
             
         
        """
        pass
import NXOpen
class BendTaperBuilder(SheetmetalBaseBuilder): 
    """
    Represents a Bend Taper feature builder
    """
    class BendTaperInputMethod(Enum):
        """
        Members Include: 
         |Angle|  Angle 
         |Distance|  Distance 
         |ToEnd|  To End 

        """
        Angle: int
        Distance: int
        ToEnd: int
        @staticmethod
        def ValueOf(value: int) -> BendTaperBuilder.BendTaperInputMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class BendTaperSides(Enum):
        """
        Members Include: 
         |Both|  Both Sides 
         |Side1|  Side 1 only 
         |Side2|  Side 2 only 
         |Symmetric|  Symmetric. Side 1 = Side 2 

        """
        Both: int
        Side1: int
        Side2: int
        Symmetric: int
        @staticmethod
        def ValueOf(value: int) -> BendTaperBuilder.BendTaperSides:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class BendTaperType(Enum):
        """
        Members Include: 
         |Linear|  Linear 
         |Tangent|  Tangent 
         |Square|  Square 

        """
        Linear: int
        Tangent: int
        Square: int
        @staticmethod
        def ValueOf(value: int) -> BendTaperBuilder.BendTaperType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class StartType(Enum):
        """
        Members Include: 
         |TaperFromBend|  Taper from Bend 
         |TaperFromWeb|  Taper from Web 

        """
        TaperFromBend: int
        TaperFromWeb: int
        @staticmethod
        def ValueOf(value: int) -> BendTaperBuilder.StartType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class WebTaperType(Enum):
        """
        Members Include: 
         |NotSet|  None 
         |Face|  Face 
         |FaceChain|  Face Chain 

        """
        NotSet: int
        Face: int
        FaceChain: int
        @staticmethod
        def ValueOf(value: int) -> BendTaperBuilder.WebTaperType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BendTaperAngle1(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BendTaperAngle1
         Returns the bend taper angle1   
            
         
        """
        pass
    @property
    def BendTaperAngle2(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BendTaperAngle2
         Returns the bend taper angle2   
            
         
        """
        pass
    @property
    def BendTaperInputMethod1(self) -> BendTaperBuilder.BendTaperInputMethod:
        """
        Getter for property: ( BendTaperBuilder.BendTaperInputMethod NXOpen.Featu) BendTaperInputMethod1
         Returns the input method for side 1   
            
         
        """
        pass
    @BendTaperInputMethod1.setter
    def BendTaperInputMethod1(self, bendTaperInputMethod1: BendTaperBuilder.BendTaperInputMethod):
        """
        Setter for property: ( BendTaperBuilder.BendTaperInputMethod NXOpen.Featu) BendTaperInputMethod1
         Returns the input method for side 1   
            
         
        """
        pass
    @property
    def BendTaperInputMethod2(self) -> BendTaperBuilder.BendTaperInputMethod:
        """
        Getter for property: ( BendTaperBuilder.BendTaperInputMethod NXOpen.Featu) BendTaperInputMethod2
         Returns the input method for side 2   
            
         
        """
        pass
    @BendTaperInputMethod2.setter
    def BendTaperInputMethod2(self, bendTaperInputMethod2: BendTaperBuilder.BendTaperInputMethod):
        """
        Setter for property: ( BendTaperBuilder.BendTaperInputMethod NXOpen.Featu) BendTaperInputMethod2
         Returns the input method for side 2   
            
         
        """
        pass
    @property
    def BendTaperSelectBendFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) BendTaperSelectBendFace
         Returns the bend taper select bend face.  
             
         
        """
        pass
    @property
    def BendTaperType1(self) -> BendTaperBuilder.BendTaperType:
        """
        Getter for property: ( BendTaperBuilder.BendTaperType NXOpen.Featu) BendTaperType1
         Returns the bend taper type for Side 1   
            
         
        """
        pass
    @BendTaperType1.setter
    def BendTaperType1(self, bendTaperType1: BendTaperBuilder.BendTaperType):
        """
        Setter for property: ( BendTaperBuilder.BendTaperType NXOpen.Featu) BendTaperType1
         Returns the bend taper type for Side 1   
            
         
        """
        pass
    @property
    def BendTaperType2(self) -> BendTaperBuilder.BendTaperType:
        """
        Getter for property: ( BendTaperBuilder.BendTaperType NXOpen.Featu) BendTaperType2
         Returns the bend taper type for Side 2   
            
         
        """
        pass
    @BendTaperType2.setter
    def BendTaperType2(self, bendTaperType2: BendTaperBuilder.BendTaperType):
        """
        Setter for property: ( BendTaperBuilder.BendTaperType NXOpen.Featu) BendTaperType2
         Returns the bend taper type for Side 2   
            
         
        """
        pass
    @property
    def EndRadius1(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EndRadius1
         Returns the end radius for side 1   
            
         
        """
        pass
    @property
    def EndRadius2(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EndRadius2
         Returns the end radius for side 2   
            
         
        """
        pass
    @property
    def InferRadius1(self) -> bool:
        """
        Getter for property: (bool) InferRadius1
         Returns the infer radius flag for side 1   
            
         
        """
        pass
    @InferRadius1.setter
    def InferRadius1(self, inferRadius1: bool):
        """
        Setter for property: (bool) InferRadius1
         Returns the infer radius flag for side 1   
            
         
        """
        pass
    @property
    def InferRadius2(self) -> bool:
        """
        Getter for property: (bool) InferRadius2
         Returns the infer radius flag for side 2   
            
         
        """
        pass
    @InferRadius2.setter
    def InferRadius2(self, inferRadius2: bool):
        """
        Setter for property: (bool) InferRadius2
         Returns the infer radius flag for side 2   
            
         
        """
        pass
    @property
    def StartRadius1(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StartRadius1
         Returns the start radius for side 1   
            
         
        """
        pass
    @property
    def StartRadius2(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StartRadius2
         Returns the start radius for side 2   
            
         
        """
        pass
    @property
    def StartType1(self) -> BendTaperBuilder.StartType:
        """
        Getter for property: ( BendTaperBuilder.StartType NXOpen.Featu) StartType1
         Returns the start type for side 1   
            
         
        """
        pass
    @StartType1.setter
    def StartType1(self, startType1: BendTaperBuilder.StartType):
        """
        Setter for property: ( BendTaperBuilder.StartType NXOpen.Featu) StartType1
         Returns the start type for side 1   
            
         
        """
        pass
    @property
    def StartType2(self) -> BendTaperBuilder.StartType:
        """
        Getter for property: ( BendTaperBuilder.StartType NXOpen.Featu) StartType2
         Returns the start type for side 2   
            
         
        """
        pass
    @StartType2.setter
    def StartType2(self, startType2: BendTaperBuilder.StartType):
        """
        Setter for property: ( BendTaperBuilder.StartType NXOpen.Featu) StartType2
         Returns the start type for side 2   
            
         
        """
        pass
    @property
    def StationaryEntity(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) StationaryEntity
         Returns the stationary entity, can be an edge or a face.  
             
         
        """
        pass
    @StationaryEntity.setter
    def StationaryEntity(self, bendTaperStationaryEntity: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) StationaryEntity
         Returns the stationary entity, can be an edge or a face.  
             
         
        """
        pass
    @property
    def TaperDistance1(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TaperDistance1
         Returns the taper distance for side 1   
            
         
        """
        pass
    @property
    def TaperDistance2(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TaperDistance2
         Returns the taper distance for side 2   
            
         
        """
        pass
    @property
    def TaperSides(self) -> BendTaperBuilder.BendTaperSides:
        """
        Getter for property: ( BendTaperBuilder.BendTaperSides NXOpen.Featu) TaperSides
         Returns the taper sides   
            
         
        """
        pass
    @TaperSides.setter
    def TaperSides(self, taperSides: BendTaperBuilder.BendTaperSides):
        """
        Setter for property: ( BendTaperBuilder.BendTaperSides NXOpen.Featu) TaperSides
         Returns the taper sides   
            
         
        """
        pass
    @property
    def WebTaperAngle1(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) WebTaperAngle1
         Returns the web taper angle1   
            
         
        """
        pass
    @property
    def WebTaperAngle2(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) WebTaperAngle2
         Returns the web taper angle2   
            
         
        """
        pass
    @property
    def WebTaperType1(self) -> BendTaperBuilder.WebTaperType:
        """
        Getter for property: ( BendTaperBuilder.WebTaperType NXOpen.Featu) WebTaperType1
         Returns the web taper type for side 1   
            
         
        """
        pass
    @WebTaperType1.setter
    def WebTaperType1(self, webTaperType1: BendTaperBuilder.WebTaperType):
        """
        Setter for property: ( BendTaperBuilder.WebTaperType NXOpen.Featu) WebTaperType1
         Returns the web taper type for side 1   
            
         
        """
        pass
    @property
    def WebTaperType2(self) -> BendTaperBuilder.WebTaperType:
        """
        Getter for property: ( BendTaperBuilder.WebTaperType NXOpen.Featu) WebTaperType2
         Returns the web taper type for side 2   
            
         
        """
        pass
    @WebTaperType2.setter
    def WebTaperType2(self, webTaperType2: BendTaperBuilder.WebTaperType):
        """
        Setter for property: ( BendTaperBuilder.WebTaperType NXOpen.Featu) WebTaperType2
         Returns the web taper type for side 2   
            
         
        """
        pass
import NXOpen
class BreakCornerBuilder(SheetmetalBaseBuilder): 
    """ Represents a break corner feature builder. """
    class TypeOptions(Enum):
        """
        Members Include: 
         |Fillet|   
         |ChamferEqualSetback|   

        """
        Fillet: int
        ChamferEqualSetback: int
        @staticmethod
        def ValueOf(value: int) -> BreakCornerBuilder.TypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Type(self) -> BreakCornerBuilder.TypeOptions:
        """
        Getter for property: ( BreakCornerBuilder.TypeOptions NXOpen.Featu) Type
         Returns the type of the break corner.  
          
                      
                        Specify  Features::SheetMetal::BreakCornerBuilder::TypeOptionsFillet  to fillet the edge.
                        Specify  Features::SheetMetal::BreakCornerBuilder::TypeOptionsChamferEqualSetback  to chamfer the edge.
                      
                  
         
        """
        pass
    @Type.setter
    def Type(self, type: BreakCornerBuilder.TypeOptions):
        """
        Setter for property: ( BreakCornerBuilder.TypeOptions NXOpen.Featu) Type
         Returns the type of the break corner.  
          
                      
                        Specify  Features::SheetMetal::BreakCornerBuilder::TypeOptionsFillet  to fillet the edge.
                        Specify  Features::SheetMetal::BreakCornerBuilder::TypeOptionsChamferEqualSetback  to chamfer the edge.
                      
                  
         
        """
        pass
    @property
    def Value(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Value
         Returns the fillet radius or the setback value, depending on the type of the break corner.  
             
         
        """
        pass
    def GetEdges(self) -> List[NXOpen.Edge]:
        """
         The array of input edges for the break corner. 
         Returns edges ( NXOpen.Edge Li):  Edge list .
        """
        pass
    def GetFaces(self) -> List[NXOpen.Face]:
        """
         The array of input faces that implicitly include all connected sharp thickness edges as input for the break corner.  
         Returns faces ( NXOpen.Face Li):  Face list .
        """
        pass
    def SetEdges(self, edges: List[NXOpen.Edge]) -> None:
        """
         The array of input edges for the break corner. 
        """
        pass
    def SetFaces(self, faces: List[NXOpen.Face]) -> None:
        """
         The array of input faces that implicitly include all connected sharp thickness edges as input for the break corner. 
        """
        pass
    def ValidateBuilderData(self) -> int:
        """
         Verify that the builder data is valid for creating a break corner.
                    
                         If the Builder data is valid, return value is 0
                    
                
         Returns builder_data_validity (int):  Data validity flag (zero for valid and non-zero for invalid) .
        """
        pass
import NXOpen
class BridgeTransitionBuilder(SheetmetalBaseBuilder): 
    """
        Represents a Bridge Transition builder
        """
    class FlexLengthOptions(Enum):
        """
        Members Include: 
         |ScaleFactor|  Flex Transition length option type is ScaleFactor. 
         |Value|  Flex Transition length option type is Value. 

        """
        ScaleFactor: int
        Value: int
        @staticmethod
        def ValueOf(value: int) -> BridgeTransitionBuilder.FlexLengthOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FoldTransitionTypeOptions(Enum):
        """
        Members Include: 
         |Length|  Fold Transition type is Length. 
         |Bend|  Fold Transition type is Bend. 

        """
        Length: int
        Bend: int
        @staticmethod
        def ValueOf(value: int) -> BridgeTransitionBuilder.FoldTransitionTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class InsetOptions(Enum):
        """
        Members Include: 
         |MaterialInside|  Bridge Transition body near tangential plane and start will be on same side of the tangential plane selected. 
         |MaterialOutside|  Bridge Transition body near tangential plane and start will be on opposite sides of the tangential plane selected. 

        """
        MaterialInside: int
        MaterialOutside: int
        @staticmethod
        def ValueOf(value: int) -> BridgeTransitionBuilder.InsetOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TypeOptions(Enum):
        """
        Members Include: 
         |Zu|  Bridge Transition type consisting of Bend-Planar-Bend regions. 
         |Fold|  Bridge Transition type consisting of Planar-Bend-Planar regions. 
         |Flex|  Bridge Transition type consisting of flex regions. 
         |Sketched|  Bridge Transition type created using sketch.

        """
        Zu: int
        Fold: int
        Flex: int
        Sketched: int
        @staticmethod
        def ValueOf(value: int) -> BridgeTransitionBuilder.TypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class WidthDirectionOptions(Enum):
        """
        Members Include: 
         |Left|  It means Bridge Transition width direction at point specified and fin direction are in opposite direction. 
         |Right|  It means Bridge Transition width direction at point specified and fin direction are in same direction. 

        """
        Left: int
        Right: int
        @staticmethod
        def ValueOf(value: int) -> BridgeTransitionBuilder.WidthDirectionOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class WidthOptions(Enum):
        """
        Members Include: 
         |Finite|  Bridge Transition starts at specified point on start edge and extends on one side by the specified distance.
         |Symmetric|  Bridge Transition starts at specified point on start edge and extends on either side by half the specified distance. 
         |FullStartEdge|  Bridge Transition spans the full length of start edge. 
         |FullEndEdge|  Bridge Transition spans the full length of end edge. 
         |FullBothEdges|  Bridge Transition spans the full length of both the edges. 

        """
        Finite: int
        Symmetric: int
        FullStartEdge: int
        FullEndEdge: int
        FullBothEdges: int
        @staticmethod
        def ValueOf(value: int) -> BridgeTransitionBuilder.WidthOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AlternateSolution(self) -> bool:
        """
        Getter for property: (bool) AlternateSolution
         Returns the option to get an alternate solution for the  Features::SheetMetal::BridgeTransitionBuilder::FoldTransitionTypeOptionsBend 
                        when the width option is finite or symmetric.  
          
                          
                            If there is only one working solution possible then this method will not do anything.
                          
                      
         
        """
        pass
    @AlternateSolution.setter
    def AlternateSolution(self, isAlternateSolution: bool):
        """
        Setter for property: (bool) AlternateSolution
         Returns the option to get an alternate solution for the  Features::SheetMetal::BridgeTransitionBuilder::FoldTransitionTypeOptionsBend 
                        when the width option is finite or symmetric.  
          
                          
                            If there is only one working solution possible then this method will not do anything.
                          
                      
         
        """
        pass
    @property
    def AttachmentList(self) -> FlexTransitionAttachmentListItemBuilderList:
        """
        Getter for property: ( FlexTransitionAttachmentListItemBuilderList NXOpen.Featu) AttachmentList
         Returns the attachment list for flex transition.  
             
         
        """
        pass
    @property
    def BendOptionsOfSketchedTransition(self) -> BendOptions:
        """
        Getter for property: ( BendOptions NXOpen.Featu) BendOptionsOfSketchedTransition
         Returns the bend options for  Features::SheetMetal::BridgeTransitionBuilder::TypeOptionsSketched  bridge bend
                          
                        The bend options object stores additional parameters for the bend, such as bend radius, neutral factor, bend
                        relief width and depth.  
          
                          
                      
         
        """
        pass
    @property
    def EndEdge(self) -> NXOpen.SelectEdge:
        """
        Getter for property: ( NXOpen.SelectEdge) EndEdge
         Returns the end edge   
            
         
        """
        pass
    @property
    def EndEdgeLateralOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EndEdgeLateralOffset
         Returnsthe lateral offset expression for end edge of bridge transition.  
             
         
        """
        pass
    @property
    def FlexEndpoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) FlexEndpoint
         Returns the end point with respect to which the finite or symmetric width is specified for flex transition.  
             
         
        """
        pass
    @FlexEndpoint.setter
    def FlexEndpoint(self, point: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) FlexEndpoint
         Returns the end point with respect to which the finite or symmetric width is specified for flex transition.  
             
         
        """
        pass
    @property
    def FlexLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlexLength
         Returns the flex length expression for flex transition type of bridge transition.  
             
         
        """
        pass
    @property
    def FlexLengthType(self) -> BridgeTransitionBuilder.FlexLengthOptions:
        """
        Getter for property: ( BridgeTransitionBuilder.FlexLengthOptions NXOpen.Featu) FlexLengthType
         Returns the flex length type  
            
         
        """
        pass
    @FlexLengthType.setter
    def FlexLengthType(self, flexLengthType: BridgeTransitionBuilder.FlexLengthOptions):
        """
        Setter for property: ( BridgeTransitionBuilder.FlexLengthOptions NXOpen.Featu) FlexLengthType
         Returns the flex length type  
            
         
        """
        pass
    @property
    def FoldBendOptions(self) -> BendOptions:
        """
        Getter for property: ( BendOptions NXOpen.Featu) FoldBendOptions
         Returns the bend options for  Features::SheetMetal::BridgeTransitionBuilder::TypeOptionsFold  bridge bend
                          
                        The bend options object stores additional parameters for the bend, such as bend radius, neutral factor, bend
                        relief width and depth.  
          
                          
                      
         
        """
        pass
    @property
    def FoldTransitionType(self) -> int:
        """
        Getter for property: (int) FoldTransitionType
         Returns the option to get fold transition type.  
          
                      
         
        """
        pass
    @FoldTransitionType.setter
    def FoldTransitionType(self, foldTransitionType: int):
        """
        Setter for property: (int) FoldTransitionType
         Returns the option to get fold transition type.  
          
                      
         
        """
        pass
    @property
    def InsetType(self) -> BridgeTransitionBuilder.InsetOptions:
        """
        Getter for property: ( BridgeTransitionBuilder.InsetOptions NXOpen.Featu) InsetType
         Returns the inset type  
            
         
        """
        pass
    @InsetType.setter
    def InsetType(self, insetType: BridgeTransitionBuilder.InsetOptions):
        """
        Setter for property: ( BridgeTransitionBuilder.InsetOptions NXOpen.Featu) InsetType
         Returns the inset type  
            
         
        """
        pass
    @property
    def Length(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Length
         Returns the length of the planar region near start edge.  
          
                        Length is required to be specified for  Features::SheetMetal::BridgeTransitionBuilder::TypeOptionsFold .
                      
         
        """
        pass
    @property
    def MultiThicknessProperty(self) -> MultiThicknessBuilder:
        """
        Getter for property: ( MultiThicknessBuilder NXOpen.Featu) MultiThicknessProperty
         Returns the multi thickness builder of given builder.  
             
         
        """
        pass
    @property
    def Plane(self) -> NXOpen.SelectISurface:
        """
        Getter for property: ( NXOpen.SelectISurface) Plane
         Returns the tangential plane
                          
                            Only use this option to edit feature created prior to NX12.  
          
                        Use  NXOpen::Features::SheetMetal::BridgeTransitionBuilder::ReferenceGeometryPlane  to locate tangential plane.
                          
                      
         
        """
        pass
    @property
    def Point(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Point
         Returns the point with respect to which the finite or symmetric width is specified.  
             
         
        """
        pass
    @Point.setter
    def Point(self, point: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Point
         Returns the point with respect to which the finite or symmetric width is specified.  
             
         
        """
        pass
    @property
    def ReferenceGeometryPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) ReferenceGeometryPlane
         Returns the reference geometry plane   
            
         
        """
        pass
    @ReferenceGeometryPlane.setter
    def ReferenceGeometryPlane(self, refGeometryPlane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) ReferenceGeometryPlane
         Returns the reference geometry plane   
            
         
        """
        pass
    @property
    def ScaleFactor(self) -> float:
        """
        Getter for property: (float) ScaleFactor
         Returns the scale factor for flex transition type.  
             
         
        """
        pass
    @ScaleFactor.setter
    def ScaleFactor(self, scaleFactor: float):
        """
        Setter for property: (float) ScaleFactor
         Returns the scale factor for flex transition type.  
             
         
        """
        pass
    @property
    def Section(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Section
         Returns the section that will be used to create sketched transition.  
            
         
        """
        pass
    @Section.setter
    def Section(self, section: NXOpen.Section):
        """
        Setter for property: ( NXOpen.Section) Section
         Returns the section that will be used to create sketched transition.  
            
         
        """
        pass
    @property
    def StartAndEndParametersEqual(self) -> bool:
        """
        Getter for property: (bool) StartAndEndParametersEqual
         Returns the option to find whether the start and end parameters are equal.  
          
                      
         
        """
        pass
    @StartAndEndParametersEqual.setter
    def StartAndEndParametersEqual(self, areBendParametersEqual: bool):
        """
        Setter for property: (bool) StartAndEndParametersEqual
         Returns the option to find whether the start and end parameters are equal.  
          
                      
         
        """
        pass
    @property
    def StartEdge(self) -> NXOpen.SelectEdge:
        """
        Getter for property: ( NXOpen.SelectEdge) StartEdge
         Returns the start edge   
            
         
        """
        pass
    @property
    def StartEdgeLateralOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StartEdgeLateralOffset
         Returnsthe lateral offset expression for start edge when  NXOpen::Features::SheetMetal::BridgeTransitionBuilder::SetType  is set as  NXOpen::Features::SheetMetal::BridgeTransitionBuilder::TypeOptionsZu .  
             
         
        """
        pass
    @property
    def TrimOrExtendToBend(self) -> bool:
        """
        Getter for property: (bool) TrimOrExtendToBend
         Returns the option to trim or extend faces to bend face.  
          
                      
         
        """
        pass
    @TrimOrExtendToBend.setter
    def TrimOrExtendToBend(self, trimOrExtend: bool):
        """
        Setter for property: (bool) TrimOrExtendToBend
         Returns the option to trim or extend faces to bend face.  
          
                      
         
        """
        pass
    @property
    def Type(self) -> BridgeTransitionBuilder.TypeOptions:
        """
        Getter for property: ( BridgeTransitionBuilder.TypeOptions NXOpen.Featu) Type
         Returns the transition type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: BridgeTransitionBuilder.TypeOptions):
        """
        Setter for property: ( BridgeTransitionBuilder.TypeOptions NXOpen.Featu) Type
         Returns the transition type   
            
         
        """
        pass
    @property
    def Width(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Width
         Returns the width   
            
         
        """
        pass
    @property
    def WidthDirection(self) -> BridgeTransitionBuilder.WidthDirectionOptions:
        """
        Getter for property: ( BridgeTransitionBuilder.WidthDirectionOptions NXOpen.Featu) WidthDirection
         Returns the width direction.  
           Only applies if the width type is  Features::SheetMetal::BridgeTransitionBuilder::WidthOptionsFinite    
         
        """
        pass
    @WidthDirection.setter
    def WidthDirection(self, widthDirection: BridgeTransitionBuilder.WidthDirectionOptions):
        """
        Setter for property: ( BridgeTransitionBuilder.WidthDirectionOptions NXOpen.Featu) WidthDirection
         Returns the width direction.  
           Only applies if the width type is  Features::SheetMetal::BridgeTransitionBuilder::WidthOptionsFinite    
         
        """
        pass
    @property
    def WidthType(self) -> BridgeTransitionBuilder.WidthOptions:
        """
        Getter for property: ( BridgeTransitionBuilder.WidthOptions NXOpen.Featu) WidthType
         Returns the width type  
            
         
        """
        pass
    @WidthType.setter
    def WidthType(self, widthType: BridgeTransitionBuilder.WidthOptions):
        """
        Setter for property: ( BridgeTransitionBuilder.WidthOptions NXOpen.Featu) WidthType
         Returns the width type  
            
         
        """
        pass
    @property
    def ZuEndEdgeBendOptions(self) -> BendOptions:
        """
        Getter for property: ( BendOptions NXOpen.Featu) ZuEndEdgeBendOptions
         Returns the bend options at end edge for  Features::SheetMetal::BridgeTransitionBuilder::TypeOptionsZu  bridge bend.  
          
                          
                        The bend options object stores additional parameters for the bend, such as bend radius and neutral factor.
                          
                      
         
        """
        pass
    @property
    def ZuStartEdgeBendOptions(self) -> BendOptions:
        """
        Getter for property: ( BendOptions NXOpen.Featu) ZuStartEdgeBendOptions
         Returns the bend options at start edge for  Features::SheetMetal::BridgeTransitionBuilder::TypeOptionsZu  bridge bend.  
          
                          
                        The bend options object stores additional parameters for the bend, such as bend radius and neutral factor.
                          
                      
         
        """
        pass
    def CreateFlexTransitionAttachmentListItemBuilder(self) -> FlexTransitionAttachmentListItemBuilder:
        """
         Create a attachment list builder for flex type bridge transition. 
         Returns listBuilder ( FlexTransitionAttachmentListItemBuilder NXOpen.Featu): .
        """
        pass
import NXOpen
class BulgeReliefBuilder(SheetmetalBaseBuilder): 
    """
        Represents a Features.SheetMetal.BulgeRelief builder
        """
    class ReliefTypes(Enum):
        """
        Members Include: 
         |Circular| 
         |UShaped| 
         |VShaped| 

        """
        Circular: int
        UShaped: int
        VShaped: int
        @staticmethod
        def ValueOf(value: int) -> BulgeReliefBuilder.ReliefTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class WidthTypes(Enum):
        """
        Members Include: 
         |Value| 
         |FullWidth| 

        """
        Value: int
        FullWidth: int
        @staticmethod
        def ValueOf(value: int) -> BulgeReliefBuilder.WidthTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BendEdges(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) BendEdges
         Returns the bend edges given by user  
            
         
        """
        pass
    @property
    def Depth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Depth
         Returns the relief depth   
            
         
        """
        pass
    @property
    def Radius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Radius
         Returns the radius   
            
         
        """
        pass
    @property
    def ReliefType(self) -> BulgeReliefBuilder.ReliefTypes:
        """
        Getter for property: ( BulgeReliefBuilder.ReliefTypes NXOpen.Featu) ReliefType
         Returns the relief type   
            
         
        """
        pass
    @ReliefType.setter
    def ReliefType(self, reliefType: BulgeReliefBuilder.ReliefTypes):
        """
        Setter for property: ( BulgeReliefBuilder.ReliefTypes NXOpen.Featu) ReliefType
         Returns the relief type   
            
         
        """
        pass
    @property
    def Width(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Width
         Returns the relief width   
            
         
        """
        pass
    @property
    def WidthType(self) -> BulgeReliefBuilder.WidthTypes:
        """
        Getter for property: ( BulgeReliefBuilder.WidthTypes NXOpen.Featu) WidthType
         Returns the width type   
            
         
        """
        pass
    @WidthType.setter
    def WidthType(self, widthType: BulgeReliefBuilder.WidthTypes):
        """
        Setter for property: ( BulgeReliefBuilder.WidthTypes NXOpen.Featu) WidthType
         Returns the width type   
            
         
        """
        pass
import NXOpen.Features
class BulgeRelief(NXOpen.Features.BodyFeature): 
    """ Represents a bulge relief feature """
    pass
import NXOpen
class CleanUpUtilityBuilder(SheetmetalBaseBuilder): 
    """ Represents a Features.SheetMetal.CleanUpUtilityBuilder """
    class CleanupType(Enum):
        """
        Members Include: 
         |UniformThickness| 
         |MultiThickness| 

        """
        UniformThickness: int
        MultiThickness: int
        @staticmethod
        def ValueOf(value: int) -> CleanUpUtilityBuilder.CleanupType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def HideOriginal(self) -> bool:
        """
        Getter for property: (bool) HideOriginal
         Returns the hide original   
            
         
        """
        pass
    @HideOriginal.setter
    def HideOriginal(self, hideOriginal: bool):
        """
        Setter for property: (bool) HideOriginal
         Returns the hide original   
            
         
        """
        pass
    @property
    def InferThickness(self) -> bool:
        """
        Getter for property: (bool) InferThickness
         Returns the infer thickness   
            
         
        """
        pass
    @InferThickness.setter
    def InferThickness(self, inferThickness: bool):
        """
        Setter for property: (bool) InferThickness
         Returns the infer thickness   
            
         
        """
        pass
    @property
    def MergeCoplanarFaces(self) -> bool:
        """
        Getter for property: (bool) MergeCoplanarFaces
         Returns the option that specifies whether to merge coplanar faces.  
             
         
        """
        pass
    @MergeCoplanarFaces.setter
    def MergeCoplanarFaces(self, mergeCoplanarFaces: bool):
        """
        Setter for property: (bool) MergeCoplanarFaces
         Returns the option that specifies whether to merge coplanar faces.  
             
         
        """
        pass
    @property
    def MultiHeightZoneList(self) -> CleanUpUtilityListItemBuilderList:
        """
        Getter for property: ( CleanUpUtilityListItemBuilderList NXOpen.Featu) MultiHeightZoneList
         Returns the zone list for cleanup utility.  
             
         
        """
        pass
    @property
    def SelectBaseFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SelectBaseFace
         Returns the select base face for clean-up utility   
            
         
        """
        pass
    @property
    def SliverTol(self) -> float:
        """
        Getter for property: (float) SliverTol
         Returns the sliver tolerance   
            
         
        """
        pass
    @SliverTol.setter
    def SliverTol(self, sliverTol: float):
        """
        Setter for property: (float) SliverTol
         Returns the sliver tolerance   
            
         
        """
        pass
    @property
    def SliverTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SliverTolerance
         Returns the sliver tolerance.  
             
         
        """
        pass
    @property
    def ThicknessTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ThicknessTolerance
         Returns the thickness tolerance.  
             
         
        """
        pass
    @property
    def ThicknessValue(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ThicknessValue
         Returns the thickness value   
            
         
        """
        pass
    @property
    def Type(self) -> CleanUpUtilityBuilder.CleanupType:
        """
        Getter for property: ( CleanUpUtilityBuilder.CleanupType NXOpen.Featu) Type
         Returns the clean up type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: CleanUpUtilityBuilder.CleanupType):
        """
        Setter for property: ( CleanUpUtilityBuilder.CleanupType NXOpen.Featu) Type
         Returns the clean up type   
            
         
        """
        pass
    @property
    def UseGlobal(self) -> bool:
        """
        Getter for property: (bool) UseGlobal
         Returns the use global, if it equals to true - use global thickness value   
            
         
        """
        pass
    @UseGlobal.setter
    def UseGlobal(self, useGlobal: bool):
        """
        Setter for property: (bool) UseGlobal
         Returns the use global, if it equals to true - use global thickness value   
            
         
        """
        pass
    def CreateCleanUpUtilityListItemBuilder(self) -> CleanUpUtilityListItemBuilder:
        """
         Create a list builder for cleanup utility.
         Returns listBuilder ( CleanUpUtilityListItemBuilder NXOpen.Featu): .
        """
        pass
import NXOpen
class CleanUpUtilityListItemBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[CleanUpUtilityListItemBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: CleanUpUtilityListItemBuilder) -> None:
        """
         Appends an object to the list
            
        """
        pass
    @overload
    def Clear(self) -> None:
        """
         Clears the entire list without deleting the objects.  The caller is responsible for 
                accounting for these objects.  If they are not used or deleted by the time the part is 
                closed (in other words, leaked) an error will occur 
        """
        pass
    def ClearIndex(self, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
               not change, but the item at this index is set to NULL.
            
        """
        pass
    @overload
    def Clear(self, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    @overload
    def Erase(self, index: int) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, obj: CleanUpUtilityListItemBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: CleanUpUtilityListItemBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: CleanUpUtilityListItemBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> CleanUpUtilityListItemBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( CleanUpUtilityListItemBuilder NXOpen.Featu):  object found at input index .
        """
        pass
    def GetContents(self) -> List[CleanUpUtilityListItemBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( CleanUpUtilityListItemBuilder List[NXOpen.Fea):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: CleanUpUtilityListItemBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    def MoveToBottom(self, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    def MoveToTop(self, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    def SetContents(self, objects: List[CleanUpUtilityListItemBuilder]) -> None:
        """
         Sets the contents of the entire list. This overwrites the previous contents of this list, 
                but does not delete any objects that were originally on the list.
             
        """
        pass
    @overload
    def Swap(self, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    @overload
    def Swap(self, object1: CleanUpUtilityListItemBuilder, object2: CleanUpUtilityListItemBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class CleanUpUtilityListItemBuilder(SheetmetalComponentBuilder): 
    """  Represents a Cleanup Utility List item builder class. """
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Offset
         Returns the zone offset   
            
         
        """
        pass
    @property
    def SelectedBaseFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SelectedBaseFace
         Returns the select base face for cleanup utility   
            
         
        """
        pass
    @property
    def ThicknessValue(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ThicknessValue
         Returns the thickness value   
            
         
        """
        pass
import NXOpen
import NXOpen.Features
class ClosedCornerBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Closed corner feature builder. """
    class ClosureTypeOptions(Enum):
        """
        Members Include: 
         |Close|  Instead of this use  NXOpen.Features.SheetMetal.ClosedCornerBuilder.OverlapTypeOptions.None  
         |Overlap|  Instead of this use  NXOpen.Features.SheetMetal.ClosedCornerBuilder.OverlapTypeOptions.Side2  

        """
        Close: int
        Overlap: int
        @staticmethod
        def ValueOf(value: int) -> ClosedCornerBuilder.ClosureTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CutMethodTypes(Enum):
        """
        Members Include: 
         |ByTool|  The cut method will be by tool. 
         |ByPath|  The cut method will be by path.

        """
        ByTool: int
        ByPath: int
        @staticmethod
        def ValueOf(value: int) -> ClosedCornerBuilder.CutMethodTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OriginTypes(Enum):
        """
        Members Include: 
         |BendCenter|  The relief origin will be at the intersection of first bend's centerline and bisector of corrner angle. 
         |CornerPoint|  The relief origin will be at the corner point.

        """
        BendCenter: int
        CornerPoint: int
        @staticmethod
        def ValueOf(value: int) -> ClosedCornerBuilder.OriginTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OverlapTypeOptions(Enum):
        """
        Members Include: 
         |NotSet|  
         |Side1|  
         |Side2|  

        """
        NotSet: int
        Side1: int
        Side2: int
        @staticmethod
        def ValueOf(value: int) -> ClosedCornerBuilder.OverlapTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TreatmentTypeOptions(Enum):
        """
        Members Include: 
         |Open|  Only Webs will be closed
         |Closed|  Bend and Webs will be closed
         |CircularCutout|  Circular shaped relief
         |UCutout|  U shaped relief
         |VCutout|  V shaped relief
         |RectangularCutout|  Rectangular shaped relief

        """
        Open: int
        Closed: int
        CircularCutout: int
        UCutout: int
        VCutout: int
        RectangularCutout: int
        @staticmethod
        def ValueOf(value: int) -> ClosedCornerBuilder.TreatmentTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |CloseAndRelief| 
         |Relief| 

        """
        CloseAndRelief: int
        Relief: int
        @staticmethod
        def ValueOf(value: int) -> ClosedCornerBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BlendMiter(self) -> bool:
        """
        Getter for property: (bool) BlendMiter
         Returns the option for smooth transition from miter to cutout edges.  
            
         
        """
        pass
    @BlendMiter.setter
    def BlendMiter(self, blendMiter: bool):
        """
        Setter for property: (bool) BlendMiter
         Returns the option for smooth transition from miter to cutout edges.  
            
         
        """
        pass
    @property
    def BlendMiterRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BlendMiterRadius
         Returns the blend miter radius.  
            
         
        """
        pass
    @property
    def ClosureType(self) -> ClosedCornerBuilder.ClosureTypeOptions:
        """
        Getter for property: ( ClosedCornerBuilder.ClosureTypeOptions NXOpen.Featu) ClosureType
         Returns the closure type.  
           This is only for legacy feature support, for new features use   NXOpen::Features::SheetMetal::ClosedCornerBuilder::OverlapType     
         
        """
        pass
    @ClosureType.setter
    def ClosureType(self, closure_type: ClosedCornerBuilder.ClosureTypeOptions):
        """
        Setter for property: ( ClosedCornerBuilder.ClosureTypeOptions NXOpen.Featu) ClosureType
         Returns the closure type.  
           This is only for legacy feature support, for new features use   NXOpen::Features::SheetMetal::ClosedCornerBuilder::OverlapType     
         
        """
        pass
    @property
    def CutMethod(self) -> ClosedCornerBuilder.CutMethodTypes:
        """
        Getter for property: ( ClosedCornerBuilder.CutMethodTypes NXOpen.Featu) CutMethod
         Returns the cut method to be used for UV cutout relief.  
            
         
        """
        pass
    @CutMethod.setter
    def CutMethod(self, cut_method: ClosedCornerBuilder.CutMethodTypes):
        """
        Setter for property: ( ClosedCornerBuilder.CutMethodTypes NXOpen.Featu) CutMethod
         Returns the cut method to be used for UV cutout relief.  
            
         
        """
        pass
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Diameter
         Returns the diameter.  
            
         
        """
        pass
    @property
    def Gap(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Gap
         Returns the gap.  
            
         
        """
        pass
    @property
    def Length(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Length
         Returns the length of U relief.  
             
         
        """
        pass
    @property
    def Length1(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Length1
         Returns the length of V relief associated with the first bend selected.  
            
         
        """
        pass
    @property
    def Length2(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Length2
         Returns the length of V relief associated with the second bend selected.  
            
         
        """
        pass
    @property
    def LimitEdge1(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) LimitEdge1
         Returns the limiting edge on the first side for miter.  
            
         
        """
        pass
    @property
    def LimitEdge2(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) LimitEdge2
         Returns the limiting edge on the second side for miter.  
            
         
        """
        pass
    @property
    def MiterCorner(self) -> bool:
        """
        Getter for property: (bool) MiterCorner
         Returns the corner will be closed using the miter algorithm.  
            
         
        """
        pass
    @MiterCorner.setter
    def MiterCorner(self, miterCorner: bool):
        """
        Setter for property: (bool) MiterCorner
         Returns the corner will be closed using the miter algorithm.  
            
         
        """
        pass
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Offset
         Returns the value by which relief origin will be offset  
            
         
        """
        pass
    @property
    def Origin(self) -> ClosedCornerBuilder.OriginTypes:
        """
        Getter for property: ( ClosedCornerBuilder.OriginTypes NXOpen.Featu) Origin
         Returns the default origin will be at the corner point instead of the intersection of bend centerlines.  
            
         
        """
        pass
    @Origin.setter
    def Origin(self, originType: ClosedCornerBuilder.OriginTypes):
        """
        Setter for property: ( ClosedCornerBuilder.OriginTypes NXOpen.Featu) Origin
         Returns the default origin will be at the corner point instead of the intersection of bend centerlines.  
            
         
        """
        pass
    @property
    def Overlap(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Overlap
         Returns the overlap.  
            
         
        """
        pass
    @property
    def OverlapType(self) -> ClosedCornerBuilder.OverlapTypeOptions:
        """
        Getter for property: ( ClosedCornerBuilder.OverlapTypeOptions NXOpen.Featu) OverlapType
         Returns the overlap type  
            
         
        """
        pass
    @OverlapType.setter
    def OverlapType(self, overlapType: ClosedCornerBuilder.OverlapTypeOptions):
        """
        Setter for property: ( ClosedCornerBuilder.OverlapTypeOptions NXOpen.Featu) OverlapType
         Returns the overlap type  
            
         
        """
        pass
    @property
    def PunchRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PunchRadius
         Returns the punch radius of tool associated with V relief.  
            
         
        """
        pass
    @property
    def RectangularLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RectangularLength
         Returns the length of rectangular relief.  
           The length is associated to the first bend selected.  
         
        """
        pass
    @property
    def RectangularWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RectangularWidth
         Returns the width of rectangular relief.  
           The width is associated to the second bend selected.   
         
        """
        pass
    @property
    def TreatmentType(self) -> ClosedCornerBuilder.TreatmentTypeOptions:
        """
        Getter for property: ( ClosedCornerBuilder.TreatmentTypeOptions NXOpen.Featu) TreatmentType
         Returns the treatment type  
            
         
        """
        pass
    @TreatmentType.setter
    def TreatmentType(self, treatment_type: ClosedCornerBuilder.TreatmentTypeOptions):
        """
        Setter for property: ( ClosedCornerBuilder.TreatmentTypeOptions NXOpen.Featu) TreatmentType
         Returns the treatment type  
            
         
        """
        pass
    @property
    def Type(self) -> ClosedCornerBuilder.Types:
        """
        Getter for property: ( ClosedCornerBuilder.Types NXOpen.Featu) Type
         Returns the feature type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: ClosedCornerBuilder.Types):
        """
        Setter for property: ( ClosedCornerBuilder.Types NXOpen.Featu) Type
         Returns the feature type   
            
         
        """
        pass
    @property
    def VAngle1(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) VAngle1
         Returns the angle1 of V relief.  
           This is the angle associated with the first bend selected.  
         
        """
        pass
    @property
    def VAngle2(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) VAngle2
         Returns the angle2 of V relief.  
           This is the angle associated to the second bend selected.  
         
        """
        pass
    def AddFacePair(self, first_face: NXOpen.Face, second_face: NXOpen.Face) -> None:
        """
         Add a face pair.
        """
        pass
    def GetFacePair(self, index: int) -> Tuple[NXOpen.Face, NXOpen.Face]:
        """
         Return the face pair. 
         Returns A tuple consisting of (first_face, second_face). 
         - first_face is:  NXOpen.Face. First face of the face pair .
         - second_face is:  NXOpen.Face. Second face of the face pair .

        """
        pass
    def GetNumberOfFacePairs(self) -> int:
        """
         Returns the number of face pairs already identified for the three bend corner feature.
                
         Returns number_of_face_pairs (int):  The number of face pairs currently identified .
        """
        pass
    def RemoveFacePair(self, first_face: NXOpen.Face, second_face: NXOpen.Face) -> None:
        """
         Removes a face pair (that represents a unique corner) from the list of face pairs already added.
                
        """
        pass
    def ValidateBuilderData(self) -> int:
        """
         Validates the builder data.
         Returns validity (int):  Returns 0 if the data in the builder is valid .
        """
        pass
import NXOpen
import NXOpen.Features
class ContourFlangeBuilder(SheetmetalBaseBuilder): 
    """ Represents a Contour Flange feature builder. """
    class SectionSideOptions(Enum):
        """
        Members Include: 
         |Left|  
         |Right|  

        """
        Left: int
        Right: int
        @staticmethod
        def ValueOf(value: int) -> ContourFlangeBuilder.SectionSideOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SweepSideOptions(Enum):
        """
        Members Include: 
         |SectionNormalSide|  
         |SectionReverseNormalSide|  

        """
        SectionNormalSide: int
        SectionReverseNormalSide: int
        @staticmethod
        def ValueOf(value: int) -> ContourFlangeBuilder.SweepSideOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SweepTypeOptions(Enum):
        """
        Members Include: 
         |Finite|  
         |Symmetric|  
         |ToEnd|  
         |Chain|  

        """
        Finite: int
        Symmetric: int
        ToEnd: int
        Chain: int
        @staticmethod
        def ValueOf(value: int) -> ContourFlangeBuilder.SweepTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BendOptions(self) -> BendOptions:
        """
        Getter for property: ( BendOptions NXOpen.Featu) BendOptions
         Returns the bend options   
            
         
        """
        pass
    @property
    def EdgeChain(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) EdgeChain
         Returns the section having chain edges.  
             
         
        """
        pass
    @EdgeChain.setter
    def EdgeChain(self, edge_chain: NXOpen.Section):
        """
        Setter for property: ( NXOpen.Section) EdgeChain
         Returns the section having chain edges.  
             
         
        """
        pass
    @property
    def IsSecondary(self) -> bool:
        """
        Getter for property: (bool) IsSecondary
         Returns the contour flange type.  
             
         
        """
        pass
    @IsSecondary.setter
    def IsSecondary(self, is_secondary: bool):
        """
        Setter for property: (bool) IsSecondary
         Returns the contour flange type.  
             
         
        """
        pass
    @property
    def MiterOptions(self) -> MiterOptions:
        """
        Getter for property: ( MiterOptions NXOpen.Featu) MiterOptions
         Returns the miter options   
            
         
        """
        pass
    @property
    def Section(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Section
         Returns the section of contour flange   
            
         
        """
        pass
    @Section.setter
    def Section(self, section: NXOpen.Section):
        """
        Setter for property: ( NXOpen.Section) Section
         Returns the section of contour flange   
            
         
        """
        pass
    @property
    def Sketch(self) -> NXOpen.Features.SketchFeature:
        """
        Getter for property: ( NXOpen.Features.SketchFeature) Sketch
         Returns the sketch   
            
         
        """
        pass
    @Sketch.setter
    def Sketch(self, sketch: NXOpen.Features.SketchFeature):
        """
        Setter for property: ( NXOpen.Features.SketchFeature) Sketch
         Returns the sketch   
            
         
        """
        pass
    @property
    def SweepSide(self) -> ContourFlangeBuilder.SweepSideOptions:
        """
        Getter for property: ( ContourFlangeBuilder.SweepSideOptions NXOpen.Featu) SweepSide
         Returns the projection direction of contour flange   
            
         
        """
        pass
    @SweepSide.setter
    def SweepSide(self, sweep_side: ContourFlangeBuilder.SweepSideOptions):
        """
        Setter for property: ( ContourFlangeBuilder.SweepSideOptions NXOpen.Featu) SweepSide
         Returns the projection direction of contour flange   
            
         
        """
        pass
    @property
    def SweepType(self) -> ContourFlangeBuilder.SweepTypeOptions:
        """
        Getter for property: ( ContourFlangeBuilder.SweepTypeOptions NXOpen.Featu) SweepType
         Returns the projection side of contour flange  
            
         
        """
        pass
    @SweepType.setter
    def SweepType(self, sweep_type: ContourFlangeBuilder.SweepTypeOptions):
        """
        Setter for property: ( ContourFlangeBuilder.SweepTypeOptions NXOpen.Featu) SweepType
         Returns the projection side of contour flange  
            
         
        """
        pass
    @property
    def ThicknessSide(self) -> ContourFlangeBuilder.SectionSideOptions:
        """
        Getter for property: ( ContourFlangeBuilder.SectionSideOptions NXOpen.Featu) ThicknessSide
         Returns the thickness side of contour flange   
            
         
        """
        pass
    @ThicknessSide.setter
    def ThicknessSide(self, section_side: ContourFlangeBuilder.SectionSideOptions):
        """
        Setter for property: ( ContourFlangeBuilder.SectionSideOptions NXOpen.Featu) ThicknessSide
         Returns the thickness side of contour flange   
            
         
        """
        pass
    def GetSweepDistance(self) -> NXOpen.Expression:
        """
         THE projection distance of contour flange 
         Returns sweep_distance ( NXOpen.Expression):  .
        """
        pass
    def GetThickness(self) -> NXOpen.Expression:
        """
         THE thickness of contour flange 
         Returns thickness ( NXOpen.Expression):  .
        """
        pass
    def ValidateBuilderData(self) -> int:
        """
         Verify whether the builder data is valid for creating a Contour Flange or not.
                    
                         If the Builder data is valid, returned value shall be 0
                    
                
         Returns builder_data_validity (int):  Data Validity Flag.
        """
        pass
import NXOpen
class ConvertInputListItemBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[ConvertInputListItemBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: ConvertInputListItemBuilder) -> None:
        """
         Appends an object to the list
            
        """
        pass
    @overload
    def Clear(self) -> None:
        """
         Clears the entire list without deleting the objects.  The caller is responsible for 
                accounting for these objects.  If they are not used or deleted by the time the part is 
                closed (in other words, leaked) an error will occur 
        """
        pass
    def ClearIndex(self, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
               not change, but the item at this index is set to NULL.
            
        """
        pass
    @overload
    def Clear(self, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    @overload
    def Erase(self, index: int) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, obj: ConvertInputListItemBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: ConvertInputListItemBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: ConvertInputListItemBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> ConvertInputListItemBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( ConvertInputListItemBuilder NXOpen.Featu):  object found at input index .
        """
        pass
    def GetContents(self) -> List[ConvertInputListItemBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( ConvertInputListItemBuilder List[NXOpen.Fea):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: ConvertInputListItemBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    def MoveToBottom(self, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    def MoveToTop(self, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    def SetContents(self, objects: List[ConvertInputListItemBuilder]) -> None:
        """
         Sets the contents of the entire list. This overwrites the previous contents of this list, 
                but does not delete any objects that were originally on the list.
             
        """
        pass
    @overload
    def Swap(self, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    @overload
    def Swap(self, object1: ConvertInputListItemBuilder, object2: ConvertInputListItemBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ConvertInputListItemBuilder(NXOpen.TaggedObject): 
    """
        Represents a Sheetmetal convert to sheet metal corner list item builder class.
        This builder is used to interrogate the corner items in the list.
        """
    @property
    def CornerFaces(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) CornerFaces
         Returns the corner faces   
            
         
        """
        pass
import NXOpen
import NXOpen.Features
class ConvertToSheetmetalBuilder(SheetmetalBaseBuilder): 
    """ This is the feature builder for the convert to sheetmetal feature. """
    class BendReliefTypeOptions(Enum):
        """
        Members Include: 
         |NotSet|   
         |Square|   
         |Round|   

        """
        NotSet: int
        Square: int
        Round: int
        @staticmethod
        def ValueOf(value: int) -> ConvertToSheetmetalBuilder.BendReliefTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AdditionalFacesToConvert(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) AdditionalFacesToConvert
         Returns the additional faces to convert   
            
         
        """
        pass
    @property
    def BaseFace(self) -> NXOpen.Face:
        """
        Getter for property: ( NXOpen.Face) BaseFace
         Returns the base face from which the thickness of the part is determined.  
          
                  
         
        """
        pass
    @BaseFace.setter
    def BaseFace(self, base_face: NXOpen.Face):
        """
        Setter for property: ( NXOpen.Face) BaseFace
         Returns the base face from which the thickness of the part is determined.  
          
                  
         
        """
        pass
    @property
    def BendReliefDepth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BendReliefDepth
         Returns the bend relief depth.  
           Not supported for multi-thickness type.
                  
         
        """
        pass
    @property
    def BendReliefType(self) -> ConvertToSheetmetalBuilder.BendReliefTypeOptions:
        """
        Getter for property: ( ConvertToSheetmetalBuilder.BendReliefTypeOptions NXOpen.Featu) BendReliefType
         Returns the bend relief type.  
           Not supported for multi-thickness type.
                  
         
        """
        pass
    @BendReliefType.setter
    def BendReliefType(self, bend_relief_type: ConvertToSheetmetalBuilder.BendReliefTypeOptions):
        """
        Setter for property: ( ConvertToSheetmetalBuilder.BendReliefTypeOptions NXOpen.Featu) BendReliefType
         Returns the bend relief type.  
           Not supported for multi-thickness type.
                  
         
        """
        pass
    @property
    def BendReliefWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BendReliefWidth
         Returns the bend relief width.  
           Not supported for multi-thickness type.
                  
         
        """
        pass
    @property
    def CornerList(self) -> ConvertInputListItemBuilderList:
        """
        Getter for property: ( ConvertInputListItemBuilderList NXOpen.Featu) CornerList
         Returns the corner list.  
           Not supported for multi-thickness type.   
         
        """
        pass
    @property
    def IsUniformThickness(self) -> bool:
        """
        Getter for property: (bool) IsUniformThickness
         Returns the convert type.  
           If true it means the conversion type is uniform thickness.
                    If false it means the conversion type is multi-thickness. It cannot be changed once set.  
         
        """
        pass
    @IsUniformThickness.setter
    def IsUniformThickness(self, isUniform: bool):
        """
        Setter for property: (bool) IsUniformThickness
         Returns the convert type.  
           If true it means the conversion type is uniform thickness.
                    If false it means the conversion type is multi-thickness. It cannot be changed once set.  
         
        """
        pass
    @property
    def LocalBaseFace(self) -> NXOpen.Face:
        """
        Getter for property: ( NXOpen.Face) LocalBaseFace
         Returns the base face of local convert from which the thickness of the part is determined.  
          
                    Not supported for multi-thickness type.
                  
         
        """
        pass
    @LocalBaseFace.setter
    def LocalBaseFace(self, local_base_face: NXOpen.Face):
        """
        Setter for property: ( NXOpen.Face) LocalBaseFace
         Returns the base face of local convert from which the thickness of the part is determined.  
          
                    Not supported for multi-thickness type.
                  
         
        """
        pass
    @property
    def LocalRegionFaces(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) LocalRegionFaces
         Returns the faces for local convert.  
           Not supported for multi-thickness type.   
         
        """
        pass
    @property
    def MaintainZeroBendRadius(self) -> bool:
        """
        Getter for property: (bool) MaintainZeroBendRadius
         Returns the option for Maintain zero bend radius.  
           If the option is set to true,
                    a tiny 0.02 mm radius bend will be created on inside sharp edge (for the 
                    features created in NX8 or later releases); else the radius value from 
                    NXSM Preferences will be used.
                  
         
        """
        pass
    @MaintainZeroBendRadius.setter
    def MaintainZeroBendRadius(self, maintain_zero_bend_radius: bool):
        """
        Setter for property: (bool) MaintainZeroBendRadius
         Returns the option for Maintain zero bend radius.  
           If the option is set to true,
                    a tiny 0.02 mm radius bend will be created on inside sharp edge (for the 
                    features created in NX8 or later releases); else the radius value from 
                    NXSM Preferences will be used.
                  
         
        """
        pass
    @property
    def RipSection(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) RipSection
         Returns the section containing curves that need to be ripped while converting to sheetmetal.  
          \n
                    For NX 12.0.2 and later release, use Edge Rip feature for ripping edges before using 
                    Convert to Sheet Metal feature.
                  
         
        """
        pass
    @RipSection.setter
    def RipSection(self, section: NXOpen.Section):
        """
        Setter for property: ( NXOpen.Section) RipSection
         Returns the section containing curves that need to be ripped while converting to sheetmetal.  
          \n
                    For NX 12.0.2 and later release, use Edge Rip feature for ripping edges before using 
                    Convert to Sheet Metal feature.
                  
         
        """
        pass
    @property
    def Sketch(self) -> NXOpen.Features.SketchFeature:
        """
        Getter for property: ( NXOpen.Features.SketchFeature) Sketch
         Returns the internal sketch (used to specify rip curves), if it exists.  
          \n
                    For NX 12.0.2 and later release, use Edge Rip feature for ripping edges before using 
                    Convert to Sheet Metal feature.
                  
         
        """
        pass
    @Sketch.setter
    def Sketch(self, sketch: NXOpen.Features.SketchFeature):
        """
        Setter for property: ( NXOpen.Features.SketchFeature) Sketch
         Returns the internal sketch (used to specify rip curves), if it exists.  
          \n
                    For NX 12.0.2 and later release, use Edge Rip feature for ripping edges before using 
                    Convert to Sheet Metal feature.
                  
         
        """
        pass
    def CreateConvertInputListItem(self) -> ConvertInputListItemBuilder:
        """
         Create a corner list item. Not supported for multi-thickness type. 
         Returns listitem ( ConvertInputListItemBuilder NXOpen.Featu): .
        """
        pass
    def GetRipEdges(self) -> List[NXOpen.Edge]:
        """
         Gets the array of edges selected for ripping while converting to sheetmetal.\n
                    For NX 12.0.2 and later release, use Edge Rip feature for ripping edges before using 
                    Convert to Sheet Metal feature.
                
         Returns rip_edges ( NXOpen.Edge Li):  .
        """
        pass
    def SetRipEdges(self, rip_edges: List[NXOpen.Edge]) -> None:
        """
          Sets the array of edges that need to be ripped while converting to sheetmetal.\n
                    For NX 12.0.2 and later release, use Edge Rip feature for ripping edges before using 
                    Convert to Sheet Metal feature.
                
        """
        pass
    def ValidateBuilderData(self) -> int:
        """
         Verify that the builder data is valid for feature creation. 
                    
                         If the builder data is valid, it returns a value of 0.
                    
                
         Returns builder_data_validity (int):  data validity flag (0 - valid, 1 - invalid) .
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class CornerTreatmentBuilder(NXOpen.TaggedObject): 
    """ The CornerTreatmentBuilder class is used to manage a builder object for
        a corner treatment in the flat solid and flat pattern dialogs. It includes
        properties and an enumeration type for a flag that indicates whether the
        global (flat pattern preferences) value is to be used, an enumeration type
        that indicates what type of corner treatment to apply, and an expression
        to indicate the value associated with treatment types chamfer and radius.
    """
    class CornerTreatmentType(Enum):
        """
        Members Include: 
         |NotSet| 
         |Chamfer| 
         |Radius| 

        """
        NotSet: int
        Chamfer: int
        Radius: int
        @staticmethod
        def ValueOf(value: int) -> CornerTreatmentBuilder.CornerTreatmentType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def TreatmentType(self) -> CornerTreatmentBuilder.CornerTreatmentType:
        """
        Getter for property: ( CornerTreatmentBuilder.CornerTreatmentType NXOpen.Featu) TreatmentType
         Returns the treatment type option menu value   
            
         
        """
        pass
    @TreatmentType.setter
    def TreatmentType(self, treatmentType: CornerTreatmentBuilder.CornerTreatmentType):
        """
        Setter for property: ( CornerTreatmentBuilder.CornerTreatmentType NXOpen.Featu) TreatmentType
         Returns the treatment type option menu value   
            
         
        """
        pass
    @property
    def UseGlobal(self) -> bool:
        """
        Getter for property: (bool) UseGlobal
         Returns the use global toggle value   
            
         
        """
        pass
    @UseGlobal.setter
    def UseGlobal(self, useGlobal: bool):
        """
        Setter for property: (bool) UseGlobal
         Returns the use global toggle value   
            
         
        """
        pass
    @property
    def Value(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Value
         Returns the value associated with the chamfer and radius treatment types   
            
         
        """
        pass
import NXOpen
import NXOpen.Features
class DimpleBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Dimple feature builder. """
    class DepthTypeOptions(Enum):
        """
        Members Include: 
         |SectionNormalSide|  Dimple punched on the side of the section normal. 
         |SectionReverseNormalSide|  Dimple punched on the side opposite to that of the section normal 

        """
        SectionNormalSide: int
        SectionReverseNormalSide: int
        @staticmethod
        def ValueOf(value: int) -> DimpleBuilder.DepthTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DimensionTypeOptions(Enum):
        """
        Members Include: 
         |Offset|  the actual depth will be depth plus the thickness of sheet. 
         |Full|  the actual extent distance will be the value specified as depth. 

        """
        Offset: int
        Full: int
        @staticmethod
        def ValueOf(value: int) -> DimpleBuilder.DimensionTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SectionSideOptions(Enum):
        """
        Members Include: 
         |Left|  Side pointed to by the inverse of the tangent cross normal vector 
         |Right|  Side pointed to by the tangent cross normal vector 

        """
        Left: int
        Right: int
        @staticmethod
        def ValueOf(value: int) -> DimpleBuilder.SectionSideOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SidewallTypeOptions(Enum):
        """
        Members Include: 
         |Outside|  the innerface of the dimple side walls coincides with the section outline. 
         |Inside|  the outerface of the dimple side walls coincides with the section outline. 

        """
        Outside: int
        Inside: int
        @staticmethod
        def ValueOf(value: int) -> DimpleBuilder.SidewallTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DepthType(self) -> DimpleBuilder.DepthTypeOptions:
        """
        Getter for property: ( DimpleBuilder.DepthTypeOptions NXOpen.Featu) DepthType
         Returns the Direction in which the Dimple is punched.  
          
                      
                        This is used to specify the direction in which the punching should happen. If Punching must happen in the
                        direction of the Section Normal (specified using the NXOpen.Features.SheetMetal.DimpleBuilder.Section) then
                        pass the value of  NXOpen::Features::SheetMetal::DimpleBuilder::DepthTypeOptionsSectionNormalSide 
                        If punching must happen in the opposite direction to that of Section Normal, set the value to be
                         NXOpen::Features::SheetMetal::DimpleBuilder::DepthTypeOptionsSectionReverseNormalSide 
                      
                  
         
        """
        pass
    @DepthType.setter
    def DepthType(self, depth_type: DimpleBuilder.DepthTypeOptions):
        """
        Setter for property: ( DimpleBuilder.DepthTypeOptions NXOpen.Featu) DepthType
         Returns the Direction in which the Dimple is punched.  
          
                      
                        This is used to specify the direction in which the punching should happen. If Punching must happen in the
                        direction of the Section Normal (specified using the NXOpen.Features.SheetMetal.DimpleBuilder.Section) then
                        pass the value of  NXOpen::Features::SheetMetal::DimpleBuilder::DepthTypeOptionsSectionNormalSide 
                        If punching must happen in the opposite direction to that of Section Normal, set the value to be
                         NXOpen::Features::SheetMetal::DimpleBuilder::DepthTypeOptionsSectionReverseNormalSide 
                      
                  
         
        """
        pass
    @property
    def DimensionType(self) -> DimpleBuilder.DimensionTypeOptions:
        """
        Getter for property: ( DimpleBuilder.DimensionTypeOptions NXOpen.Featu) DimensionType
         Returns the Offset Dimension.  
           For NX1872 or later Dimple features this option will always be  NXOpen::Features::SheetMetal::DimpleBuilder::DimensionTypeOptionsFull .
                      
                        The actual extent distance of the Dimple will be determined by the active dimension option.
                        In case of  NXOpen::Features::SheetMetal::DimpleBuilder::DimensionTypeOptionsOffset  the actual extent distance will be offset dimension distance plus the thickness of sheet.
                        In case of  NXOpen::Features::SheetMetal::DimpleBuilder::DimensionTypeOptionsFull  the actual extent distance will be the Full dimension distance.
                      
                  
         
        """
        pass
    @DimensionType.setter
    def DimensionType(self, dimension_type: DimpleBuilder.DimensionTypeOptions):
        """
        Setter for property: ( DimpleBuilder.DimensionTypeOptions NXOpen.Featu) DimensionType
         Returns the Offset Dimension.  
           For NX1872 or later Dimple features this option will always be  NXOpen::Features::SheetMetal::DimpleBuilder::DimensionTypeOptionsFull .
                      
                        The actual extent distance of the Dimple will be determined by the active dimension option.
                        In case of  NXOpen::Features::SheetMetal::DimpleBuilder::DimensionTypeOptionsOffset  the actual extent distance will be offset dimension distance plus the thickness of sheet.
                        In case of  NXOpen::Features::SheetMetal::DimpleBuilder::DimensionTypeOptionsFull  the actual extent distance will be the Full dimension distance.
                      
                  
         
        """
        pass
    @property
    def FilletSectionCorners(self) -> bool:
        """
        Getter for property: (bool) FilletSectionCorners
         Returns the Rounding Option for section Corners which contain Non Fillet Radii
                  
            
         
        """
        pass
    @FilletSectionCorners.setter
    def FilletSectionCorners(self, fillet_section_corners: bool):
        """
        Setter for property: (bool) FilletSectionCorners
         Returns the Rounding Option for section Corners which contain Non Fillet Radii
                  
            
         
        """
        pass
    @property
    def IncludeRounding(self) -> bool:
        """
        Getter for property: (bool) IncludeRounding
         Returns the Rounding type of the Sharp edges of bottom face and top face.  
          
                  
         
        """
        pass
    @IncludeRounding.setter
    def IncludeRounding(self, include_rounding: bool):
        """
        Setter for property: (bool) IncludeRounding
         Returns the Rounding type of the Sharp edges of bottom face and top face.  
          
                  
         
        """
        pass
    @property
    def MinimumToolClearance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumToolClearance
         Returns 
                 the minimum tool clearance expression.  
          
                   
                  
         
        """
        pass
    @property
    def Section(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Section
         Returns the Section used by the Dimple.  
           Section can be OpenClosed.
                      
                        The section is protruded on the reference face at finite distance of extent and in the direction of
                        extent side. The actual extent distance will be determined by the active dimension option i.e. Offset
                        Dimension or Full Dimension. In case of Offset Dimension the actual extent distance will be offset
                        dimension distance plus the thickness of sheet. In case of Full Dimension the actual extent distance
                        will be the Full dimension distance.
                        In case of open section, the end segments are extended to the nearest flat face edges. If the end
                        segments are already crossing the flat face edges, those segments will be trimmed to the edges.
                      
                  
         
        """
        pass
    @Section.setter
    def Section(self, section: NXOpen.Section):
        """
        Setter for property: ( NXOpen.Section) Section
         Returns the Section used by the Dimple.  
           Section can be OpenClosed.
                      
                        The section is protruded on the reference face at finite distance of extent and in the direction of
                        extent side. The actual extent distance will be determined by the active dimension option i.e. Offset
                        Dimension or Full Dimension. In case of Offset Dimension the actual extent distance will be offset
                        dimension distance plus the thickness of sheet. In case of Full Dimension the actual extent distance
                        will be the Full dimension distance.
                        In case of open section, the end segments are extended to the nearest flat face edges. If the end
                        segments are already crossing the flat face edges, those segments will be trimmed to the edges.
                      
                  
         
        """
        pass
    @property
    def SectionSide(self) -> DimpleBuilder.SectionSideOptions:
        """
        Getter for property: ( DimpleBuilder.SectionSideOptions NXOpen.Featu) SectionSide
         Returns the section Side for the Dimple section.  
          
                      
                        This is used to specify which side of the section should remain stationary during the Dimple operation.
                        Dimple's section is a set of connected curves. The material exists on both sides of the section curves.
                        section Side specifies - the material on which side of the curve must be punched.The other side shall
                        be bent to the specified angle with respect to this fixed side. This is how you calculate LeftRight.
                        Get the Section Normal (N)Get the Tangent of the section.(T) Result =  CrossProduct(N, T). The resultant
                        vector is called RIGHT. This vector shall be in the direction of one if the two sides of the material.If
                        you want the material on the side of Result to be punched, then you have to pass the value of
                         NXOpen::Features::SheetMetal::DimpleBuilder::SectionSideOptionsRight  If you want the
                        other side to be punched, then you have to send  NXOpen::Features::SheetMetal::DimpleBuilder::SectionSideOptionsLeft .
                      
                  
         
        """
        pass
    @SectionSide.setter
    def SectionSide(self, section_side: DimpleBuilder.SectionSideOptions):
        """
        Setter for property: ( DimpleBuilder.SectionSideOptions NXOpen.Featu) SectionSide
         Returns the section Side for the Dimple section.  
          
                      
                        This is used to specify which side of the section should remain stationary during the Dimple operation.
                        Dimple's section is a set of connected curves. The material exists on both sides of the section curves.
                        section Side specifies - the material on which side of the curve must be punched.The other side shall
                        be bent to the specified angle with respect to this fixed side. This is how you calculate LeftRight.
                        Get the Section Normal (N)Get the Tangent of the section.(T) Result =  CrossProduct(N, T). The resultant
                        vector is called RIGHT. This vector shall be in the direction of one if the two sides of the material.If
                        you want the material on the side of Result to be punched, then you have to pass the value of
                         NXOpen::Features::SheetMetal::DimpleBuilder::SectionSideOptionsRight  If you want the
                        other side to be punched, then you have to send  NXOpen::Features::SheetMetal::DimpleBuilder::SectionSideOptionsLeft .
                      
                  
         
        """
        pass
    @property
    def SidewallType(self) -> DimpleBuilder.SidewallTypeOptions:
        """
        Getter for property: ( DimpleBuilder.SidewallTypeOptions NXOpen.Featu) SidewallType
         Returns the side where the material must be added to the dimple.  
           Done with Respect to the section
                      
                        If  NXOpen::Features::SheetMetal::DimpleBuilder::SidewallTypeOptionsInside  is specified, the material of the dimple sidewalls will be added to the interior of the section.
                        If  NXOpen::Features::SheetMetal::DimpleBuilder::SidewallTypeOptionsOutside  is specified,the material will be added from the lifted section such that the volume of the dimple cavity is increased.
                      
                  
         
        """
        pass
    @SidewallType.setter
    def SidewallType(self, sidewall_type: DimpleBuilder.SidewallTypeOptions):
        """
        Setter for property: ( DimpleBuilder.SidewallTypeOptions NXOpen.Featu) SidewallType
         Returns the side where the material must be added to the dimple.  
           Done with Respect to the section
                      
                        If  NXOpen::Features::SheetMetal::DimpleBuilder::SidewallTypeOptionsInside  is specified, the material of the dimple sidewalls will be added to the interior of the section.
                        If  NXOpen::Features::SheetMetal::DimpleBuilder::SidewallTypeOptionsOutside  is specified,the material will be added from the lifted section such that the volume of the dimple cavity is increased.
                      
                  
         
        """
        pass
    @property
    def Sketch(self) -> NXOpen.Features.SketchFeature:
        """
        Getter for property: ( NXOpen.Features.SketchFeature) Sketch
         Returns the Slave Sketch used by the Dimple, If one exists.  
          
                      
                        If the Sketch is created internally as part of the Dimple command in the UI, then it shall be consumed by the Dimple and shall not show up as a separate feature in the Part Navigator.
                        If such a behaviour is desired, then specify the Sketch here.
                      
                  
         
        """
        pass
    @Sketch.setter
    def Sketch(self, sketch: NXOpen.Features.SketchFeature):
        """
        Setter for property: ( NXOpen.Features.SketchFeature) Sketch
         Returns the Slave Sketch used by the Dimple, If one exists.  
          
                      
                        If the Sketch is created internally as part of the Dimple command in the UI, then it shall be consumed by the Dimple and shall not show up as a separate feature in the Part Navigator.
                        If such a behaviour is desired, then specify the Sketch here.
                      
                  
         
        """
        pass
    def GetDepth(self) -> NXOpen.Expression:
        """
         Depth of the Dimple
         Returns extent ( NXOpen.Expression):  .
        """
        pass
    def GetDieRadius(self) -> NXOpen.Expression:
        """
         Radius value of the sharp edges of the bottom face
         Returns die_radius ( NXOpen.Expression):  .
        """
        pass
    def GetFilletRadius(self) -> NXOpen.Expression:
        """
         Fillet Radius to be applied for rounding the Sharp section Corners
                
         Returns fillet_radius ( NXOpen.Expression):  .
        """
        pass
    def GetPunchRadius(self) -> NXOpen.Expression:
        """
         Radius value of the sharp edges on the top face
         Returns punch_radius ( NXOpen.Expression):  .
        """
        pass
    def GetTaperAngle(self) -> NXOpen.Expression:
        """
         Taper Angle of the Dimple.
                    
                        In case of a tapered dimple, the taper angle is applied on the side faces of the above-protruded section.
                        The affects of taper angle will always increases the cavity volume of the dimple.
                    
                
         Returns taper_angle ( NXOpen.Expression):  .
        """
        pass
    def ValidateBuilderData(self) -> int:
        """
         Verify whether the builder data is valid for creating a dimple or not.
                    
                         If the Builder data is valid, returned value shall be 0
                    
                
         Returns builderDataValidity (int):  Data Validity Flag.
        """
        pass
import NXOpen
import NXOpen.Features
class DrawnCutoutBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Drawn Cutout feature builder. """
    class DepthTypeOptions(Enum):
        """
        Members Include: 
         |SectionNormalSide|  Drawn Cutout punched on the side of the section normal. 
         |SectionReverseNormalSide|  Drawn Cutout punched on the side opposite to that of the section normal 

        """
        SectionNormalSide: int
        SectionReverseNormalSide: int
        @staticmethod
        def ValueOf(value: int) -> DrawnCutoutBuilder.DepthTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SectionSideOptions(Enum):
        """
        Members Include: 
         |Left|  Side pointed to by the inverse of the tangent cross normal vector 
         |Right|  Side pointed to by the tangent cross normal vector 

        """
        Left: int
        Right: int
        @staticmethod
        def ValueOf(value: int) -> DrawnCutoutBuilder.SectionSideOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SidewallTypeOptions(Enum):
        """
        Members Include: 
         |Outside|  the innerface of the drawn cutout side walls coincides with the section outline. 
         |Inside|  the outerface of the drawn cutout side walls coincides with the section outline. 

        """
        Outside: int
        Inside: int
        @staticmethod
        def ValueOf(value: int) -> DrawnCutoutBuilder.SidewallTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CornerRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CornerRadius
         Returns the Radius to be applied for rounding the sharp section corners
                  
            
         
        """
        pass
    @property
    def CutoutDepth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CutoutDepth
         Returns the depth of the Drawn Cutout  
            
         
        """
        pass
    @property
    def DepthType(self) -> DrawnCutoutBuilder.DepthTypeOptions:
        """
        Getter for property: ( DrawnCutoutBuilder.DepthTypeOptions NXOpen.Featu) DepthType
         Returns the Direction in which the Drawn Cutout is punched.  
          
                      
                        This is used to specify the direction in which the punching should happen. If Punching must happen in the
                        direction of the Section Normal (see  NXOpen::Features::SheetMetal::DrawnCutoutBuilder::Section ) then
                        pass the value of  NXOpen::Features::SheetMetal::DrawnCutoutBuilder::DepthTypeOptionsSectionNormalSide 
                        If punching must happen in the opposite direction to that of Section Normal, set the value to be
                         NXOpen::Features::SheetMetal::DrawnCutoutBuilder::DepthTypeOptionsSectionReverseNormalSide 
                      
                  
         
        """
        pass
    @DepthType.setter
    def DepthType(self, depth_type: DrawnCutoutBuilder.DepthTypeOptions):
        """
        Setter for property: ( DrawnCutoutBuilder.DepthTypeOptions NXOpen.Featu) DepthType
         Returns the Direction in which the Drawn Cutout is punched.  
          
                      
                        This is used to specify the direction in which the punching should happen. If Punching must happen in the
                        direction of the Section Normal (see  NXOpen::Features::SheetMetal::DrawnCutoutBuilder::Section ) then
                        pass the value of  NXOpen::Features::SheetMetal::DrawnCutoutBuilder::DepthTypeOptionsSectionNormalSide 
                        If punching must happen in the opposite direction to that of Section Normal, set the value to be
                         NXOpen::Features::SheetMetal::DrawnCutoutBuilder::DepthTypeOptionsSectionReverseNormalSide 
                      
                  
         
        """
        pass
    @property
    def FilletSectionCorners(self) -> bool:
        """
        Getter for property: (bool) FilletSectionCorners
         Returns the Rounding Option for section Corners which contain Non Fillet Radii
                  
            
         
        """
        pass
    @FilletSectionCorners.setter
    def FilletSectionCorners(self, fillet_section_corners: bool):
        """
        Setter for property: (bool) FilletSectionCorners
         Returns the Rounding Option for section Corners which contain Non Fillet Radii
                  
            
         
        """
        pass
    @property
    def IncludeRounding(self) -> bool:
        """
        Getter for property: (bool) IncludeRounding
         Returns the Rounding type of the Sharp edges of bottom face and top face.  
          
                  
         
        """
        pass
    @IncludeRounding.setter
    def IncludeRounding(self, round_type: bool):
        """
        Setter for property: (bool) IncludeRounding
         Returns the Rounding type of the Sharp edges of bottom face and top face.  
          
                  
         
        """
        pass
    @property
    def MinimumToolClearance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumToolClearance
         Returns 
                the minimum tool clearance expression.  
          
                   
                  
         
        """
        pass
    @property
    def RadiusOfDie(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RadiusOfDie
         Returns the Radius value of the sharp edges of the bottom face  
            
         
        """
        pass
    @property
    def Section(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Section
         Returns the Section used by the Drawn Cutout.  
           Section can be OpenClosed.
                      
                        The section is protruded on the reference face at finite distance of extent and in the direction of
                        extent side. The actual extent distance will be determined by the active dimension option i.e. Offset
                        Dimension or Full Dimension. In case of Offset Dimension the actual extent distance will be offset
                        dimension distance plus the thickness of sheet. In case of Full Dimension the actual extent distance
                        will be the Full dimension distance.
                        In case of open section, the end segments are extended to the nearest flat face edges. If the end
                        segments are already crossing the flat face edges, those segments will be trimmed to the edges.
                      
                  
         
        """
        pass
    @Section.setter
    def Section(self, section: NXOpen.Section):
        """
        Setter for property: ( NXOpen.Section) Section
         Returns the Section used by the Drawn Cutout.  
           Section can be OpenClosed.
                      
                        The section is protruded on the reference face at finite distance of extent and in the direction of
                        extent side. The actual extent distance will be determined by the active dimension option i.e. Offset
                        Dimension or Full Dimension. In case of Offset Dimension the actual extent distance will be offset
                        dimension distance plus the thickness of sheet. In case of Full Dimension the actual extent distance
                        will be the Full dimension distance.
                        In case of open section, the end segments are extended to the nearest flat face edges. If the end
                        segments are already crossing the flat face edges, those segments will be trimmed to the edges.
                      
                  
         
        """
        pass
    @property
    def SectionSide(self) -> DrawnCutoutBuilder.SectionSideOptions:
        """
        Getter for property: ( DrawnCutoutBuilder.SectionSideOptions NXOpen.Featu) SectionSide
         Returns the section side for the Drawn Cutout.  
          
                      
                        This is used to specify which side of the section should remain stationary during the drawn cutout operation.
                        drawn cutout's section is a set of connected curves. The material exists on both sides of the section curves.
                        section Side specifies - the material on which side of the curve must be punched.The other side shall
                        be bent to the specified angle with respect to this fixed side. This is how you calculate LeftRight.
                        Get the Section Normal (N)Get the Tangent of the section.(T) Result =  CrossProduct(N, T). The resultant
                        vector is called RIGHT. This vector shall be in the direction of one if the two sides of the material.If
                        you want the material on the side of Result to be punched, then you have to pass the value of
                         NXOpen::Features::SheetMetal::DrawnCutoutBuilder::SectionSideOptionsRight  If you want the
                        other side to be punched, then you have to send  NXOpen::Features::SheetMetal::DrawnCutoutBuilder::SectionSideOptionsLeft .
                      
                  
         
        """
        pass
    @SectionSide.setter
    def SectionSide(self, section_side: DrawnCutoutBuilder.SectionSideOptions):
        """
        Setter for property: ( DrawnCutoutBuilder.SectionSideOptions NXOpen.Featu) SectionSide
         Returns the section side for the Drawn Cutout.  
          
                      
                        This is used to specify which side of the section should remain stationary during the drawn cutout operation.
                        drawn cutout's section is a set of connected curves. The material exists on both sides of the section curves.
                        section Side specifies - the material on which side of the curve must be punched.The other side shall
                        be bent to the specified angle with respect to this fixed side. This is how you calculate LeftRight.
                        Get the Section Normal (N)Get the Tangent of the section.(T) Result =  CrossProduct(N, T). The resultant
                        vector is called RIGHT. This vector shall be in the direction of one if the two sides of the material.If
                        you want the material on the side of Result to be punched, then you have to pass the value of
                         NXOpen::Features::SheetMetal::DrawnCutoutBuilder::SectionSideOptionsRight  If you want the
                        other side to be punched, then you have to send  NXOpen::Features::SheetMetal::DrawnCutoutBuilder::SectionSideOptionsLeft .
                      
                  
         
        """
        pass
    @property
    def SideAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SideAngle
         Returns the Side Angle used by the Drawn Cutout.  
          
                      
                        In case of a tapered drawn cutout, the side angle is applied on the side faces of the above-protruded section.
                        The affects of side angle will always increases the cavity volume of the drawn cutout.
                      
                  
         
        """
        pass
    @property
    def SidewallType(self) -> DrawnCutoutBuilder.SidewallTypeOptions:
        """
        Getter for property: ( DrawnCutoutBuilder.SidewallTypeOptions NXOpen.Featu) SidewallType
         Returns the side where the material must be added to the Drawn Cutout.  
           Done with Respect to the section
                      
                        If  NXOpen::Features::SheetMetal::DrawnCutoutBuilder::SidewallTypeOptionsInside  is specified, the material of the drawn cutout sidewalls will be added to the interior of the section.
                        If  NXOpen::Features::SheetMetal::DrawnCutoutBuilder::SidewallTypeOptionsOutside  is specified,the material will be added from the lifted section such that the volume of the drawn cutout cavity is increased.
                      
                  
         
        """
        pass
    @SidewallType.setter
    def SidewallType(self, sidewall_type: DrawnCutoutBuilder.SidewallTypeOptions):
        """
        Setter for property: ( DrawnCutoutBuilder.SidewallTypeOptions NXOpen.Featu) SidewallType
         Returns the side where the material must be added to the Drawn Cutout.  
           Done with Respect to the section
                      
                        If  NXOpen::Features::SheetMetal::DrawnCutoutBuilder::SidewallTypeOptionsInside  is specified, the material of the drawn cutout sidewalls will be added to the interior of the section.
                        If  NXOpen::Features::SheetMetal::DrawnCutoutBuilder::SidewallTypeOptionsOutside  is specified,the material will be added from the lifted section such that the volume of the drawn cutout cavity is increased.
                      
                  
         
        """
        pass
    @property
    def Sketch(self) -> NXOpen.Features.SketchFeature:
        """
        Getter for property: ( NXOpen.Features.SketchFeature) Sketch
         Returns the Slave Sketch used by the Drawn Cutout, If one exists.  
          
                      
                        If the Sketch is created internally as part of the Drawn Cutout command in the UI, then it shall be consumed by the Drawn Cutout and shall not show up as a separate feature in the Part Navigator.
                        If such a behaviour is deired, then specify the Sketch here.
                      
                  
         
        """
        pass
    @Sketch.setter
    def Sketch(self, sketch: NXOpen.Features.SketchFeature):
        """
        Setter for property: ( NXOpen.Features.SketchFeature) Sketch
         Returns the Slave Sketch used by the Drawn Cutout, If one exists.  
          
                      
                        If the Sketch is created internally as part of the Drawn Cutout command in the UI, then it shall be consumed by the Drawn Cutout and shall not show up as a separate feature in the Part Navigator.
                        If such a behaviour is deired, then specify the Sketch here.
                      
                  
         
        """
        pass
    def ValidateBuilderData(self) -> int:
        """
         Verify whether the builder data is valid for creating a Drawn Cutout or not.
                    
                         If the Builder data is valid, returned value shall be 0
                    
                
         Returns builder_data_validity (int):  Data Validity Flag.
        """
        pass
import NXOpen
import NXOpen.Features
class EdgeRipBuilder(SheetmetalBaseBuilder): 
    """ Represents a Edge Rip feature builder. """
    class EndCapShapeOptions(Enum):
        """
        Members Include: 
         |Square| square end caps
         |Round| round end caps

        """
        Square: int
        Round: int
        @staticmethod
        def ValueOf(value: int) -> EdgeRipBuilder.EndCapShapeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BlendRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BlendRadius
         Returns the blend radius.  
           This only applies if  NXOpen::Features::SheetMetal::EdgeRipBuilder::BlendSharpCorners  is set to true.   
         
        """
        pass
    @property
    def BlendSharpCorners(self) -> bool:
        """
        Getter for property: (bool) BlendSharpCorners
         Returns whether sharp corners should be blended.  
           If true, blends will be applied at sharp corners with radius specified by  NXOpen::Features::SheetMetal::EdgeRipBuilder::BlendRadius .   
         
        """
        pass
    @BlendSharpCorners.setter
    def BlendSharpCorners(self, blendSharpCorners: bool):
        """
        Setter for property: (bool) BlendSharpCorners
         Returns whether sharp corners should be blended.  
           If true, blends will be applied at sharp corners with radius specified by  NXOpen::Features::SheetMetal::EdgeRipBuilder::BlendRadius .   
         
        """
        pass
    @property
    def EndCapShape(self) -> EdgeRipBuilder.EndCapShapeOptions:
        """
        Getter for property: ( EdgeRipBuilder.EndCapShapeOptions NXOpen.Featu) EndCapShape
         Returns the end cap shape type.  
           This only applies if  NXOpen::Features::SheetMetal::EdgeRipBuilder::UseSystemWidth  is set to false.
                      
                        Specify  NXOpen::Features::SheetMetal::EdgeRipBuilder::EndCapShapeOptionsSquare  for square end caps.
                        Specify  NXOpen::Features::SheetMetal::EdgeRipBuilder::EndCapShapeOptionsRound  for rounded end caps.
                      
                  
         
        """
        pass
    @EndCapShape.setter
    def EndCapShape(self, endCapShape: EdgeRipBuilder.EndCapShapeOptions):
        """
        Setter for property: ( EdgeRipBuilder.EndCapShapeOptions NXOpen.Featu) EndCapShape
         Returns the end cap shape type.  
           This only applies if  NXOpen::Features::SheetMetal::EdgeRipBuilder::UseSystemWidth  is set to false.
                      
                        Specify  NXOpen::Features::SheetMetal::EdgeRipBuilder::EndCapShapeOptionsSquare  for square end caps.
                        Specify  NXOpen::Features::SheetMetal::EdgeRipBuilder::EndCapShapeOptionsRound  for rounded end caps.
                      
                  
         
        """
        pass
    @property
    def ReverseWidthDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseWidthDirection
         Returns the Rip width is flipped or not.  
           This only applies when  NXOpen::Features::SheetMetal::EdgeRipBuilder::Symmetric  is set to false.  
         
        """
        pass
    @ReverseWidthDirection.setter
    def ReverseWidthDirection(self, isRipFlip: bool):
        """
        Setter for property: (bool) ReverseWidthDirection
         Returns the Rip width is flipped or not.  
           This only applies when  NXOpen::Features::SheetMetal::EdgeRipBuilder::Symmetric  is set to false.  
         
        """
        pass
    @property
    def Section(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Section
         Returns the section used by Edge Rip   
            
         
        """
        pass
    @Section.setter
    def Section(self, section: NXOpen.Section):
        """
        Setter for property: ( NXOpen.Section) Section
         Returns the section used by Edge Rip   
            
         
        """
        pass
    @property
    def Sketch(self) -> NXOpen.Features.SketchFeature:
        """
        Getter for property: ( NXOpen.Features.SketchFeature) Sketch
         Returns the Slave Sketch used by the Edge Rip, If one exists.  
            
         
        """
        pass
    @Sketch.setter
    def Sketch(self, sketch: NXOpen.Features.SketchFeature):
        """
        Setter for property: ( NXOpen.Features.SketchFeature) Sketch
         Returns the Slave Sketch used by the Edge Rip, If one exists.  
            
         
        """
        pass
    @property
    def Symmetric(self) -> bool:
        """
        Getter for property: (bool) Symmetric
         Returns the Rip is symmetric or not  
            
         
        """
        pass
    @Symmetric.setter
    def Symmetric(self, symmToggle: bool):
        """
        Setter for property: (bool) Symmetric
         Returns the Rip is symmetric or not  
            
         
        """
        pass
    @property
    def UseSystemWidth(self) -> bool:
        """
        Getter for property: (bool) UseSystemWidth
         Returns whether the system width should be used.  
            If true, edge rip will be created with the system default rip width.   
         
        """
        pass
    @UseSystemWidth.setter
    def UseSystemWidth(self, useSystemWidth: bool):
        """
        Setter for property: (bool) UseSystemWidth
         Returns whether the system width should be used.  
            If true, edge rip will be created with the system default rip width.   
         
        """
        pass
    @property
    def Width(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Width
         Returns the rip width.  
           This only applies if  NXOpen::Features::SheetMetal::EdgeRipBuilder::UseSystemWidth  is set to false.   
         
        """
        pass
    def GetRipEdges(self) -> List[NXOpen.Edge]:
        """
         Edges to rip 
         Returns rip_edges ( NXOpen.Edge Li):  Rip Edges .
        """
        pass
    def SetRipEdges(self, rip_edges: List[NXOpen.Edge]) -> None:
        """
         Edges to rip 
        """
        pass
    def ValidateBuilderData(self) -> int:
        """
         Verify whether the builder data is valid for creating a Edge Rip or not.
                    
                         If the Builder data is valid, returned value shall be 0
                    
                
         Returns builder_data_validity (int):  Data Validity Flag.
        """
        pass
import NXOpen
import NXOpen.Features
class ExportFlatPatternBuilder(NXOpen.Builder): 
    """ Represents a Export flat pattern builder. """
    class DxfRevisionType(Enum):
        """
        Members Include: 
         |R12|  Export in the DXF Revision Release 12 format 
         |R13|  Export in the DXF Revision Release 13 format 
         |R14|  Export in the DXF Revision Release 14 format 
         |R2000|  Export in the DXF Revision Release 2000 format 
         |R2004|  Export in the DXF Revision Release 2004 format 
         |R2005|  Export in the DXF Revision Release 2005 format 
         |R2007|  Export in the DXF Revision Release 2007 format 
         |R20102012|  Export in the DXF Revision Release 2010-2012 format 
         |R20132016|  Export in the DXF Revision Release 2013-2017 format 
         |R2018|  Export in the DXF Revision Release 2018-2025 format 

        """
        R12: int
        R13: int
        R14: int
        R2000: int
        R2004: int
        R2005: int
        R2007: int
        R20102012: int
        R20132016: int
        R2018: int
        @staticmethod
        def ValueOf(value: int) -> ExportFlatPatternBuilder.DxfRevisionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ExportLocationOptions(Enum):
        """
        Members Include: 
         |Teamcenter| Teamcenter
         |Native| Native

        """
        Teamcenter: int
        Native: int
        @staticmethod
        def ValueOf(value: int) -> ExportFlatPatternBuilder.ExportLocationOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FileType(Enum):
        """
        Members Include: 
         |Dxf|  DXF Export 
         |TrumpfGeo|  Trumpf Geo Export 

        """
        Dxf: int
        TrumpfGeo: int
        @staticmethod
        def ValueOf(value: int) -> ExportFlatPatternBuilder.FileType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AddedBottom(self) -> bool:
        """
        Getter for property: (bool) AddedBottom
         Returns the option to export the added bottom geometry   
            
         
        """
        pass
    @AddedBottom.setter
    def AddedBottom(self, addedBottom: bool):
        """
        Setter for property: (bool) AddedBottom
         Returns the option to export the added bottom geometry   
            
         
        """
        pass
    @property
    def AddedTop(self) -> bool:
        """
        Getter for property: (bool) AddedTop
         Returns the option to export the added top geometry   
            
         
        """
        pass
    @AddedTop.setter
    def AddedTop(self, addedTop: bool):
        """
        Setter for property: (bool) AddedTop
         Returns the option to export the added top geometry   
            
         
        """
        pass
    @property
    def BendDown(self) -> bool:
        """
        Getter for property: (bool) BendDown
         Returns the option to export the bend down center line   
            
         
        """
        pass
    @BendDown.setter
    def BendDown(self, bendDown: bool):
        """
        Setter for property: (bool) BendDown
         Returns the option to export the bend down center line   
            
         
        """
        pass
    @property
    def BendTangent(self) -> bool:
        """
        Getter for property: (bool) BendTangent
         Returns the option to export the bend tangent line   
            
         
        """
        pass
    @BendTangent.setter
    def BendTangent(self, bendTangent: bool):
        """
        Setter for property: (bool) BendTangent
         Returns the option to export the bend tangent line   
            
         
        """
        pass
    @property
    def BendUp(self) -> bool:
        """
        Getter for property: (bool) BendUp
         Returns the option to export the bend up center line   
            
         
        """
        pass
    @BendUp.setter
    def BendUp(self, bendUp: bool):
        """
        Setter for property: (bool) BendUp
         Returns the option to export the bend up center line   
            
         
        """
        pass
    @property
    def DeviationalTolerance(self) -> float:
        """
        Getter for property: (float) DeviationalTolerance
         Returns the deviational tolerance   
            
         
        """
        pass
    @DeviationalTolerance.setter
    def DeviationalTolerance(self, deviationalTolerance: float):
        """
        Setter for property: (float) DeviationalTolerance
         Returns the deviational tolerance   
            
         
        """
        pass
    @property
    def DxfRevision(self) -> ExportFlatPatternBuilder.DxfRevisionType:
        """
        Getter for property: ( ExportFlatPatternBuilder.DxfRevisionType NXOpen.Featu) DxfRevision
         Returns the dxf revision.  
           The options are in  NXOpen::Features::SheetMetal::ExportFlatPatternBuilder::DxfRevisionType .  
         
        """
        pass
    @DxfRevision.setter
    def DxfRevision(self, dxfRevision: ExportFlatPatternBuilder.DxfRevisionType):
        """
        Setter for property: ( ExportFlatPatternBuilder.DxfRevisionType NXOpen.Featu) DxfRevision
         Returns the dxf revision.  
           The options are in  NXOpen::Features::SheetMetal::ExportFlatPatternBuilder::DxfRevisionType .  
         
        """
        pass
    @property
    def ExportLocation(self) -> ExportFlatPatternBuilder.ExportLocationOptions:
        """
        Getter for property: ( ExportFlatPatternBuilder.ExportLocationOptions NXOpen.Featu) ExportLocation
         Returns the export location.  
             
         
        """
        pass
    @ExportLocation.setter
    def ExportLocation(self, exportLocation: ExportFlatPatternBuilder.ExportLocationOptions):
        """
        Setter for property: ( ExportFlatPatternBuilder.ExportLocationOptions NXOpen.Featu) ExportLocation
         Returns the export location.  
             
         
        """
        pass
    @property
    def FlatPattern(self) -> NXOpen.Features.SelectFlatPattern:
        """
        Getter for property: ( NXOpen.Features.SelectFlatPattern) FlatPattern
         Returns the flat pattern feature   
            
         
        """
        pass
    @property
    def InnerMold(self) -> bool:
        """
        Getter for property: (bool) InnerMold
         Returns the option to export the inner mold 
                      
                        Use this option only for the DXF type.  
          
                      
                  
         
        """
        pass
    @InnerMold.setter
    def InnerMold(self, innerMold: bool):
        """
        Setter for property: (bool) InnerMold
         Returns the option to export the inner mold 
                      
                        Use this option only for the DXF type.  
          
                      
                  
         
        """
        pass
    @property
    def InteriorCutout(self) -> bool:
        """
        Getter for property: (bool) InteriorCutout
         Returns the option to export the interior cutout   
            
         
        """
        pass
    @InteriorCutout.setter
    def InteriorCutout(self, interiorCutout: bool):
        """
        Setter for property: (bool) InteriorCutout
         Returns the option to export the interior cutout   
            
         
        """
        pass
    @property
    def InteriorFeature(self) -> bool:
        """
        Getter for property: (bool) InteriorFeature
         Returns the option to export the interior feature   
            
         
        """
        pass
    @InteriorFeature.setter
    def InteriorFeature(self, interiorFeature: bool):
        """
        Setter for property: (bool) InteriorFeature
         Returns the option to export the interior feature   
            
         
        """
        pass
    @property
    def OuterMold(self) -> bool:
        """
        Getter for property: (bool) OuterMold
         Returns the option to export the outer mold 
                      
                        Use this option only for the DXF type.  
          
                      
                  
         
        """
        pass
    @OuterMold.setter
    def OuterMold(self, outerMold: bool):
        """
        Setter for property: (bool) OuterMold
         Returns the option to export the outer mold 
                      
                        Use this option only for the DXF type.  
          
                      
                  
         
        """
        pass
    @property
    def OutputFile(self) -> str:
        """
        Getter for property: (str) OutputFile
         Returns the output file used to export flat pattern curves   
            
         
        """
        pass
    @OutputFile.setter
    def OutputFile(self, filename: str):
        """
        Setter for property: (str) OutputFile
         Returns the output file used to export flat pattern curves   
            
         
        """
        pass
    @property
    def Type(self) -> ExportFlatPatternBuilder.FileType:
        """
        Getter for property: ( ExportFlatPatternBuilder.FileType NXOpen.Featu) Type
         Returns the type for the flat pattern export.  
          The options are in  NXOpen::Features::SheetMetal::ExportFlatPatternBuilder::Type .   
         
        """
        pass
    @Type.setter
    def Type(self, type: ExportFlatPatternBuilder.FileType):
        """
        Setter for property: ( ExportFlatPatternBuilder.FileType NXOpen.Featu) Type
         Returns the type for the flat pattern export.  
          The options are in  NXOpen::Features::SheetMetal::ExportFlatPatternBuilder::Type .   
         
        """
        pass
import NXOpen
class FeatureBendPropertiesBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[FeatureBendPropertiesBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: FeatureBendPropertiesBuilder) -> None:
        """
         Appends an object to the list
            
        """
        pass
    @overload
    def Clear(self) -> None:
        """
         Clears the entire list without deleting the objects.  The caller is responsible for 
                accounting for these objects.  If they are not used or deleted by the time the part is 
                closed (in other words, leaked) an error will occur 
        """
        pass
    def ClearIndex(self, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
               not change, but the item at this index is set to NULL.
            
        """
        pass
    @overload
    def Clear(self, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    @overload
    def Erase(self, index: int) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, obj: FeatureBendPropertiesBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: FeatureBendPropertiesBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: FeatureBendPropertiesBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> FeatureBendPropertiesBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( FeatureBendPropertiesBuilder NXOpen.Featu):  object found at input index .
        """
        pass
    def GetContents(self) -> List[FeatureBendPropertiesBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( FeatureBendPropertiesBuilder List[NXOpen.Fea):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: FeatureBendPropertiesBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    def MoveToBottom(self, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    def MoveToTop(self, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    def SetContents(self, objects: List[FeatureBendPropertiesBuilder]) -> None:
        """
         Sets the contents of the entire list. This overwrites the previous contents of this list, 
                but does not delete any objects that were originally on the list.
             
        """
        pass
    @overload
    def Swap(self, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    @overload
    def Swap(self, object1: FeatureBendPropertiesBuilder, object2: FeatureBendPropertiesBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class FeatureBendPropertiesBuilder(SheetmetalComponentBuilder): 
    """ Represents a Sheetmetal Feature bend properties builder class. This builder is used to
        interrogate the feature properties in the list."""
    @property
    def BendOptions(self) -> BendOptions:
        """
        Getter for property: ( BendOptions NXOpen.Featu) BendOptions
         Returns the Sheet Metal Bend Options   
            
         
        """
        pass
    @property
    def Value(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Value
         Returns the offset   
            
         
        """
        pass
class FeatureBendPropertiesListBuilder(SheetmetalComponentBuilder): 
    """ Represents a Sheetmetal Feature properties List builder class. This builder is used to
        interrogate the feature properties list."""
    @property
    def FeatureBendPropertiesList(self) -> FeatureBendPropertiesBuilderList:
        """
        Getter for property: ( FeatureBendPropertiesBuilderList NXOpen.Featu) FeatureBendPropertiesList
         Returns the feature properties list   
            
         
        """
        pass
    def CreateFeatureProperties(self) -> FeatureBendPropertiesBuilder:
        """
         Create a feature properties. 
         Returns listitem ( FeatureBendPropertiesBuilder NXOpen.Featu): .
        """
        pass
class FeatureProperty(Enum):
    """
    Members Include: 
     |IgNullConstant|  
     |IgLeft|  
     |IgRight|  
     |IgSymmetric|  
     |IgInside|  
     |IgOutside|  
     |IgBoth|  
     |IgNormalSidedummy|  
     |IgReverseNormalSidedummy|  
     |IgExtend|  
     |IgNoextend|  
     |IgThkinprofileplane|  
     |IgThkNormalToProfilePlane|  
     |IgFinite|  
     |IgTonext|  
     |IgFromTo|  
     |IgThroughAll|  
     |IgThreeHundredAndSixty|  
     |IgParallelDummy|  
     |IgAngularDummy|  
     |IgNormal|  
     |IgThroughAxis|  
     |IgSingleEdge|  
     |IgMultipleEdges|  
     |IgEdgesByLoop|  
     |IgEdgesByVertex|  
     |IgAll|  
     |IgConcave|  
     |IgConvex|  
     |IgStart|  
     |IgEnd|  
     |IgLinear|  
     |IgRadial|  
     |IgRegularHole|  
     |IgCounterBoreHole|  
     |IgCounterSinkHole|  
     |IgCounterDrillHole|  
     |IgTappedHole|  
     |IgTaperedHole|  
     |IgConstRadiusRound|  
     |IgVarRadiusRound|  
     |IgChamfer45degSetback|  
     |IgChamferAngleSetback|  
     |IgChamfer2Serbacks|  
     |IgNone|  
     |IgTaperByAngle|  
     |IgTaperByRatio|  
     |IgClosed|  
     |IgProfileBasedCrosssection|  
     |IgEdgeBasedCrosssection|  
     |IgTangent|  
     |IgRectangularBendRelief|  
     |IgFilletBendRelief|  
     |IgRipBendRelief|  
     |IgBendOnlyCornerRelief|  
     |IgBendAndFaceCornerRelief|  
     |IgRipCornerRelief|  
     |IgNftype|  
     |IgEquationType|  
     |IgPatternMirror|  
     |IgPatternRectangular|  
     |IgPatternCircular|  
     |IgPatternUserDefined|  
     |IgFromReferenceEnd|  
     |IgFromNonreferenceEnd|  
     |IgRndRollAcrossTnagentEdgesOn|  
     |IgRndRollAcrossTangentEdgesOff|  
     |IgRndCapAcrossSharpEdges|  
     |IgRndRollAcrossSharpEdges|  
     |IgRndRollAlongBlendEdgesOn|  
     |IgRndRollAlongBlendEdgesOff|  
     |IgToKepPoint|  
     |IgFlatten|  
     |IgAsConstruction|  
     |IgOffset|  
     |IgMitreParalletToThickness|  
     |IgMitreNormalToThickness|  
     |IgMitreByDist|  
     |IgMitreByAngle|  
     |IgMiterRegularCut|  
     |IgMitreManufacturingCut|  
     |IgProjectOptionProject|  
     |IgProjectOptionWrap|  
     |IgLip|  
     |IgGroove|  
     |IgPartingFromPlane|  
     |IgPartingFromSurface|  
     |IgPartingFromEdge|  
     |IgPartingFromCurve|  
     |IgSplitDraft|  
     |IgSplitAngle1Right|  
     |IgSplitAngle1Left|  
     |IgLouverformedendtype|  
     |IgLouverlancedendtype|  
     |IgLouverround|  
     |IgLouverroundnone|  
     |IgInsideDimension|  
     |IgOutsideDimension|  
     |IgFull|  
     |IgBend|  
     |IgAddRound|  
     |IgNoRound|  
     |IgCloseFaces|  
     |IgOverlapFaces|  
     |IgTreatmentOff|  
     |IgTreatmentIntersect|  
     |IgTreatmentCircleCutout|  
     |IgStepDreat|  
     |IgShowBoundaries|  
     |IgRemoveBoundaries|  
     |IgCornerRound|  
     |IgNoCornerRound|  
     |IgNatural|  
     |IgPeriodic|  
     |IgRoundAllVertexSetback|  
     |IgRoundSingleVertexSetback|  
     |IgRoundVertexEdgeSetback|  
     |IgRoundSetbackIsAbsolute|  
     |IgRoundSetbackIsRelative|  
     |IgCircular|  
     |IgUshaped|  
     |IgVshaped|  
     |IgPunchedEnd|  
     |IgLancedEnd|  
     |IgFormedEnd|  
     |IgSweepAlignParallel|  
     |IgSweepAlignNormal|  
     |IgRoundStartVertexEdgeSetback|  
     |IgRoundEndVertexEdgeSetback|  
     |IgSubtract|  
     |IgUnite|  
     |IgIntersect|  
     |IgContinuous|  
     |IgFlangeFulledge|  
     |IgFlangeCenterOfEdge|  
     |IgFlangeStartOnEndEdge|  
     |IgFlangeEndOnEndEdge|  
     |IgFlangeStartFromEndEdge|  
     |IgFlangeEndFromEndEdge|  
     |IgFlangeFromBothEndsOfEdge|  
     |IgFlangeOffset|  
     |IgChainedCornerRelief|  
     |IgTangentInterior|  
     |IgParallelToPlane|  
     |IgVbottomDimToFlat|  
     |IgVbottomDimToV|  
     |IgTaperDimAtTop|  
     |IgTaperDimAtBottom|  
     |IgCounterBoreProfileIsAtTop|  
     |IgCounterBoreProfileIsAtBottom|  
     |IgTaperByRlRatio|  
     |IgRndmiteratCorner|  
     |IgRndRollAroundCorner|  
     |IgRndPreserveTopologyon|  
     |IgRndPreserveTopologyOff|  
     |IgStepDraftPerpendicular|  
     |IgExtendBendRelief|  
     |IgEqualOffset|  
     |IgUnequalOffset|  
     |IgThickness|  
     |IgFacesTouchingCurvesOnly|  
     |IgCurvesetSeperator|  
     |IgSideInfosetSeperator|  
     |IgRegularThread|  
     |IgStraightPipethread|  
     |IgTaperedPipethread|  
     |IgRemoveInternalBoundaries|  
     |IgRemoveExternalBoundaries|  
     |IgDeleteFaceheal|  
     |IgEndcaps|  
     |IgCurvatureContinuous|  
     |IgNonsymmetric|  
     |IgTreatmentDraft|  
     |IgTreatmentCrown|  
     |IgCloseCornerNone|  
     |IgCloseCornerOpen|  
     |IgCloseCornerClosed|  
     |IgCloseCornerCircleCutout|  
     |IgPatternAlongCurve|  
     |IgPatternMountingBoss|  
     |IgSmClearanceCutout|  
     |IgSmMidplaceCutout|  
     |IgCentermark|  
     |IgHoleAndCentermark|  

    """
    IgNullConstant: int
    IgLeft: int
    IgRight: int
    IgSymmetric: int
    IgInside: int
    IgOutside: int
    IgBoth: int
    IgNormalSidedummy: int
    IgReverseNormalSidedummy: int
    IgExtend: int
    IgNoextend: int
    IgThkinprofileplane: int
    IgThkNormalToProfilePlane: int
    IgFinite: int
    IgTonext: int
    IgFromTo: int
    IgThroughAll: int
    IgThreeHundredAndSixty: int
    IgParallelDummy: int
    IgAngularDummy: int
    IgNormal: int
    IgThroughAxis: int
    IgSingleEdge: int
    IgMultipleEdges: int
    IgEdgesByLoop: int
    IgEdgesByVertex: int
    IgAll: int
    IgConcave: int
    IgConvex: int
    IgStart: int
    IgEnd: int
    IgLinear: int
    IgRadial: int
    IgRegularHole: int
    IgCounterBoreHole: int
    IgCounterSinkHole: int
    IgCounterDrillHole: int
    IgTappedHole: int
    IgTaperedHole: int
    IgConstRadiusRound: int
    IgVarRadiusRound: int
    IgChamfer45degSetback: int
    IgChamferAngleSetback: int
    IgChamfer2Serbacks: int
    IgNone: int
    IgTaperByAngle: int
    IgTaperByRatio: int
    IgClosed: int
    IgProfileBasedCrosssection: int
    IgEdgeBasedCrosssection: int
    IgTangent: int
    IgRectangularBendRelief: int
    IgFilletBendRelief: int
    IgRipBendRelief: int
    IgBendOnlyCornerRelief: int
    IgBendAndFaceCornerRelief: int
    IgRipCornerRelief: int
    IgNftype: int
    IgEquationType: int
    IgPatternMirror: int
    IgPatternRectangular: int
    IgPatternCircular: int
    IgPatternUserDefined: int
    IgFromReferenceEnd: int
    IgFromNonreferenceEnd: int
    IgRndRollAcrossTnagentEdgesOn: int
    IgRndRollAcrossTangentEdgesOff: int
    IgRndCapAcrossSharpEdges: int
    IgRndRollAcrossSharpEdges: int
    IgRndRollAlongBlendEdgesOn: int
    IgRndRollAlongBlendEdgesOff: int
    IgToKepPoint: int
    IgFlatten: int
    IgAsConstruction: int
    IgOffset: int
    IgMitreParalletToThickness: int
    IgMitreNormalToThickness: int
    IgMitreByDist: int
    IgMitreByAngle: int
    IgMiterRegularCut: int
    IgMitreManufacturingCut: int
    IgProjectOptionProject: int
    IgProjectOptionWrap: int
    IgLip: int
    IgGroove: int
    IgPartingFromPlane: int
    IgPartingFromSurface: int
    IgPartingFromEdge: int
    IgPartingFromCurve: int
    IgSplitDraft: int
    IgSplitAngle1Right: int
    IgSplitAngle1Left: int
    IgLouverformedendtype: int
    IgLouverlancedendtype: int
    IgLouverround: int
    IgLouverroundnone: int
    IgInsideDimension: int
    IgOutsideDimension: int
    IgFull: int
    IgBend: int
    IgAddRound: int
    IgNoRound: int
    IgCloseFaces: int
    IgOverlapFaces: int
    IgTreatmentOff: int
    IgTreatmentIntersect: int
    IgTreatmentCircleCutout: int
    IgStepDreat: int
    IgShowBoundaries: int
    IgRemoveBoundaries: int
    IgCornerRound: int
    IgNoCornerRound: int
    IgNatural: int
    IgPeriodic: int
    IgRoundAllVertexSetback: int
    IgRoundSingleVertexSetback: int
    IgRoundVertexEdgeSetback: int
    IgRoundSetbackIsAbsolute: int
    IgRoundSetbackIsRelative: int
    IgCircular: int
    IgUshaped: int
    IgVshaped: int
    IgPunchedEnd: int
    IgLancedEnd: int
    IgFormedEnd: int
    IgSweepAlignParallel: int
    IgSweepAlignNormal: int
    IgRoundStartVertexEdgeSetback: int
    IgRoundEndVertexEdgeSetback: int
    IgSubtract: int
    IgUnite: int
    IgIntersect: int
    IgContinuous: int
    IgFlangeFulledge: int
    IgFlangeCenterOfEdge: int
    IgFlangeStartOnEndEdge: int
    IgFlangeEndOnEndEdge: int
    IgFlangeStartFromEndEdge: int
    IgFlangeEndFromEndEdge: int
    IgFlangeFromBothEndsOfEdge: int
    IgFlangeOffset: int
    IgChainedCornerRelief: int
    IgTangentInterior: int
    IgParallelToPlane: int
    IgVbottomDimToFlat: int
    IgVbottomDimToV: int
    IgTaperDimAtTop: int
    IgTaperDimAtBottom: int
    IgCounterBoreProfileIsAtTop: int
    IgCounterBoreProfileIsAtBottom: int
    IgTaperByRlRatio: int
    IgRndmiteratCorner: int
    IgRndRollAroundCorner: int
    IgRndPreserveTopologyon: int
    IgRndPreserveTopologyOff: int
    IgStepDraftPerpendicular: int
    IgExtendBendRelief: int
    IgEqualOffset: int
    IgUnequalOffset: int
    IgThickness: int
    IgFacesTouchingCurvesOnly: int
    IgCurvesetSeperator: int
    IgSideInfosetSeperator: int
    IgRegularThread: int
    IgStraightPipethread: int
    IgTaperedPipethread: int
    IgRemoveInternalBoundaries: int
    IgRemoveExternalBoundaries: int
    IgDeleteFaceheal: int
    IgEndcaps: int
    IgCurvatureContinuous: int
    IgNonsymmetric: int
    IgTreatmentDraft: int
    IgTreatmentCrown: int
    IgCloseCornerNone: int
    IgCloseCornerOpen: int
    IgCloseCornerClosed: int
    IgCloseCornerCircleCutout: int
    IgPatternAlongCurve: int
    IgPatternMountingBoss: int
    IgSmClearanceCutout: int
    IgSmMidplaceCutout: int
    IgCentermark: int
    IgHoleAndCentermark: int
    @staticmethod
    def ValueOf(value: int) -> FeatureProperty:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class FlangeBendPropertiesBuilder(FeatureBendPropertiesBuilder): 
    """ Represents a Sheetmetal Flange Bend Properties builder class. This builder is used to
        interrogate the flange bend properties in the list."""
    class Insets(Enum):
        """
        Members Include: 
         |MaterialInside| 
         |MaterialOutside| 
         |BendOutside| 
         |MaterialInsideOML| 

        """
        MaterialInside: int
        MaterialOutside: int
        BendOutside: int
        MaterialInsideOML: int
        @staticmethod
        def ValueOf(value: int) -> FlangeBendPropertiesBuilder.Insets:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LengthReferences(Enum):
        """
        Members Include: 
         |Inside| 
         |Outside| 
         |Web| 
         |Tangent| 

        """
        Inside: int
        Outside: int
        Web: int
        Tangent: int
        @staticmethod
        def ValueOf(value: int) -> FlangeBendPropertiesBuilder.LengthReferences:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class WidthOptions(Enum):
        """
        Members Include: 
         |Full| 
         |AtCenter| 
         |AtEnd| 
         |FromEnd| 
         |FromBothEnds| 

        """
        Full: int
        AtCenter: int
        AtEnd: int
        FromEnd: int
        FromBothEnds: int
        @staticmethod
        def ValueOf(value: int) -> FlangeBendPropertiesBuilder.WidthOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Angle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Angle
         Returns the angle   
            
         
        """
        pass
    @property
    def Distance1(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Distance1
         Returns the distance1   
            
         
        """
        pass
    @property
    def Distance2(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Distance2
         Returns the distance2   
            
         
        """
        pass
    @property
    def Edges(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) Edges
         Returns the base edge for the flange.  
            
         
        """
        pass
    @property
    def Inset(self) -> FlangeBendPropertiesBuilder.Insets:
        """
        Getter for property: ( FlangeBendPropertiesBuilder.Insets NXOpen.Featu) Inset
         Returns the inset   
            
         
        """
        pass
    @Inset.setter
    def Inset(self, inset: FlangeBendPropertiesBuilder.Insets):
        """
        Setter for property: ( FlangeBendPropertiesBuilder.Insets NXOpen.Featu) Inset
         Returns the inset   
            
         
        """
        pass
    @property
    def Length(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Length
         Returns the length   
            
         
        """
        pass
    @property
    def LengthReference(self) -> FlangeBendPropertiesBuilder.LengthReferences:
        """
        Getter for property: ( FlangeBendPropertiesBuilder.LengthReferences NXOpen.Featu) LengthReference
         Returns the length reference   
            
         
        """
        pass
    @LengthReference.setter
    def LengthReference(self, lengthReference: FlangeBendPropertiesBuilder.LengthReferences):
        """
        Setter for property: ( FlangeBendPropertiesBuilder.LengthReferences NXOpen.Featu) LengthReference
         Returns the length reference   
            
         
        """
        pass
    @property
    def Miter(self) -> bool:
        """
        Getter for property: (bool) Miter
         Returns the  option to specify behaviour of mirrorpattern of the flange  
            
         
        """
        pass
    @Miter.setter
    def Miter(self, bMiter: bool):
        """
        Setter for property: (bool) Miter
         Returns the  option to specify behaviour of mirrorpattern of the flange  
            
         
        """
        pass
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Offset
         Returns the offset   
            
         
        """
        pass
    @property
    def Point(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Point
         Returns the point   
            
         
        """
        pass
    @Point.setter
    def Point(self, point: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Point
         Returns the point   
            
         
        """
        pass
    @property
    def ReverseDirectionLength(self) -> bool:
        """
        Getter for property: (bool) ReverseDirectionLength
         Returns the reverse direction   
            
         
        """
        pass
    @ReverseDirectionLength.setter
    def ReverseDirectionLength(self, reverseDirectionLength: bool):
        """
        Setter for property: (bool) ReverseDirectionLength
         Returns the reverse direction   
            
         
        """
        pass
    @property
    def ReverseDirectionOffset(self) -> bool:
        """
        Getter for property: (bool) ReverseDirectionOffset
         Returns the reverse direction   
            
         
        """
        pass
    @ReverseDirectionOffset.setter
    def ReverseDirectionOffset(self, reverseDirectionOffset: bool):
        """
        Setter for property: (bool) ReverseDirectionOffset
         Returns the reverse direction   
            
         
        """
        pass
    @property
    def UseRecipe(self) -> bool:
        """
        Getter for property: (bool) UseRecipe
         Returns the  option to specify behaviour of mirrorpattern of the flange  
            
         
        """
        pass
    @UseRecipe.setter
    def UseRecipe(self, bUseRecipe: bool):
        """
        Setter for property: (bool) UseRecipe
         Returns the  option to specify behaviour of mirrorpattern of the flange  
            
         
        """
        pass
    @property
    def Width(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Width
         Returns the width   
            
         
        """
        pass
    @property
    def WidthOption(self) -> FlangeBendPropertiesBuilder.WidthOptions:
        """
        Getter for property: ( FlangeBendPropertiesBuilder.WidthOptions NXOpen.Featu) WidthOption
         Returns the width option   
            
         
        """
        pass
    @WidthOption.setter
    def WidthOption(self, widthOption: FlangeBendPropertiesBuilder.WidthOptions):
        """
        Setter for property: ( FlangeBendPropertiesBuilder.WidthOptions NXOpen.Featu) WidthOption
         Returns the width option   
            
         
        """
        pass
    def DeleteFlangeBendProperties(self) -> None:
        """
         Create a flange properties. 
        """
        pass
class FlangeBendPropertiesListBuilder(FeatureBendPropertiesListBuilder): 
    """ Represents a Sheetmetal Feature properties List builder class. This builder is used to
        interrogate the feature properties list."""
    def CreateFlangeBendProperties(self) -> FlangeBendPropertiesBuilder:
        """
         Create a flange properties. 
         Returns listitem ( FlangeBendPropertiesBuilder NXOpen.Featu): .
        """
        pass
import NXOpen
class FlangeBuilder(SheetmetalBaseBuilder): 
    """ Represents a Flange feature builder. """
    class InsetTypeOptions(Enum):
        """
        Members Include: 
         |MaterialInside|  The flange is flush with the thickness face on the inside 
         |MaterialOutside|  The flange is flush with the thickness face on the outside 
         |BendOutside|  The bend and flange are outside the thickness face 

        """
        MaterialInside: int
        MaterialOutside: int
        BendOutside: int
        @staticmethod
        def ValueOf(value: int) -> FlangeBuilder.InsetTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LengthTypeOptions(Enum):
        """
        Members Include: 
         |InsideDimension|  The flange length is dimensioned to the Inner Mold line. 
         |OutsideDimension|  The flange length is dimensioned to the Outer Mold Line. 
         |WebDimension|  The flange length is dimensioned to the Bend Tangent Line. 

        """
        InsideDimension: int
        OutsideDimension: int
        WebDimension: int
        @staticmethod
        def ValueOf(value: int) -> FlangeBuilder.LengthTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MatchFaceOptions(Enum):
        """
        Members Include: 
         |NotSet|  The flange is placed on the selected edge 
         |UntilSelected|  The flange face is extended until the selected plane 

        """
        NotSet: int
        UntilSelected: int
        @staticmethod
        def ValueOf(value: int) -> FlangeBuilder.MatchFaceOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OffsetTypeOptions(Enum):
        """
        Members Include: 
         |Inside|  The flange is offset to the inside of the face 
         |Outside|  The flange is offset to the outside of the face 

        """
        Inside: int
        Outside: int
        @staticmethod
        def ValueOf(value: int) -> FlangeBuilder.OffsetTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class WidthTypeOptions(Enum):
        """
        Members Include: 
         |FullEdge|  The flange spans the entire edge. 
         |CenterOfEdge|  The flange is centered on the edge. 
         |AtEdgeEnd|  The flange starts from the specified end of the edge. 
         |FromEdgeEnd|  The flange starts at a specified distance from an end of the edge. 
         |FromBothEnds|  The flange starts and ends at specified distances from the ends of the edge. 
         |Custom|  The flange sketch has been edited after creation and may or may not conform to any of the above. 

        """
        FullEdge: int
        CenterOfEdge: int
        AtEdgeEnd: int
        FromEdgeEnd: int
        FromBothEnds: int
        Custom: int
        @staticmethod
        def ValueOf(value: int) -> FlangeBuilder.WidthTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BendAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BendAngle
         Returns the bend angle for flange.  
           It should be set in degrees (??????).   
         
        """
        pass
    @property
    def BendOptions(self) -> BendOptions:
        """
        Getter for property: ( BendOptions NXOpen.Featu) BendOptions
         Returns the bend options object.  
           
                      
                    The bend options object stores additional parameters for the bend, such as bend radius, bend 
                    relief width and depth, corner relief type etc.
                      
                  
         
        """
        pass
    @property
    def Edge(self) -> NXOpen.Edge:
        """
        Getter for property: ( NXOpen.Edge) Edge
         Returns the edge on which the flange is created.  
          
                      
                        The edge should be linear and it should not be a thickness edge.
                      
                  
         
        """
        pass
    @Edge.setter
    def Edge(self, edge: NXOpen.Edge):
        """
        Setter for property: ( NXOpen.Edge) Edge
         Returns the edge on which the flange is created.  
          
                      
                        The edge should be linear and it should not be a thickness edge.
                      
                  
         
        """
        pass
    @property
    def FirstDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FirstDistance
         Returns a distance based on  NXOpen::Features::SheetMetal::FlangeBuilder::WidthType .  
          
                      
                        See  NXOpen::Features::SheetMetal::FlangeBuilder::WidthType  for a detailed desctiption of what this distance stands for.
                      
                  
         
        """
        pass
    @property
    def InsetType(self) -> FlangeBuilder.InsetTypeOptions:
        """
        Getter for property: ( FlangeBuilder.InsetTypeOptions NXOpen.Featu) InsetType
         Returns the inset type (inside, outside, bendoutside) for the flange.  
          
                  
         
        """
        pass
    @InsetType.setter
    def InsetType(self, inset_type: FlangeBuilder.InsetTypeOptions):
        """
        Setter for property: ( FlangeBuilder.InsetTypeOptions NXOpen.Featu) InsetType
         Returns the inset type (inside, outside, bendoutside) for the flange.  
          
                  
         
        """
        pass
    @property
    def Length(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Length
         Returns the length of the flange.  
          
                  
         
        """
        pass
    @property
    def LengthType(self) -> FlangeBuilder.LengthTypeOptions:
        """
        Getter for property: ( FlangeBuilder.LengthTypeOptions NXOpen.Featu) LengthType
         Returns a enum indicating the length type.  
                  
                For Features created in NX8 and above:
                The way length is measured for the flange. It can either be measure from the inside edge or the outside edge.
                      
                        Flange length can be specified starting from the selected edge or from the corresponding edge on the other face 
                        (other linear edge on the other side of the thickness face). If the length is specified from the
                        selected edge use value  NXOpen::Features::SheetMetal::FlangeBuilder::LengthTypeOptionsInsideDimension  or
                        if the flange length is specifed from the other edge use value  NXOpen::Features::SheetMetal::FlangeBuilder::LengthTypeOptionsOutsideDimension .
                      
                
                For Features created in NX8 and above:        
                Flange length can be measure from the Inner Mold Line, Outer Mold Line or Bend Tangent Line.
                      
                        Inner Mold Line: Intersection of inner tab face and inner flange web face
                        Outer Mold Line: Intersection of outer tab face and outer flange web face
                        Bend  Tangent Line: common edge between flange web face and bend face.
                        
                        Flange length can be specified starting from the inner mold line or outer mold line or bend tangent line. If the length is specified from the
                        inner mold line use value  NXOpen::Features::SheetMetal::FlangeBuilder::LengthTypeOptionsInsideDimension  or
                        if the flange length is specifed from the outer mold line use value  NXOpen::Features::SheetMetal::FlangeBuilder::LengthTypeOptionsOutsideDimension or
                        if the flange length is specifed from the bend tangent line use value  NXOpen::Features::SheetMetal::FlangeBuilder::LengthTypeOptionsWebDimension .
                      
                  
         
        """
        pass
    @LengthType.setter
    def LengthType(self, length_type: FlangeBuilder.LengthTypeOptions):
        """
        Setter for property: ( FlangeBuilder.LengthTypeOptions NXOpen.Featu) LengthType
         Returns a enum indicating the length type.  
                  
                For Features created in NX8 and above:
                The way length is measured for the flange. It can either be measure from the inside edge or the outside edge.
                      
                        Flange length can be specified starting from the selected edge or from the corresponding edge on the other face 
                        (other linear edge on the other side of the thickness face). If the length is specified from the
                        selected edge use value  NXOpen::Features::SheetMetal::FlangeBuilder::LengthTypeOptionsInsideDimension  or
                        if the flange length is specifed from the other edge use value  NXOpen::Features::SheetMetal::FlangeBuilder::LengthTypeOptionsOutsideDimension .
                      
                
                For Features created in NX8 and above:        
                Flange length can be measure from the Inner Mold Line, Outer Mold Line or Bend Tangent Line.
                      
                        Inner Mold Line: Intersection of inner tab face and inner flange web face
                        Outer Mold Line: Intersection of outer tab face and outer flange web face
                        Bend  Tangent Line: common edge between flange web face and bend face.
                        
                        Flange length can be specified starting from the inner mold line or outer mold line or bend tangent line. If the length is specified from the
                        inner mold line use value  NXOpen::Features::SheetMetal::FlangeBuilder::LengthTypeOptionsInsideDimension  or
                        if the flange length is specifed from the outer mold line use value  NXOpen::Features::SheetMetal::FlangeBuilder::LengthTypeOptionsOutsideDimension or
                        if the flange length is specifed from the bend tangent line use value  NXOpen::Features::SheetMetal::FlangeBuilder::LengthTypeOptionsWebDimension .
                      
                  
         
        """
        pass
    @property
    def MatchFaceOption(self) -> FlangeBuilder.MatchFaceOptions:
        """
        Getter for property: ( FlangeBuilder.MatchFaceOptions NXOpen.Featu) MatchFaceOption
         Returns the match face selection type.  
          
                      
                        None for Regular Flange.
                        Until Selected for Match To Face type Flange .
                      
                  
         
        """
        pass
    @MatchFaceOption.setter
    def MatchFaceOption(self, matchFaceOption: FlangeBuilder.MatchFaceOptions):
        """
        Setter for property: ( FlangeBuilder.MatchFaceOptions NXOpen.Featu) MatchFaceOption
         Returns the match face selection type.  
          
                      
                        None for Regular Flange.
                        Until Selected for Match To Face type Flange .
                      
                  
         
        """
        pass
    @property
    def MatchPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) MatchPlane
         Returns the Match Plane.  
             
         
        """
        pass
    @MatchPlane.setter
    def MatchPlane(self, matchPlane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) MatchPlane
         Returns the Match Plane.  
             
         
        """
        pass
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Offset
         Returns the offset value for the flange.  
           
                   
         
        """
        pass
    @property
    def OffsetType(self) -> FlangeBuilder.OffsetTypeOptions:
        """
        Getter for property: ( FlangeBuilder.OffsetTypeOptions NXOpen.Featu) OffsetType
         Returns the offset type for the flange.  
            
                  
         
        """
        pass
    @OffsetType.setter
    def OffsetType(self, offset_type: FlangeBuilder.OffsetTypeOptions):
        """
        Setter for property: ( FlangeBuilder.OffsetTypeOptions NXOpen.Featu) OffsetType
         Returns the offset type for the flange.  
            
                  
         
        """
        pass
    @property
    def SecondDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SecondDistance
         Returns a distance based on  NXOpen::Features::SheetMetal::FlangeBuilder::WidthType .  
          
                      
                        See  NXOpen::Features::SheetMetal::FlangeBuilder::WidthType  for a detailed desctiption of what this distance stands for.
                      
                  
         
        """
        pass
    @property
    def Vertex(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) Vertex
         Returns the vertex on the flange edge, needed to dimension the flange width.  
          
                      
                        The vertex needs to be specified ONLY if  NXOpen::Features::SheetMetal::FlangeBuilder::WidthType  is
                        set to one of  NXOpen::Features::SheetMetal::FlangeBuilder::WidthTypeOptionsAtEdgeEnd ,  
                         NXOpen::Features::SheetMetal::FlangeBuilder::WidthTypeOptionsFromEdgeEnd . In case of 
                         NXOpen::Features::SheetMetal::FlangeBuilder::WidthTypeOptionsFromBothEnds , the start vertex of the edge
                        is assumed to be the start point for  NXOpen::Features::SheetMetal::FlangeBuilder::FirstDistance .
                      
                  
         
        """
        pass
    @Vertex.setter
    def Vertex(self, vertex: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) Vertex
         Returns the vertex on the flange edge, needed to dimension the flange width.  
          
                      
                        The vertex needs to be specified ONLY if  NXOpen::Features::SheetMetal::FlangeBuilder::WidthType  is
                        set to one of  NXOpen::Features::SheetMetal::FlangeBuilder::WidthTypeOptionsAtEdgeEnd ,  
                         NXOpen::Features::SheetMetal::FlangeBuilder::WidthTypeOptionsFromEdgeEnd . In case of 
                         NXOpen::Features::SheetMetal::FlangeBuilder::WidthTypeOptionsFromBothEnds , the start vertex of the edge
                        is assumed to be the start point for  NXOpen::Features::SheetMetal::FlangeBuilder::FirstDistance .
                      
                  
         
        """
        pass
    @property
    def WidthType(self) -> FlangeBuilder.WidthTypeOptions:
        """
        Getter for property: ( FlangeBuilder.WidthTypeOptions NXOpen.Featu) WidthType
         Returns the width type for flange.  
          
                      
                        Use one of the values from  NXOpen::Features::SheetMetal::FlangeBuilder::WidthTypeOptions . Depending on which of the 
                        values from the enum is used, none, either or both of the distance values from 
                         NXOpen::Features::SheetMetal::FlangeBuilder::FirstDistance   and 
                         NXOpen::Features::SheetMetal::FlangeBuilder::SecondDistance 
                        may be used. Here is a description of the distances:
                        
                        If the value is  NXOpen::Features::SheetMetal::FlangeBuilder::WidthTypeOptionsFullEdge , 
                        then both the  FirstDistance 
                        and  NXOpen::Features::SheetMetal::FlangeBuilder::SecondDistance  values are unused.
                        
                        If the value is  NXOpen::Features::SheetMetal::FlangeBuilder::WidthTypeOptionsCenterOfEdge , 
                        then both the  NXOpen::Features::SheetMetal::FlangeBuilder::FirstDistance 
                        and  NXOpen::Features::SheetMetal::FlangeBuilder::SecondDistance  represent exactly half the width of the flange.
                        If the value is  NXOpen::Features::SheetMetal::FlangeBuilder::WidthTypeOptionsAtEdgeEnd ,
                         then  NXOpen::Features::SheetMetal::FlangeBuilder::FirstDistance 
                        represents the width of the flange, starting from the end of the edge specified by the 
                         NXOpen::Features::SheetMetal::FlangeBuilder::Vertex  and 
                        the  NXOpen::Features::SheetMetal::FlangeBuilder::SecondDistance  is not used.
                       
                        If the value is  NXOpen::Features::SheetMetal::FlangeBuilder::WidthTypeOptionsFromEdgeEnd ,
                         then  NXOpen::Features::SheetMetal::FlangeBuilder::FirstDistance 
                        represents the distance of the start point of the flange from the end of the edge specified by 
                         NXOpen::Features::SheetMetal::FlangeBuilder::Vertex  
                        and  NXOpen::Features::SheetMetal::FlangeBuilder::SecondDistance  represents the width of the flange.
                       
                        If the value is  NXOpen::Features::SheetMetal::FlangeBuilder::WidthTypeOptionsFromBothEnds , 
                        then  NXOpen::Features::SheetMetal::FlangeBuilder::FirstDistance 
                        represents the distance of the start point of the flange from the from the end of the edge specified by
                          NXOpen::Features::SheetMetal::FlangeBuilder::Vertex   
                        and  NXOpen::Features::SheetMetal::FlangeBuilder::SecondDistance 
                         represents the distance of the end point of the flange from end of the edge opposite to the end 
                        specified by  NXOpen::Features::SheetMetal::FlangeBuilder::Vertex .
                        
                        The value  NXOpen::Features::SheetMetal::FlangeBuilder::WidthTypeOptionsCustom , cannot be set by the user. It is set internally if the
                        sketch for the flange has been edited after creation. In this case, the expressions
                          NXOpen::Features::SheetMetal::FlangeBuilder::FirstDistance 
                        and  NXOpen::Features::SheetMetal::FlangeBuilder::SecondDistance 
                         may or may not retain their original meaning when the flange was first created, 
                        so the user should not rely on these any more to mean anything specific.
                        
                      
                  
         
        """
        pass
    @WidthType.setter
    def WidthType(self, width_option: FlangeBuilder.WidthTypeOptions):
        """
        Setter for property: ( FlangeBuilder.WidthTypeOptions NXOpen.Featu) WidthType
         Returns the width type for flange.  
          
                      
                        Use one of the values from  NXOpen::Features::SheetMetal::FlangeBuilder::WidthTypeOptions . Depending on which of the 
                        values from the enum is used, none, either or both of the distance values from 
                         NXOpen::Features::SheetMetal::FlangeBuilder::FirstDistance   and 
                         NXOpen::Features::SheetMetal::FlangeBuilder::SecondDistance 
                        may be used. Here is a description of the distances:
                        
                        If the value is  NXOpen::Features::SheetMetal::FlangeBuilder::WidthTypeOptionsFullEdge , 
                        then both the  FirstDistance 
                        and  NXOpen::Features::SheetMetal::FlangeBuilder::SecondDistance  values are unused.
                        
                        If the value is  NXOpen::Features::SheetMetal::FlangeBuilder::WidthTypeOptionsCenterOfEdge , 
                        then both the  NXOpen::Features::SheetMetal::FlangeBuilder::FirstDistance 
                        and  NXOpen::Features::SheetMetal::FlangeBuilder::SecondDistance  represent exactly half the width of the flange.
                        If the value is  NXOpen::Features::SheetMetal::FlangeBuilder::WidthTypeOptionsAtEdgeEnd ,
                         then  NXOpen::Features::SheetMetal::FlangeBuilder::FirstDistance 
                        represents the width of the flange, starting from the end of the edge specified by the 
                         NXOpen::Features::SheetMetal::FlangeBuilder::Vertex  and 
                        the  NXOpen::Features::SheetMetal::FlangeBuilder::SecondDistance  is not used.
                       
                        If the value is  NXOpen::Features::SheetMetal::FlangeBuilder::WidthTypeOptionsFromEdgeEnd ,
                         then  NXOpen::Features::SheetMetal::FlangeBuilder::FirstDistance 
                        represents the distance of the start point of the flange from the end of the edge specified by 
                         NXOpen::Features::SheetMetal::FlangeBuilder::Vertex  
                        and  NXOpen::Features::SheetMetal::FlangeBuilder::SecondDistance  represents the width of the flange.
                       
                        If the value is  NXOpen::Features::SheetMetal::FlangeBuilder::WidthTypeOptionsFromBothEnds , 
                        then  NXOpen::Features::SheetMetal::FlangeBuilder::FirstDistance 
                        represents the distance of the start point of the flange from the from the end of the edge specified by
                          NXOpen::Features::SheetMetal::FlangeBuilder::Vertex   
                        and  NXOpen::Features::SheetMetal::FlangeBuilder::SecondDistance 
                         represents the distance of the end point of the flange from end of the edge opposite to the end 
                        specified by  NXOpen::Features::SheetMetal::FlangeBuilder::Vertex .
                        
                        The value  NXOpen::Features::SheetMetal::FlangeBuilder::WidthTypeOptionsCustom , cannot be set by the user. It is set internally if the
                        sketch for the flange has been edited after creation. In this case, the expressions
                          NXOpen::Features::SheetMetal::FlangeBuilder::FirstDistance 
                        and  NXOpen::Features::SheetMetal::FlangeBuilder::SecondDistance 
                         may or may not retain their original meaning when the flange was first created, 
                        so the user should not rely on these any more to mean anything specific.
                        
                      
                  
         
        """
        pass
    def DeleteSketch(self) -> None:
        """
         Delete the flange sketch 
        """
        pass
    def EditSketch(self) -> None:
        """
         Edit the sketch base on a new edge you need to call SetEdge to set a new edge
        """
        pass
    def GetSketch(self) -> NXOpen.Sketch:
        """
         Get the flange sketch  
         Returns sketch ( NXOpen.Sketch): .
        """
        pass
    def ValidateBuilderData(self) -> int:
        """
         Verify that the builder data is valid for creating a flange.
                    
                         If the builder data is valid, return value is zero.
                    
                
         Returns builder_data_validity (int):  A value of zero is returned if the data in the builder is valid. .
        """
        pass
import NXOpen
class FlatPatternBuilder(SheetmetalBaseBuilder): 
    """ Represents a Flat Pattern feature builder. """
    @property
    def AddedGeometry(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) AddedGeometry
         Returns the added geometry selection   
            
         
        """
        pass
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
         Returns the setting which decides whether the flattened solid will be associative to parent body.  
          
                      This is applicable to flat pattern features created in NX12 and later release.
                      Cannot change during feature edit if the feature was created as non associative.
                      
         
        """
        pass
    @Associative.setter
    def Associative(self, isAssociative: bool):
        """
        Setter for property: (bool) Associative
         Returns the setting which decides whether the flattened solid will be associative to parent body.  
          
                      This is applicable to flat pattern features created in NX12 and later release.
                      Cannot change during feature edit if the feature was created as non associative.
                      
         
        """
        pass
    @property
    def BendDirectionDownText(self) -> str:
        """
        Getter for property: (str) BendDirectionDownText
         Returns the bend direction down texts in flat pattern PMIs
                     This is applicable during creation of flat pattern feature.  
          
                      
         
        """
        pass
    @BendDirectionDownText.setter
    def BendDirectionDownText(self, bendDirectionDown: str):
        """
        Setter for property: (str) BendDirectionDownText
         Returns the bend direction down texts in flat pattern PMIs
                     This is applicable during creation of flat pattern feature.  
          
                      
         
        """
        pass
    @property
    def BendDirectionUpText(self) -> str:
        """
        Getter for property: (str) BendDirectionUpText
         Returns the bend direction up texts in flat pattern PMIs
                     This is applicable during creation of flat pattern feature.  
          
                      
         
        """
        pass
    @BendDirectionUpText.setter
    def BendDirectionUpText(self, bendDirectionUp: str):
        """
        Setter for property: (str) BendDirectionUpText
         Returns the bend direction up texts in flat pattern PMIs
                     This is applicable during creation of flat pattern feature.  
          
                      
         
        """
        pass
    @property
    def FixAtTimestamp(self) -> bool:
        """
        Getter for property: (bool) FixAtTimestamp
         Returns the setting which decides whether the flattened solid will be fixed at timestamp.  
          
                      This is applicable to flat pattern features created in NX12 and later release.
                      Cannot change during feature edit if the feature was created as fixed at timestamp.
                      
         
        """
        pass
    @FixAtTimestamp.setter
    def FixAtTimestamp(self, isFixedAtTimestamp: bool):
        """
        Setter for property: (bool) FixAtTimestamp
         Returns the setting which decides whether the flattened solid will be fixed at timestamp.  
          
                      This is applicable to flat pattern features created in NX12 and later release.
                      Cannot change during feature edit if the feature was created as fixed at timestamp.
                      
         
        """
        pass
    @property
    def FlatPatternViewName(self) -> str:
        """
        Getter for property: (str) FlatPatternViewName
         Returns the flat pattern view name string   
            
         
        """
        pass
    @property
    def HoleTreatment(self) -> HoleTreatmentBuilder:
        """
        Getter for property: ( HoleTreatmentBuilder NXOpen.Featu) HoleTreatment
         Returns the hole treatment object
                      This is applicable to flat pattern features created in NX12 and later release.  
          
                      
         
        """
        pass
    @property
    def InnerCornerTreatment(self) -> CornerTreatmentBuilder:
        """
        Getter for property: ( CornerTreatmentBuilder NXOpen.Featu) InnerCornerTreatment
         Returns the inner corner treatment corner object   
            
         
        """
        pass
    @property
    def KeepFlatSolidExternal(self) -> bool:
        """
        Getter for property: (bool) KeepFlatSolidExternal
         Returns the value indicating whether or not to keep the flat solid external while creating the flat pattern.  
          
                        This is applicable only during flat pattern creation and not during edit mode.
                      
         
        """
        pass
    @KeepFlatSolidExternal.setter
    def KeepFlatSolidExternal(self, isKeepExternal: bool):
        """
        Setter for property: (bool) KeepFlatSolidExternal
         Returns the value indicating whether or not to keep the flat solid external while creating the flat pattern.  
          
                        This is applicable only during flat pattern creation and not during edit mode.
                      
         
        """
        pass
    @property
    def Orientation(self) -> FlatSolidBuilder.OrientationType:
        """
        Getter for property: ( FlatSolidBuilder.OrientationType NXOpen.Featu) Orientation
         Returns the option which decides if the flattened solid will be transformed to Absolute CSYS.  
          
                      This flag will only be used if the Upward face belongs to a formed sheet metal body.
                      If a face from a flat solid is selected, this value will be ignored.
                      This is applicable to flat solid  flat pattern features created (or renewed) to NX12 and later release.
                      
         
        """
        pass
    @Orientation.setter
    def Orientation(self, orientation: FlatSolidBuilder.OrientationType):
        """
        Setter for property: ( FlatSolidBuilder.OrientationType NXOpen.Featu) Orientation
         Returns the option which decides if the flattened solid will be transformed to Absolute CSYS.  
          
                      This flag will only be used if the Upward face belongs to a formed sheet metal body.
                      If a face from a flat solid is selected, this value will be ignored.
                      This is applicable to flat solid  flat pattern features created (or renewed) to NX12 and later release.
                      
         
        """
        pass
    @property
    def OrientationCsys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) OrientationCsys
         Returns the orientation csys 
                      This is applicable to flat pattern features created (or renewed) in NX12 and later release.  
          
                      
         
        """
        pass
    @OrientationCsys.setter
    def OrientationCsys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) OrientationCsys
         Returns the orientation csys 
                      This is applicable to flat pattern features created (or renewed) in NX12 and later release.  
          
                      
         
        """
        pass
    @property
    def OuterCornerTreatment(self) -> CornerTreatmentBuilder:
        """
        Getter for property: ( CornerTreatmentBuilder NXOpen.Featu) OuterCornerTreatment
         Returns the outer corner treatment corner object   
            
         
        """
        pass
    @property
    def ReferenceVertex(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) ReferenceVertex
         Returns the end of the edge where the tangent will define the x axis for flat as solid.  
           This value will only
                      be used when a face from a formed solid body is picked as Upward face. If a face from a flat solid is selected,
                      this value will be ignored.
                      
         
        """
        pass
    @ReferenceVertex.setter
    def ReferenceVertex(self, vertex: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) ReferenceVertex
         Returns the end of the edge where the tangent will define the x axis for flat as solid.  
           This value will only
                      be used when a face from a formed solid body is picked as Upward face. If a face from a flat solid is selected,
                      this value will be ignored.
                      
         
        """
        pass
    @property
    def ShowInteriorFeatureCurves(self) -> bool:
        """
        Getter for property: (bool) ShowInteriorFeatureCurves
         Returns the show interior feature curves toggle value   
            
         
        """
        pass
    @ShowInteriorFeatureCurves.setter
    def ShowInteriorFeatureCurves(self, showInteriorFeatureCurves: bool):
        """
        Setter for property: (bool) ShowInteriorFeatureCurves
         Returns the show interior feature curves toggle value   
            
         
        """
        pass
    @property
    def TransformToAbsoluteCsys(self) -> bool:
        """
        Getter for property: (bool) TransformToAbsoluteCsys
         Returns the flag which decides if the flattened solid will be transformed to Absolute CSYS.  
           This flag will only be 
                      used if the Upward face belongs to a formed sheet metal body. If a face from a flat solid is selected,
                      this value will be ignored.
                      This is applicable to flat solid  flat pattern features created before NX12 release and not yet renewed.
                      The API can not be deprecated because it is required to edit features created before NX12 release.
                      But user should modify automation programs written before NX12 and replace use this option with the orientation option,
                      before using the program to create new features in NX12 or later.
                      
         
        """
        pass
    @TransformToAbsoluteCsys.setter
    def TransformToAbsoluteCsys(self, transform_flag: bool):
        """
        Setter for property: (bool) TransformToAbsoluteCsys
         Returns the flag which decides if the flattened solid will be transformed to Absolute CSYS.  
           This flag will only be 
                      used if the Upward face belongs to a formed sheet metal body. If a face from a flat solid is selected,
                      this value will be ignored.
                      This is applicable to flat solid  flat pattern features created before NX12 release and not yet renewed.
                      The API can not be deprecated because it is required to edit features created before NX12 release.
                      But user should modify automation programs written before NX12 and replace use this option with the orientation option,
                      before using the program to create new features in NX12 or later.
                      
         
        """
        pass
    @property
    def UpwardFace(self) -> NXOpen.SelectFace:
        """
        Getter for property: ( NXOpen.SelectFace) UpwardFace
         Returns the upward face selection   
            
         
        """
        pass
    @property
    def XAxisEdge(self) -> NXOpen.SelectEdge:
        """
        Getter for property: ( NXOpen.SelectEdge) XAxisEdge
         Returns the x axis edge selection.  
           This edge selection is necessary when a face from a formed 
                      solid body is picked as Upward face. If a face from a flat solid is selected,
                      this value will be ignored.   
         
        """
        pass
    def GenerateMoldLines(self) -> None:
        """
         Set the flag to generate inner and outer mold lines for flat pattern features created before NX11.
        """
        pass
import NXOpen
class FlatSolidBuilder(SheetmetalBaseBuilder): 
    """ Represents a Flat As Solid feature builder. """
    class LayerSettingOption(Enum):
        """
        Members Include: 
         |Default| 
         |Preference| 
         |Specify| 

        """
        Default: int
        Preference: int
        Specify: int
        @staticmethod
        def ValueOf(value: int) -> FlatSolidBuilder.LayerSettingOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OrientationType(Enum):
        """
        Members Include: 
         |Default|  do not orient flat solid body 
         |Edge|  transform flat solid body as per orientation defined by edge 
         |Csys|  transform flat solid body as per orientation defined by CSYS 

        """
        Default: int
        Edge: int
        Csys: int
        @staticmethod
        def ValueOf(value: int) -> FlatSolidBuilder.OrientationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TransformComponentsOption(Enum):
        """
        Members Include: 
         |NotSet|  do not transform components 
         |Body|  transform components as bodies 
         |Csys|  transform components as CSYS 

        """
        NotSet: int
        Body: int
        Csys: int
        @staticmethod
        def ValueOf(value: int) -> FlatSolidBuilder.TransformComponentsOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AddedGeometry(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) AddedGeometry
         Returns the added geometry selection   
            
         
        """
        pass
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
         Returns the setting which decides whether the flattened solid will be associative to parent body.  
          
                      This is applicable to flat solid features created in NX12 and later release.
                      Cannot change during feature edit if the feature was created as non associative.
                      
         
        """
        pass
    @Associative.setter
    def Associative(self, isAssociative: bool):
        """
        Setter for property: (bool) Associative
         Returns the setting which decides whether the flattened solid will be associative to parent body.  
          
                      This is applicable to flat solid features created in NX12 and later release.
                      Cannot change during feature edit if the feature was created as non associative.
                      
         
        """
        pass
    @property
    def AutoAssignComponentLayer(self) -> bool:
        """
        Getter for property: (bool) AutoAssignComponentLayer
         Returns the setting indicating whether to associate component layer.  
          
                    Only applies to the Flexible Printed Circuit Design application and will have no effect in Sheet Metal.   
         
        """
        pass
    @AutoAssignComponentLayer.setter
    def AutoAssignComponentLayer(self, autoAssignComponentLayer: bool):
        """
        Setter for property: (bool) AutoAssignComponentLayer
         Returns the setting indicating whether to associate component layer.  
          
                    Only applies to the Flexible Printed Circuit Design application and will have no effect in Sheet Metal.   
         
        """
        pass
    @property
    def AutoAssociateObjects(self) -> bool:
        """
        Getter for property: (bool) AutoAssociateObjects
         Returns the flag which decides whether copies of associated objects will remain associated
                        to faces of flat solid body during down stream unbend, rebend and bend operations.  
          
                      
         
        """
        pass
    @AutoAssociateObjects.setter
    def AutoAssociateObjects(self, isAutoAssociate: bool):
        """
        Setter for property: (bool) AutoAssociateObjects
         Returns the flag which decides whether copies of associated objects will remain associated
                        to faces of flat solid body during down stream unbend, rebend and bend operations.  
          
                      
         
        """
        pass
    @property
    def FixAtTimestamp(self) -> bool:
        """
        Getter for property: (bool) FixAtTimestamp
         Returns the setting decides whether the flattened solid will be fixed at timestamp.  
          
                      This is applicable to flat solid features created in NX12 and later release.
                      Cannot change during feature edit if the feature was created as fixed at timestamp.
                      
         
        """
        pass
    @FixAtTimestamp.setter
    def FixAtTimestamp(self, isFixedAtTimestamp: bool):
        """
        Setter for property: (bool) FixAtTimestamp
         Returns the setting decides whether the flattened solid will be fixed at timestamp.  
          
                      This is applicable to flat solid features created in NX12 and later release.
                      Cannot change during feature edit if the feature was created as fixed at timestamp.
                      
         
        """
        pass
    @property
    def FlatBodyColor(self) -> int:
        """
        Getter for property: (int) FlatBodyColor
         Returnsthe color of flat solid body.  
            
         
        """
        pass
    @FlatBodyColor.setter
    def FlatBodyColor(self, color: int):
        """
        Setter for property: (int) FlatBodyColor
         Returnsthe color of flat solid body.  
            
         
        """
        pass
    @property
    def FlatBodyLayer(self) -> int:
        """
        Getter for property: (int) FlatBodyLayer
         Returnsthe layer of flat solid body.  
            
         
        """
        pass
    @FlatBodyLayer.setter
    def FlatBodyLayer(self, layer: int):
        """
        Setter for property: (int) FlatBodyLayer
         Returnsthe layer of flat solid body.  
            
         
        """
        pass
    @property
    def InnerCornerTreatment(self) -> CornerTreatmentBuilder:
        """
        Getter for property: ( CornerTreatmentBuilder NXOpen.Featu) InnerCornerTreatment
         Returns the inner corner treatment corner object   
            
         
        """
        pass
    @property
    def LayerSetting(self) -> FlatSolidBuilder.LayerSettingOption:
        """
        Getter for property: ( FlatSolidBuilder.LayerSettingOption NXOpen.Featu) LayerSetting
         Returns the layer setting.  
            
         
        """
        pass
    @LayerSetting.setter
    def LayerSetting(self, layerSetting: FlatSolidBuilder.LayerSettingOption):
        """
        Setter for property: ( FlatSolidBuilder.LayerSettingOption NXOpen.Featu) LayerSetting
         Returns the layer setting.  
            
         
        """
        pass
    @property
    def Orientation(self) -> FlatSolidBuilder.OrientationType:
        """
        Getter for property: ( FlatSolidBuilder.OrientationType NXOpen.Featu) Orientation
         Returns the option which decides if the flattened solid will be transformed to Absolute CSYS.  
          
                    This is applicable to flat solid  flat pattern features created (or renewed) to NX12 and later release.
                      
         
        """
        pass
    @Orientation.setter
    def Orientation(self, orientation: FlatSolidBuilder.OrientationType):
        """
        Setter for property: ( FlatSolidBuilder.OrientationType NXOpen.Featu) Orientation
         Returns the option which decides if the flattened solid will be transformed to Absolute CSYS.  
          
                    This is applicable to flat solid  flat pattern features created (or renewed) to NX12 and later release.
                      
         
        """
        pass
    @property
    def OrientationCsys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) OrientationCsys
         Returns the orientation csys 
                      This is applicable to flat solid features created (or renewed) in NX12 and later release.  
          
                      
         
        """
        pass
    @OrientationCsys.setter
    def OrientationCsys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) OrientationCsys
         Returns the orientation csys 
                      This is applicable to flat solid features created (or renewed) in NX12 and later release.  
          
                      
         
        """
        pass
    @property
    def OuterCornerTreatment(self) -> CornerTreatmentBuilder:
        """
        Getter for property: ( CornerTreatmentBuilder NXOpen.Featu) OuterCornerTreatment
         Returns the outer corner treatment corner object   
            
         
        """
        pass
    @property
    def ReferenceVertex(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) ReferenceVertex
         Returns the end of the edge where the tangent will define the x axis for flat as solid.  
          
                      
         
        """
        pass
    @ReferenceVertex.setter
    def ReferenceVertex(self, vertex: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) ReferenceVertex
         Returns the end of the edge where the tangent will define the x axis for flat as solid.  
          
                      
         
        """
        pass
    @property
    def StationaryFace(self) -> NXOpen.SelectFace:
        """
        Getter for property: ( NXOpen.SelectFace) StationaryFace
         Returns the stationary face selection   
            
         
        """
        pass
    @property
    def TransformComponents(self) -> FlatSolidBuilder.TransformComponentsOption:
        """
        Getter for property: ( FlatSolidBuilder.TransformComponentsOption NXOpen.Featu) TransformComponents
         Returns the setting indicating how to represent transformed components in flat solid.  
          
                    Only applies to the Flexible Printed Circuit Design application and will have no effect in Sheet Metal.   
         
        """
        pass
    @TransformComponents.setter
    def TransformComponents(self, transformComponents: FlatSolidBuilder.TransformComponentsOption):
        """
        Setter for property: ( FlatSolidBuilder.TransformComponentsOption NXOpen.Featu) TransformComponents
         Returns the setting indicating how to represent transformed components in flat solid.  
          
                    Only applies to the Flexible Printed Circuit Design application and will have no effect in Sheet Metal.   
         
        """
        pass
    @property
    def TransformPinAndCCP(self) -> bool:
        """
        Getter for property: (bool) TransformPinAndCCP
         Returns the setting indicating whether to transform Pins and CCPs in flat solid.  
          
                    Only applies to the Flexible Printed Circuit Design application and will have no effect in Sheet Metal.   
         
        """
        pass
    @TransformPinAndCCP.setter
    def TransformPinAndCCP(self, transformPinAndCCP: bool):
        """
        Setter for property: (bool) TransformPinAndCCP
         Returns the setting indicating whether to transform Pins and CCPs in flat solid.  
          
                    Only applies to the Flexible Printed Circuit Design application and will have no effect in Sheet Metal.   
         
        """
        pass
    @property
    def TransformRestrictionAreas(self) -> bool:
        """
        Getter for property: (bool) TransformRestrictionAreas
         Returns the setting indicating whether to transform restriction areas in flat solid.  
          
                    Only applies to the Flexible Printed Circuit Design application and will have no effect in Sheet Metal.   
         
        """
        pass
    @TransformRestrictionAreas.setter
    def TransformRestrictionAreas(self, transformRestrictionAreas: bool):
        """
        Setter for property: (bool) TransformRestrictionAreas
         Returns the setting indicating whether to transform restriction areas in flat solid.  
          
                    Only applies to the Flexible Printed Circuit Design application and will have no effect in Sheet Metal.   
         
        """
        pass
    @property
    def TransformToAbsoluteCsys(self) -> bool:
        """
        Getter for property: (bool) TransformToAbsoluteCsys
         Returns the flag which decides if the flattened solid will be transformed to Absolute CSYS.  
          
                    This is applicable to flat solid  flat pattern features created before NX12 release and not yet renewed.
                    The API can not be deprecated because it is required to edit features created before NX12 release.
                    But user should modify automation programs written before NX12 and replace use this option with the orientation option,
                    before using the program to create new features in NX12 or later.
                      
         
        """
        pass
    @TransformToAbsoluteCsys.setter
    def TransformToAbsoluteCsys(self, transform_flag: bool):
        """
        Setter for property: (bool) TransformToAbsoluteCsys
         Returns the flag which decides if the flattened solid will be transformed to Absolute CSYS.  
          
                    This is applicable to flat solid  flat pattern features created before NX12 release and not yet renewed.
                    The API can not be deprecated because it is required to edit features created before NX12 release.
                    But user should modify automation programs written before NX12 and replace use this option with the orientation option,
                    before using the program to create new features in NX12 or later.
                      
         
        """
        pass
    @property
    def XAxisEdge(self) -> NXOpen.SelectEdge:
        """
        Getter for property: ( NXOpen.SelectEdge) XAxisEdge
         Returns the x axis edge selection   
            
         
        """
        pass
    def ValidateBuilderData(self) -> int:
        """
         Validate the builder data 
         Returns builder_data_validity (int):  0 Means no errors. .
        """
        pass
import NXOpen
import NXOpen.Features
class FlexibleCableBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Flexible Cable feature builder. """
    class BendAngleDirectionOptions(Enum):
        """
        Members Include: 
         |ReverseNormalDirection|  Bend angle reverse normal direction.
         |NormalDirection|  Bend angle normal direction. 

        """
        ReverseNormalDirection: int
        NormalDirection: int
        @staticmethod
        def ValueOf(value: int) -> FlexibleCableBuilder.BendAngleDirectionOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PathAdjustmentAngleDirectionOptions(Enum):
        """
        Members Include: 
         |LeftDirection|  Path adjustment angle left direction. 
         |RightDirection|  Path adjustment angle right direction. 

        """
        LeftDirection: int
        RightDirection: int
        @staticmethod
        def ValueOf(value: int) -> FlexibleCableBuilder.PathAdjustmentAngleDirectionOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SegmentTypeOptions(Enum):
        """
        Members Include: 
         |Planar|  Planar cable segment. 
         |Bend|  Bend cable segment. 

        """
        Planar: int
        Bend: int
        @staticmethod
        def ValueOf(value: int) -> FlexibleCableBuilder.SegmentTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CableDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) CableDirection
         Returns the cable direction.  
             
         
        """
        pass
    @CableDirection.setter
    def CableDirection(self, cableDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) CableDirection
         Returns the cable direction.  
             
         
        """
        pass
    @property
    def ConductorCount(self) -> int:
        """
        Getter for property: (int) ConductorCount
         Returns the count of conductors.  
             
         
        """
        pass
    @ConductorCount.setter
    def ConductorCount(self, noOfConductors: int):
        """
        Setter for property: (int) ConductorCount
         Returns the count of conductors.  
             
         
        """
        pass
    @property
    def ConductorSpacing(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ConductorSpacing
         Returns the conductor spacing.  
             
         
        """
        pass
    @property
    def ConductorWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ConductorWidth
         Returns the conductor width.  
             
         
        """
        pass
    @property
    def CrossSectionWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CrossSectionWidth
         Returns the cross section width.  
             
         
        """
        pass
    @property
    def SegmentList(self) -> NXOpen.TaggedObjectList:
        """
        Getter for property: ( NXOpen.TaggedObjectList) SegmentList
         Returns the cable segment list.  
             
         
        """
        pass
    @property
    def StartPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) StartPoint
         Returns the start point.  
             
         
        """
        pass
    @StartPoint.setter
    def StartPoint(self, startPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) StartPoint
         Returns the start point.  
             
         
        """
        pass
    @property
    def StrippingLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StrippingLength
         Returns the stripping length.  
             
         
        """
        pass
    @property
    def Thickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Thickness
         Returns the thickness.  
             
         
        """
        pass
    @property
    def ThicknessDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) ThicknessDirection
         Returns the thickness direction.  
             
         
        """
        pass
    @ThicknessDirection.setter
    def ThicknessDirection(self, thicknessDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) ThicknessDirection
         Returns the thickness direction.  
             
         
        """
        pass
    def CreateBendSegment(self, bendAngle: str, bendRadius: str, pathAdjustmentAngle: str, bendAngleDirection: FlexibleCableBuilder.BendAngleDirectionOptions, pathAdjustmentAngleDirection: FlexibleCableBuilder.PathAdjustmentAngleDirectionOptions, segmentIndex: int) -> FlexibleCableSegment:
        """
         Creates a new Features.SheetMetal.FlexibleCableSegment bend segment. This
                       can be either appended at the end, or inserted in between the list. This is decided by
                       the input index. 
         Returns bendSegment ( FlexibleCableSegment NXOpen.Featu): .
        """
        pass
    def CreatePlanarSegment(self, length: str, segmentIndex: int) -> FlexibleCableSegment:
        """
         Creates a new Features.SheetMetal.FlexibleCableSegment planar segment. This
                       can be either appended at the end, or inserted in between the list. This is decided by
                       the input index. 
         Returns planarSegment ( FlexibleCableSegment NXOpen.Featu): .
        """
        pass
    def DeleteAllSegments(self) -> None:
        """
         Deletes all cable segments. 
        """
        pass
    def DeleteSegment(self, index: int) -> None:
        """
         Deletes a cable segment at given index. 
        """
        pass
    def GetIndexOfSegment(self, flexibleCableSegment: FlexibleCableSegment) -> int:
        """
         Returns the index of cable segment. 
         Returns index (int): .
        """
        pass
    def GetSegment(self, index: int) -> FlexibleCableSegment:
        """
         Returns the cable segment at given index. 
         Returns flexibleCableSegment ( FlexibleCableSegment NXOpen.Featu): .
        """
        pass
    def GetSegmentCount(self) -> int:
        """
         Get the count of Features.SheetMetal.FlexibleCableSegment. 
         Returns segmentCount (int):  Segment count. .
        """
        pass
import NXOpen
class FlexibleCableSegment(NXOpen.NXObject): 
    """ Represents a Flexible Cable Segment class. """
    @property
    def BendAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BendAngle
         Returns the bend angle.  
             
         
        """
        pass
    @property
    def BendAngleDirection(self) -> FlexibleCableBuilder.BendAngleDirectionOptions:
        """
        Getter for property: ( FlexibleCableBuilder.BendAngleDirectionOptions NXOpen.Featu) BendAngleDirection
         Returns the bend angle direction.  
             
         
        """
        pass
    @BendAngleDirection.setter
    def BendAngleDirection(self, bendAngleDirectionOption: FlexibleCableBuilder.BendAngleDirectionOptions):
        """
        Setter for property: ( FlexibleCableBuilder.BendAngleDirectionOptions NXOpen.Featu) BendAngleDirection
         Returns the bend angle direction.  
             
         
        """
        pass
    @property
    def BendRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BendRadius
         Returns the bend radius.  
             
         
        """
        pass
    @property
    def Length(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Length
         Returns the length.  
             
         
        """
        pass
    @property
    def PathAdjustmentAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PathAdjustmentAngle
         Returns the path adjustment angle.  
             
         
        """
        pass
    @property
    def PathAdjustmentAngleDirection(self) -> FlexibleCableBuilder.PathAdjustmentAngleDirectionOptions:
        """
        Getter for property: ( FlexibleCableBuilder.PathAdjustmentAngleDirectionOptions NXOpen.Featu) PathAdjustmentAngleDirection
         Returns the path adjustment angle direction.  
             
         
        """
        pass
    @PathAdjustmentAngleDirection.setter
    def PathAdjustmentAngleDirection(self, pathAdjustmentAngleDirectionOption: FlexibleCableBuilder.PathAdjustmentAngleDirectionOptions):
        """
        Setter for property: ( FlexibleCableBuilder.PathAdjustmentAngleDirectionOptions NXOpen.Featu) PathAdjustmentAngleDirection
         Returns the path adjustment angle direction.  
             
         
        """
        pass
    def GetSegmentType(self) -> FlexibleCableBuilder.SegmentTypeOptions:
        """
         Returns the type of cable segment. It could be of NXOpen.Features.SheetMetal.FlexibleCableBuilder.SegmentTypeOptions.Planar, 
                    or NXOpen.Features.SheetMetal.FlexibleCableBuilder.SegmentTypeOptions.Bend
         Returns segmentTypeOption ( FlexibleCableBuilder.SegmentTypeOptions NXOpen.Featu):  Cable segment type. .
        """
        pass
import NXOpen
class FlexTransitionAttachmentListItemBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[FlexTransitionAttachmentListItemBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: FlexTransitionAttachmentListItemBuilder) -> None:
        """
         Appends an object to the list
            
        """
        pass
    @overload
    def Clear(self) -> None:
        """
         Clears the entire list without deleting the objects.  The caller is responsible for 
                accounting for these objects.  If they are not used or deleted by the time the part is 
                closed (in other words, leaked) an error will occur 
        """
        pass
    def ClearIndex(self, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
               not change, but the item at this index is set to NULL.
            
        """
        pass
    @overload
    def Clear(self, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    @overload
    def Erase(self, index: int) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, obj: FlexTransitionAttachmentListItemBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: FlexTransitionAttachmentListItemBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: FlexTransitionAttachmentListItemBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> FlexTransitionAttachmentListItemBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( FlexTransitionAttachmentListItemBuilder NXOpen.Featu):  object found at input index .
        """
        pass
    def GetContents(self) -> List[FlexTransitionAttachmentListItemBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( FlexTransitionAttachmentListItemBuilder List[NXOpen.Fea):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: FlexTransitionAttachmentListItemBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    def MoveToBottom(self, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    def MoveToTop(self, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    def SetContents(self, objects: List[FlexTransitionAttachmentListItemBuilder]) -> None:
        """
         Sets the contents of the entire list. This overwrites the previous contents of this list, 
                but does not delete any objects that were originally on the list.
             
        """
        pass
    @overload
    def Swap(self, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    @overload
    def Swap(self, object1: FlexTransitionAttachmentListItemBuilder, object2: FlexTransitionAttachmentListItemBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class FlexTransitionAttachmentListItemBuilder(NXOpen.TaggedObject): 
    """  Represents a Flex Transition Attachment List item builder class. """
    @property
    def AttachmentCsys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) AttachmentCsys
         Returns the tag of the coordinate system which defines the position and orientation of flex transition attachment.  
             
         
        """
        pass
    @AttachmentCsys.setter
    def AttachmentCsys(self, attachmentCsys: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) AttachmentCsys
         Returns the tag of the coordinate system which defines the position and orientation of flex transition attachment.  
             
         
        """
        pass
    @property
    def ConstrainRotationInAttachment(self) -> bool:
        """
        Getter for property: (bool) ConstrainRotationInAttachment
         Returns whether the rotational degree of freedom of the flex transition is constrained at the attachment or not.  
             
         
        """
        pass
    @ConstrainRotationInAttachment.setter
    def ConstrainRotationInAttachment(self, isConstrRotation: bool):
        """
        Setter for property: (bool) ConstrainRotationInAttachment
         Returns whether the rotational degree of freedom of the flex transition is constrained at the attachment or not.  
             
         
        """
        pass
    @property
    def ConstrainSlidingInAttachment(self) -> bool:
        """
        Getter for property: (bool) ConstrainSlidingInAttachment
         Returns whether the sliding degree of freedom of the flex transition is constrained at the attachment or not.  
             
         
        """
        pass
    @ConstrainSlidingInAttachment.setter
    def ConstrainSlidingInAttachment(self, isConstrSliding: bool):
        """
        Setter for property: (bool) ConstrainSlidingInAttachment
         Returns whether the sliding degree of freedom of the flex transition is constrained at the attachment or not.  
             
         
        """
        pass
    @property
    def ControlRotation(self) -> bool:
        """
        Getter for property: (bool) ControlRotation
         Returns whether the rotational degree of freedom of the flex transition is controlled by the attachment CSYS or not.  
             
         
        """
        pass
    @ControlRotation.setter
    def ControlRotation(self, isControlRotation: bool):
        """
        Setter for property: (bool) ControlRotation
         Returns whether the rotational degree of freedom of the flex transition is controlled by the attachment CSYS or not.  
             
         
        """
        pass
    @property
    def OptimizePath(self) -> bool:
        """
        Getter for property: (bool) OptimizePath
         Returns whether the flex transition path is optimized or not.  
             
         
        """
        pass
    @OptimizePath.setter
    def OptimizePath(self, isOptimizePath: bool):
        """
        Setter for property: (bool) OptimizePath
         Returns whether the flex transition path is optimized or not.  
             
         
        """
        pass
import NXOpen
import NXOpen.Features
class GussetBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a NX Sheet Metal NXOpen.Features.Gusset builder
    """
    class PlacementTypes(Enum):
        """
        Members Include: 
         |Single|  One Gusset will be created at an offset from an edge on the selected bend face. 
         |Fit|  Users will specify the number of occurances of Gusset on the selected bend face and software will calculate the spacing. 
         |Fill|  Users will specify the spacing of Gussets on the selected bend face and software will calculate the number of occurances. 
         |Fixed|  Users will specify the number of occurances and the spacing for Gussets on the selected bend face. 

        """
        Single: int
        Fit: int
        Fill: int
        Fixed: int
        @staticmethod
        def ValueOf(value: int) -> GussetBuilder.PlacementTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Shapes(Enum):
        """
        Members Include: 
         |Square|  Specifies a square shape for the Gusset 
         |Round|  Specifies a round shape for the Gusset 

        """
        Square: int
        Round: int
        @staticmethod
        def ValueOf(value: int) -> GussetBuilder.Shapes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |AutomaticProfile|  Gusset(s) will be created between the planar faces adjacent to the selected bend face. 
         |UserDefinedProfile|  Gusset will be created using a profile defined by the user. 

        """
        AutomaticProfile: int
        UserDefinedProfile: int
        @staticmethod
        def ValueOf(value: int) -> GussetBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class WidthSides(Enum):
        """
        Members Include: 
         |Side1|  The Gusset will be created on the side of plane normal of the user defined profile. 
         |Side2|  The Gusset will be created on the opposite side of the plane normal of the user defined profile. 
         |Symmetric|  The Gusset will be created on both sides of the plane of the user defined profile. 

        """
        Side1: int
        Side2: int
        Symmetric: int
        @staticmethod
        def ValueOf(value: int) -> GussetBuilder.WidthSides:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BendFace(self) -> NXOpen.SelectFace:
        """
        Getter for property: ( NXOpen.SelectFace) BendFace
         Returns the bend face 
                      
                        Selects the bend face along which the gusset is placed.  
          
                      
                  
         
        """
        pass
    @property
    def CornerRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CornerRadius
         Returns the corner radius 
                      
                        Only use this option to edit gussets created prior to NX10.  
          
                        From NX10 onwards, this is going to be automatically determined by adding the material thickness to the  NXOpen::Features::SheetMetal::GussetBuilder::PunchRadius 
                        This value is used only for the  NXOpen::Features::SheetMetal::GussetBuilder::ShapesSquare  shape. The value must be greater than or equal to zero.
                      
                  
         
        """
        pass
    @property
    def DatumPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) DatumPlane
         Returns the plane of the gusset profile.  
             
                      
                        Returns the datum plane on the bend face that contains the profile of the automatic profile gusset.
                      
                  
         
        """
        pass
    @DatumPlane.setter
    def DatumPlane(self, dPlane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) DatumPlane
         Returns the plane of the gusset profile.  
             
                      
                        Returns the datum plane on the bend face that contains the profile of the automatic profile gusset.
                      
                  
         
        """
        pass
    @property
    def Depth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Depth
         Returns the depth 
                      
                        This value is used for the automatic profile Gussets.  
           It represents the distance from the outer
                        bend face of the selected bends along the bisector of the planar faces adjacent to the outer bend face.
                      
                  
         
        """
        pass
    @property
    def DieRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DieRadius
         Returns the die radius value of the sharp edges of the bottom face.  
           The value must be greater than or equal to zero.   
         
        """
        pass
    @property
    def PlacementCount(self) -> int:
        """
        Getter for property: (int) PlacementCount
         Returns the placement count 
                      
                        Only use this option to edit gussets created prior to NX10.  
          
                        Use patterns to create multiple gussets from NX10 onwards. 
                        This value is used if the  NXOpen::Features::SheetMetal::GussetBuilder::PlacementTypes  is set 
                        to  NXOpen::Features::SheetMetal::GussetBuilder::PlacementTypesFit  or
                         NXOpen::Features::SheetMetal::GussetBuilder::PlacementTypesFixed . It represents 
                        the number of occurances of the automatic profile Gusset to create on the selected bend face. The count
                        must be greater than zero for  NXOpen::Features::SheetMetal::GussetBuilder::PlacementTypesFit  and greater than one for
                         NXOpen::Features::SheetMetal::GussetBuilder::PlacementTypesFixed .
                      
                  
         
        """
        pass
    @PlacementCount.setter
    def PlacementCount(self, placementCount: int):
        """
        Setter for property: (int) PlacementCount
         Returns the placement count 
                      
                        Only use this option to edit gussets created prior to NX10.  
          
                        Use patterns to create multiple gussets from NX10 onwards. 
                        This value is used if the  NXOpen::Features::SheetMetal::GussetBuilder::PlacementTypes  is set 
                        to  NXOpen::Features::SheetMetal::GussetBuilder::PlacementTypesFit  or
                         NXOpen::Features::SheetMetal::GussetBuilder::PlacementTypesFixed . It represents 
                        the number of occurances of the automatic profile Gusset to create on the selected bend face. The count
                        must be greater than zero for  NXOpen::Features::SheetMetal::GussetBuilder::PlacementTypesFit  and greater than one for
                         NXOpen::Features::SheetMetal::GussetBuilder::PlacementTypesFixed .
                      
                  
         
        """
        pass
    @property
    def PlacementDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PlacementDistance
         Returns the placement distance 
                      
                       Only use this option to edit gussets created prior to NX10.  
           
                       Use  NXOpen::Features::SheetMetal::GussetBuilder::DatumPlane  to locate automatic profile gussets from NX10 onwards. 
                       If the  NXOpen::Features::SheetMetal::GussetBuilder::PlacementTypes  is set to  NXOpen::Features::SheetMetal::GussetBuilder::PlacementTypesSingle , then this option
                       represents the location of the automatic profile Gusset from one of the ends of the selected bend face. The distance is measured in a direction going from 
                       the start end to the other end. Users can specify which end of the selected bend face to use as the start.
                      
                  
         
        """
        pass
    @property
    def PlacementSpacing(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PlacementSpacing
         Returns the placement spacing  
                      
                       Only use this option to edit gussets created prior to NX10.  
          
                       Use patterns to create multiple gussets from NX10 onwards. 
                       This value is used if the  NXOpen::Features::SheetMetal::GussetBuilder::PlacementTypes  is set 
                        to  NXOpen::Features::SheetMetal::GussetBuilder::PlacementTypesFill  or
                         NXOpen::Features::SheetMetal::GussetBuilder::PlacementTypesFixed . It represents 
                        the spacing between the automatic profile Gussets to create on the selected bend face.
                      
                  
         
        """
        pass
    @property
    def PlacementType(self) -> GussetBuilder.PlacementTypes:
        """
        Getter for property: ( GussetBuilder.PlacementTypes NXOpen.Featu) PlacementType
         Returns the placement type 
                      
                        Only use this option to edit gussets created prior to NX10.  
          
                        Use patterns to create multiple gussets from NX10 onwards. 
                        Specify the Gusset placement option. See the description of  NXOpen::Features::SheetMetal::GussetBuilder::PlacementTypes  elements for details.
                      
                  
         
        """
        pass
    @PlacementType.setter
    def PlacementType(self, placementType: GussetBuilder.PlacementTypes):
        """
        Setter for property: ( GussetBuilder.PlacementTypes NXOpen.Featu) PlacementType
         Returns the placement type 
                      
                        Only use this option to edit gussets created prior to NX10.  
          
                        Use patterns to create multiple gussets from NX10 onwards. 
                        Specify the Gusset placement option. See the description of  NXOpen::Features::SheetMetal::GussetBuilder::PlacementTypes  elements for details.
                      
                  
         
        """
        pass
    @property
    def PunchRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PunchRadius
         Returns the punch radius value 
                   
                       The application of the punch radius has changed from NX10 onwards, to ensure material thickness is constant in the gusset.  
           
                       See the legend in the gusset dialog for more information. 
                  
                  
         
        """
        pass
    @property
    def Section(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Section
         Returns the section 
                      
                        This section object contains a planar set of connected curves that will be used to
                        create a Gusset of type  NXOpen::Features::SheetMetal::GussetBuilder::TypesUserDefinedProfile .  
           This
                        profile can be closed or open. If it is open, then the end points can touch face(s). The profile must not intersect the
                        solid body. If an open profile does not intersect or touch any face, each end will be extended until it touches a face.
                      
                  
         
        """
        pass
    @property
    def Shape(self) -> GussetBuilder.Shapes:
        """
        Getter for property: ( GussetBuilder.Shapes NXOpen.Featu) Shape
         Returns the shape 
                       See  NXOpen::Features::SheetMetal::GussetBuilder::Shapes  for details.  
          
                      
                  
         
        """
        pass
    @Shape.setter
    def Shape(self, shape: GussetBuilder.Shapes):
        """
        Setter for property: ( GussetBuilder.Shapes NXOpen.Featu) Shape
         Returns the shape 
                       See  NXOpen::Features::SheetMetal::GussetBuilder::Shapes  for details.  
          
                      
                  
         
        """
        pass
    @property
    def SideAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SideAngle
         Returns the side angle.  
           The value must be greater than or equal to zero.   
         
        """
        pass
    @property
    def StartEdge(self) -> NXOpen.SelectEdge:
        """
        Getter for property: ( NXOpen.SelectEdge) StartEdge
         Returns the start edge  
                      
                        Only use this option to edit gussets created prior to NX10.  
          
                        Use  NXOpen::Features::SheetMetal::GussetBuilder::DatumPlane  to locate automatic profile gussets from NX10 onwards.  
                        Selects the edge on the bend face to determine the gusset offset direction.
                      
                  
         
        """
        pass
    @property
    def Type(self) -> GussetBuilder.Types:
        """
        Getter for property: ( GussetBuilder.Types NXOpen.Featu) Type
         Returns the type of Gusset feature   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: GussetBuilder.Types):
        """
        Setter for property: ( GussetBuilder.Types NXOpen.Featu) Type
         Returns the type of Gusset feature   
            
         
        """
        pass
    @property
    def Width(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Width
         Returns the width value for the Gusset   
            
         
        """
        pass
    @property
    def WidthSide(self) -> GussetBuilder.WidthSides:
        """
        Getter for property: ( GussetBuilder.WidthSides NXOpen.Featu) WidthSide
         Returns the width side 
                      
                        Defines the side of the profile to which material should be added or from which material should be removed to construct 
                        the feature.  
           
                        The side option is not required when the profile is closed.
                      
                  
         
        """
        pass
    @WidthSide.setter
    def WidthSide(self, widthSide: GussetBuilder.WidthSides):
        """
        Setter for property: ( GussetBuilder.WidthSides NXOpen.Featu) WidthSide
         Returns the width side 
                      
                        Defines the side of the profile to which material should be added or from which material should be removed to construct 
                        the feature.  
           
                        The side option is not required when the profile is closed.
                      
                  
         
        """
        pass
    def AlternateSolution(self) -> None:
        """
         Cycles the available solutions when a user defined profile intersects the solid body. If there is
                    only one working solution then it will be automatically selected and this method will not do anything. 
        """
        pass
    def GetIsPreNx10(self) -> bool:
        """
          Whether this is a pre-NX10 gusset. 
                    
                        Use this to determine whether the gusset is created prior to NX10.
                    
                
         Returns isPreNX10 (bool): .
        """
        pass
    def GetPlacementOriginAndDirection(self) -> Tuple[NXOpen.Vector3d, NXOpen.Point3d]:
        """
         Get the placement origin and direction. 
                    
                        Only use this option to edit gussets created prior to NX10.
                        Use NXOpen.Features.SheetMetal.GussetBuilder.DatumPlane to locate automatic profile gussets from NX10 onwards.  
                        Get the point from which the placement distance will be measured and the 
                        direction along which the positive distance is defined.
                    
                
         Returns A tuple consisting of (direction, origin). 
         - direction is:  NXOpen.Vector3d. Direction along which the placement distance is measured. .
         - origin is:  NXOpen.Point3d. Start point from which placement distance is measured. .

        """
        pass
    def GetStartEdgeCandidates(self) -> List[NXOpen.Edge]:
        """
         Get the edges on the bend face that can be selected as Start Edge.
                    
                        Only use this option to edit gussets created prior to NX10.
                        Use NXOpen.Features.SheetMetal.GussetBuilder.DatumPlane to locate automatic profile gussets from NX10 onwards. 
                        Get the edges on the bend face that can be selected as Start Edge.
                        If there is no Bend Face, then no edges will be returned.
                    
                
         Returns candidateEdges ( NXOpen.Edge Li):  An array of edges that are valid for selection as start edge .
        """
        pass
import NXOpen
class HemFlangeBuilder(SheetmetalBaseBuilder): 
    """
    Represents a NXOpen.Features.HemFlange builder
    """
    class BendReliefOptions(Enum):
        """
        Members Include: 
         |Square|   
         |Round|   
         |NotSet|  

        """
        Square: int
        Round: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> HemFlangeBuilder.BendReliefOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class InsetTypeOptions(Enum):
        """
        Members Include: 
         |MaterialInside|  The hem flange is flush with the thickness face on the inside 
         |MaterialOutside|  The hem flange is flush with the thickness face on the outside 
         |BendOutside|  The bend and hem flange are outside the thickness face 

        """
        MaterialInside: int
        MaterialOutside: int
        BendOutside: int
        @staticmethod
        def ValueOf(value: int) -> HemFlangeBuilder.InsetTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TypeOptions(Enum):
        """
        Members Include: 
         |ClosedHemType|  
         |OpenHemType|  
         |SFlangeHemType|  
         |CurlHemType|    
         |OpenLoopHemType|   
         |ClosedLoopHemType|    
         |CenteredLoopHemType|  

        """
        ClosedHemType: int
        OpenHemType: int
        SFlangeHemType: int
        CurlHemType: int
        OpenLoopHemType: int
        ClosedLoopHemType: int
        CenteredLoopHemType: int
        @staticmethod
        def ValueOf(value: int) -> HemFlangeBuilder.TypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BendReliefDepth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BendReliefDepth
         Returns the bend relief depth   
            
         
        """
        pass
    @property
    def BendReliefType(self) -> HemFlangeBuilder.BendReliefOptions:
        """
        Getter for property: ( HemFlangeBuilder.BendReliefOptions NXOpen.Featu) BendReliefType
         Returns the bend relief type   
            
         
        """
        pass
    @BendReliefType.setter
    def BendReliefType(self, bendReliefType: HemFlangeBuilder.BendReliefOptions):
        """
        Setter for property: ( HemFlangeBuilder.BendReliefOptions NXOpen.Featu) BendReliefType
         Returns the bend relief type   
            
         
        """
        pass
    @property
    def BendReliefWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BendReliefWidth
         Returns the bend relief width   
            
         
        """
        pass
    @property
    def EdgeChain(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) EdgeChain
         Returns the edge chain   
            
         
        """
        pass
    @property
    def FirstBendRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FirstBendRadius
         Returns the first bend radius   
            
         
        """
        pass
    @property
    def FirstFlangeLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FirstFlangeLength
         Returns the first flange length   
            
         
        """
        pass
    @property
    def InsetType(self) -> HemFlangeBuilder.InsetTypeOptions:
        """
        Getter for property: ( HemFlangeBuilder.InsetTypeOptions NXOpen.Featu) InsetType
         Returns the inset type options   
            
         
        """
        pass
    @InsetType.setter
    def InsetType(self, insetType: HemFlangeBuilder.InsetTypeOptions):
        """
        Setter for property: ( HemFlangeBuilder.InsetTypeOptions NXOpen.Featu) InsetType
         Returns the inset type options   
            
         
        """
        pass
    @property
    def MiterAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MiterAngle
         Returns the miter angle   
            
         
        """
        pass
    @property
    def NeutralFactor(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) NeutralFactor
         Returns the neutral factor   
            
         
        """
        pass
    @property
    def SecondBendRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SecondBendRadius
         Returns the second bend radius   
            
         
        """
        pass
    @property
    def SecondFlangeLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SecondFlangeLength
         Returns the second flange length   
            
         
        """
        pass
    @property
    def SweepAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SweepAngle
         Returns the sweep   
            
         
        """
        pass
    @property
    def Type(self) -> HemFlangeBuilder.TypeOptions:
        """
        Getter for property: ( HemFlangeBuilder.TypeOptions NXOpen.Featu) Type
         Returns the hem type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: HemFlangeBuilder.TypeOptions):
        """
        Setter for property: ( HemFlangeBuilder.TypeOptions NXOpen.Featu) Type
         Returns the hem type   
            
         
        """
        pass
    @property
    def UseMiter(self) -> bool:
        """
        Getter for property: (bool) UseMiter
         Returns the use miter hem   
            
         
        """
        pass
    @UseMiter.setter
    def UseMiter(self, useMiterHem: bool):
        """
        Setter for property: (bool) UseMiter
         Returns the use miter hem   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class HoleTreatmentBuilder(NXOpen.TaggedObject): 
    """ The HoleTreatmentBuilder class is used to manage a builder object for
        a hole treatment in the flat pattern dialogs. It includes
        properties and an enumeration type for a flag that indicates whether the
        global (flat pattern preferences) value is to be used, an enumeration type
        that indicates what type of hole treatment to apply, and an expression
        to indicate the diameter value associated with treatment type.
    """
    class TreatmentType(Enum):
        """
        Members Include: 
         |NotSet| 
         |Centermark| 
         |HoleAndCentermark| 

        """
        NotSet: int
        Centermark: int
        HoleAndCentermark: int
        @staticmethod
        def ValueOf(value: int) -> HoleTreatmentBuilder.TreatmentType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Diameter
         Returns the hole diameter value associated with the treatment type   
            
         
        """
        pass
    @property
    def Treatment(self) -> HoleTreatmentBuilder.TreatmentType:
        """
        Getter for property: ( HoleTreatmentBuilder.TreatmentType NXOpen.Featu) Treatment
         Returns the treatment type option menu value   
            
         
        """
        pass
    @Treatment.setter
    def Treatment(self, treatmentType: HoleTreatmentBuilder.TreatmentType):
        """
        Setter for property: ( HoleTreatmentBuilder.TreatmentType NXOpen.Featu) Treatment
         Returns the treatment type option menu value   
            
         
        """
        pass
    @property
    def UseGlobal(self) -> bool:
        """
        Getter for property: (bool) UseGlobal
         Returns the use global toggle value   
            
         
        """
        pass
    @UseGlobal.setter
    def UseGlobal(self, useGlobal: bool):
        """
        Setter for property: (bool) UseGlobal
         Returns the use global toggle value   
            
         
        """
        pass
import NXOpen
import NXOpen.Features
class JogBuilder(SheetmetalBaseBuilder): 
    """ Represents a Jog feature builder. """
    class BendLocationOptions(Enum):
        """
        Members Include: 
         |MaterialInside|  
         |MaterialOutside|  
         |BendOutside|  

        """
        MaterialInside: int
        MaterialOutside: int
        BendOutside: int
        @staticmethod
        def ValueOf(value: int) -> JogBuilder.BendLocationOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DimensionTypeOptions(Enum):
        """
        Members Include: 
         |Offset|  the actual depth will be depth plus the thickness of sheet. 
         |Full|  the actual extent distance will be the value specified as depth. 

        """
        Offset: int
        Full: int
        @staticmethod
        def ValueOf(value: int) -> JogBuilder.DimensionTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DirectionTypeOptions(Enum):
        """
        Members Include: 
         |SectionNormalSide|  jog created on the side of the section normal. 
         |SectionReverseNormalSide|  jog created on the side opposite to that of the section normal 

        """
        SectionNormalSide: int
        SectionReverseNormalSide: int
        @staticmethod
        def ValueOf(value: int) -> JogBuilder.DirectionTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FixedSideOptions(Enum):
        """
        Members Include: 
         |SectionSideLeft|  Side pointed to by the inverse of the tangent cross normal vector 
         |SectionSideRight|  Side pointed to by the tangent cross normal vector 

        """
        SectionSideLeft: int
        SectionSideRight: int
        @staticmethod
        def ValueOf(value: int) -> JogBuilder.FixedSideOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Angle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Angle
         Returns the angle   
            
         
        """
        pass
    @property
    def BendLocation(self) -> JogBuilder.BendLocationOptions:
        """
        Getter for property: ( JogBuilder.BendLocationOptions NXOpen.Featu) BendLocation
         Returns   
            
         
        """
        pass
    @BendLocation.setter
    def BendLocation(self, bend_location: JogBuilder.BendLocationOptions):
        """
        Setter for property: ( JogBuilder.BendLocationOptions NXOpen.Featu) BendLocation
         Returns   
            
         
        """
        pass
    @property
    def BendOptions(self) -> BendOptions:
        """
        Getter for property: ( BendOptions NXOpen.Featu) BendOptions
         Returns the bend options.  
           The option  Features::SheetMetal::BendOptions::CornerReliefTypeOptionsNone  is not valid for the  Features::Jog  starting NX11 onwards.
                       
                         From NX 12  Features::SheetMetal::BendOptions::SetExtendBendRelief 
                         has no effect on the Jog feature.
                       
                   
         
        """
        pass
    @property
    def DimensionType(self) -> JogBuilder.DimensionTypeOptions:
        """
        Getter for property: ( JogBuilder.DimensionTypeOptions NXOpen.Featu) DimensionType
         Returns the Offset Dimension
                      
                        The actual extent distance of the Jog will be determined by the active dimension option.  
          
                        In case of  Features::SheetMetal::JogBuilder::DimensionTypeOptionsOffset  the actual extent distance will be offset dimension distance plus the thickness of sheet.
                        In case of  Features::SheetMetal::JogBuilder::DimensionTypeOptionsFull  the actual extent distance will be the Full dimension distance.
                      
                  
         
        """
        pass
    @DimensionType.setter
    def DimensionType(self, dimension_type: JogBuilder.DimensionTypeOptions):
        """
        Setter for property: ( JogBuilder.DimensionTypeOptions NXOpen.Featu) DimensionType
         Returns the Offset Dimension
                      
                        The actual extent distance of the Jog will be determined by the active dimension option.  
          
                        In case of  Features::SheetMetal::JogBuilder::DimensionTypeOptionsOffset  the actual extent distance will be offset dimension distance plus the thickness of sheet.
                        In case of  Features::SheetMetal::JogBuilder::DimensionTypeOptionsFull  the actual extent distance will be the Full dimension distance.
                      
                  
         
        """
        pass
    @property
    def DirectionType(self) -> JogBuilder.DirectionTypeOptions:
        """
        Getter for property: ( JogBuilder.DirectionTypeOptions NXOpen.Featu) DirectionType
         Returns   
            
         
        """
        pass
    @DirectionType.setter
    def DirectionType(self, direction_type: JogBuilder.DirectionTypeOptions):
        """
        Setter for property: ( JogBuilder.DirectionTypeOptions NXOpen.Featu) DirectionType
         Returns   
            
         
        """
        pass
    @property
    def ExtendProfile(self) -> bool:
        """
        Getter for property: (bool) ExtendProfile
         Returns   
            
         
        """
        pass
    @ExtendProfile.setter
    def ExtendProfile(self, extend_option: bool):
        """
        Setter for property: (bool) ExtendProfile
         Returns   
            
         
        """
        pass
    @property
    def FixedSide(self) -> JogBuilder.FixedSideOptions:
        """
        Getter for property: ( JogBuilder.FixedSideOptions NXOpen.Featu) FixedSide
         Returns   
            
         
        """
        pass
    @FixedSide.setter
    def FixedSide(self, section_side: JogBuilder.FixedSideOptions):
        """
        Setter for property: ( JogBuilder.FixedSideOptions NXOpen.Featu) FixedSide
         Returns   
            
         
        """
        pass
    @property
    def Section(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Section
         Returns   
            
         
        """
        pass
    @Section.setter
    def Section(self, section: NXOpen.Section):
        """
        Setter for property: ( NXOpen.Section) Section
         Returns   
            
         
        """
        pass
    @property
    def Sketch(self) -> NXOpen.Features.SketchFeature:
        """
        Getter for property: ( NXOpen.Features.SketchFeature) Sketch
         Returns   
            
         
        """
        pass
    @Sketch.setter
    def Sketch(self, sketch: NXOpen.Features.SketchFeature):
        """
        Setter for property: ( NXOpen.Features.SketchFeature) Sketch
         Returns   
            
         
        """
        pass
    @property
    def TargetFace(self) -> NXOpen.Face:
        """
        Getter for property: ( NXOpen.Face) TargetFace
         Returns the target face on which jog feature applies.  
             
         
        """
        pass
    @TargetFace.setter
    def TargetFace(self, targetFace: NXOpen.Face):
        """
        Setter for property: ( NXOpen.Face) TargetFace
         Returns the target face on which jog feature applies.  
             
         
        """
        pass
    def GetHeight(self) -> NXOpen.Expression:
        """
         Height of the Jog
         Returns height ( NXOpen.Expression):  .
        """
        pass
    def ValidateBuilderData(self) -> int:
        """
         Verify whether the builder data is valid for creating a jog or not.
                    
                         If the Builder data is valid, returned value shall be 0
                    
                
         Returns builderDataValidity (int):  Data Validity Flag.
        """
        pass
import NXOpen
import NXOpen.Features
class JoggleBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Sheetmetal joggle builder class. """
    class LimitTypes(Enum):
        """
        Members Include: 
         |Single| 
         |Twin| 

        """
        Single: int
        Twin: int
        @staticmethod
        def ValueOf(value: int) -> JoggleBuilder.LimitTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Adjustment(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Adjustment
         Returns the adjustment   
            
         
        """
        pass
    @property
    def EndPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) EndPlane
         Returns the end plane   
            
         
        """
        pass
    @EndPlane.setter
    def EndPlane(self, endPlane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) EndPlane
         Returns the end plane   
            
         
        """
        pass
    @property
    def FlatPatternCompensation(self) -> bool:
        """
        Getter for property: (bool) FlatPatternCompensation
         Returns the flat pattern compensation   
            
         
        """
        pass
    @FlatPatternCompensation.setter
    def FlatPatternCompensation(self, flatPatternCompensation: bool):
        """
        Setter for property: (bool) FlatPatternCompensation
         Returns the flat pattern compensation   
            
         
        """
        pass
    @property
    def InputList(self) -> JoggleInputListItemBuilderList:
        """
        Getter for property: ( JoggleInputListItemBuilderList NXOpen.Featu) InputList
         Returns the input list   
            
         
        """
        pass
    @property
    def LimitType(self) -> JoggleBuilder.LimitTypes:
        """
        Getter for property: ( JoggleBuilder.LimitTypes NXOpen.Featu) LimitType
         Returns the limit type   
            
         
        """
        pass
    @LimitType.setter
    def LimitType(self, limitType: JoggleBuilder.LimitTypes):
        """
        Setter for property: ( JoggleBuilder.LimitTypes NXOpen.Featu) LimitType
         Returns the limit type   
            
         
        """
        pass
    @property
    def Side1Options(self) -> JoggleSideOptionsBuilder:
        """
        Getter for property: ( JoggleSideOptionsBuilder NXOpen.Featu) Side1Options
         Returns the joggle side 1 options   
            
         
        """
        pass
    @property
    def Side2Options(self) -> JoggleSideOptionsBuilder:
        """
        Getter for property: ( JoggleSideOptionsBuilder NXOpen.Featu) Side2Options
         Returns the joggle side 2 options   
            
         
        """
        pass
    @property
    def StartPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) StartPlane
         Returns the start plane   
            
         
        """
        pass
    @StartPlane.setter
    def StartPlane(self, startPlane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) StartPlane
         Returns the start plane   
            
         
        """
        pass
    @property
    def SymmetricSides(self) -> bool:
        """
        Getter for property: (bool) SymmetricSides
         Returns the symmetric sides   
            
         
        """
        pass
    @SymmetricSides.setter
    def SymmetricSides(self, symmetricSides: bool):
        """
        Setter for property: (bool) SymmetricSides
         Returns the symmetric sides   
            
         
        """
        pass
    @property
    def UseMaterialTable(self) -> bool:
        """
        Getter for property: (bool) UseMaterialTable
         Returns the Use Material Table   
            
         
        """
        pass
    @UseMaterialTable.setter
    def UseMaterialTable(self, useMaterialTable: bool):
        """
        Setter for property: (bool) UseMaterialTable
         Returns the Use Material Table   
            
         
        """
        pass
    def CreateJoggleInputListItem(self) -> JoggleInputListItemBuilder:
        """
         Create a input list item. 
         Returns listitem ( JoggleInputListItemBuilder NXOpen.Featu): .
        """
        pass
import NXOpen
class JoggleInputListItemBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[JoggleInputListItemBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: JoggleInputListItemBuilder) -> None:
        """
         Appends an object to the list
            
        """
        pass
    @overload
    def Clear(self) -> None:
        """
         Clears the entire list without deleting the objects.  The caller is responsible for 
                accounting for these objects.  If they are not used or deleted by the time the part is 
                closed (in other words, leaked) an error will occur 
        """
        pass
    def ClearIndex(self, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
               not change, but the item at this index is set to NULL.
            
        """
        pass
    @overload
    def Clear(self, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    @overload
    def Erase(self, index: int) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, obj: JoggleInputListItemBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: JoggleInputListItemBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: JoggleInputListItemBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> JoggleInputListItemBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( JoggleInputListItemBuilder NXOpen.Featu):  object found at input index .
        """
        pass
    def GetContents(self) -> List[JoggleInputListItemBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( JoggleInputListItemBuilder List[NXOpen.Fea):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: JoggleInputListItemBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    def MoveToBottom(self, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    def MoveToTop(self, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    def SetContents(self, objects: List[JoggleInputListItemBuilder]) -> None:
        """
         Sets the contents of the entire list. This overwrites the previous contents of this list, 
                but does not delete any objects that were originally on the list.
             
        """
        pass
    @overload
    def Swap(self, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    @overload
    def Swap(self, object1: JoggleInputListItemBuilder, object2: JoggleInputListItemBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class JoggleInputListItemBuilder(NXOpen.TaggedObject): 
    """
    Represents a Sheetmetal joggle input list item builder class. This builder is used to
    interrogate the joggle inputitems in the list.
    """
    @property
    def Depth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Depth
         Returns the depth   
            
         
        """
        pass
    @property
    def Faces(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) Faces
         Returns the faces   
            
         
        """
        pass
    @property
    def ReverseDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseDirection
         Returns the reverse direction   
            
         
        """
        pass
    @ReverseDirection.setter
    def ReverseDirection(self, reverseDirection: bool):
        """
        Setter for property: (bool) ReverseDirection
         Returns the reverse direction   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class JoggleSideOptionsBuilder(NXOpen.TaggedObject): 
    """ Represents a Sheetmetal Joggle side Options class. """
    @property
    def Clearance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Clearance
         Returns the clearance   
            
         
        """
        pass
    @property
    def OffsetRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) OffsetRadius
         Returns the offset radius   
            
         
        """
        pass
    @property
    def Runout(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Runout
         Returns the runout   
            
         
        """
        pass
    @property
    def StationaryRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StationaryRadius
         Returns the stationary radius   
            
         
        """
        pass
import NXOpen.Features
class Joggle(NXOpen.Features.Feature): 
    """ Represents a joggle feature """
    pass
import NXOpen
import NXOpen.Features
class LighteningCutoutBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Features.SheetMetal.LighteningCutout builder """
    class CutoutType(Enum):
        """
        Members Include: 
         |Hole| 
         |UserDefined| 

        """
        Hole: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> LighteningCutoutBuilder.CutoutType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Angle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Angle
         Returns the angle   
            
         
        """
        pass
    @property
    def BendOptions(self) -> BendOptions:
        """
        Getter for property: ( BendOptions NXOpen.Featu) BendOptions
         Returns the bend options   
            
         
        """
        pass
    @property
    def CheckClearance(self) -> bool:
        """
        Getter for property: (bool) CheckClearance
         Returns whether to check the clearance   
            
         
        """
        pass
    @CheckClearance.setter
    def CheckClearance(self, checkClearance: bool):
        """
        Setter for property: (bool) CheckClearance
         Returns whether to check the clearance   
            
         
        """
        pass
    @property
    def Clearance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Clearance
         Returns the clearance   
            
         
        """
        pass
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Diameter
         Returns the diameter when the type is  NXOpen::Features::SheetMetal::LighteningCutoutBuilder::CutoutTypeHole    
            
         
        """
        pass
    @property
    def DieRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DieRadius
         Returns the die radius   
            
         
        """
        pass
    @property
    def HoleCenter(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) HoleCenter
         Returns the hole center when the type is  NXOpen::Features::SheetMetal::LighteningCutoutBuilder::CutoutTypeHole    
            
         
        """
        pass
    @property
    def Length(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Length
         Returns the length   
            
         
        """
        pass
    @property
    def ReverseBendDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseBendDirection
         Returns whether the bend direction is reversed   
            
         
        """
        pass
    @ReverseBendDirection.setter
    def ReverseBendDirection(self, reverseBendDirection: bool):
        """
        Setter for property: (bool) ReverseBendDirection
         Returns whether the bend direction is reversed   
            
         
        """
        pass
    @property
    def SectionCornerRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SectionCornerRadius
         Returns the section corner radius   
            
         
        """
        pass
    @property
    def Sketch(self) -> NXOpen.Features.SketchFeature:
        """
        Getter for property: ( NXOpen.Features.SketchFeature) Sketch
         Returns the Sketch used by Lightening Cutout   
            
         
        """
        pass
    @property
    def StandardName(self) -> str:
        """
        Getter for property: (str) StandardName
         Returns the standard name selected   
            
         
        """
        pass
    @StandardName.setter
    def StandardName(self, standardName: str):
        """
        Setter for property: (str) StandardName
         Returns the standard name selected   
            
         
        """
        pass
    @property
    def Type(self) -> LighteningCutoutBuilder.CutoutType:
        """
        Getter for property: ( LighteningCutoutBuilder.CutoutType NXOpen.Featu) Type
         Returns the type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: LighteningCutoutBuilder.CutoutType):
        """
        Setter for property: ( LighteningCutoutBuilder.CutoutType NXOpen.Featu) Type
         Returns the type   
            
         
        """
        pass
    @property
    def UserDefinedSection(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) UserDefinedSection
         Returns the section when the type is  NXOpen::Features::SheetMetal::LighteningCutoutBuilder::CutoutTypeUserDefined    
            
         
        """
        pass
    def GetStandards(self) -> List[str]:
        """
         Returns the standard names available for the material selected 
         Returns standardNames (List[str]): .
        """
        pass
import NXOpen.Features
class LighteningCutout(NXOpen.Features.BodyFeature): 
    """ Represents a lightening cutout feature """
    pass
import NXOpen
import NXOpen.Features
class LoftedFlangeBuilder(SheetmetalBaseBuilder): 
    """ Represents a Lofted Flange feature builder. """
    class AutoReliefTypes(Enum):
        """
        Members Include: 
         |Linear| 
         |Spherical| 

        """
        Linear: int
        Spherical: int
        @staticmethod
        def ValueOf(value: int) -> LoftedFlangeBuilder.AutoReliefTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class BendDivideParameters(Enum):
        """
        Members Include: 
         |NumberOfBendSegments| 
         |MaximumChordHeight| 
         |MaximumSegmentLength| 
         |MaximumSegmentAngle| 

        """
        NumberOfBendSegments: int
        MaximumChordHeight: int
        MaximumSegmentLength: int
        MaximumSegmentAngle: int
        @staticmethod
        def ValueOf(value: int) -> LoftedFlangeBuilder.BendDivideParameters:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class BendingMethods(Enum):
        """
        Members Include: 
         |Formed| 
         |Advanced| 
         |Bends| 

        """
        Formed: int
        Advanced: int
        Bends: int
        @staticmethod
        def ValueOf(value: int) -> LoftedFlangeBuilder.BendingMethods:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SectionSideOptions(Enum):
        """
        Members Include: 
         |Left|  Side pointed to by the inverse of the tangent cross normal vector 
         |Right|  Side pointed to by the tangent cross normal vector 

        """
        Left: int
        Right: int
        @staticmethod
        def ValueOf(value: int) -> LoftedFlangeBuilder.SectionSideOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AutoReliefType(self) -> LoftedFlangeBuilder.AutoReliefTypes:
        """
        Getter for property: ( LoftedFlangeBuilder.AutoReliefTypes NXOpen.Featu) AutoReliefType
         Returns the auto relief of lofted flange.  
            
         
        """
        pass
    @AutoReliefType.setter
    def AutoReliefType(self, autoReliefType: LoftedFlangeBuilder.AutoReliefTypes):
        """
        Setter for property: ( LoftedFlangeBuilder.AutoReliefTypes NXOpen.Featu) AutoReliefType
         Returns the auto relief of lofted flange.  
            
         
        """
        pass
    @property
    def BendDivideParameter(self) -> LoftedFlangeBuilder.BendDivideParameters:
        """
        Getter for property: ( LoftedFlangeBuilder.BendDivideParameters NXOpen.Featu) BendDivideParameter
         Returns the bend divide parameter.  
            
         
        """
        pass
    @BendDivideParameter.setter
    def BendDivideParameter(self, bendDivideParameter: LoftedFlangeBuilder.BendDivideParameters):
        """
        Setter for property: ( LoftedFlangeBuilder.BendDivideParameters NXOpen.Featu) BendDivideParameter
         Returns the bend divide parameter.  
            
         
        """
        pass
    @property
    def BendOptions(self) -> BendOptions:
        """
        Getter for property: ( BendOptions NXOpen.Featu) BendOptions
         Returns the bend options object.  
          
                Get the bend options object which is created while creating builder. Then set values to parameters of
                bend options object(like bend radius, bend relief type etc.) using set methods of bend options object.
                  
         
        """
        pass
    @property
    def BendingMethod(self) -> LoftedFlangeBuilder.BendingMethods:
        """
        Getter for property: ( LoftedFlangeBuilder.BendingMethods NXOpen.Featu) BendingMethod
         Returns the bending method of lofted flange.  
            
         
        """
        pass
    @BendingMethod.setter
    def BendingMethod(self, bendingMethod: LoftedFlangeBuilder.BendingMethods):
        """
        Setter for property: ( LoftedFlangeBuilder.BendingMethods NXOpen.Featu) BendingMethod
         Returns the bending method of lofted flange.  
            
         
        """
        pass
    @property
    def EndSection(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) EndSection
         Returns the end section of the lofted flange.  
          The section profile should be open looped.
                 
         
        """
        pass
    @EndSection.setter
    def EndSection(self, end_section: NXOpen.Section):
        """
        Setter for property: ( NXOpen.Section) EndSection
         Returns the end section of the lofted flange.  
          The section profile should be open looped.
                 
         
        """
        pass
    @property
    def EndSectionPoint(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) EndSectionPoint
         Returns the startend point of the end section.  
          It can be startend point of the section profile.
                 
         
        """
        pass
    @EndSectionPoint.setter
    def EndSectionPoint(self, point: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) EndSectionPoint
         Returns the startend point of the end section.  
          It can be startend point of the section profile.
                 
         
        """
        pass
    @property
    def EndSketch(self) -> NXOpen.Features.SketchFeature:
        """
        Getter for property: ( NXOpen.Features.SketchFeature) EndSketch
         Returns the end section sketch as slave.  
          
               Set the sketch which is used to create end section.
               This is only used when the section is created from sketch. If the section is created
               from edges or if the end sketch is not required to be slave, set the value as NULL .
                 
         
        """
        pass
    @EndSketch.setter
    def EndSketch(self, slave_end_sketch: NXOpen.Features.SketchFeature):
        """
        Setter for property: ( NXOpen.Features.SketchFeature) EndSketch
         Returns the end section sketch as slave.  
          
               Set the sketch which is used to create end section.
               This is only used when the section is created from sketch. If the section is created
               from edges or if the end sketch is not required to be slave, set the value as NULL .
                 
         
        """
        pass
    @property
    def IndexMarkLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) IndexMarkLength
         Returns the index mark length 
                Get the index mark length expression 
                If use segmented bends is set to true the only the index mark length value 
                is used for dividing the bend even though a value is set 
                Index mark length value only gets reflected in flat pattern view  
            
         
        """
        pass
    @property
    def IsSecondary(self) -> bool:
        """
        Getter for property: (bool) IsSecondary
         Returns the type of lofted flange feature - base lofted flangesecondary lofted flange.  
           Specify false for base lofted flanges and true for secondary lofted flanges.
                   
         
        """
        pass
    @IsSecondary.setter
    def IsSecondary(self, is_secondary: bool):
        """
        Setter for property: (bool) IsSecondary
         Returns the type of lofted flange feature - base lofted flangesecondary lofted flange.  
           Specify false for base lofted flanges and true for secondary lofted flanges.
                   
         
        """
        pass
    @property
    def MaximumChordHeight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaximumChordHeight
         Returns the maximum chord height.  
            
         
        """
        pass
    @property
    def MaximumSegmentAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaximumSegmentAngle
         Returns the maximum segment angle.  
            
         
        """
        pass
    @property
    def MaximumSegmentLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaximumSegmentLength
         Returns the maximum segment length.  
            
         
        """
        pass
    @property
    def NumberOfBendSegments(self) -> int:
        """
        Getter for property: (int) NumberOfBendSegments
         Returns the number of bend segments 
                 Get and set the number of bend segments
                If use segmented bends is set to true then only the number of bend segments value is used for dividing the bend even though a value is set  
            
         
        """
        pass
    @NumberOfBendSegments.setter
    def NumberOfBendSegments(self, numberOfBendSegments: int):
        """
        Setter for property: (int) NumberOfBendSegments
         Returns the number of bend segments 
                 Get and set the number of bend segments
                If use segmented bends is set to true then only the number of bend segments value is used for dividing the bend even though a value is set  
            
         
        """
        pass
    @property
    def StartSection(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) StartSection
         Returns the start section of the lofted flange.  
           The section profile should be open looped.
                  
         
        """
        pass
    @StartSection.setter
    def StartSection(self, start_section: NXOpen.Section):
        """
        Setter for property: ( NXOpen.Section) StartSection
         Returns the start section of the lofted flange.  
           The section profile should be open looped.
                  
         
        """
        pass
    @property
    def StartSectionPoint(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) StartSectionPoint
         Returns the startend point of the start section.  
          It can be startend point of the section profile.
                 
         
        """
        pass
    @StartSectionPoint.setter
    def StartSectionPoint(self, point: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) StartSectionPoint
         Returns the startend point of the start section.  
          It can be startend point of the section profile.
                 
         
        """
        pass
    @property
    def StartSketch(self) -> NXOpen.Features.SketchFeature:
        """
        Getter for property: ( NXOpen.Features.SketchFeature) StartSketch
         Returns the start section sketch as slave.  
          
               Set the sketch which is used to create start section.
               This is only used when the section is created from sketch. If the section is created
               from edges or start sketch is not required to be slave, set slave sketch as NULL.
                
         
        """
        pass
    @StartSketch.setter
    def StartSketch(self, slave_start_sketch: NXOpen.Features.SketchFeature):
        """
        Setter for property: ( NXOpen.Features.SketchFeature) StartSketch
         Returns the start section sketch as slave.  
          
               Set the sketch which is used to create start section.
               This is only used when the section is created from sketch. If the section is created
               from edges or start sketch is not required to be slave, set slave sketch as NULL.
                
         
        """
        pass
    @property
    def ThicknessSide(self) -> LoftedFlangeBuilder.SectionSideOptions:
        """
        Getter for property: ( LoftedFlangeBuilder.SectionSideOptions NXOpen.Featu) ThicknessSide
         Returns the thickness side of base lofted flange.  
          
                  
         
        """
        pass
    @ThicknessSide.setter
    def ThicknessSide(self, thickness_side: LoftedFlangeBuilder.SectionSideOptions):
        """
        Setter for property: ( LoftedFlangeBuilder.SectionSideOptions NXOpen.Featu) ThicknessSide
         Returns the thickness side of base lofted flange.  
          
                  
         
        """
        pass
    @property
    def TrimEndPlates(self) -> bool:
        """
        Getter for property: (bool) TrimEndPlates
         Returns the trim end plates.  
            
         
        """
        pass
    @TrimEndPlates.setter
    def TrimEndPlates(self, trimEndPlates: bool):
        """
        Setter for property: (bool) TrimEndPlates
         Returns the trim end plates.  
            
         
        """
        pass
    @property
    def UseSegmentedBends(self) -> bool:
        """
        Getter for property: (bool) UseSegmentedBends
         Returns  the use multi segment bends 
                Set use_segmented_bends to true or false and get the same 
                If use multi segment bends is set to true then lofted flange bend face is gets divided as per the number bend segments mentioned by the user  
            
         
        """
        pass
    @UseSegmentedBends.setter
    def UseSegmentedBends(self, useMultiSegmentBends: bool):
        """
        Setter for property: (bool) UseSegmentedBends
         Returns  the use multi segment bends 
                Set use_segmented_bends to true or false and get the same 
                If use multi segment bends is set to true then lofted flange bend face is gets divided as per the number bend segments mentioned by the user  
            
         
        """
        pass
    def GetThickness(self) -> NXOpen.Expression:
        """
         The thickness  of base lofted flange.Applicable only for Base lofted flange. Ignored for a Secondary Lofted Flange.
         Returns thickness ( NXOpen.Expression):  .
        """
        pass
    def ValidateBuilderData(self) -> int:
        """
         Verify user data validity.
                If the data is valid, returned value should be 0.
                
         Returns builder_data_validity (int):  Data Validity Flag.
        """
        pass
import NXOpen
import NXOpen.Features
class LouverBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a louver feature builder. """
    class DepthSideOptions(Enum):
        """
        Members Include: 
         |SectionNormalSide|  Material added on the side of the section normal. 
         |SectionReverseNormalSide|  Material added on the side opposite to that of the section normal. 

        """
        SectionNormalSide: int
        SectionReverseNormalSide: int
        @staticmethod
        def ValueOf(value: int) -> LouverBuilder.DepthSideOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class EndTypeOptions(Enum):
        """
        Members Include: 
         |Formed|  
         |Lanced|  

        """
        Formed: int
        Lanced: int
        @staticmethod
        def ValueOf(value: int) -> LouverBuilder.EndTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SectionSideOptions(Enum):
        """
        Members Include: 
         |Left|  Side pointed to by the inverse of the tangent cross normal vector 
         |Right|  Side pointed to by the tangent cross normal vector 

        """
        Left: int
        Right: int
        @staticmethod
        def ValueOf(value: int) -> LouverBuilder.SectionSideOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Depth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Depth
         Returns the depth of the louver   
            
         
        """
        pass
    @property
    def DepthSide(self) -> LouverBuilder.DepthSideOptions:
        """
        Getter for property: ( LouverBuilder.DepthSideOptions NXOpen.Featu) DepthSide
         Returns the depth side for the louver.  
          
                  
         
        """
        pass
    @DepthSide.setter
    def DepthSide(self, depth_side: LouverBuilder.DepthSideOptions):
        """
        Setter for property: ( LouverBuilder.DepthSideOptions NXOpen.Featu) DepthSide
         Returns the depth side for the louver.  
          
                  
         
        """
        pass
    @property
    def DieRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DieRadius
         Returns the die radius.  
           Not used if  NXOpen::Features::SheetMetal::LouverBuilder::IncludeRounding  is false.   
         
        """
        pass
    @property
    def EndType(self) -> LouverBuilder.EndTypeOptions:
        """
        Getter for property: ( LouverBuilder.EndTypeOptions NXOpen.Featu) EndType
         Returns the end type for the louver.  
           Select lanced end or formed end from  NXOpen::Features::SheetMetal::LouverBuilder::EndTypeOptions .
                  
         
        """
        pass
    @EndType.setter
    def EndType(self, end_type: LouverBuilder.EndTypeOptions):
        """
        Setter for property: ( LouverBuilder.EndTypeOptions NXOpen.Featu) EndType
         Returns the end type for the louver.  
           Select lanced end or formed end from  NXOpen::Features::SheetMetal::LouverBuilder::EndTypeOptions .
                  
         
        """
        pass
    @property
    def IncludeRounding(self) -> bool:
        """
        Getter for property: (bool) IncludeRounding
         Returns the option to round the edges of the louver using the die radius.  
           If this is false, then the value 
                    of  NXOpen::Features::SheetMetal::LouverBuilder::DieRadius  is not used.
                  
         
        """
        pass
    @IncludeRounding.setter
    def IncludeRounding(self, include_rounding: bool):
        """
        Setter for property: (bool) IncludeRounding
         Returns the option to round the edges of the louver using the die radius.  
           If this is false, then the value 
                    of  NXOpen::Features::SheetMetal::LouverBuilder::DieRadius  is not used.
                  
         
        """
        pass
    @property
    def MinimumToolClearance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumToolClearance
         Returns
                the minimum tool clearance expression.  
          
                   
                  
         
        """
        pass
    @property
    def Section(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Section
         Returns the section used by the louver.  
           The section should be open.  
         
        """
        pass
    @Section.setter
    def Section(self, section: NXOpen.Section):
        """
        Setter for property: ( NXOpen.Section) Section
         Returns the section used by the louver.  
           The section should be open.  
         
        """
        pass
    @property
    def SectionSide(self) -> LouverBuilder.SectionSideOptions:
        """
        Getter for property: ( LouverBuilder.SectionSideOptions NXOpen.Featu) SectionSide
         Returns the side of the section on which the louver is created and width is measure.  
           
                  
         
        """
        pass
    @SectionSide.setter
    def SectionSide(self, section_side: LouverBuilder.SectionSideOptions):
        """
        Setter for property: ( LouverBuilder.SectionSideOptions NXOpen.Featu) SectionSide
         Returns the side of the section on which the louver is created and width is measure.  
           
                  
         
        """
        pass
    @property
    def Sketch(self) -> NXOpen.Features.SketchFeature:
        """
        Getter for property: ( NXOpen.Features.SketchFeature) Sketch
         Returns the internal sketch used by the louver's section.  
          
                      
                        If the sketch is created internally as part of the louver command in the UI, then it 
                        is consumed by the louver and does not show up as a separate feature in the part navigator.
                        By setting the sketch object here, you will be making it internal to the louver feature. 
                      
                  
         
        """
        pass
    @Sketch.setter
    def Sketch(self, sketch: NXOpen.Features.SketchFeature):
        """
        Setter for property: ( NXOpen.Features.SketchFeature) Sketch
         Returns the internal sketch used by the louver's section.  
          
                      
                        If the sketch is created internally as part of the louver command in the UI, then it 
                        is consumed by the louver and does not show up as a separate feature in the part navigator.
                        By setting the sketch object here, you will be making it internal to the louver feature. 
                      
                  
         
        """
        pass
    @property
    def Width(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Width
         Returns the width of the louver.  
           The side of the section that the width is measured from depends on the 
                     value of the section side (see  NXOpen::Features::SheetMetal::LouverBuilder::SectionSide ).   
         
        """
        pass
    def ValidateBuilderData(self) -> int:
        """
         This method verifies that the builder data is valid for louver creation.
                    
                         If the builder data is valid, it returns a value of 0.
                    
                
         Returns valid (int):  data validity flag .
        """
        pass
import NXOpen
import NXOpen.Features
class MetaformBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a NXOpen.Features.Metaform builder
    """
    @property
    def AngularTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) AngularTolerance
         Returns the angular tolerance   
            
         
        """
        pass
    @property
    def ChordalTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ChordalTolerance
         Returns the chordal tolerance   
            
         
        """
        pass
    @property
    def ElasticModulus(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ElasticModulus
         Returns the elastic modulus   
            
         
        """
        pass
    @property
    def EndRegion(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) EndRegion
         Returns the end region Metaform feature will map geometry "From" surfaces "To" surfaces.  
           The End
                    Region defines the "To" surface.   
         
        """
        pass
    @property
    def HoleRemovalMinModulus(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) HoleRemovalMinModulus
         Returns the hole removal min modulus   
            
         
        """
        pass
    @property
    def InferThickness(self) -> bool:
        """
        Getter for property: (bool) InferThickness
         Returns the option to infer thickness from the Start Region.  
             
         
        """
        pass
    @InferThickness.setter
    def InferThickness(self, inferThickness: bool):
        """
        Setter for property: (bool) InferThickness
         Returns the option to infer thickness from the Start Region.  
             
         
        """
        pass
    @property
    def LinearTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LinearTolerance
         Returns the linear tolerance   
            
         
        """
        pass
    @property
    def NeutralFactor(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) NeutralFactor
         Returns the neutral factor   
            
         
        """
        pass
    @property
    def OutputLayer(self) -> int:
        """
        Getter for property: (int) OutputLayer
         Returns the output layer.  
           Layer on which the Transform Geometry will be created.   
         
        """
        pass
    @OutputLayer.setter
    def OutputLayer(self, outputLayer: int):
        """
        Setter for property: (int) OutputLayer
         Returns the output layer.  
           Layer on which the Transform Geometry will be created.   
         
        """
        pass
    @property
    def PoissonsRatio(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PoissonsRatio
         Returns the Poisson's ratio   
            
         
        """
        pass
    @property
    def RValue(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RValue
         Returns the r value   
            
         
        """
        pass
    @property
    def RemoveHoles(self) -> bool:
        """
        Getter for property: (bool) RemoveHoles
         Returns the remove holes   
            
         
        """
        pass
    @RemoveHoles.setter
    def RemoveHoles(self, removeHoles: bool):
        """
        Setter for property: (bool) RemoveHoles
         Returns the remove holes   
            
         
        """
        pass
    @property
    def ReverseThicknessDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseThicknessDirection
         Returns the thickness direction   
            
         
        """
        pass
    @ReverseThicknessDirection.setter
    def ReverseThicknessDirection(self, reverseThicknessDirection: bool):
        """
        Setter for property: (bool) ReverseThicknessDirection
         Returns the thickness direction   
            
         
        """
        pass
    @property
    def SMBoundaryConditions(self) -> SMBoundaryConditionBuilderList:
        """
        Getter for property: ( SMBoundaryConditionBuilderList NXOpen.Featu) SMBoundaryConditions
         Returns the boundary conditions   
            
         
        """
        pass
    @property
    def StartRegion(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) StartRegion
         Returns the start region.  
           Metaform feature will map geometry "From" surfaces "To" surfaces. The Start
                    Region defines the "From" surface.   
         
        """
        pass
    @property
    def TangentModulus(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TangentModulus
         Returns the tangent modulus   
            
         
        """
        pass
    @property
    def Thickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Thickness
         Returns the thickness   
            
         
        """
        pass
    @property
    def TransformGeometry(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) TransformGeometry
         Returns the transform geometry Metaform feature will map geometry "From" surfaces "To" surfaces.  
           The Start
                    Region defines the "From" surface and the End Region defines the "To" surface. Transform Geometry 
                    is the actual geometry on the "From" surfaces that will be produced as output geometry.
                  
         
        """
        pass
    @property
    def YieldStress(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) YieldStress
         Returns the yield stress   
            
         
        """
        pass
    def CreateSMBoundaryCondition(self) -> SMBoundaryConditionBuilder:
        """
         Create a new boundary condition. 
         Returns listitem ( SMBoundaryConditionBuilder NXOpen.Featu): .
        """
        pass
import NXOpen
import NXOpen.Features
class MigratedPanelBuilder(NXOpen.Features.FeatureBuilder): 
    """
        Represents an I-DEAS Migrated Panel feature builder
    """
    @property
    def AlongFaceNormal(self) -> bool:
        """
        Getter for property: (bool) AlongFaceNormal
         Returns
                 the along face normal flag.  
           This value only has meaning
                 for the ground panel.
                   
                  The edge that defines an end condition must be linear and must be on the
                  stationary face for the Ground Panel and the moving face for other panels.
                  The index indicates the position of the End Condition that will be
                  modified.  The first End Condition has an index of zero.
                   
                
         
        """
        pass
    @AlongFaceNormal.setter
    def AlongFaceNormal(self, along_face_normal: bool):
        """
        Setter for property: (bool) AlongFaceNormal
         Returns
                 the along face normal flag.  
           This value only has meaning
                 for the ground panel.
                   
                  The edge that defines an end condition must be linear and must be on the
                  stationary face for the Ground Panel and the moving face for other panels.
                  The index indicates the position of the End Condition that will be
                  modified.  The first End Condition has an index of zero.
                   
                
         
        """
        pass
    @property
    def BendFace(self) -> NXOpen.Face:
        """
        Getter for property: ( NXOpen.Face) BendFace
         Returns
                  the parent bend face.  
            This face will usually be NULL.  It will
                  be non-NULL if this Migrated Panel was defined using the BFCS
                  (Bend From Cylindrical Surface) method.
                
                  The set method is only available inside the I-DEAS to NX Content Migration Manager.
                
                
         
        """
        pass
    @BendFace.setter
    def BendFace(self, bend_face: NXOpen.Face):
        """
        Setter for property: ( NXOpen.Face) BendFace
         Returns
                  the parent bend face.  
            This face will usually be NULL.  It will
                  be non-NULL if this Migrated Panel was defined using the BFCS
                  (Bend From Cylindrical Surface) method.
                
                  The set method is only available inside the I-DEAS to NX Content Migration Manager.
                
                
         
        """
        pass
    @property
    def BendOptions(self) -> BendOptions:
        """
        Getter for property: ( BendOptions NXOpen.Featu) BendOptions
         Returns the bend options for the panel feature.  
          
              
         
        """
        pass
    @property
    def BendRadius(self) -> str:
        """
        Getter for property: (str) BendRadius
         Returns
                 the bend radius expression.  
          
                
         
        """
        pass
    @BendRadius.setter
    def BendRadius(self, gap_tolerance: str):
        """
        Setter for property: (str) BendRadius
         Returns
                 the bend radius expression.  
          
                
         
        """
        pass
    @property
    def CutoffAngle(self) -> str:
        """
        Getter for property: (str) CutoffAngle
         Returns
                  the cutoff angle expression.  
          
                
         
        """
        pass
    @CutoffAngle.setter
    def CutoffAngle(self, cutoff_angle: str):
        """
        Setter for property: (str) CutoffAngle
         Returns
                  the cutoff angle expression.  
          
                
         
        """
        pass
    @property
    def EndConditions(self) -> NXOpen.ExpressionCollectorSet:
        """
        Getter for property: ( NXOpen.ExpressionCollectorSet) EndConditions
         Returns the end conditions   
            
         
        """
        pass
    @property
    def GapTolerance(self) -> str:
        """
        Getter for property: (str) GapTolerance
         Returns
                  the gap tolerance expression.  
            This is the size of the gap introduced
                  between this panel and neighboring features.
                
         
        """
        pass
    @GapTolerance.setter
    def GapTolerance(self, gap_tolerance: str):
        """
        Setter for property: (str) GapTolerance
         Returns
                  the gap tolerance expression.  
            This is the size of the gap introduced
                  between this panel and neighboring features.
                
         
        """
        pass
    @property
    def MovingFace(self) -> NXOpen.Face:
        """
        Getter for property: ( NXOpen.Face) MovingFace
         Returns
                  the parent moving face.  
            This face will be NULL for the ground panel.
                  If non-NULL, the face must be planar.
                
                  The set method is only available inside the I-DEAS to NX Content Migration Manager.
                
                
         
        """
        pass
    @MovingFace.setter
    def MovingFace(self, moving_face: NXOpen.Face):
        """
        Setter for property: ( NXOpen.Face) MovingFace
         Returns
                  the parent moving face.  
            This face will be NULL for the ground panel.
                  If non-NULL, the face must be planar.
                
                  The set method is only available inside the I-DEAS to NX Content Migration Manager.
                
                
         
        """
        pass
    @property
    def NeutralOffset(self) -> str:
        """
        Getter for property: (str) NeutralOffset
         Returns
                  the neutral offset (i.  
          e., K Factor) expression.
                
         
        """
        pass
    @NeutralOffset.setter
    def NeutralOffset(self, gap_tolerance: str):
        """
        Setter for property: (str) NeutralOffset
         Returns
                  the neutral offset (i.  
          e., K Factor) expression.
                
         
        """
        pass
    @property
    def ParentSmBody(self) -> NXOpen.Body:
        """
        Getter for property: ( NXOpen.Body) ParentSmBody
         Returns
                  the parent sheet metal body.  
            The Migrated Panel is applied to this
                  body.  The body must be made up of other Migrated Panel features. This
                  body will be NULL for the ground panel.
                
                  The set method is only available inside the I-DEAS to NX Content Migration Manager.
                
                
         
        """
        pass
    @ParentSmBody.setter
    def ParentSmBody(self, sheet_metal_body: NXOpen.Body):
        """
        Setter for property: ( NXOpen.Body) ParentSmBody
         Returns
                  the parent sheet metal body.  
            The Migrated Panel is applied to this
                  body.  The body must be made up of other Migrated Panel features. This
                  body will be NULL for the ground panel.
                
                  The set method is only available inside the I-DEAS to NX Content Migration Manager.
                
                
         
        """
        pass
    @property
    def StationaryFace(self) -> NXOpen.Face:
        """
        Getter for property: ( NXOpen.Face) StationaryFace
         Returns
                  the parent stationary face.  
            This face cannot be NULL.
                    
                      The set method is only available inside the I-DEAS to NX Content Migration Manager.
                    
                
         
        """
        pass
    @StationaryFace.setter
    def StationaryFace(self, stationary_face: NXOpen.Face):
        """
        Setter for property: ( NXOpen.Face) StationaryFace
         Returns
                  the parent stationary face.  
            This face cannot be NULL.
                    
                      The set method is only available inside the I-DEAS to NX Content Migration Manager.
                    
                
         
        """
        pass
import NXOpen
class MiterOptions(NXOpen.TaggedObject): 
    """ Represents a Miter Data Options builder. Mitre cut is essentially an end treatment to the contour flange feature,
        which shall prevent merginginterference with the existing or newly placed features in sheet metal."""
    class ClosedCornerTypeOptions(Enum):
        """
        Members Include: 
         |NotSet|  Corner is not closed
         |Open|  corner is open
         |Closed|  corner is closed completely
         |CircularCutout|  corner has a circular cutout in it
         |UCutout|  corner has a U shaped cutout in it
         |VCutout|  corner has a V shaped cutout in it

        """
        NotSet: int
        Open: int
        Closed: int
        CircularCutout: int
        UCutout: int
        VCutout: int
        @staticmethod
        def ValueOf(value: int) -> MiterOptions.ClosedCornerTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CornerTreatmentOriginTypeOptions(Enum):
        """
        Members Include: 
         |BendCenter|  The cutout origin will be at the intersection of first bend's centerline and bisector of corner angle. 
         |CornerPoint|  The cutout origin will be at the corner point.

        """
        BendCenter: int
        CornerPoint: int
        @staticmethod
        def ValueOf(value: int) -> MiterOptions.CornerTreatmentOriginTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PositionOptions(Enum):
        """
        Members Include: 
         |NotSet|  no miter 
         |Start|  miter is done at the beginning
         |End|  miter is done at the ending 
         |Both|  miter is done both at beginning and ending

        """
        NotSet: int
        Start: int
        End: int
        Both: int
        @staticmethod
        def ValueOf(value: int) -> MiterOptions.PositionOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TypeOptions(Enum):
        """
        Members Include: 
         |NormalToSourceFace|  mitering is done along the normal to source face
         |NormalToThicknessFace|  mitering is done along the normal to thickness face

        """
        NormalToSourceFace: int
        NormalToThicknessFace: int
        @staticmethod
        def ValueOf(value: int) -> MiterOptions.TypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BlendMiter(self) -> bool:
        """
        Getter for property: (bool) BlendMiter
         Returns the option that specifies whether to blend the sharp edges created by the miter   
            
         
        """
        pass
    @BlendMiter.setter
    def BlendMiter(self, blendMiter: bool):
        """
        Setter for property: (bool) BlendMiter
         Returns the option that specifies whether to blend the sharp edges created by the miter   
            
         
        """
        pass
    @property
    def ClosedCornerGap(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ClosedCornerGap
         Returns the corner gap used for a contour flange corner in case of a closed corner condition.  
           
                This applies for all treatment types in  Features::SheetMetal::MiterOptions::ClosedCornerTypeOptions 
                  
         
        """
        pass
    @property
    def ClosedCornerType(self) -> MiterOptions.ClosedCornerTypeOptions:
        """
        Getter for property: ( MiterOptions.ClosedCornerTypeOptions NXOpen.Featu) ClosedCornerType
         Returns the closed corner option type.  
            
         
        """
        pass
    @ClosedCornerType.setter
    def ClosedCornerType(self, cut_type: MiterOptions.ClosedCornerTypeOptions):
        """
        Setter for property: ( MiterOptions.ClosedCornerTypeOptions NXOpen.Featu) ClosedCornerType
         Returns the closed corner option type.  
            
         
        """
        pass
    @property
    def ClosedCornerVAngle1(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ClosedCornerVAngle1
         Returns the v cutout angle1 expression of the closed corner.  
           Applicable only when  NXOpen::Features::SheetMetal::MiterOptions::ClosedCornerTypeOptions 
                    is  Features::SheetMetal::MiterOptions::ClosedCornerTypeOptionsVCutout .  
         
        """
        pass
    @property
    def ClosedCornerVAngle2(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ClosedCornerVAngle2
         Returns the v cutout angle2 expression of the closed corner.  
           Applicable only when  NXOpen::Features::SheetMetal::MiterOptions::ClosedCornerTypeOptions 
                    is  Features::SheetMetal::MiterOptions::ClosedCornerTypeOptionsVCutout .  
         
        """
        pass
    @property
    def CornerTreatmentOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CornerTreatmentOffset
         Returns the offset used for circular, u and v cutout corner treatments.  
           This only applies when the treatment type is set to 
                     Features::SheetMetal::MiterOptions::ClosedCornerTypeOptionsCircularCutout  or 
                     Features::SheetMetal::MiterOptions::ClosedCornerTypeOptionsUCutout  or 
                     Features::SheetMetal::MiterOptions::ClosedCornerTypeOptionsVCutout .
                  
         
        """
        pass
    @property
    def CornerTreatmentOriginType(self) -> MiterOptions.CornerTreatmentOriginTypeOptions:
        """
        Getter for property: ( MiterOptions.CornerTreatmentOriginTypeOptions NXOpen.Featu) CornerTreatmentOriginType
         Returns the origin used for circular, u and v cutout corner treatments.  
           This only applies when the treatment type is set to 
                     Features::SheetMetal::MiterOptions::ClosedCornerTypeOptionsCircularCutout  or 
                     Features::SheetMetal::MiterOptions::ClosedCornerTypeOptionsUCutout  or 
                     Features::SheetMetal::MiterOptions::ClosedCornerTypeOptionsVCutout .
                  
         
        """
        pass
    @CornerTreatmentOriginType.setter
    def CornerTreatmentOriginType(self, originType: MiterOptions.CornerTreatmentOriginTypeOptions):
        """
        Setter for property: ( MiterOptions.CornerTreatmentOriginTypeOptions NXOpen.Featu) CornerTreatmentOriginType
         Returns the origin used for circular, u and v cutout corner treatments.  
           This only applies when the treatment type is set to 
                     Features::SheetMetal::MiterOptions::ClosedCornerTypeOptionsCircularCutout  or 
                     Features::SheetMetal::MiterOptions::ClosedCornerTypeOptionsUCutout  or 
                     Features::SheetMetal::MiterOptions::ClosedCornerTypeOptionsVCutout .
                  
         
        """
        pass
    @property
    def EndType(self) -> MiterOptions.TypeOptions:
        """
        Getter for property: ( MiterOptions.TypeOptions NXOpen.Featu) EndType
         Returns the miter end type.  
            
         
        """
        pass
    @EndType.setter
    def EndType(self, end_type: MiterOptions.TypeOptions):
        """
        Setter for property: ( MiterOptions.TypeOptions NXOpen.Featu) EndType
         Returns the miter end type.  
            
         
        """
        pass
    @property
    def MiterCorner(self) -> bool:
        """
        Getter for property: (bool) MiterCorner
         Returns the miter toggle value that specifies whether to miter the corner.  
          This only applies when the treatment type is set to 
                     Features::SheetMetal::MiterOptions::ClosedCornerTypeOptionsClosed  or
                     Features::SheetMetal::MiterOptions::ClosedCornerTypeOptionsCircularCutout  or 
                     Features::SheetMetal::MiterOptions::ClosedCornerTypeOptionsUCutout  or 
                     Features::SheetMetal::MiterOptions::ClosedCornerTypeOptionsVCutout .
                  
         
        """
        pass
    @MiterCorner.setter
    def MiterCorner(self, miterCorner: bool):
        """
        Setter for property: (bool) MiterCorner
         Returns the miter toggle value that specifies whether to miter the corner.  
          This only applies when the treatment type is set to 
                     Features::SheetMetal::MiterOptions::ClosedCornerTypeOptionsClosed  or
                     Features::SheetMetal::MiterOptions::ClosedCornerTypeOptionsCircularCutout  or 
                     Features::SheetMetal::MiterOptions::ClosedCornerTypeOptionsUCutout  or 
                     Features::SheetMetal::MiterOptions::ClosedCornerTypeOptionsVCutout .
                  
         
        """
        pass
    @property
    def MiterInteriorCornersIfNecessary(self) -> bool:
        """
        Getter for property: (bool) MiterInteriorCornersIfNecessary
         Returns the miter_corners option.  
          If set to true, it miter bend edges that are larger than default bend radius.  
         
        """
        pass
    @MiterInteriorCornersIfNecessary.setter
    def MiterInteriorCornersIfNecessary(self, miter_corners: bool):
        """
        Setter for property: (bool) MiterInteriorCornersIfNecessary
         Returns the miter_corners option.  
          If set to true, it miter bend edges that are larger than default bend radius.  
         
        """
        pass
    @property
    def MiterRootRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MiterRootRadius
         Returns the root radius used when mitering the corner.  
           This only applies when the treatment type is set to 
                     Features::SheetMetal::MiterOptions::ClosedCornerTypeOptionsClosed  or
                     Features::SheetMetal::MiterOptions::ClosedCornerTypeOptionsCircularCutout  or 
                     Features::SheetMetal::MiterOptions::ClosedCornerTypeOptionsUCutout  or 
                     Features::SheetMetal::MiterOptions::ClosedCornerTypeOptionsVCutout .
                  
         
        """
        pass
    @property
    def Position(self) -> MiterOptions.PositionOptions:
        """
        Getter for property: ( MiterOptions.PositionOptions NXOpen.Featu) Position
         Returns the position of miter.  
            
         
        """
        pass
    @Position.setter
    def Position(self, miter_position: MiterOptions.PositionOptions):
        """
        Setter for property: ( MiterOptions.PositionOptions NXOpen.Featu) Position
         Returns the position of miter.  
            
         
        """
        pass
    @property
    def StartType(self) -> MiterOptions.TypeOptions:
        """
        Getter for property: ( MiterOptions.TypeOptions NXOpen.Featu) StartType
         Returns the miter start type.  
            
         
        """
        pass
    @StartType.setter
    def StartType(self, start_type: MiterOptions.TypeOptions):
        """
        Setter for property: ( MiterOptions.TypeOptions NXOpen.Featu) StartType
         Returns the miter start type.  
            
         
        """
        pass
    @property
    def ThreeBendCornerFlangeClearance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ThreeBendCornerFlangeClearance
         Returns the flange clearance used for a contour flange corner in case of a three bend corner condition.  
           
                    This applies for all treatment types in  Features::SheetMetal::MiterOptions::ClosedCornerTypeOptions  
                  
         
        """
        pass
    @property
    def UseNormalCutoutMethod(self) -> bool:
        """
        Getter for property: (bool) UseNormalCutoutMethod
         Returns the cut type of the sheet.  
           If set to true, mitering is done using the normal cutout method and aims
                to reduce the small segements that result as part of miter computation, and is carried out on an unbent sheet.
                Normally, the cut runs through from one bend centre to another.  The sheet is later bent to achieve the desired result.
                This option is not applicable for feature created in NX1926 and above and set method will not do any operation  
         
        """
        pass
    @UseNormalCutoutMethod.setter
    def UseNormalCutoutMethod(self, cut_type: bool):
        """
        Setter for property: (bool) UseNormalCutoutMethod
         Returns the cut type of the sheet.  
           If set to true, mitering is done using the normal cutout method and aims
                to reduce the small segements that result as part of miter computation, and is carried out on an unbent sheet.
                Normally, the cut runs through from one bend centre to another.  The sheet is later bent to achieve the desired result.
                This option is not applicable for feature created in NX1926 and above and set method will not do any operation  
         
        """
        pass
    def GetClosedCornerDiameter(self) -> NXOpen.Expression:
        """
         The diameter expression of the closed corner. Applicable only when NXOpen.Features.SheetMetal.MiterOptions.ClosedCornerTypeOptions
                    is Features.SheetMetal.MiterOptions.ClosedCornerTypeOptions.CircularCutout or 
                    Features.SheetMetal.MiterOptions.ClosedCornerTypeOptions.UCutout or 
                    Features.SheetMetal.MiterOptions.ClosedCornerTypeOptions.VCutout.
         Returns end_value ( NXOpen.Expression):  .
        """
        pass
    def GetEndValue(self) -> NXOpen.Expression:
        """
         THE miter end value expression.
         Returns end_value ( NXOpen.Expression):  .
        """
        pass
    def GetStartValue(self) -> NXOpen.Expression:
        """
         THE miter start value expression.Positive value adds material and negative v
         Returns start_value ( NXOpen.Expression):  .
        """
        pass
    def SetClosedCornerDiameter(self, end_value: str) -> None:
        """
         
        """
        pass
import NXOpen
class MultiBendBendPropertiesBuilder(FeatureBendPropertiesBuilder): 
    """ Represents a Sheetmetal Multi Bend properties builder class. This builder is used to
    interrogate the properties of multiple bends in the list."""
    class Insets(Enum):
        """
        Members Include: 
         |MaterialInside| 
         |MaterialOutside| 

        """
        MaterialInside: int
        MaterialOutside: int
        @staticmethod
        def ValueOf(value: int) -> MultiBendBendPropertiesBuilder.Insets:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Inset(self) -> MultiBendBendPropertiesBuilder.Insets:
        """
        Getter for property: ( MultiBendBendPropertiesBuilder.Insets NXOpen.Featu) Inset
         Returns the inset   
            
         
        """
        pass
    @Inset.setter
    def Inset(self, inset: MultiBendBendPropertiesBuilder.Insets):
        """
        Setter for property: ( MultiBendBendPropertiesBuilder.Insets NXOpen.Featu) Inset
         Returns the inset   
            
         
        """
        pass
    @property
    def ParentPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) ParentPlane
         Returns the plane   
            
         
        """
        pass
    @ParentPlane.setter
    def ParentPlane(self, plane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) ParentPlane
         Returns the plane   
            
         
        """
        pass
    @property
    def Plane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) Plane
         Returns the plane   
            
         
        """
        pass
    @Plane.setter
    def Plane(self, plane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) Plane
         Returns the plane   
            
         
        """
        pass
    @property
    def SketchParentPlane(self) -> bool:
        """
        Getter for property: (bool) SketchParentPlane
         Returns the option to set sketch plane as parent   
            
         
        """
        pass
    @SketchParentPlane.setter
    def SketchParentPlane(self, isSketchPlaneParent: bool):
        """
        Setter for property: (bool) SketchParentPlane
         Returns the option to set sketch plane as parent   
            
         
        """
        pass
    def DeleteMultiBendBendProperties(self) -> None:
        """
         Deletes a multi bend properties. 
        """
        pass
class MultiBendBendPropertiesListBuilder(FeatureBendPropertiesListBuilder): 
    """ Represents a Sheetmetal Multi Bend properties List builder class. This builder is used to
    interrogate the properties list of multiple bends."""
    def CreateMultiBendBendProperties(self) -> MultiBendBendPropertiesBuilder:
        """
         Create a multi bend properties. 
         Returns listitem ( MultiBendBendPropertiesBuilder NXOpen.Featu): .
        """
        pass
import NXOpen
class MultiFlangeBuilder(SheetmetalBaseBuilder): 
    """
        Represents a Features.SheetMetal.MultiFlange builder
        """
    class MatchFaceOptions(Enum):
        """
        Members Include: 
         |NotSet| 
         |UntilSelected| 

        """
        NotSet: int
        UntilSelected: int
        @staticmethod
        def ValueOf(value: int) -> MultiFlangeBuilder.MatchFaceOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FlangePropertiesList(self) -> FeatureBendPropertiesListBuilder:
        """
        Getter for property: ( FeatureBendPropertiesListBuilder NXOpen.Featu) FlangePropertiesList
         Returns the flange properties list   
            
         
        """
        pass
    @property
    def MatchFace(self) -> MultiFlangeBuilder.MatchFaceOptions:
        """
        Getter for property: ( MultiFlangeBuilder.MatchFaceOptions NXOpen.Featu) MatchFace
         Returns the match face   
            
         
        """
        pass
    @MatchFace.setter
    def MatchFace(self, matchFace: MultiFlangeBuilder.MatchFaceOptions):
        """
        Setter for property: ( MultiFlangeBuilder.MatchFaceOptions NXOpen.Featu) MatchFace
         Returns the match face   
            
         
        """
        pass
    @property
    def MultiThicknessProperty(self) -> MultiThicknessBuilder:
        """
        Getter for property: ( MultiThicknessBuilder NXOpen.Featu) MultiThicknessProperty
         Returns the multi thickness property.  
             
         
        """
        pass
    @property
    def Plane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) Plane
         Returns the plane   
            
         
        """
        pass
    @Plane.setter
    def Plane(self, plane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) Plane
         Returns the plane   
            
         
        """
        pass
import NXOpen.Features
class MultiFlange(NXOpen.Features.Feature): 
    """ Represents a multi flange feature """
    pass
class MultiThicknessBuilder(SheetmetalComponentBuilder): 
    """ Represents a multi-thickness builder. """
    @property
    def MultiThicknessToggle(self) -> bool:
        """
        Getter for property: (bool) MultiThicknessToggle
         Returns the multi-thickness toggle.  
           This is applicable to base features only.   
         
        """
        pass
    @MultiThicknessToggle.setter
    def MultiThicknessToggle(self, toggle: bool):
        """
        Setter for property: (bool) MultiThicknessToggle
         Returns the multi-thickness toggle.  
           This is applicable to base features only.   
         
        """
        pass
    @property
    def ZoneName(self) -> str:
        """
        Getter for property: (str) ZoneName
         Returns the zone name.  
           This will be used only if
            ##  NXOpen.Features.SheetMetal.MultiTh is on.   
         
        """
        pass
    @ZoneName.setter
    def ZoneName(self, zoneName: str):
        """
        Setter for property: (str) ZoneName
         Returns the zone name.  
           This will be used only if
            ##  NXOpen.Features.SheetMetal.MultiTh is on.   
         
        """
        pass
import NXOpen
class NestingBuilder(NXOpen.Builder): 
    """ Represents a sheet metal nesting builder class. """
    class InputFileLoadStatus(Enum):
        """
        Members Include: 
         |Success| 
         |InvalidFile| 
         |InvalidFileUnit| 

        """
        Success: int
        InvalidFile: int
        InvalidFileUnit: int
        @staticmethod
        def ValueOf(value: int) -> NestingBuilder.InputFileLoadStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BestSolution(self) -> NXOpen.NestedSolution:
        """
        Getter for property: ( NXOpen.NestedSolution) BestSolution
         Returns the best  NXOpen::NestedSolution .  
          
                     Should be used only after calling  NestingBuilder::StartNesting .  
         
        """
        pass
    @property
    def DesiredSolution(self) -> NXOpen.NestedSolution:
        """
        Getter for property: ( NXOpen.NestedSolution) DesiredSolution
         Returns the best desired solution.  
          
                     Should be used only after calling  NestingBuilder::StartNesting .  
         
        """
        pass
    @DesiredSolution.setter
    def DesiredSolution(self, desiredSolution: NXOpen.NestedSolution):
        """
        Setter for property: ( NXOpen.NestedSolution) DesiredSolution
         Returns the best desired solution.  
          
                     Should be used only after calling  NestingBuilder::StartNesting .  
         
        """
        pass
    @property
    def NestingSettings(self) -> NXOpen.NestingSettings:
        """
        Getter for property: ( NXOpen.NestingSettings) NestingSettings
         Returns the nesting settings.  
             
         
        """
        pass
    def CreateNestingPart(self, partFilePath: str, includeSubAssembly: bool) -> NXOpen.NestingPart:
        """
         Creates a NXOpen.NestingPart. 
         Returns nestingPart ( NXOpen.NestingPart): .
        """
        pass
    def CreateNestingStock(self, length: float, width: float, thickness: float) -> NXOpen.NestingStock:
        """
         Creates a NXOpen.NestingStock. 
         Returns nestingStock ( NXOpen.NestingStock): .
        """
        pass
    def CreateStandardNestingStock(self, stockName: str) -> NXOpen.NestingStock:
        """
         Creates a NXOpen.NestingStock from given standard stock name. 
         Returns nestingStock ( NXOpen.NestingStock): .
        """
        pass
    def CreateUserDefinedNestingStock(self, thickness: float, fileLocation: str) -> NXOpen.NestingStock:
        """
         Creates a NXOpen.NestingStock from given user defined file. 
         Returns nestingStock ( NXOpen.NestingStock): .
        """
        pass
    def GetNestedSolution(self, identifier: int) -> NXOpen.NestedSolution:
        """
         Returns the nested solution with given identifier.
                     Should be used only after calling NestingBuilder.StartNesting.
         Returns nestingSolution ( NXOpen.NestedSolution): .
        """
        pass
    def GetNestedSolutions(self) -> List[NXOpen.NestedSolution]:
        """
         Returns a list of NXOpen.NestedSolution.
                     Should be used only after calling NestingBuilder.StartNesting.
         Returns nestedSolutions ( NXOpen.NestedSolution Li): .
        """
        pass
    def GetPart(self, identifier: str) -> NXOpen.NestingPart:
        """
         Returns the NXOpen.NestingPart for given identifier. 
         Returns nestingPart ( NXOpen.NestingPart): .
        """
        pass
    def GetParts(self) -> List[NXOpen.NestingPart]:
        """
         Returns a list of NXOpen.NestingPart. 
         Returns parts ( NXOpen.NestingPart Li): .
        """
        pass
    def GetStock(self, identifier: str) -> NXOpen.NestingStock:
        """
         Returns the NXOpen.NestingStock for given identifier. 
         Returns nestingStock ( NXOpen.NestingStock): .
        """
        pass
    def GetStocks(self) -> List[NXOpen.NestingStock]:
        """
         Returns a list of NXOpen.NestingStock. 
         Returns stocks ( NXOpen.NestingStock Li): .
        """
        pass
    def IncludeRemnants(self) -> None:
        """
         Includes all the remnants for driving stock. 
        """
        pass
    def LoadInputsFromFile(self, filePath: str) -> NestingBuilder.InputFileLoadStatus:
        """
         Loads all the inputs from given JSON file. 
         Returns status ( NestingBuilder.InputFileLoadStatus NXOpen.Featu): .
        """
        pass
    def RemovePart(self, nestingPart: NXOpen.NestingStock) -> None:
        """
         Removes given nesting part. 
        """
        pass
    def RemoveStock(self, nestingStock: NXOpen.NestingStock) -> None:
        """
         Removes given nesting stock. 
        """
        pass
    def SaveInputsToFile(self, filePath: str) -> bool:
        """
         Saves all the inputs to given file in JSON format. 
         Returns isSaved (bool): .
        """
        pass
    def StartNesting(self) -> None:
        """
         Starts the nesting process. 
        """
        pass
import NXOpen
import NXOpen.Features
class NormalCutoutBuilder(SheetmetalBaseBuilder): 
    """ Represents a NormalCutout feature builder. """
    class CutTypeOptions(Enum):
        """
        Members Include: 
         |ThicknessCut|  
         |MidPlaneCut|  
         |NearestFaceCut|  

        """
        ThicknessCut: int
        MidPlaneCut: int
        NearestFaceCut: int
        @staticmethod
        def ValueOf(value: int) -> NormalCutoutBuilder.CutTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DepthSideOptions(Enum):
        """
        Members Include: 
         |SectionNormalSide|  Material removed on the side of the section normal. 
         |SectionReverseNormalSide|  Material removed on the side opposite to that of the section normal 
         |Symmetric|  Material removed in both directions equally. Only applies when the depth type is NXOpen.Features.SheetMetal.NormalCutoutBuilder.DepthTypeOptions.Finite. 

        """
        SectionNormalSide: int
        SectionReverseNormalSide: int
        Symmetric: int
        @staticmethod
        def ValueOf(value: int) -> NormalCutoutBuilder.DepthSideOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DepthTypeOptions(Enum):
        """
        Members Include: 
         |Finite|  Finite 
         |FromTo|  From To 
         |ThroughNext|  Though Next 
         |ThroughAll|  Through All 

        """
        Finite: int
        FromTo: int
        ThroughNext: int
        ThroughAll: int
        @staticmethod
        def ValueOf(value: int) -> NormalCutoutBuilder.DepthTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SectionSideOptions(Enum):
        """
        Members Include: 
         |Left|  Side pointed to by the inverse of the tangent cross normal vector 
         |Right|  Side pointed to by the tangent cross normal vector 

        """
        Left: int
        Right: int
        @staticmethod
        def ValueOf(value: int) -> NormalCutoutBuilder.SectionSideOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TypeOptions(Enum):
        """
        Members Include: 
         |SketchType|  Sketch type normal cutout 
         |NonPlanarCurveType|  3D curves type normal cutout  

        """
        SketchType: int
        NonPlanarCurveType: int
        @staticmethod
        def ValueOf(value: int) -> NormalCutoutBuilder.TypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CutType(self) -> NormalCutoutBuilder.CutTypeOptions:
        """
        Getter for property: ( NormalCutoutBuilder.CutTypeOptions NXOpen.Featu) CutType
         Returns the cut type for the normal cutout.  
           The options are in  NXOpen::Features::SheetMetal::NormalCutoutBuilder::CutTypeOptions .
                  
         
        """
        pass
    @CutType.setter
    def CutType(self, cut_type: NormalCutoutBuilder.CutTypeOptions):
        """
        Setter for property: ( NormalCutoutBuilder.CutTypeOptions NXOpen.Featu) CutType
         Returns the cut type for the normal cutout.  
           The options are in  NXOpen::Features::SheetMetal::NormalCutoutBuilder::CutTypeOptions .
                  
         
        """
        pass
    @property
    def Depth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Depth
         Returns the depth of the cutout.  
           Only applies when the depth type is  NXOpen::Features::SheetMetal::NormalCutoutBuilder::DepthTypeOptionsFinite .  
         
        """
        pass
    @property
    def DepthSide(self) -> NormalCutoutBuilder.DepthSideOptions:
        """
        Getter for property: ( NormalCutoutBuilder.DepthSideOptions NXOpen.Featu) DepthSide
         Returns the depth side for the normal cutout.  
           The options are in  NXOpen::Features::SheetMetal::NormalCutoutBuilder::DepthSideOptions .
                  
         
        """
        pass
    @DepthSide.setter
    def DepthSide(self, depth_side: NormalCutoutBuilder.DepthSideOptions):
        """
        Setter for property: ( NormalCutoutBuilder.DepthSideOptions NXOpen.Featu) DepthSide
         Returns the depth side for the normal cutout.  
           The options are in  NXOpen::Features::SheetMetal::NormalCutoutBuilder::DepthSideOptions .
                  
         
        """
        pass
    @property
    def DepthType(self) -> NormalCutoutBuilder.DepthTypeOptions:
        """
        Getter for property: ( NormalCutoutBuilder.DepthTypeOptions NXOpen.Featu) DepthType
         Returns the depth type for the normal cutout.  
           The options are in  NXOpen::Features::SheetMetal::NormalCutoutBuilder::DepthTypeOptions .
                  
         
        """
        pass
    @DepthType.setter
    def DepthType(self, type: NormalCutoutBuilder.DepthTypeOptions):
        """
        Setter for property: ( NormalCutoutBuilder.DepthTypeOptions NXOpen.Featu) DepthType
         Returns the depth type for the normal cutout.  
           The options are in  NXOpen::Features::SheetMetal::NormalCutoutBuilder::DepthTypeOptions .
                  
         
        """
        pass
    @property
    def From(self) -> NXOpen.ISurface:
        """
        Getter for property: ( NXOpen.ISurface) From
         Returns the face or datum plane from which the cutout begins.  
           This is only applicable if the depth type
                    is  NXOpen::Features::SheetMetal::NormalCutoutBuilder::DepthTypeOptionsFromTo    
         
        """
        pass
    @From.setter
    def From(self, ffrom: NXOpen.ISurface):
        """
        Setter for property: ( NXOpen.ISurface) From
         Returns the face or datum plane from which the cutout begins.  
           This is only applicable if the depth type
                    is  NXOpen::Features::SheetMetal::NormalCutoutBuilder::DepthTypeOptionsFromTo    
         
        """
        pass
    @property
    def Section(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Section
         Returns the section used by the normal cutout.  
           It can be open or closed.  
         
        """
        pass
    @Section.setter
    def Section(self, section: NXOpen.Section):
        """
        Setter for property: ( NXOpen.Section) Section
         Returns the section used by the normal cutout.  
           It can be open or closed.  
         
        """
        pass
    @property
    def SectionSide(self) -> NormalCutoutBuilder.SectionSideOptions:
        """
        Getter for property: ( NormalCutoutBuilder.SectionSideOptions NXOpen.Featu) SectionSide
         Returns the side of the section that the normal cutout removes material.  
           The options are in  NXOpen::Features::SheetMetal::NormalCutoutBuilder::SectionSideOptions .
                  
         
        """
        pass
    @SectionSide.setter
    def SectionSide(self, section_side: NormalCutoutBuilder.SectionSideOptions):
        """
        Setter for property: ( NormalCutoutBuilder.SectionSideOptions NXOpen.Featu) SectionSide
         Returns the side of the section that the normal cutout removes material.  
           The options are in  NXOpen::Features::SheetMetal::NormalCutoutBuilder::SectionSideOptions .
                  
         
        """
        pass
    @property
    def Sketch(self) -> NXOpen.Features.SketchFeature:
        """
        Getter for property: ( NXOpen.Features.SketchFeature) Sketch
         Returns the internal sketch used by the normal cutout, if it exists.  
          
                  
         
        """
        pass
    @Sketch.setter
    def Sketch(self, sketch: NXOpen.Features.SketchFeature):
        """
        Setter for property: ( NXOpen.Features.SketchFeature) Sketch
         Returns the internal sketch used by the normal cutout, if it exists.  
          
                  
         
        """
        pass
    @property
    def TargetBody(self) -> NXOpen.Body:
        """
        Getter for property: ( NXOpen.Body) TargetBody
         Returns the target body on which the normal cutout is created.  
             
         
        """
        pass
    @TargetBody.setter
    def TargetBody(self, targetBody: NXOpen.Body):
        """
        Setter for property: ( NXOpen.Body) TargetBody
         Returns the target body on which the normal cutout is created.  
             
         
        """
        pass
    @property
    def To(self) -> NXOpen.ISurface:
        """
        Getter for property: ( NXOpen.ISurface) To
         Returns the face or datum plane at which the cutout ends.  
           This is only applicable if the depth type
                    is  NXOpen::Features::SheetMetal::NormalCutoutBuilder::DepthTypeOptionsFromTo    
         
        """
        pass
    @To.setter
    def To(self, to: NXOpen.ISurface):
        """
        Setter for property: ( NXOpen.ISurface) To
         Returns the face or datum plane at which the cutout ends.  
           This is only applicable if the depth type
                    is  NXOpen::Features::SheetMetal::NormalCutoutBuilder::DepthTypeOptionsFromTo    
         
        """
        pass
    @property
    def Type(self) -> NormalCutoutBuilder.TypeOptions:
        """
        Getter for property: ( NormalCutoutBuilder.TypeOptions NXOpen.Featu) Type
         Returns the type for the normal cutout.  
           The options are in  NXOpen::Features::SheetMetal::NormalCutoutBuilder::TypeOptions .
                  
         
        """
        pass
    @Type.setter
    def Type(self, type: NormalCutoutBuilder.TypeOptions):
        """
        Setter for property: ( NormalCutoutBuilder.TypeOptions NXOpen.Featu) Type
         Returns the type for the normal cutout.  
           The options are in  NXOpen::Features::SheetMetal::NormalCutoutBuilder::TypeOptions .
                  
         
        """
        pass
    def ValidateBuilderData(self) -> int:
        """
         Verify that the builder data is valid for creating a normal cutout. 
                    
                         If the builder data is valid, a value of 0 is returned.
                    
                
         Returns builder_data_validity (int):  data validity flag (zero is valid, non-zero is invalid).
        """
        pass
import NXOpen
class RebendBuilder(SheetmetalBaseBuilder): 
    """ The Rebend feature class."""
    @property
    def FaceCollector(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FaceCollector
         Returns the unbent faces to rebend   
            
         
        """
        pass
    @FaceCollector.setter
    def FaceCollector(self, face_collector: NXOpen.ScCollector):
        """
        Setter for property: ( NXOpen.ScCollector) FaceCollector
         Returns the unbent faces to rebend   
            
         
        """
        pass
    @property
    def ReferenceEntity(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) ReferenceEntity
         Returns the non-thickness planar face or linear edge to remain fixed while part is rebent   
            
         
        """
        pass
    @ReferenceEntity.setter
    def ReferenceEntity(self, reference_entity: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) ReferenceEntity
         Returns the non-thickness planar face or linear edge to remain fixed while part is rebent   
            
         
        """
        pass
    def ValidateBuilderData(self) -> int:
        """
         Verify whether the builder data is valid for creating Rebend or not.
                    
                         If the Builder data is valid, returned value shall be 0
                    
                
         Returns validity_code (int): .
        """
        pass
import NXOpen
class ResizeBendAngleBuilder(SheetmetalBaseBuilder): 
    """
    Represents a NXOpen.Features.ResizeBendAngle builder
    """
    @property
    def Angle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Angle
         Returns  the bend angle   
            
         
        """
        pass
    @property
    def BendFace(self) -> NXOpen.SelectFace:
        """
        Getter for property: ( NXOpen.SelectFace) BendFace
         Returns  the bend face   
            
         
        """
        pass
    @property
    def KeepRadiusFixed(self) -> bool:
        """
        Getter for property: (bool) KeepRadiusFixed
         Returns the flag indicationg to keep radius fixed   
            
         
        """
        pass
    @KeepRadiusFixed.setter
    def KeepRadiusFixed(self, keepRadiusFixed: bool):
        """
        Setter for property: (bool) KeepRadiusFixed
         Returns the flag indicationg to keep radius fixed   
            
         
        """
        pass
    @property
    def ReferenceEdge(self) -> NXOpen.SelectEdge:
        """
        Getter for property: ( NXOpen.SelectEdge) ReferenceEdge
         Returns  the reference edge  
            
         
        """
        pass
    @property
    def ReferenceFace(self) -> NXOpen.SelectFace:
        """
        Getter for property: ( NXOpen.SelectFace) ReferenceFace
         Returns  the reference face  
            
         
        """
        pass
import NXOpen
class ResizeBendRadiusBuilder(SheetmetalBaseBuilder): 
    """
    Represents a ResizeBendRadius feature builder.
    """
    class BendReliefTypeOptions(Enum):
        """
        Members Include: 
         |Square| 
         |Round| 
         |NotSet| 

        """
        Square: int
        Round: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> ResizeBendRadiusBuilder.BendReliefTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |FixedFoldedLength| 
         |FixedUnfoldedLength| 

        """
        FixedFoldedLength: int
        FixedUnfoldedLength: int
        @staticmethod
        def ValueOf(value: int) -> ResizeBendRadiusBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BendFaces(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) BendFaces
         Returns the bend faces   
            
         
        """
        pass
    @property
    def BendRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BendRadius
         Returns the bend radius   
            
         
        """
        pass
    @property
    def BendReliefDepth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BendReliefDepth
         Returns the bend relief depth.  
          
                  
         
        """
        pass
    @property
    def BendReliefType(self) -> ResizeBendRadiusBuilder.BendReliefTypeOptions:
        """
        Getter for property: ( ResizeBendRadiusBuilder.BendReliefTypeOptions NXOpen.Featu) BendReliefType
         Returns the relief type for the resize bend radius feature.  
          The options are in  NXOpen::Features::SheetMetal::ResizeBendRadiusBuilder::BendReliefType .   
         
        """
        pass
    @property
    def BendReliefWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BendReliefWidth
         Returns the bend relief width.  
          
                  
         
        """
        pass
    @property
    def ReferenceEntity(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: ( NXOpen.SelectDisplayableObject) ReferenceEntity
         Returns the non-thickness planar face or linear edge to remain fixed while bend is resized   
            
         
        """
        pass
    @property
    def Type(self) -> ResizeBendRadiusBuilder.Types:
        """
        Getter for property: ( ResizeBendRadiusBuilder.Types NXOpen.Featu) Type
         Returns the feature type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: ResizeBendRadiusBuilder.Types):
        """
        Setter for property: ( ResizeBendRadiusBuilder.Types NXOpen.Featu) Type
         Returns the feature type   
            
         
        """
        pass
    def SetBendReliefType(self, bend_relief_type: ResizeBendRadiusBuilder.BendReliefTypeOptions) -> None:
        """
         
        """
        pass
import NXOpen
import NXOpen.Features
class ResizeNeutralFactorBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a Resize Neutral Factor Builder
    """
    @property
    def BendFaces(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) BendFaces
         Returns the bend face list provided by user   
            
         
        """
        pass
    @property
    def NeutralFactor(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) NeutralFactor
         Returns the neutral factor   
            
         
        """
        pass
    @property
    def UseGlobal(self) -> bool:
        """
        Getter for property: (bool) UseGlobal
         Returns the Use Global Neutral Factor toggle.  
             
         
        """
        pass
    @UseGlobal.setter
    def UseGlobal(self, useGlobal: bool):
        """
        Setter for property: (bool) UseGlobal
         Returns the Use Global Neutral Factor toggle.  
             
         
        """
        pass
import NXOpen.Features
class SheetmetalBaseBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a Sheet Metal Feature Builder to be used in the creation and modification of features. Feature Builders
    manage the steps needed to correctly create features on a part. 
    """
    def GetApplicationContext(self) -> ApplicationContext:
        """
         Get the application context. 
                     
                        This feature is available in more than one application and under different licenses. The enum NXOpen.Features.SheetMetal.ApplicationContext
                        contains a list of all sheet metal related applications and a feature might be available in one or more applications listed there. 
                    
                
         Returns app_context ( ApplicationContext NXOpen.Featu): .
        """
        pass
    def SetApplicationContext(self, app_context: ApplicationContext) -> None:
        """
         Set the application context. This should be called immediately after creating the feature builder.
                
        """
        pass
class SheetmetalBendParameters:
    """
     This structure contains the bend parameters for a Sheet Metal bend area. 
    """
    @property
    def InnerRadius(self) -> float:
        """
        Getter for property InnerRadius
        Inner Bend Radius.

        """
        pass
    @InnerRadius.setter
    def InnerRadius(self, value: float):
        """
        Getter for property InnerRadius
        Inner Bend Radius.
        Setter for property InnerRadius
        Inner Bend Radius.

        """
        pass
    @property
    def NeutralFactor(self) -> float:
        """
        Getter for property NeutralFactor
        Neutral factor value.

        """
        pass
    @NeutralFactor.setter
    def NeutralFactor(self, value: float):
        """
        Getter for property NeutralFactor
        Neutral factor value.
        Setter for property NeutralFactor
        Neutral factor value.

        """
        pass
    @property
    def BendAngle(self) -> float:
        """
        Getter for property BendAngle
        Bend Angle

        """
        pass
    @BendAngle.setter
    def BendAngle(self, value: float):
        """
        Getter for property BendAngle
        Bend Angle
        Setter for property BendAngle
        Bend Angle

        """
        pass
    @property
    def BendState(self) -> SheetmetalBendState:
        """
        Getter for property BendState
        Bend Face is flat or bent

        """
        pass
    @BendState.setter
    def BendState(self, value: SheetmetalBendState):
        """
        Getter for property BendState
        Bend Face is flat or bent
        Setter for property BendState
        Bend Face is flat or bent

        """
        pass
class SheetmetalBendState(Enum):
    """
    Members Include: 
     |Unknown| 
     |Bent| 
     |Flat| 

    """
    Unknown: int
    Bent: int
    Flat: int
    @staticmethod
    def ValueOf(value: int) -> SheetmetalBendState:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SheetmetalComponentBuilder(NXOpen.TaggedObject): 
    """
        Represents a sheet metal component builder to be used in the creation and modification of features componenets. Component builders
        manage the steps needed to correctly create features components on a feature. 
        """
    def GetApplicationContext(self) -> ApplicationContext:
        """
         Get the application context. 
                         
                            This component is available in more than one application and under different licenses. The enum NXOpen.Features.SheetMetal.ApplicationContext
                            contains a list of all sheet metal related applications and a component might be available in one or more applications listed there. 
                        
                    
         Returns appContext ( ApplicationContext NXOpen.Featu): .
        """
        pass
    def SetApplicationContext(self, appContext: ApplicationContext) -> None:
        """
         Set the application context. 
                    
        """
        pass
class SheetmetalFaceLayer(Enum):
    """
    Members Include: 
     |Unknown| 
     |Top| 
     |Bottom| 

    """
    Unknown: int
    Top: int
    Bottom: int
    @staticmethod
    def ValueOf(value: int) -> SheetmetalFaceLayer:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class SheetmetalFaceType(Enum):
    """
    Members Include: 
     |Unknown| 
     |Web| 
     |Bend| 
     |Deform| 
     |Thickness| 

    """
    Unknown: int
    Web: int
    Bend: int
    Deform: int
    Thickness: int
    @staticmethod
    def ValueOf(value: int) -> SheetmetalFaceType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class SheetMetalFromSolidBendPropertiesBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[SheetMetalFromSolidBendPropertiesBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: SheetMetalFromSolidBendPropertiesBuilder) -> None:
        """
         Appends an object to the list
            
        """
        pass
    @overload
    def Clear(self) -> None:
        """
         Clears the entire list without deleting the objects.  The caller is responsible for 
                accounting for these objects.  If they are not used or deleted by the time the part is 
                closed (in other words, leaked) an error will occur 
        """
        pass
    def ClearIndex(self, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
               not change, but the item at this index is set to NULL.
            
        """
        pass
    @overload
    def Clear(self, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    @overload
    def Erase(self, index: int) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, obj: SheetMetalFromSolidBendPropertiesBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: SheetMetalFromSolidBendPropertiesBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: SheetMetalFromSolidBendPropertiesBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> SheetMetalFromSolidBendPropertiesBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( SheetMetalFromSolidBendPropertiesBuilder NXOpen.Featu):  object found at input index .
        """
        pass
    def GetContents(self) -> List[SheetMetalFromSolidBendPropertiesBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( SheetMetalFromSolidBendPropertiesBuilder List[NXOpen.Fea):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: SheetMetalFromSolidBendPropertiesBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    def MoveToBottom(self, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    def MoveToTop(self, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    def SetContents(self, objects: List[SheetMetalFromSolidBendPropertiesBuilder]) -> None:
        """
         Sets the contents of the entire list. This overwrites the previous contents of this list, 
                but does not delete any objects that were originally on the list.
             
        """
        pass
    @overload
    def Swap(self, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    @overload
    def Swap(self, object1: SheetMetalFromSolidBendPropertiesBuilder, object2: SheetMetalFromSolidBendPropertiesBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SheetMetalFromSolidBendPropertiesBuilder(NXOpen.TaggedObject): 
    """ Represents a Sheetmetal From Solid Bend properties builder class. This builder is used to
    interrogate the sheet metal from properties in the list."""
    @property
    def BendEdges(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) BendEdges
         Returns the bend edges   
            
         
        """
        pass
    @property
    def BendOptions(self) -> BendOptions:
        """
        Getter for property: ( BendOptions NXOpen.Featu) BendOptions
         Returns the sheet metal bend options   
            
         
        """
        pass
    def DeleteBendProperties(self) -> None:
        """
         Delete bend properties. 
        """
        pass
import NXOpen
class SheetMetalFromSolidBuilder(SheetmetalBaseBuilder): 
    """
    Represents a NXOpen.Features.SheetMetalFromSolid builder
    (Sheet Metal from Solid).
    """
    @property
    def BendEdges(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) BendEdges
         Returns the bend edges   
            
         
        """
        pass
    @property
    def BendOptions(self) -> BendOptions:
        """
        Getter for property: ( BendOptions NXOpen.Featu) BendOptions
         Returns the bend options   
            
         
        """
        pass
    @property
    def BendPropertiesList(self) -> SheetMetalFromSolidBendPropertiesBuilderList:
        """
        Getter for property: ( SheetMetalFromSolidBendPropertiesBuilderList NXOpen.Featu) BendPropertiesList
         Returns the bend properties list   
            
         
        """
        pass
    @property
    def HideOriginal(self) -> bool:
        """
        Getter for property: (bool) HideOriginal
         Returns the hide original   
            
         
        """
        pass
    @HideOriginal.setter
    def HideOriginal(self, hideOriginal: bool):
        """
        Setter for property: (bool) HideOriginal
         Returns the hide original   
            
         
        """
        pass
    @property
    def ReverseDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseDirection
         Returns the reverse direction   
            
         
        """
        pass
    @ReverseDirection.setter
    def ReverseDirection(self, reverseDirection: bool):
        """
        Setter for property: (bool) ReverseDirection
         Returns the reverse direction   
            
         
        """
        pass
    @property
    def Thickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Thickness
         Returns the thickness   
            
         
        """
        pass
    @property
    def UseGlobalThickness(self) -> bool:
        """
        Getter for property: (bool) UseGlobalThickness
         Returns the use global thickness   
            
         
        """
        pass
    @UseGlobalThickness.setter
    def UseGlobalThickness(self, useGlobalThickness: bool):
        """
        Setter for property: (bool) UseGlobalThickness
         Returns the use global thickness   
            
         
        """
        pass
    @property
    def WebFaces(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) WebFaces
         Returns the web faces   
            
         
        """
        pass
    def CreateSheetMetalFromSolidBendProperties(self) -> SheetMetalFromSolidBendPropertiesBuilder:
        """
         Create a bend properties. 
         Returns listitem ( SheetMetalFromSolidBendPropertiesBuilder NXOpen.Featu): .
        """
        pass
    def GetAutomaticBendEdges(self) -> List[NXOpen.Edge]:
        """
         Get the automatic bend edges 
         Returns automatic_edges ( NXOpen.Edge Li):  .
        """
        pass
    def GetCandidateBendEdges(self) -> List[NXOpen.Edge]:
        """
         Get the candidate bend edges 
         Returns candidate_edges ( NXOpen.Edge Li):  .
        """
        pass
class SheetmetalManagerFlangeWidthOption(Enum):
    """
    Members Include: 
     |CustomizeWidth|  customize width
     |FullWidth|  full width
     |Centred|  centred 
     |AtEnd|  at end
     |FromBothEnds|  from both ends
     |FromEnd|  from end

    """
    CustomizeWidth: int
    FullWidth: int
    Centred: int
    AtEnd: int
    FromBothEnds: int
    FromEnd: int
    @staticmethod
    def ValueOf(value: int) -> SheetmetalManagerFlangeWidthOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class SheetmetalManagerTabSweepDir(Enum):
    """
    Members Include: 
     |Normal|  Tab sweep direction along normal direction 
     |OppositeToNormal|  Tab sweep direction opposite to normal direction 

    """
    Normal: int
    OppositeToNormal: int
    @staticmethod
    def ValueOf(value: int) -> SheetmetalManagerTabSweepDir:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class SheetmetalManagerTabType(Enum):
    """
    Members Include: 
     |Base|  base tab 
     |Secondary|  secondary tab 

    """
    Base: int
    Secondary: int
    @staticmethod
    def ValueOf(value: int) -> SheetmetalManagerTabType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.Annotations
import NXOpen.Features
class SheetmetalManager(NXOpen.Object): 
    """ Represents an object that manages sheetmetal features """
    def CreateAdvancedFlangeBuilder(self, joggle: NXOpen.Features.Feature) -> AdvancedFlangeBuilder:
        """
         Creates a NXOpen.Features.SheetMetal.AdvancedFlangeBuilder 
         Returns builder ( AdvancedFlangeBuilder NXOpen.Featu): .
        """
        pass
    def CreateAssociateObjectBuilder(self, associateObject: NXOpen.Features.Feature) -> AssociateObjectBuilder:
        """
         Creates a Features.SheetMetal.AssociateObjectBuilder 
         Returns builder ( AssociateObjectBuilder NXOpen.Featu):  .
        """
        pass
    def CreateBeadFeatureBuilder(self, bead: NXOpen.Features.Feature) -> BeadBuilder:
        """
         Create a NXSM Bead feature Builder
         Returns beadBuilder ( BeadBuilder NXOpen.Featu):  BeadBuilder object .
        """
        pass
    def CreateBendFeatureBuilder(self, bend: NXOpen.Features.Feature) -> BendBuilder:
        """
         Create a NXSM Bend feature Builder
         Returns builder ( BendBuilder NXOpen.Featu):  Bend object .
        """
        pass
    def CreateBendListBuilder(self) -> BendListBuilder:
        """
         Creates a NXOpen.Features.SheetMetal.BendListBuilder 
         Returns builder ( BendListBuilder NXOpen.Featu): .
        """
        pass
    def CreateBendListItemBuilder(self) -> BendListItemBuilder:
        """
         Creates a NXOpen.Features.SheetMetal.BendListItemBuilder 
                    BendListItemBuilder objects will be created and populated in the BendListBuilder when bend information of a flat pattern view is populated.
                    User should never need to create or delete BendListItemBuilder object on its own.
         Returns builder ( BendListItemBuilder NXOpen.Featu): .
        """
        pass
    def CreateBendTaperBuilder(self, bend_taper: NXOpen.Features.Feature) -> BendTaperBuilder:
        """
         Create a NXSM Bend taper feature Builder
         Returns builder ( BendTaperBuilder NXOpen.Featu):  Bend Taper object .
        """
        pass
    def CreateBreakCornerFeatureBuilder(self, brcorner: NXOpen.Features.Feature) -> BreakCornerBuilder:
        """
         Create a NXSM Break Corner feature Builder
         Returns sheet_metal_break_corner_builder ( BreakCornerBuilder NXOpen.Featu):  BrcornerBuilder object .
        """
        pass
    def CreateBridgeTransitionBuilder(self, transition: NXOpen.Features.Feature) -> BridgeTransitionBuilder:
        """
         Creates a NXOpen.Features.SheetMetal.BridgeTransitionBuilder 
         Returns builder ( BridgeTransitionBuilder NXOpen.Featu): Bridge Transition Builder.
        """
        pass
    def CreateBulgeReliefBuilder(self, bulgeRelief: NXOpen.Features.Feature) -> BulgeReliefBuilder:
        """
         Creates a NXOpen.Features.SheetMetal.BulgeReliefBuilder 
         Returns builder ( BulgeReliefBuilder NXOpen.Featu): .
        """
        pass
    def CreateCleanUpUtilityBuilder(self) -> CleanUpUtilityBuilder:
        """
         Creates a NXOpen.Features.SheetMetal.CleanUpUtilityBuilder 
         Returns builder ( CleanUpUtilityBuilder NXOpen.Featu):  Clean-Up Utility Builder object.
        """
        pass
    def CreateClosedCornerFeatureBuilder(self, closed_corner: NXOpen.Features.Feature) -> ClosedCornerBuilder:
        """
         Create a NXSM Closed Corner feature Builder
         Returns builder ( ClosedCornerBuilder NXOpen.Featu):  Closed Corner object .
        """
        pass
    def CreateContourFlangeFeatureBuilder(self, contour_flange: NXOpen.Features.Feature) -> ContourFlangeBuilder:
        """
         Create a NXSM Contour Flange feature Builder
         Returns builder ( ContourFlangeBuilder NXOpen.Featu):  ContourFlangeBuilder object .
        """
        pass
    def CreateConvertToSheetmetalFeatureBuilder(self, convert_to_sheet_metal: NXOpen.Features.Feature) -> ConvertToSheetmetalBuilder:
        """
         Create a NXSM Convert To Sheetmetal feature Builder
         Returns builder ( ConvertToSheetmetalBuilder NXOpen.Featu):  Convert To Sheetmetal Builder object .
        """
        pass
    def CreateDimpleFeatureBuilder(self, dimple: NXOpen.Features.Feature) -> DimpleBuilder:
        """
         Create a NXSM Dimple feature Builder
         Returns dimpleBuilder ( DimpleBuilder NXOpen.Featu):  DimpleBuilder object .
        """
        pass
    def CreateDrawnCutoutFeatureBuilder(self, d_cutout: NXOpen.Features.Feature) -> DrawnCutoutBuilder:
        """
         Create a NXSM Drawn Cutout feature Builder
         Returns builder ( DrawnCutoutBuilder NXOpen.Featu):  DrawnCutoutBuilder object .
        """
        pass
    def CreateEdgeRipFeatureBuilder(self, edge_rip: NXOpen.Features.Feature) -> EdgeRipBuilder:
        """
         Create a NXSM Edge Rip feature Builder
         Returns sheet_metal_edge_rip_builder ( EdgeRipBuilder NXOpen.Featu):  Edge Rip Builder object .
        """
        pass
    def CreateExportFlatPatternBuilder(self) -> ExportFlatPatternBuilder:
        """
         Creates a NXOpen.Features.SheetMetal.ExportFlatPatternBuilder 
         Returns builder ( ExportFlatPatternBuilder NXOpen.Featu): .
        """
        pass
    def CreateFlangeFeatureBuilder(self, d_cutout: NXOpen.Features.Feature) -> FlangeBuilder:
        """
         Create a NXSM Flange feature Builder
         Returns builder ( FlangeBuilder NXOpen.Featu):  FlangeBuilder object .
        """
        pass
    def CreateFlatPatternBuilder(self, flat_pattern: NXOpen.Features.Feature) -> FlatPatternBuilder:
        """
         Create a NXSM Flat Pattern feature Builder
         Returns builder ( FlatPatternBuilder NXOpen.Featu):  Flat Pattern object .
        """
        pass
    def CreateFlatSolidFeatureBuilder(self, flat_solid: NXOpen.Features.Feature) -> FlatSolidBuilder:
        """
         Create a NXSM Flat Solid feature Builder
         Returns builder ( FlatSolidBuilder NXOpen.Featu):  Flat Solid object .
        """
        pass
    def CreateFlexibleCableBuilder(self, flexible_cable: NXOpen.Features.Feature) -> FlexibleCableBuilder:
        """
         Creates a NXOpen.Features.SheetMetal.FlexibleCableBuilder 
         Returns builder ( FlexibleCableBuilder NXOpen.Featu): Flexible Cable Builder object.
        """
        pass
    def CreateGussetBuilder(self, gusset: NXOpen.Features.Feature) -> GussetBuilder:
        """
         Creates a NXOpen.Features.SheetMetal.GussetBuilder 
         Returns builder ( GussetBuilder NXOpen.Featu):  Gusset Builder object.
        """
        pass
    def CreateHemFlangeFeatureBuilder(self, hem_falnge: NXOpen.Features.Feature) -> HemFlangeBuilder:
        """
         Create hem flange feature builder 
         Returns builder ( HemFlangeBuilder NXOpen.Featu):  Hem Flange Builder object.
        """
        pass
    def CreateJogFeatureBuilder(self, jog: NXOpen.Features.Feature) -> JogBuilder:
        """
         Create a NXSM Jog feature Builder
         Returns jog_builder ( JogBuilder NXOpen.Featu):  JogBuilder object .
        """
        pass
    def CreateJoggleBuilder(self, joggle: NXOpen.Features.Feature) -> JoggleBuilder:
        """
         Creates a NXOpen.Features.SheetMetal.JoggleBuilder 
         Returns builder ( JoggleBuilder NXOpen.Featu): .
        """
        pass
    def CreateLighteningCutoutBuilder(self, lightening_cutout: LighteningCutout) -> LighteningCutoutBuilder:
        """
         Creates a Features.SheetMetal.LighteningCutoutBuilder 
         Returns builder ( LighteningCutoutBuilder NXOpen.Featu):  .
        """
        pass
    def CreateLoftedFlangeFeatureBuilder(self, lflange: NXOpen.Features.Feature) -> LoftedFlangeBuilder:
        """
         Create a NXSM Lofted Flange feature Builder
         Returns builder ( LoftedFlangeBuilder NXOpen.Featu):  LoftedFlangeBuilder object .
        """
        pass
    def CreateLouverFeatureBuilder(self, louver: NXOpen.Features.Feature) -> LouverBuilder:
        """
         Create a NXSM Louver feature Builder
         Returns louverBuilder ( LouverBuilder NXOpen.Featu):  LouverBuilder object .
        """
        pass
    def CreateMetaformBuilder(self, metaform: NXOpen.Features.Feature) -> MetaformBuilder:
        """
         Creates a NXOpen.Features.SheetMetal.MetaformBuilder 
         Returns builder ( MetaformBuilder NXOpen.Featu):  .
        """
        pass
    def CreateMigratedPanelFeatureBuilder(self, migrated_panel: NXOpen.Features.Feature) -> MigratedPanelBuilder:
        """
         Create a NXSM Migrated Panel feature Builder
         Returns builder ( MigratedPanelBuilder NXOpen.Featu):  Migrated Panel Builder object .
        """
        pass
    def CreateMultiFlangeBuilder(self, multiFlange: MultiFlange) -> MultiFlangeBuilder:
        """
         Creates a Features.SheetMetal.MultiFlangeBuilder 
         Returns builder ( MultiFlangeBuilder NXOpen.Featu):  .
        """
        pass
    def CreateNestingBuilder(self) -> NestingBuilder:
        """
         Creates a NXOpen.Features.SheetMetal.NestingBuilder 
         Returns builder ( NestingBuilder NXOpen.Featu): .
        """
        pass
    def CreateNormalCutoutFeatureBuilder(self, ncutout: NXOpen.Features.Feature) -> NormalCutoutBuilder:
        """
         Create a NXSM Normal Cutout feature Builder
         Returns normal_cutout_builder ( NormalCutoutBuilder NXOpen.Featu):  NormalCutoutBuilder object .
        """
        pass
    def CreateRebendFeatureBuilder(self, rebend: NXOpen.Features.Feature) -> RebendBuilder:
        """
         Create a NXSM Rebend feature builder
         Returns rebend_builder ( RebendBuilder NXOpen.Featu):  Rebend object.
        """
        pass
    def CreateResizeBendAngleBuilder(self, resize_bend_angle: NXOpen.Features.Feature) -> ResizeBendAngleBuilder:
        """
         Creates Resize Bend Angle Builder 
         Returns builder ( ResizeBendAngleBuilder NXOpen.Featu): Resize Bend Angle Builder object.
        """
        pass
    def CreateResizeBendRadiusFeatureBuilder(self, resize_bend_radius: NXOpen.Features.Feature) -> ResizeBendRadiusBuilder:
        """
         Create a Resize Bend Radius Builder
         Returns builder ( ResizeBendRadiusBuilder NXOpen.Featu):  ResizeBendRadius Builder object.
        """
        pass
    def CreateResizeNeutralFactorBuilder(self, resize_neutral_factor: NXOpen.Features.Feature) -> ResizeNeutralFactorBuilder:
        """
         Creates Resize Neutral Factor Builder 
         Returns builder ( ResizeNeutralFactorBuilder NXOpen.Featu):  .
        """
        pass
    def CreateSheetMetalFromSolidBuilder(self, sheet_metal_from_solid: NXOpen.Features.Feature) -> SheetMetalFromSolidBuilder:
        """
         Creates a NXOpen.Features.SheetMetal.SheetMetalFromSolidBuilder 
         Returns builder ( SheetMetalFromSolidBuilder NXOpen.Featu):  Sheet Metal from Solid Builder object.
        """
        pass
    def CreateSheetMetalPmiBuilder(self, annotation: NXOpen.Annotations.SimpleDraftingAid) -> NXOpen.Annotations.SheetMetalPMIBuilder:
        """
         Creates a Annotations.SheetMetalPMIBuilder 
         Returns builder ( NXOpen.Annotations.SheetMetalPMIBuilder): .
        """
        pass
    def CreateSolidPunchBuilder(self, solid_punch: NXOpen.Features.Feature) -> SolidPunchBuilder:
        """
         Creates a NXOpen.Features.SheetMetal.SolidPunchBuilder 
         Returns builder ( SolidPunchBuilder NXOpen.Featu):  .
        """
        pass
    def CreateTabFeatureBuilder(self, tab: NXOpen.Features.Feature) -> TabBuilder:
        """
         Create a NXSM Tab feature Builder
         Returns sheet_metal_tab_builder ( TabBuilder NXOpen.Featu):  TabBuilder object .
        """
        pass
    def CreateThreeBendCornerFeatureBuilder(self, three_bend_corner: NXOpen.Features.Feature) -> ThreeBendCornerBuilder:
        """
         Create a NXSM Three Bend Corner feature Builder
         Returns three_bend_corner_builder ( ThreeBendCornerBuilder NXOpen.Featu):  ThreeBendCornerBuilder object .
        """
        pass
    def CreateUnbendFeatureBuilder(self, unbend: NXOpen.Features.Feature) -> UnbendBuilder:
        """
         Create a NXSM Unbend feature builder
         Returns unbend_builder ( UnbendBuilder NXOpen.Featu):  Unbend object.
        """
        pass
    def CreateVariationalFlangeBuilder(self, variationalFlange: NXOpen.Features.Feature) -> VariationalFlangeBuilder:
        """
         Creates a NXOpen.Features.SheetMetal.VariationalFlangeBuilder 
         Returns builder ( VariationalFlangeBuilder NXOpen.Featu): .
        """
        pass
    def GetBendParameters(self, bendFace: NXOpen.Face) -> SheetmetalBendParameters:
        """
         Bend region parameters. The values are calculated from the inner face of bend region. The radius and angle values are returned in part units. This function will raise an exception of the face is not a valid bend face.
         Returns bendParameters ( SheetmetalBendParameters NXOpen.Featu): .
        """
        pass
    def GetBodyThickness(self, sheetmetalBody: NXOpen.Body) -> float:
        """
         Thickness of sheet metal body. Value is returned in part units. 
         Returns thicknessValue (float): Thickness Value.
        """
        pass
    def GetFaceLayer(self, inputFace: NXOpen.Face) -> SheetmetalFaceLayer:
        """
         Sheet metal face layer 
         Returns faceLayer ( SheetmetalFaceLayer NXOpen.Featu): Sheet Metal Face Layer.
        """
        pass
    def GetFaceType(self, inputFace: NXOpen.Face) -> SheetmetalFaceType:
        """
         Sheet metal face type 
         Returns faceType ( SheetmetalFaceType NXOpen.Featu): Sheet Metal Face Type.
        """
        pass
    def GetInnerBendFaces(self, sheetmetalBody: NXOpen.Body) -> Tuple[List[NXOpen.Face], List[SheetmetalBendState]]:
        """
         Get inner bend faces. For every bend the inner face is the face with smaller radius.
         Returns A tuple consisting of (innerBendFaces, bendStates). 
         - innerBendFaces is:  NXOpen.Face Li.Inner bend faces.
         - bendStates is:  SheetmetalBendState List[NXOpen.Fea.Bend Face is flat or bent.

        """
        pass
    def GetOppositeFace(self, inputFace: NXOpen.Face) -> NXOpen.Face:
        """
         Opposite face to bend, web or deform face. Will raise an exception if the input face is not a valid face.
         Returns oppositeFace ( NXOpen.Face): Opposite Layer Face.
        """
        pass
    def IsSheetmetalBody(self, inputBody: NXOpen.Body) -> bool:
        """
         Is a sheet metal body. This function will return True if the body has at least one NX Sheet Metal feature or
                        a Flexible Printed Circuit Design feature. 
         Returns isSheetmetalBody (bool): True = Body has NX Sheet Metal features or Flexible Printed Circuit Design features.
        """
        pass
    def IsThicknessEdge(self, inputEdge: NXOpen.Edge) -> bool:
        """
         Check if this edge is a thickness edge 
         Returns isThicknessEdge (bool): True = Thickness Edge.
        """
        pass
import NXOpen
class SMBoundaryConditionBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[SMBoundaryConditionBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: SMBoundaryConditionBuilder) -> None:
        """
         Appends an object to the list
            
        """
        pass
    @overload
    def Clear(self) -> None:
        """
         Clears the entire list without deleting the objects.  The caller is responsible for 
                accounting for these objects.  If they are not used or deleted by the time the part is 
                closed (in other words, leaked) an error will occur 
        """
        pass
    def ClearIndex(self, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
               not change, but the item at this index is set to NULL.
            
        """
        pass
    @overload
    def Clear(self, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    @overload
    def Erase(self, index: int) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, obj: SMBoundaryConditionBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: SMBoundaryConditionBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: SMBoundaryConditionBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> SMBoundaryConditionBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( SMBoundaryConditionBuilder NXOpen.Featu):  object found at input index .
        """
        pass
    def GetContents(self) -> List[SMBoundaryConditionBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( SMBoundaryConditionBuilder List[NXOpen.Fea):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: SMBoundaryConditionBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    def MoveToBottom(self, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    def MoveToTop(self, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    def SetContents(self, objects: List[SMBoundaryConditionBuilder]) -> None:
        """
         Sets the contents of the entire list. This overwrites the previous contents of this list, 
                but does not delete any objects that were originally on the list.
             
        """
        pass
    @overload
    def Swap(self, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    @overload
    def Swap(self, object1: SMBoundaryConditionBuilder, object2: SMBoundaryConditionBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SMBoundaryConditionBuilder(NXOpen.TaggedObject): 
    """ Represents a Boundary condition object for Metaform. A Metaform feature can have one or more boundary
        conditions and each condition determines how the mapped geometry will be locked. """
    class ConstraintTypes(Enum):
        """
        Members Include: 
         |PointToPoint| 
         |PointAlongCurve| 
         |CurveToCurve| 
         |CurveAlongCurve| 

        """
        PointToPoint: int
        PointAlongCurve: int
        CurveToCurve: int
        CurveAlongCurve: int
        @staticmethod
        def ValueOf(value: int) -> SMBoundaryConditionBuilder.ConstraintTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ConstraintName(self) -> str:
        """
        Getter for property: (str) ConstraintName
         Returns the constraint name.  
           If a constraint is added interactively, an automatic name will be generated for the
                    users which can be edited. Each of the constraint name must be unique.   
         
        """
        pass
    @ConstraintName.setter
    def ConstraintName(self, constraintName: str):
        """
        Setter for property: (str) ConstraintName
         Returns the constraint name.  
           If a constraint is added interactively, an automatic name will be generated for the
                    users which can be edited. Each of the constraint name must be unique.   
         
        """
        pass
    @property
    def ConstraintType(self) -> SMBoundaryConditionBuilder.ConstraintTypes:
        """
        Getter for property: ( SMBoundaryConditionBuilder.ConstraintTypes NXOpen.Featu) ConstraintType
         Returns the constraint type   
            
         
        """
        pass
    @ConstraintType.setter
    def ConstraintType(self, constraintType: SMBoundaryConditionBuilder.ConstraintTypes):
        """
        Setter for property: ( SMBoundaryConditionBuilder.ConstraintTypes NXOpen.Featu) ConstraintType
         Returns the constraint type   
            
         
        """
        pass
    @property
    def EndRegionCurve(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) EndRegionCurve
         Returns the end region curve This input is required if the Constraint Type is NOT  Features::SheetMetal::SMBoundaryConditionBuilder::ConstraintTypesPointToPoint .  
              
         
        """
        pass
    @property
    def EndRegionPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) EndRegionPoint
         Returns the end region point This input is required only if the Constraint Type is  Features::SheetMetal::SMBoundaryConditionBuilder::ConstraintTypesPointToPoint .  
              
         
        """
        pass
    @EndRegionPoint.setter
    def EndRegionPoint(self, endRegionPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) EndRegionPoint
         Returns the end region point This input is required only if the Constraint Type is  Features::SheetMetal::SMBoundaryConditionBuilder::ConstraintTypesPointToPoint .  
              
         
        """
        pass
    @property
    def StartRegionCurve(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) StartRegionCurve
         Returns the start region curve This input is required only if the Constraint Type is  Features::SheetMetal::SMBoundaryConditionBuilder::ConstraintTypesCurveToCurve  or 
                     Features::SheetMetal::SMBoundaryConditionBuilder::ConstraintTypesCurveAlongCurve .  
              
         
        """
        pass
    @property
    def StartRegionPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) StartRegionPoint
         Returns the start region point.  
           This input is required only if the Constraint Type is  Features::SheetMetal::SMBoundaryConditionBuilder::ConstraintTypesPointToPoint  or 
                     Features::SheetMetal::SMBoundaryConditionBuilder::ConstraintTypesPointAlongCurve .    
         
        """
        pass
    @StartRegionPoint.setter
    def StartRegionPoint(self, startRegionPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) StartRegionPoint
         Returns the start region point.  
           This input is required only if the Constraint Type is  Features::SheetMetal::SMBoundaryConditionBuilder::ConstraintTypesPointToPoint  or 
                     Features::SheetMetal::SMBoundaryConditionBuilder::ConstraintTypesPointAlongCurve .    
         
        """
        pass
import NXOpen
import NXOpen.Features
class SolidPunchBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a NXOpen.Features.SheetMetal.SolidPunchBuilder 
    """
    class Types(Enum):
        """
        Members Include: 
         |PunchType| 
         |DieType| 

        """
        PunchType: int
        DieType: int
        @staticmethod
        def ValueOf(value: int) -> SolidPunchBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AutoCentroid(self) -> bool:
        """
        Getter for property: (bool) AutoCentroid
         Returns the option to create centroid automatically.  
            
         
        """
        pass
    @AutoCentroid.setter
    def AutoCentroid(self, autoCentroid: bool):
        """
        Setter for property: (bool) AutoCentroid
         Returns the option to create centroid automatically.  
            
         
        """
        pass
    @property
    def ConstantThickness(self) -> bool:
        """
        Getter for property: (bool) ConstantThickness
         Returns the option to maintain constant thickness during thickening.  
            
         
        """
        pass
    @ConstantThickness.setter
    def ConstantThickness(self, constantThickness: bool):
        """
        Setter for property: (bool) ConstantThickness
         Returns the option to maintain constant thickness during thickening.  
            
         
        """
        pass
    @property
    def DieRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DieRadius
         Returns the Radius value of the sharp edges of the bottom face   
            
         
        """
        pass
    @property
    def FromCsys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) FromCsys
         Returns the csys that defines the start of transformation of the tool body.  
             
         
        """
        pass
    @FromCsys.setter
    def FromCsys(self, fromCsys: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) FromCsys
         Returns the csys that defines the start of transformation of the tool body.  
             
         
        """
        pass
    @property
    def HideTool(self) -> bool:
        """
        Getter for property: (bool) HideTool
         Returns the option to hide the tool body after creating the punch.  
             
         
        """
        pass
    @HideTool.setter
    def HideTool(self, hideTool: bool):
        """
        Setter for property: (bool) HideTool
         Returns the option to hide the tool body after creating the punch.  
             
         
        """
        pass
    @property
    def IncludeRounding(self) -> bool:
        """
        Getter for property: (bool) IncludeRounding
         Returns the option to round the sharp edges of bottom face and top face.  
             
         
        """
        pass
    @IncludeRounding.setter
    def IncludeRounding(self, includeRounding: bool):
        """
        Setter for property: (bool) IncludeRounding
         Returns the option to round the sharp edges of bottom face and top face.  
             
         
        """
        pass
    @property
    def InferThickness(self) -> bool:
        """
        Getter for property: (bool) InferThickness
         Returns the option to infer the thickness from the target body.  
             
         
        """
        pass
    @InferThickness.setter
    def InferThickness(self, inferThickness: bool):
        """
        Setter for property: (bool) InferThickness
         Returns the option to infer the thickness from the target body.  
             
         
        """
        pass
    @property
    def PierceFaces(self) -> NXOpen.SelectFaceList:
        """
        Getter for property: ( NXOpen.SelectFaceList) PierceFaces
         Returns the pierce faces of the tool body.  
            
         
        """
        pass
    @property
    def PunchRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PunchRadius
         Returns the Radius value of the sharp edges on the top face   
            
         
        """
        pass
    @property
    def TargetFace(self) -> NXOpen.SelectFace:
        """
        Getter for property: ( NXOpen.SelectFace) TargetFace
         Returns the target face   
            
         
        """
        pass
    @property
    def Thickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Thickness
         Returns the thickness expression to use when the option to infer thickness is turned off.  
            
         
        """
        pass
    @property
    def ToCsys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) ToCsys
         Returns the csys that defines the end of transformation of the tool body.  
             
         
        """
        pass
    @ToCsys.setter
    def ToCsys(self, toCsys: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) ToCsys
         Returns the csys that defines the end of transformation of the tool body.  
             
         
        """
        pass
    @property
    def ToolBody(self) -> NXOpen.SelectBody:
        """
        Getter for property: ( NXOpen.SelectBody) ToolBody
         Returns the tool body   
            
         
        """
        pass
    @property
    def Type(self) -> SolidPunchBuilder.Types:
        """
        Getter for property: ( SolidPunchBuilder.Types NXOpen.Featu) Type
         Returns the type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: SolidPunchBuilder.Types):
        """
        Setter for property: ( SolidPunchBuilder.Types NXOpen.Featu) Type
         Returns the type   
            
         
        """
        pass
import NXOpen
import NXOpen.Features
class TabBuilder(SheetmetalBaseBuilder): 
    """ Represents a Tab feature builder. """
    class SectionSideOptions(Enum):
        """
        Members Include: 
         |Left|  Side pointed to by the inverse of the tangent cross normal vector 
         |Right|  Side pointed to by the tangent cross normal vector 

        """
        Left: int
        Right: int
        @staticmethod
        def ValueOf(value: int) -> TabBuilder.SectionSideOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ThicknessSideOptions(Enum):
        """
        Members Include: 
         |SectionNormalSide|  Material created on the side of the section normal. 
         |SectionReverseNormalSide|  Material created on the side opposite to that of the section normal 

        """
        SectionNormalSide: int
        SectionReverseNormalSide: int
        @staticmethod
        def ValueOf(value: int) -> TabBuilder.ThicknessSideOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def IsSecondary(self) -> bool:
        """
        Getter for property: (bool) IsSecondary
         Returns the tab type   
            
         
        """
        pass
    @IsSecondary.setter
    def IsSecondary(self, is_secondary: bool):
        """
        Setter for property: (bool) IsSecondary
         Returns the tab type   
            
         
        """
        pass
    @property
    def MaterialSide(self) -> TabBuilder.SectionSideOptions:
        """
        Getter for property: ( TabBuilder.SectionSideOptions NXOpen.Featu) MaterialSide
         Returns the material side value of secondary tab   
            
         
        """
        pass
    @MaterialSide.setter
    def MaterialSide(self, section_side: TabBuilder.SectionSideOptions):
        """
        Setter for property: ( TabBuilder.SectionSideOptions NXOpen.Featu) MaterialSide
         Returns the material side value of secondary tab   
            
         
        """
        pass
    @property
    def MultiBendPropertiesList(self) -> FeatureBendPropertiesListBuilder:
        """
        Getter for property: ( FeatureBendPropertiesListBuilder NXOpen.Featu) MultiBendPropertiesList
         Returns the multi bend  properties list   
            
         
        """
        pass
    @property
    def MultiThicknessProperty(self) -> MultiThicknessBuilder:
        """
        Getter for property: ( MultiThicknessBuilder NXOpen.Featu) MultiThicknessProperty
         Returns the multi thickness property.  
             
         
        """
        pass
    @property
    def Section(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Section
         Returns the section of tab   
            
         
        """
        pass
    @Section.setter
    def Section(self, section: NXOpen.Section):
        """
        Setter for property: ( NXOpen.Section) Section
         Returns the section of tab   
            
         
        """
        pass
    @property
    def Sketch(self) -> NXOpen.Features.SketchFeature:
        """
        Getter for property: ( NXOpen.Features.SketchFeature) Sketch
         Returns the sketch of tab   
            
         
        """
        pass
    @Sketch.setter
    def Sketch(self, sketch: NXOpen.Features.SketchFeature):
        """
        Setter for property: ( NXOpen.Features.SketchFeature) Sketch
         Returns the sketch of tab   
            
         
        """
        pass
    @property
    def TargetBody(self) -> NXOpen.Body:
        """
        Getter for property: ( NXOpen.Body) TargetBody
         Returns the target body on which the secondary tab is created.  
          
                      
                       Use  NXOpen::Features::SheetMetal::TabBuilder::IsSecondary  to determine whether this is a secondary tab.
                      
                  
         
        """
        pass
    @TargetBody.setter
    def TargetBody(self, targetBody: NXOpen.Body):
        """
        Setter for property: ( NXOpen.Body) TargetBody
         Returns the target body on which the secondary tab is created.  
          
                      
                       Use  NXOpen::Features::SheetMetal::TabBuilder::IsSecondary  to determine whether this is a secondary tab.
                      
                  
         
        """
        pass
    @property
    def Thickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Thickness
         Returns the thickness of tab   
            
         
        """
        pass
    @property
    def ThicknessSide(self) -> TabBuilder.ThicknessSideOptions:
        """
        Getter for property: ( TabBuilder.ThicknessSideOptions NXOpen.Featu) ThicknessSide
         Returns the sweep direction flag of tab   
            
         
        """
        pass
    @ThicknessSide.setter
    def ThicknessSide(self, flag: TabBuilder.ThicknessSideOptions):
        """
        Setter for property: ( TabBuilder.ThicknessSideOptions NXOpen.Featu) ThicknessSide
         Returns the sweep direction flag of tab   
            
         
        """
        pass
    def UpdateReferenceCurves(self) -> NXOpen.Features.Feature:
        """
         This is only applicable for base tab created with bends. This extracts boundary curves of the faces
                    that are attached to the planes specified by  NXOpen.Features.SheetMetal.MultiBendBendPropertiesBuilder.Plane.
         Returns transformer ( NXOpen.Features.Feature): .
        """
        pass
    def ValidateBuilderData(self) -> int:
        """
         Verify whether the builder data is valid for creating a Tab or not.
                    
                         If the Builder data is valid, returned value shall be 0.
                    
                
         Returns builder_data_validity (int):  Data Validity Flag.
        """
        pass
import NXOpen
import NXOpen.Features
class ThreeBendCornerBuilder(NXOpen.Features.FeatureBuilder): 
    """ The Three Bend Corner feature class. Users can identify multiple input face pairs for each three bend 
        corner feature. Each pair is made up of one face each from adjacent bends. The bends must both have the 
        same radius and sweep angle, and they must also be connected via another adjoining bend.
    """
    class CutMethodTypes(Enum):
        """
        Members Include: 
         |ByTool|  The cut method will be by tool. 
         |ByPath|  The cut method will be by path.

        """
        ByTool: int
        ByPath: int
        @staticmethod
        def ValueOf(value: int) -> ThreeBendCornerBuilder.CutMethodTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OriginTypes(Enum):
        """
        Members Include: 
         |BendCenter|  The relief origin will be at the intersection of first bend's centerline and bisector of corner angle. 
         |CornerPoint|  The relief origin will be at the corner point.

        """
        BendCenter: int
        CornerPoint: int
        @staticmethod
        def ValueOf(value: int) -> ThreeBendCornerBuilder.OriginTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TreatmentTypeOptions(Enum):
        """
        Members Include: 
         |Open|   
         |Closed|   
         |CircularCutout|   
         |UCutout|   
         |VCutout|   

        """
        Open: int
        Closed: int
        CircularCutout: int
        UCutout: int
        VCutout: int
        @staticmethod
        def ValueOf(value: int) -> ThreeBendCornerBuilder.TreatmentTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BlendMiter(self) -> bool:
        """
        Getter for property: (bool) BlendMiter
         Returns the option for smooth transition from miter to cutout edges.  
            
         
        """
        pass
    @BlendMiter.setter
    def BlendMiter(self, blendMiter: bool):
        """
        Setter for property: (bool) BlendMiter
         Returns the option for smooth transition from miter to cutout edges.  
            
         
        """
        pass
    @property
    def BlendMiterRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BlendMiterRadius
         Returns the blend miter radius used for three bend corner miter treatment.  
           This only applies when the treatment type is set to 
                     NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsClosed  or
                     NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsCircularCutout  or 
                     NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsUCutout  or
                     NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsVCutout .  
                  
         
        """
        pass
    @property
    def CornerGap(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CornerGap
         Returns the corner gap.  
            
         
        """
        pass
    @property
    def CutMethod(self) -> ThreeBendCornerBuilder.CutMethodTypes:
        """
        Getter for property: ( ThreeBendCornerBuilder.CutMethodTypes NXOpen.Featu) CutMethod
         Returns the cut method to be used for UV cutout relief.  
            
         
        """
        pass
    @CutMethod.setter
    def CutMethod(self, cutMethod: ThreeBendCornerBuilder.CutMethodTypes):
        """
        Setter for property: ( ThreeBendCornerBuilder.CutMethodTypes NXOpen.Featu) CutMethod
         Returns the cut method to be used for UV cutout relief.  
            
         
        """
        pass
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Diameter
         Returns the diameter used for circular, u and v cutout corner treatments.  
           This only applies when the treatment type is set to 
                     NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsCircularCutout  or
                     NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsUCutout  or
                     NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsVCutout .
                  
         
        """
        pass
    @property
    def FlangeClearance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlangeClearance
         Returns the flange clearance used for three bend corner miter treatment.  
           This only applies when the treatment type is set to 
                     NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsOpen  or
                     NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsClosed  or
                     NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsCircularCutout  or 
                     NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsUCutout  or
                     NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsVCutout .  
                  
         
        """
        pass
    @property
    def Length(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Length
         Returns the length of U relief.  
             
         
        """
        pass
    @property
    def Length1(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Length1
         Returns the length of V relief associated with the first bend selected.  
            
         
        """
        pass
    @property
    def Length2(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Length2
         Returns the length of V relief associated with the second bend selected.  
            
         
        """
        pass
    @property
    def MiterCorner(self) -> bool:
        """
        Getter for property: (bool) MiterCorner
         Returns whether the corner will be closed using miter.  
            
         
        """
        pass
    @MiterCorner.setter
    def MiterCorner(self, miterCorner: bool):
        """
        Setter for property: (bool) MiterCorner
         Returns whether the corner will be closed using miter.  
            
         
        """
        pass
    @property
    def MiterRootRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MiterRootRadius
         Returns the miter root radius used for three bend corner miter treatment.  
           This only applies when the treatment type is set to 
                     NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsClosed .
                  
         
        """
        pass
    @property
    def NumberOfFacePairs(self) -> int:
        """
        Getter for property: (int) NumberOfFacePairs
         Returns the number of face pairs already identified for the three bend corner feature.  
          
                  
         
        """
        pass
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Offset
         Returns the offset used for circular, u and v cutout corner treatments.  
           This only applies when the treatment type is set to 
                     NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsCircularCutout  or
                     NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsUCutout  or
                     NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsVCutout .
                  
         
        """
        pass
    @property
    def OriginType(self) -> ThreeBendCornerBuilder.OriginTypes:
        """
        Getter for property: ( ThreeBendCornerBuilder.OriginTypes NXOpen.Featu) OriginType
         Returns the relief origin used for circular, u and v cutout corner treatments.  
           This only applies when the treatment type is set to 
                     NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsCircularCutout  or
                     NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsUCutout  or
                     NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsVCutout .
                  
         
        """
        pass
    @OriginType.setter
    def OriginType(self, originType: ThreeBendCornerBuilder.OriginTypes):
        """
        Setter for property: ( ThreeBendCornerBuilder.OriginTypes NXOpen.Featu) OriginType
         Returns the relief origin used for circular, u and v cutout corner treatments.  
           This only applies when the treatment type is set to 
                     NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsCircularCutout  or
                     NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsUCutout  or
                     NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsVCutout .
                  
         
        """
        pass
    @property
    def PunchRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PunchRadius
         Returns the punch radius of tool associated with V relief.  
            
         
        """
        pass
    @property
    def TreatmentType(self) -> ThreeBendCornerBuilder.TreatmentTypeOptions:
        """
        Getter for property: ( ThreeBendCornerBuilder.TreatmentTypeOptions NXOpen.Featu) TreatmentType
         Returns the corner treatment type.  
          
                      
                        The NXOpen.Features.SheetMetal.ThreeBendCornerBuilder.TreatmentType) specifies how the 
                        corner should be treated. Valid options are in  NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptions . 
                      
                  
         
        """
        pass
    @TreatmentType.setter
    def TreatmentType(self, treatment_type: ThreeBendCornerBuilder.TreatmentTypeOptions):
        """
        Setter for property: ( ThreeBendCornerBuilder.TreatmentTypeOptions NXOpen.Featu) TreatmentType
         Returns the corner treatment type.  
          
                      
                        The NXOpen.Features.SheetMetal.ThreeBendCornerBuilder.TreatmentType) specifies how the 
                        corner should be treated. Valid options are in  NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptions . 
                      
                  
         
        """
        pass
    @property
    def VCutoutAngle1(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) VCutoutAngle1
         Returns the angle 1 used for the v cutout treatment.  
           This only applies when the treatment type is set to 
                     NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsVCutout .
                  
         
        """
        pass
    @property
    def VCutoutAngle2(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) VCutoutAngle2
         Returns the angle 2 used for the v cutout treatment.  
           This only applies when the treatment type is set to 
                     NXOpen::Features::SheetMetal::ThreeBendCornerBuilder::TreatmentTypeOptionsVCutout .
                  
         
        """
        pass
    def AddFacePair(self, first_face: NXOpen.Face, second_face: NXOpen.Face) -> None:
        """
         Input a bend face pair for the three bend corner feature. This method can be called multiple  
                   times for a feature, with each bend face pair representing a unique corner.
                
        """
        pass
    def GetFacePair(self, index: int) -> Tuple[NXOpen.Face, NXOpen.Face]:
        """
         Gets the bend face pair at the given index. The index can vary between zero and one less than the 
                    value returned by NXOpen.Features.SheetMetal.ThreeBendCornerBuilder.NumberOfFacePairs.
                
         Returns A tuple consisting of (first_face, second_face). 
         - first_face is:  NXOpen.Face. First face of the face pair .
         - second_face is:  NXOpen.Face. Second face of the face pair .

        """
        pass
    def RemoveFacePair(self, first_face: NXOpen.Face, second_face: NXOpen.Face) -> None:
        """
         Removes a face pair (that represents a unique corner) from the list of face pairs already added.
                
        """
        pass
    def ValidateBuilderData(self) -> int:
        """
         Verify that the builder data is valid for creation of a three bend corner.
                    
                         If the data in the builder is valid, the return value is 0
                    
                
         Returns validity (int):  Returns 0 if the data in the builder is valid .
        """
        pass
import NXOpen
class UnbendBuilder(SheetmetalBaseBuilder): 
    """ The Unbend feature class."""
    @property
    def AddedGeometry(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) AddedGeometry
         Returns the added geometry selection   
            
         
        """
        pass
    @AddedGeometry.setter
    def AddedGeometry(self, addedGeometry: NXOpen.Section):
        """
        Setter for property: ( NXOpen.Section) AddedGeometry
         Returns the added geometry selection   
            
         
        """
        pass
    @property
    def ExtractGussetCurves(self) -> bool:
        """
        Getter for property: (bool) ExtractGussetCurves
         Returns the option to extract gusset boundary curves   
            
         
        """
        pass
    @ExtractGussetCurves.setter
    def ExtractGussetCurves(self, extractGussetCurves: bool):
        """
        Setter for property: (bool) ExtractGussetCurves
         Returns the option to extract gusset boundary curves   
            
         
        """
        pass
    @property
    def FaceCollector(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FaceCollector
         Returns the bend faces   
            
         
        """
        pass
    @FaceCollector.setter
    def FaceCollector(self, face_collector: NXOpen.ScCollector):
        """
        Setter for property: ( NXOpen.ScCollector) FaceCollector
         Returns the bend faces   
            
         
        """
        pass
    @property
    def HideOriginalCurves(self) -> bool:
        """
        Getter for property: (bool) HideOriginalCurves
         Returns the option to keep or hide input curves   
            
         
        """
        pass
    @HideOriginalCurves.setter
    def HideOriginalCurves(self, hideOriginalCurves: bool):
        """
        Setter for property: (bool) HideOriginalCurves
         Returns the option to keep or hide input curves   
            
         
        """
        pass
    @property
    def ReferenceEntity(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) ReferenceEntity
         Returns the non-thickness planar face or linear edge to remain fixed while part is unbent   
            
         
        """
        pass
    @ReferenceEntity.setter
    def ReferenceEntity(self, reference_entity: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) ReferenceEntity
         Returns the non-thickness planar face or linear edge to remain fixed while part is unbent   
            
         
        """
        pass
    def ValidateBuilderData(self) -> int:
        """
         Verify whether the builder data is valid for creating Unbend or not.
                    
                         If the Builder data is valid, returned value shall be 0
                    
                
         Returns validity_code (int): .
        """
        pass
import NXOpen
class VariationalFlangeBuilder(SheetmetalBaseBuilder): 
    """ Represents a Features.SheetMetal.VariationalFlangeBuilder """
    class LawTypes(Enum):
        """
        Members Include: 
         |Constant| 
         |Linear| 

        """
        Constant: int
        Linear: int
        @staticmethod
        def ValueOf(value: int) -> VariationalFlangeBuilder.LawTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LengthReferences(Enum):
        """
        Members Include: 
         |Inside| 
         |Outside| 
         |Web| 
         |Tangent| 

        """
        Inside: int
        Outside: int
        Web: int
        Tangent: int
        @staticmethod
        def ValueOf(value: int) -> VariationalFlangeBuilder.LengthReferences:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |NormalToFace| 
         |AlongPunchVector| 

        """
        NormalToFace: int
        AlongPunchVector: int
        @staticmethod
        def ValueOf(value: int) -> VariationalFlangeBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Angle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Angle
         Returns the angle   
            
         
        """
        pass
    @property
    def AngleLawType(self) -> VariationalFlangeBuilder.LawTypes:
        """
        Getter for property: ( VariationalFlangeBuilder.LawTypes NXOpen.Featu) AngleLawType
         Returns the angle law type   
            
         
        """
        pass
    @AngleLawType.setter
    def AngleLawType(self, angleLawType: VariationalFlangeBuilder.LawTypes):
        """
        Setter for property: ( VariationalFlangeBuilder.LawTypes NXOpen.Featu) AngleLawType
         Returns the angle law type   
            
         
        """
        pass
    @property
    def Edges(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) Edges
         Returns the base edge for the variational flange.  
            
         
        """
        pass
    @property
    def EndAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EndAngle
         Returns the end angle   
            
         
        """
        pass
    @property
    def EndLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EndLength
         Returns the end length   
            
         
        """
        pass
    @property
    def Length(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Length
         Returns the length   
            
         
        """
        pass
    @property
    def LengthLawType(self) -> VariationalFlangeBuilder.LawTypes:
        """
        Getter for property: ( VariationalFlangeBuilder.LawTypes NXOpen.Featu) LengthLawType
         Returns the length law type   
            
         
        """
        pass
    @LengthLawType.setter
    def LengthLawType(self, lengthLawType: VariationalFlangeBuilder.LawTypes):
        """
        Setter for property: ( VariationalFlangeBuilder.LawTypes NXOpen.Featu) LengthLawType
         Returns the length law type   
            
         
        """
        pass
    @property
    def LengthReference(self) -> VariationalFlangeBuilder.LengthReferences:
        """
        Getter for property: ( VariationalFlangeBuilder.LengthReferences NXOpen.Featu) LengthReference
         Returns the length reference   
            
         
        """
        pass
    @LengthReference.setter
    def LengthReference(self, lengthReference: VariationalFlangeBuilder.LengthReferences):
        """
        Setter for property: ( VariationalFlangeBuilder.LengthReferences NXOpen.Featu) LengthReference
         Returns the length reference   
            
         
        """
        pass
    @property
    def NeutralFactor(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) NeutralFactor
         Returns the neutral factor   
            
         
        """
        pass
    @property
    def Radius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Radius
         Returns the radius   
            
         
        """
        pass
    @property
    def ReverseDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseDirection
         Returns the option to reverse length direction   
            
         
        """
        pass
    @ReverseDirection.setter
    def ReverseDirection(self, reverseDirection: bool):
        """
        Setter for property: (bool) ReverseDirection
         Returns the option to reverse length direction   
            
         
        """
        pass
    @property
    def StartAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StartAngle
         Returns the start angle   
            
         
        """
        pass
    @property
    def StartLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StartLength
         Returns the start length   
            
         
        """
        pass
import NXOpen.Features
class VariationalFlange(NXOpen.Features.Feature): 
    """ Represents a variational flange feature """
    pass
