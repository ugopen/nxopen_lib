from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class IssueAttachment(NXOpen.NXObject): 
    """ Represents the Issue Attachment object. """
    class Type(Enum):
        """
        Members Include: 
         |Generic|  Generic type 
         |Text|  Text type 
         |Part|  Part type 
         |Xml|  XML type 
         |Image|  Image type 
         |ValidationLog|  Validation log file 
         |Bookmark|  Bookmark type 
         |Snapshot|  Snapshot type 
         |ValidationResult|  ValidationResult object type 
         |Workset|  Workset type 
         |ShapeDesignElement|  Shape Design Element type 
         |ReuseDesignElement|  Reuse Design Element type 
         |SubordinateDesignElement|  Subordinate Design Element type 
         |PromissoryDesignElement|  Promissory Design Element type 
         |DesignControlElement|  Design Control Element type 
         |Subset|  Subset type 
         |MSWord|  Microsoft Word type 
         |MSExcel|  Microsoft Excel type 
         |MSPowerPoint|  Microsoft Power Point type 
         |VisualizationSession|  Visualization Session type 

        """
        Generic: int
        Text: int
        Part: int
        Xml: int
        Image: int
        ValidationLog: int
        Bookmark: int
        Snapshot: int
        ValidationResult: int
        Workset: int
        ShapeDesignElement: int
        ReuseDesignElement: int
        SubordinateDesignElement: int
        PromissoryDesignElement: int
        DesignControlElement: int
        Subset: int
        MSWord: int
        MSExcel: int
        MSPowerPoint: int
        VisualizationSession: int
        @staticmethod
        def ValueOf(value: int) -> IssueAttachment.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AttachmentType(self) -> IssueAttachment.Type:
        """
        Getter for property: ( IssueAttachment.Type NXOpe) AttachmentType
         Returns the attachment type   
            
         
        """
        pass
    @AttachmentType.setter
    def AttachmentType(self, type: IssueAttachment.Type):
        """
        Setter for property: ( IssueAttachment.Type NXOpe) AttachmentType
         Returns the attachment type   
            
         
        """
        pass
    @property
    def ReferencedAttachmentId(self) -> str:
        """
        Getter for property: (str) ReferencedAttachmentId
         Returns the refereced attachment id which specifies one attachment that is related 
                to this  NXOpen::Issue::IssueAttachment    
            
         
        """
        pass
    @ReferencedAttachmentId.setter
    def ReferencedAttachmentId(self, referencedAttachmentId: str):
        """
        Setter for property: (str) ReferencedAttachmentId
         Returns the refereced attachment id which specifies one attachment that is related 
                to this  NXOpen::Issue::IssueAttachment    
            
         
        """
        pass
    def RecaptureSnapshot(self, bookmarkFileSpec: str, imageFileSpec: str) -> None:
        """
         Recapture the snapshot 
        """
        pass
