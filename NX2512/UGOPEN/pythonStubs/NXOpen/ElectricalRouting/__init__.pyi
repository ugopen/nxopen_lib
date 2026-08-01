from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class BuilderFactory(NXOpen.Object): 
    """ Represents an NXOpen.ElectricalRouting.BuilderFactory object.  Use this object
        to create specific routing electrical builders.
    """
    def CreatePlaceSpliceBuilder(part: NXOpen.Part, splicePoint: NXOpen.Point) -> PlaceSpliceBuilder:
        """
          Creates a NXOpen.ElectricalRouting.PlaceSpliceBuilder object. 
         Returns builder ( PlaceSpliceBuilder NXOpen.Elec): .
        """
        pass
    def CreateTeamcenterExporterBuilder(part: NXOpen.Part) -> TeamcenterExporterBuilder:
        """
          Creates a NXOpen.ElectricalRouting.TeamcenterExporterBuilder object. 
         Returns builder ( TeamcenterExporterBuilder NXOpen.Elec): .
        """
        pass
    def CreateTeamcenterImporterBuilder(part: NXOpen.Part) -> TeamcenterImporterBuilder:
        """
          Creates a NXOpen.ElectricalRouting.TeamcenterImporterBuilder object. 
         Returns builder ( TeamcenterImporterBuilder NXOpen.Elec): .
        """
        pass
import NXOpen
class CollectionsManager(NXOpen.Object): 
    """ Represents an NXOpen.ElectricalRouting.CollectionsManager object,
        which manages various collections of Routing objects.
     """
    @property
    def SplicePoints() -> RSDSplicePointCollection:
        """
         Splice Point Collection 
        """
        pass