import NXOpen
class IssueBriefcaseSynchronizeBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Issue.IssueBriefcase synchronize builder """
    def AddPartAttachment(self, attachment: IssueAttachment) -> None:
        """
         Adds an part type NXOpen.Issue.IssueAttachment,
                only the added parts can be synchronized to server.
                
        """
        pass
    def RemovePartAttachment(self, attachment: IssueAttachment) -> None:
        """
         Adds an part type NXOpen.Issue.IssueAttachment. 
        """
        pass
class IssueBriefcase(IssueList): 
    """ Represents the Issue Briefcase object. """
    @property
    def Location(self) -> str:
        """
        Getter for property: (str) Location
         Returns the briefcase location  
            
         
        """
        pass
    @Location.setter
    def Location(self, folder: str):
        """
        Setter for property: (str) Location
         Returns the briefcase location  
            
         
        """
        pass
    def AddIssue(self, issue: IssueContent) -> None:
        """
         Adds an NXOpen.Issue.IssueContent from an existing NXOpen.Issue.IssueContent. 
        """
        pass
    def Close(self) -> None:
        """
         Closes NXOpen.Issue.IssueBriefcase. 
        """
        pass
    def CreateSynchronizeContentBuilder(self) -> IssueBriefcaseSynchronizeBuilder:
        """
         Creates an NXOpen.Issue.IssueBriefcaseSynchronizeBuilder 
         Returns builder ( IssueBriefcaseSynchronizeBuilder NXOpe): .
        """
        pass
    def RemoveIssue(self, issue: IssueContent) -> None:
        """
         Removes an NXOpen.Issue.IssueContent. 
        """
        pass
    def Save(self) -> None:
        """
         Saves all NXOpen.Issue.IssueContents. 
        """
        pass
import NXOpen
class IssueContentBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Issue.IssueContent builder """
    @property
    def AssignedUser(self) -> str:
        """
        Getter for property: (str) AssignedUser
         Returns the assigned user   
            
         
        """
        pass
    @AssignedUser.setter
    def AssignedUser(self, assignedUser: str):
        """
        Setter for property: (str) AssignedUser
         Returns the assigned user   
            
         
        """
        pass
    @property
    def Comment(self) -> str:
        """
        Getter for property: (str) Comment
         Returns the issue comment   
            
         
        """
        pass
    @Comment.setter
    def Comment(self, comment: str):
        """
        Setter for property: (str) Comment
         Returns the issue comment   
            
         
        """
        pass
    @property
    def DueDate(self) -> str:
        """
        Getter for property: (str) DueDate
         Returns the due date   
            
         
        """
        pass
    @DueDate.setter
    def DueDate(self, dueDate: str):
        """
        Setter for property: (str) DueDate
         Returns the due date   
            
         
        """
        pass
    @property
    def Priority(self) -> str:
        """
        Getter for property: (str) Priority
         Returns the issue priority   
            
         
        """
        pass
    @Priority.setter
    def Priority(self, priority: str):
        """
        Setter for property: (str) Priority
         Returns the issue priority   
            
         
        """
        pass
    @property
    def Status(self) -> str:
        """
        Getter for property: (str) Status
         Returns the issue status   
            
         
        """
        pass
    @Status.setter
    def Status(self, status: str):
        """
        Setter for property: (str) Status
         Returns the issue status   
            
         
        """
        pass
    @property
    def Title(self) -> str:
        """
        Getter for property: (str) Title
         Returns the issue title   
            
         
        """
        pass
    @Title.setter
    def Title(self, title: str):
        """
        Setter for property: (str) Title
         Returns the issue title   
            
         
        """
        pass
    def AddAttachment(self, attachment: IssueAttachment) -> None:
        """
         Adds an NXOpen.Issue.IssueAttachment 
        """
        pass
    def GetAllAttachments(self) -> List[IssueAttachment]:
        """
         Returns all the NXOpen.Issue.IssueAttachments 
         Returns attachments ( IssueAttachment List[NXO): .
        """
        pass
    def GetAttachment(self, attachmentName: str) -> IssueAttachment:
        """
         Returns the NXOpen.Issue.IssueAttachment with this attachment name 
         Returns attachment ( IssueAttachment NXOpe): .
        """
        pass
    def GetEditableUserProperties(self) -> List[IssueProperty]:
        """
         Returns the editable user defined NXOpen.Issue.IssuePropertys 
         Returns properties ( IssueProperty List[NXO): .
        """
        pass
    def GetPropertyValue(self, propertyName: str) -> str:
        """
         Returns the value of NXOpen.Issue.IssueProperty 
         Returns propertyValue (str): .
        """
        pass
    def RemoveAttachment(self, attachment: IssueAttachment) -> None:
        """
         Removes an NXOpen.Issue.IssueAttachment 
        """
        pass
    def SetPreviewImage(self, attachment: IssueAttachment) -> None:
        """
         Sets preview image 
        """
        pass
    def SetPropertyValue(self, propertyName: str, propertyValue: str) -> None:
        """
         Sets the value of NXOpen.Issue.IssueProperty 
        """
        pass
import NXOpen
class IssueContent(NXOpen.NXObject): 
    """ Represents the Issue Issue object. """
    @property
    def AssignedUser(self) -> str:
        """
        Getter for property: (str) AssignedUser
         Returns the assigned user   
            
         
        """
        pass
    @AssignedUser.setter
    def AssignedUser(self, assignedUser: str):
        """
        Setter for property: (str) AssignedUser
         Returns the assigned user   
            
         
        """
        pass
    @property
    def Comment(self) -> str:
        """
        Getter for property: (str) Comment
         Returns the issue comment   
            
         
        """
        pass
    @Comment.setter
    def Comment(self, comment: str):
        """
        Setter for property: (str) Comment
         Returns the issue comment   
            
         
        """
        pass
    @property
    def DueDate(self) -> str:
        """
        Getter for property: (str) DueDate
         Returns the due date   
            
         
        """
        pass
    @DueDate.setter
    def DueDate(self, dueDate: str):
        """
        Setter for property: (str) DueDate
         Returns the due date   
            
         
        """
        pass
    @property
    def IsLocked(self) -> bool:
        """
        Getter for property: (bool) IsLocked
         Returns the lock state   
            
         
        """
        pass
    @property
    def IssueId(self) -> str:
        """
        Getter for property: (str) IssueId
         Returns the issue id   
            
         
        """
        pass
    @property
    def PreviewImage(self) -> IssueAttachment:
        """
        Getter for property: ( IssueAttachment NXOpe) PreviewImage
         Returns the preview image   
            
         
        """
        pass
    @PreviewImage.setter
    def PreviewImage(self, previewImage: IssueAttachment):
        """
        Setter for property: ( IssueAttachment NXOpe) PreviewImage
         Returns the preview image   
            
         
        """
        pass
    @property
    def Priority(self) -> str:
        """
        Getter for property: (str) Priority
         Returns the issue priority   
            
         
        """
        pass
    @Priority.setter
    def Priority(self, priority: str):
        """
        Setter for property: (str) Priority
         Returns the issue priority   
            
         
        """
        pass
    @property
    def Status(self) -> str:
        """
        Getter for property: (str) Status
         Returns the issue status   
            
         
        """
        pass
    @Status.setter
    def Status(self, status: str):
        """
        Setter for property: (str) Status
         Returns the issue status   
            
         
        """
        pass
    @property
    def Title(self) -> str:
        """
        Getter for property: (str) Title
         Returns the issue title   
            
         
        """
        pass
    @Title.setter
    def Title(self, title: str):
        """
        Setter for property: (str) Title
         Returns the issue title   
            
         
        """
        pass
    def AddAttachment(self, attachment: IssueAttachment) -> None:
        """
         Adds an NXOpen.Issue.IssueAttachment 
        """
        pass
    def Close(self, coseNote: str) -> None:
        """
         Closes the issue 
        """
        pass
    def DiscardIssue(self) -> None:
        """
         Discards the newly created issue which has not saved in external db yet 
        """
        pass
    def GetAllAttachments(self) -> List[IssueAttachment]:
        """
         Returns all the NXOpen.Issue.IssueAttachments 
         Returns attachments ( IssueAttachment List[NXO): .
        """
        pass
    def GetAttachment(self, attachmentName: str) -> IssueAttachment:
        """
         Returns the NXOpen.Issue.IssueAttachment with this attachment name 
         Returns attachment ( IssueAttachment NXOpe): .
        """
        pass
    def GetChildAttachments(self) -> List[IssueAttachment]:
        """
         Returns the child NXOpen.Issue.IssueAttachments 
         Returns attachments ( IssueAttachment List[NXO): .
        """
        pass
    def GetFolders(self) -> List[IssueFolder]:
        """
         Returns all the child NXOpen.Issue.IssueFolders 
         Returns folders ( IssueFolder List[NXO): .
        """
        pass
    def GetPartAttachment(self) -> IssueAttachment:
        """
         Returns the NXOpen.Issue.IssueAttachment with part type 
         Returns attachment ( IssueAttachment NXOpe): .
        """
        pass
    def GetProperty(self, propertyName: str) -> IssueProperty:
        """
         Returns the NXOpen.Issue.IssueProperty with this property name 
         Returns property ( IssueProperty NXOpe): .
        """
        pass
    def GetPropertyValue(self, propertyName: str) -> str:
        """
         Returns the value of NXOpen.Issue.IssueProperty 
         Returns propertyValue (str): .
        """
        pass
    def GetUserProperties(self) -> List[IssueProperty]:
        """
         Returns the user definded NXOpen.Issue.IssuePropertys 
         Returns properties ( IssueProperty List[NXO): .
        """
        pass
    def IsCheckedOut(self) -> Tuple[bool, str]:
        """
         Returns whether the issue is checked out  
         Returns A tuple consisting of (isCheckOut, user). 
         - isCheckOut is: bool.
         - user is: str.

        """
        pass
    def IsClosed(self) -> bool:
        """
         Returns whether the issue is closed 
         Returns isClosed (bool): .
        """
        pass
    def IsReadOnly(self) -> bool:
        """
         Returns whether the issue is read only 
         Returns isReadOnly (bool): .
        """
        pass
    def LoadAttachments(self) -> None:
        """
         Loads the NXOpen.Issue.IssueAttachments 
        """
        pass
    def ReloadProperties(self) -> None:
        """
         Reloads all the NXOpen.Issue.IssuePropertys 
        """
        pass
    def RemoveAttachment(self, attachment: IssueAttachment) -> None:
        """
         Removes an NXOpen.Issue.IssueAttachment 
        """
        pass
    def Review(self, reviewDecision: str, comment: str) -> None:
        """
         Signs off the current workflow task with decision 
        """
        pass
    def SaveChanges(self) -> None:
        """
         Saves the changes to issue server 
        """
        pass
    def SendToWorkflow(self, workflowTemplate: str) -> None:
        """
         Sends the issue to workflow process 
        """
        pass
    def SetPropertyValue(self, propertyName: str, propertyValue: str) -> None:
        """
         Sets the value of NXOpen.Issue.IssueProperty 
        """
        pass