import NXOpen
import NXOpen.Routing
import NXOpen.Routing.Electrical
class PlaceSpliceBuilder(NXOpen.Builder): 
    """ Represents NXOpen.ElectricalRouting.PlaceSpliceBuilder. """
    @property
    def AdditionalWireLength(self) -> float:
        """
        Getter for property: (float) AdditionalWireLength
         Returns the additional length required for the wire for the fabrication of the splice.  
             
         
        """
        pass
    @AdditionalWireLength.setter
    def AdditionalWireLength(self, additionalLength: float):
        """
        Setter for property: (float) AdditionalWireLength
         Returns the additional length required for the wire for the fabrication of the splice.  
             
         
        """
        pass
    @property
    def AnchorControlPoint(self) -> NXOpen.Routing.ControlPoint:
        """
        Getter for property: ( NXOpen.Routing.ControlPoint) AnchorControlPoint
         Returns the anchor control point from which the distance to the splice is measured.  
            
         
        """
        pass
    @AnchorControlPoint.setter
    def AnchorControlPoint(self, controlPoint: NXOpen.Routing.ControlPoint):
        """
        Setter for property: ( NXOpen.Routing.ControlPoint) AnchorControlPoint
         Returns the anchor control point from which the distance to the splice is measured.  
            
         
        """
        pass
    @property
    def ConnectorDevice(self) -> NXOpen.Routing.Electrical.ConnectorDevice:
        """
        Getter for property: ( NXOpen.Routing.Electrical.ConnectorDevice) ConnectorDevice
         Returns the  Routing::Electrical::ConnectorDevice  to which this splice is assigned.  
            
         
        """
        pass
    @ConnectorDevice.setter
    def ConnectorDevice(self, connectorDevice: NXOpen.Routing.Electrical.ConnectorDevice):
        """
        Setter for property: ( NXOpen.Routing.Electrical.ConnectorDevice) ConnectorDevice
         Returns the  Routing::Electrical::ConnectorDevice  to which this splice is assigned.  
            
         
        """
        pass
    @property
    def DistanceFromAnchor(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DistanceFromAnchor
         Returns the distance for splice point from the inferred anchor node on the route section.  
             
         
        """
        pass
    @property
    def PointOnPath(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) PointOnPath
         Returns the point on pathcurve selected by user to position a splice   
            
         
        """
        pass
    @PointOnPath.setter
    def PointOnPath(self, pointOnPath: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) PointOnPath
         Returns the point on pathcurve selected by user to position a splice   
            
         
        """
        pass
    @property
    def Segment(self) -> NXOpen.Routing.ISegment:
        """
        Getter for property: ( NXOpen.Routing.ISegment) Segment
         Returns the segment on which the splice lives.  
           Must be the same segment on which the
                    point on path was created.  
         
        """
        pass
    @Segment.setter
    def Segment(self, segment: NXOpen.Routing.ISegment):
        """
        Setter for property: ( NXOpen.Routing.ISegment) Segment
         Returns the segment on which the splice lives.  
           Must be the same segment on which the
                    point on path was created.  
         
        """
        pass
    @property
    def SpliceName(self) -> str:
        """
        Getter for property: (str) SpliceName
         Returns the splice name given by NX user or received from Capital.  
             
         
        """
        pass
    @SpliceName.setter
    def SpliceName(self, spliceName: str):
        """
        Setter for property: (str) SpliceName
         Returns the splice name given by NX user or received from Capital.  
             
         
        """
        pass
    @property
    def SwitchReferencePoint(self) -> bool:
        """
        Getter for property: (bool) SwitchReferencePoint
         Returns the switch route node can be used by user to highlight and store the route node
                    opposite to the inferred anchor node.  
             
         
        """
        pass
    @SwitchReferencePoint.setter
    def SwitchReferencePoint(self, switchReferencePoint: bool):
        """
        Setter for property: (bool) SwitchReferencePoint
         Returns the switch route node can be used by user to highlight and store the route node
                    opposite to the inferred anchor node.  
             
         
        """
        pass
    def SetDistanceFromAnchorNode(self, distance: float) -> None:
        """
         Sets the distance from the splice point to the anchor node.
                    The NX Open user has to set distance to place a splice on the route section.
                    The distance would be considered from the start node of the route section. 
        """
        pass
    def SetEndRouteNodesOfRouteSection(self, startRouteNode: NXOpen.Routing.ControlPoint, endRouteNode: NXOpen.Routing.ControlPoint) -> None:
        """
         The automation user has to set the end route nodes of the route section in order to
                    place the splice on route section. 
        """
        pass
    def SetRouteSectionLength(self, totalLengthOfRouteSection: float) -> None:
        """
         Sets the total curve length of the route section.
                    The NX Open user has to set the total length of the route section.
                    This will be used for internal validations and to place the splice correctly. 
        """
        pass
import NXOpen
class RSDSplicePointCollection(NXOpen.TaggedObjectCollection): 
    """ The collection of all NXOpen.ElectricalRouting.RSDSplicePoints.
        Use the NXOpen.ElectricalRouting.PlaceSpliceBuilder to create
        a NXOpen.ElectricalRouting.RSDSplicePoint.
    """
    pass
import NXOpen.Routing.Electrical
class RSDSplicePoint(NXOpen.Routing.Electrical.SplicePoint): 
    """ Represents a NXOpen.ElectricalRouting.RSDSplicePoint. """
    pass
import NXOpen
class TeamcenterExporterBuilder(NXOpen.Builder): 
    """ Builder class for Teamcenter Export dialog. """
    class DatasetExportMode(Enum):
        """
        Members Include: 
         |CreateNew|  Create a new data set. Will not overwrite an existing dataset. 
         |OverwriteExisting|  Overwrite an existing dataset if you have permission. 

        """
        CreateNew: int
        OverwriteExisting: int
        @staticmethod
        def ValueOf(value: int) -> TeamcenterExporterBuilder.DatasetExportMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ExportFileType(Enum):
        """
        Members Include: 
         |PlmXml|  A PLMXML File 
         |Zip|  A Zip file containing a PLMXML file and a JSON file. 
         |Hrn|  A harness data file. 
         |Cmp|  A component data file. 
         |Hx2ml|  A HX2ML file. 

        """
        PlmXml: int
        Zip: int
        Hrn: int
        Cmp: int
        Hx2ml: int
        @staticmethod
        def ValueOf(value: int) -> TeamcenterExporterBuilder.ExportFileType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DatasetName(self) -> str:
        """
        Getter for property: (str) DatasetName
         Returns the name of the dataset that contains the data files to import.  
             
         
        """
        pass
    @DatasetName.setter
    def DatasetName(self, datasetName: str):
        """
        Setter for property: (str) DatasetName
         Returns the name of the dataset that contains the data files to import.  
             
         
        """
        pass
    @property
    def ExportMode(self) -> TeamcenterExporterBuilder.DatasetExportMode:
        """
        Getter for property: ( TeamcenterExporterBuilder.DatasetExportMode NXOpen.Elec) ExportMode
         Returns the export mode: create a new dataset or overwrite an existing dataset.  
             
         
        """
        pass
    @ExportMode.setter
    def ExportMode(self, exportMode: TeamcenterExporterBuilder.DatasetExportMode):
        """
        Setter for property: ( TeamcenterExporterBuilder.DatasetExportMode NXOpen.Elec) ExportMode
         Returns the export mode: create a new dataset or overwrite an existing dataset.  
             
         
        """
        pass
    @property
    def FileType(self) -> TeamcenterExporterBuilder.ExportFileType:
        """
        Getter for property: ( TeamcenterExporterBuilder.ExportFileType NXOpen.Elec) FileType
         Returns the type of file to create in the Teamcenter database.  
          
                    See  NXOpen::ElectricalRouting::TeamcenterExporterBuilder::ExportFileType 
                  
         
        """
        pass
    @FileType.setter
    def FileType(self, fileType: TeamcenterExporterBuilder.ExportFileType):
        """
        Setter for property: ( TeamcenterExporterBuilder.ExportFileType NXOpen.Elec) FileType
         Returns the type of file to create in the Teamcenter database.  
          
                    See  NXOpen::ElectricalRouting::TeamcenterExporterBuilder::ExportFileType 
                  
         
        """
        pass
    @property
    def ItemId(self) -> str:
        """
        Getter for property: (str) ItemId
         Returns the item ID that contains the dataset to import.  
             
         
        """
        pass
    @ItemId.setter
    def ItemId(self, itemID: str):
        """
        Setter for property: (str) ItemId
         Returns the item ID that contains the dataset to import.  
             
         
        """
        pass
    @property
    def ItemRevision(self) -> str:
        """
        Getter for property: (str) ItemRevision
         Returns the item revision that contains the dataset to import.  
             
         
        """
        pass
    @ItemRevision.setter
    def ItemRevision(self, itemRevision: str):
        """
        Setter for property: (str) ItemRevision
         Returns the item revision that contains the dataset to import.  
             
         
        """
        pass
import NXOpen
import NXOpen.Routing
class TeamcenterImporterBuilder(NXOpen.Builder): 
    """ Builder class for Import from PDM dialog. """
    @property
    def DatasetName(self) -> str:
        """
        Getter for property: (str) DatasetName
         Returns the name of the dataset that contains the data files to import.  
             
         
        """
        pass
    @DatasetName.setter
    def DatasetName(self, datasetName: str):
        """
        Setter for property: (str) DatasetName
         Returns the name of the dataset that contains the data files to import.  
             
         
        """
        pass
    @property
    def ImportMode(self) -> NXOpen.Routing.RouteManager.ImportMode:
        """
        Getter for property: ( NXOpen.Routing.RouteManager.ImportMode) ImportMode
         Returns the current import mode.  
             
         
        """
        pass
    @ImportMode.setter
    def ImportMode(self, importMode: NXOpen.Routing.RouteManager.ImportMode):
        """
        Setter for property: ( NXOpen.Routing.RouteManager.ImportMode) ImportMode
         Returns the current import mode.  
             
         
        """
        pass
    @property
    def ItemId(self) -> str:
        """
        Getter for property: (str) ItemId
         Returns the item ID that contains the dataset to import.  
             
         
        """
        pass
    @ItemId.setter
    def ItemId(self, itemID: str):
        """
        Setter for property: (str) ItemId
         Returns the item ID that contains the dataset to import.  
             
         
        """
        pass
    @property
    def ItemRevision(self) -> str:
        """
        Getter for property: (str) ItemRevision
         Returns the item revision that contains the dataset to import.  
             
         
        """
        pass
    @ItemRevision.setter
    def ItemRevision(self, itemRevision: str):
        """
        Setter for property: (str) ItemRevision
         Returns the item revision that contains the dataset to import.  
             
         
        """
        pass
    @property
    def ScaleFactor(self) -> float:
        """
        Getter for property: (float) ScaleFactor
         Returns the difference between the units of a PLM XML file and the units of the part into which
                    you are importing the data.  
           Used when importing JSON files.
                  
         
        """
        pass
    @ScaleFactor.setter
    def ScaleFactor(self, scaleFactor: float):
        """
        Setter for property: (float) ScaleFactor
         Returns the difference between the units of a PLM XML file and the units of the part into which
                    you are importing the data.  
           Used when importing JSON files.
                  
         
        """
        pass
    def GetDatasetFileNames(self) -> List[str]:
        """
         Gets the names of the files in the dataset that contain the data to import. 
         Returns names (List[str]): .
        """
        pass
    def SetDatasetFileNames(self, names: List[str]) -> None:
        """
         Sets the names of the files in the dataset that contain the data to import. 
        """
        pass