import NXOpen
class IssueFolder(NXOpen.NXObject): 
    """ Represents the Issue Folder object. """
    class Type(Enum):
        """
        Members Include: 
         |ProblemItems|  Problem items type     
         |ImpactedItems|  Impacted items type    
         |ReferenceItems|  Reference items type   
         |ImplementedBy|  Implemented by type    
         |IssueImage|  Issue image type       
         |IssueFixedImage|  Issue fixed image type 
         |SnapshotBeforeFix|  Snapshot before fix type 
         |SnapshotAfterFix|  Snapshot after fix type 
         |ValidationResults|  ValidationResult type 

        """
        ProblemItems: int
        ImpactedItems: int
        ReferenceItems: int
        ImplementedBy: int
        IssueImage: int
        IssueFixedImage: int
        SnapshotBeforeFix: int
        SnapshotAfterFix: int
        ValidationResults: int
        @staticmethod
        def ValueOf(value: int) -> IssueFolder.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FolderType(self) -> IssueFolder.Type:
        """
        Getter for property: ( IssueFolder.Type NXOpe) FolderType
         Returns the folder type   
            
         
        """
        pass
    def AddAttachment(self, attachment: IssueAttachment) -> None:
        """
         Adds an NXOpen.Issue.IssueAttachment 
        """
        pass
    def GetAttachments(self) -> List[IssueAttachment]:
        """
         Returns the child NXOpen.Issue.IssueAttachments 
         Returns attachments ( IssueAttachment List[NXO): .
        """
        pass
    def RemoveAttachment(self, attachment: IssueAttachment) -> None:
        """
         Removes an NXOpen.Issue.IssueAttachment 
        """
        pass
import NXOpen
class IssueListCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a NXOpen.Issue.IssueListCollection """
    def FindObject(self, name: str) -> IssueList:
        """
         Finds the NXOpen.Issue.IssueList with the given name.
                    An exception will be thrown if no object can be found with given name. 
         Returns list ( IssueList NXOpe):  NXOpen.Issue.IssueList with this name. .
        """
        pass
import NXOpen
class IssueList(NXOpen.NXObject): 
    """ Represents the Issue List object. """
    def ChangeConfig(self, queryName: str, criteriaTitles: List[str], criteriaValues: List[str]) -> None:
        """
         Changes the config of NXOpen.Issue.IssueList 
        """
        pass
    def DiscardChanges(self) -> None:
        """
         Discards the modified NXOpen.Issue.IssueContents 
        """
        pass
    def ExistsInDatabase(self) -> bool:
        """
         Returns whether the list exists in database 
         Returns exists (bool): .
        """
        pass
    def GetIssues(self) -> List[IssueContent]:
        """
         Returns all the NXOpen.Issue.IssueContents 
         Returns issues ( IssueContent List[NXO): .
        """
        pass
    def ReloadIssues(self) -> None:
        """
         Reloads the NXOpen.Issue.IssueContents 
        """
        pass
    def ResetConfig(self) -> None:
        """
         Resets the config of NXOpen.Issue.IssueList 
        """
        pass
    def SaveChanges(self) -> None:
        """
         Saves the modified NXOpen.Issue.IssueContents 
        """
        pass
    def SaveConfig(self) -> None:
        """
         Saves the config of NXOpen.Issue.IssueList to server 
        """
        pass
    def SetRelatedParts(self, parts: List[NXOpen.NXObject]) -> None:
        """
         Sets the related parts of NXOpen.Issue.IssueList 
        """
        pass
import NXOpen
class IssueManager(NXOpen.Object): 
    """ Contains the collection objects for creating and iterating over issue objects. """
    class Mode(Enum):
        """
        Members Include: 
         |TeamcenterCommunity|  Teamcenter community mode 
         |Teamcenter|  Teamcenter mode           
         |Briefcase|  Briefcase mode       

        """
        TeamcenterCommunity: int
        Teamcenter: int
        Briefcase: int
        @staticmethod
        def ValueOf(value: int) -> IssueManager.Mode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class State(Enum):
        """
        Members Include: 
         |Original|  Original state 
         |Created|  Created state  
         |Modified|  Modified state 
         |Removed|  Removed state  

        """
        Original: int
        Created: int
        Modified: int
        Removed: int
        @staticmethod
        def ValueOf(value: int) -> IssueManager.State:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CurrentMode(self) -> IssueManager.Mode:
        """
        Getter for property: ( IssueManager.Mode NXOpe) CurrentMode
         Returns the current mode   
            
         
        """
        pass
    @CurrentMode.setter
    def CurrentMode(self, mode: IssueManager.Mode):
        """
        Setter for property: ( IssueManager.Mode NXOpe) CurrentMode
         Returns the current mode   
            
         
        """
        pass
    @property
    def CurrentSite(self) -> IssueSite:
        """
        Getter for property: ( IssueSite NXOpe) CurrentSite
         Returns the current  NXOpen::Issue::IssueSite    
            
         
        """
        pass
    @property
    def IssueListCollection() -> IssueListCollection:
        """
         Returns the  NXOpen::Issue::IssueListCollection  instance 
        """
        pass
    def CaptureAndCreateAttachmentForSnapshot() -> IssueAttachment:
        """
         Creates a NXOpen.Issue.IssueAttachment for Snapshot 
         Returns attachObj ( IssueAttachment NXOpe): .
        """
        pass
    def Connect(siteUrl: str, userName: str, password: str) -> IssueSite:
        """
         Connects to issue server and returns the NXOpen.Issue.IssueSite 
         Returns site ( IssueSite NXOpe): .
        """
        pass
    def CreateAttachmentForBookMark() -> IssueAttachment:
        """
         Creates a NXOpen.Issue.IssueAttachment for BookMark 
         Returns attachObj ( IssueAttachment NXOpe): .
        """
        pass
    def CreateAttachmentForScreenImage() -> IssueAttachment:
        """
         Creates a NXOpen.Issue.IssueAttachment for ScreenImage 
         Returns attachObj ( IssueAttachment NXOpe): .
        """
        pass
    def CreateAttachmentForSnapshot(bookmarkFileSpec: str, imageFileSpec: str, name: str) -> IssueAttachment:
        """
         Creates a NXOpen.Issue.IssueAttachment for Sanpshot 
         Returns attachment ( IssueAttachment NXOpe): .
        """
        pass
    def CreateBriefcase(briefcaseName: str, filePath: str) -> IssueBriefcase:
        """
         Creates an NXOpen.Issue.IssueBriefcase. 
         Returns briefcase ( IssueBriefcase NXOpe): .
        """
        pass
    def CreateIssueAttachment(fileSpec: str, name: str, type: IssueAttachment.Type) -> IssueAttachment:
        """
         Creates a NXOpen.Issue.IssueAttachment 
         Returns attachment ( IssueAttachment NXOpe): .
        """
        pass
    def CreateIssueContent(list: IssueList) -> IssueContent:
        """
         Creates a NXOpen.Issue.IssueContent 
         Returns issue ( IssueContent NXOpe): .
        """
        pass
    def CreateIssueContentBuilder(issue: IssueContent) -> IssueContentBuilder:
        """
         Creates a NXOpen.Issue.IssueContentBuilder 
         Returns builder ( IssueContentBuilder NXOpe): .
        """
        pass
    def CreateIssueSnapshotSubsetBuilder(subsetPart: NXOpen.Part) -> SnapshotSubsetBuilder:
        """
         Creates a NXOpen.Issue.SnapshotSubsetBuilder 
         Returns builder ( SnapshotSubsetBuilder NXOpe): .
        """
        pass
    def CreateIssueSnapshotWorksetBuilder(issue: IssueContent) -> SnapshotWorksetBuilder:
        """
         Creates a NXOpen.Issue.SnapshotWorksetBuilder 
         Returns builder ( SnapshotWorksetBuilder NXOpe): .
        """
        pass
    def Disconnect() -> None:
        """
         Disconnects from issue server 
        """
        pass
    def GetAttachmentState(attachment: IssueAttachment) -> IssueManager.State:
        """
         Gets the modified state of NXOpen.Issue.IssueAttachment 
         Returns state ( IssueManager.State NXOpe): .
        """
        pass
    def GetIssueState(issue: IssueContent) -> IssueManager.State:
        """
         Gets the modified state of NXOpen.Issue.IssueContent 
         Returns state ( IssueManager.State NXOpe): .
        """
        pass
    def GetPropertyState(property: IssueProperty) -> IssueManager.State:
        """
         Gets the modified state of NXOpen.Issue.IssueProperty 
         Returns state ( IssueManager.State NXOpe): .
        """
        pass
    def GetWorkingList() -> IssueList:
        """
         Gets the current working NXOpen.Issue.IssueList 
         Returns list ( IssueList NXOpe): .
        """
        pass
    def OpenBriefcase(filePath: str) -> IssueBriefcase:
        """
         Opens an NXOpen.Issue.IssueBriefcase .
         Returns list ( IssueBriefcase NXOpe): .
        """
        pass
    def SetWorkingList(list: IssueList) -> None:
        """
         Sets the current working NXOpen.Issue.IssueList 
        """
        pass
import NXOpen
class IssueProperty(NXOpen.NXObject): 
    """ Represents the Issue Property object. """
    class Type(Enum):
        """
        Members Include: 
         |Text|  Text type 
         |Note|  Note type 
         |User|  User type 
         |Choice|  Choice type 
         |Url|  URL type  
         |Boolean|  Boolean type 
         |Date|  Date type  
         |Number|  Number type 
         |Integer|  Integer type 
         |Point3D|  3D point type 
         |Vector3D|  3D vector type 

        """
        Text: int
        Note: int
        User: int
        Choice: int
        Url: int
        Boolean: int
        Date: int
        Number: int
        Integer: int
        Point3D: int
        Vector3D: int
        @staticmethod
        def ValueOf(value: int) -> IssueProperty.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def IsReadOnly(self) -> bool:
        """
        Getter for property: (bool) IsReadOnly
         Returns whether the property is read only   
            
         
        """
        pass
    @property
    def StringValue(self) -> str:
        """
        Getter for property: (str) StringValue
         Returns the string value   
            
         
        """
        pass
    @property
    def ValueType(self) -> IssueProperty.Type:
        """
        Getter for property: ( IssueProperty.Type NXOpe) ValueType
         Returns the property type   
            
         
        """
        pass
    def GetChoices(self) -> List[str]:
        """
         Returns the choices  
         Returns choices (List[str]): .
        """
        pass
    def GetDefaultChoice(self) -> str:
        """
         Returns the default choice  
         Returns defaultChoice (str): .
        """
        pass
import NXOpen
class IssueSite(NXOpen.NXObject): 
    """ Represents the Issue Site object. """
    def CreateList(self, listName: str, queryName: str, criteriaTitles: List[str], criteriaValues: List[str]) -> IssueList:
        """
         Creates an NXOpen.Issue.IssueList 
         Returns list ( IssueList NXOpe): .
        """
        pass
    def GetQuickSearchList(self) -> IssueList:
        """
         Gets the NXOpen.Issue.IssueList for quick search 
         Returns list ( IssueList NXOpe): .
        """
        pass
    def IsConnected(self) -> bool:
        """
         Returns whether the site is connected 
         Returns isConnected (bool): .
        """
        pass
    def RemoveList(self, list: IssueList) -> None:
        """
         Removes an NXOpen.Issue.IssueList 
        """
        pass
import NXOpen
import NXOpen.Assemblies
class SnapshotSubsetBuilder(NXOpen.Builder): 
    """ Used to create or edit issue snapshot subset. """
    class ContextType(Enum):
        """
        Members Include: 
         |Problem|  Problem Subset 
         |Impacted|  Impacted Subset 
         |Reference|  Reference Subset 

        """
        Problem: int
        Impacted: int
        Reference: int
        @staticmethod
        def ValueOf(value: int) -> SnapshotSubsetBuilder.ContextType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Context(self) -> SnapshotSubsetBuilder.ContextType:
        """
        Getter for property: ( SnapshotSubsetBuilder.ContextType NXOpe) Context
         Returns the context indicating the issue snapshot subset type.  
             
         
        """
        pass
    @Context.setter
    def Context(self, context: SnapshotSubsetBuilder.ContextType):
        """
        Setter for property: ( SnapshotSubsetBuilder.ContextType NXOpe) Context
         Returns the context indicating the issue snapshot subset type.  
             
         
        """
        pass
    @property
    def SelectParts(self) -> NXOpen.Assemblies.SelectComponentList:
        """
        Getter for property: ( NXOpen.Assemblies.SelectComponentList) SelectParts
         Returns the select parts which will be collected into issue snapshot subset.  
             
         
        """
        pass
import NXOpen
class SnapshotWorksetBuilder(NXOpen.Builder): 
    """ 
    Used to create or edit issue snapshot workset which is a container to hold all the corresponding 
    parts to represent an issue.
     """
    @property
    def ImpactedSubset(self) -> SnapshotSubsetBuilder:
        """
        Getter for property: ( SnapshotSubsetBuilder NXOpe) ImpactedSubset
         Returns the impactedSubset containing the impacted parts.  
             
         
        """
        pass
    @property
    def ProblemSubset(self) -> SnapshotSubsetBuilder:
        """
        Getter for property: ( SnapshotSubsetBuilder NXOpe) ProblemSubset
         Returns the problemSubset containing the problem parts.  
             
         
        """
        pass
    @property
    def ReferenceSubset(self) -> SnapshotSubsetBuilder:
        """
        Getter for property: ( SnapshotSubsetBuilder NXOpe) ReferenceSubset
         Returns the referenceSubset containing the reference parts.  
             
         
        """
        pass
