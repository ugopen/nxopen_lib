from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Represents the Issue Attachment object.  <br> To create a new instance of this class, use @link NXOpen::Issue::IssueManager::CreateIssueAttachment  NXOpen::Issue::IssueManager::CreateIssueAttachment @endlink  <br> 
## 
##   <br>  Created in NX8.5.0  <br> 

class IssueAttachment(NXOpen.NXObject): 
    """ Represents the Issue Attachment object. """


    ##  Represents the possible attachment types
    ##              for a @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink .
    ##         
    ##  Generic type 
    class Type(Enum):
        """
        Members Include: <Generic> <Text> <Part> <Xml> <Image> <ValidationLog> <Bookmark> <Snapshot> <ValidationResult> <Workset> <ShapeDesignElement> <ReuseDesignElement> <SubordinateDesignElement> <PromissoryDesignElement> <DesignControlElement> <Subset> <MSWord> <MSExcel> <MSPowerPoint> <VisualizationSession>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> IssueAttachment.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link IssueAttachment.Type NXOpen.Issue.IssueAttachment.Type@endlink) AttachmentType
    ##   the attachment type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return IssueAttachment.Type
    @property
    def AttachmentType(self) -> IssueAttachment.Type:
        """
        Getter for property: (@link IssueAttachment.Type NXOpen.Issue.IssueAttachment.Type@endlink) AttachmentType
          the attachment type   
            
         
        """
        pass
    
    ## Setter for property: (@link IssueAttachment.Type NXOpen.Issue.IssueAttachment.Type@endlink) AttachmentType

    ##   the attachment type   
    ##     
    ##  
    ## Setter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @AttachmentType.setter
    def AttachmentType(self, type: IssueAttachment.Type):
        """
        Setter for property: (@link IssueAttachment.Type NXOpen.Issue.IssueAttachment.Type@endlink) AttachmentType
          the attachment type   
            
         
        """
        pass
    
    ## Getter for property: (str) ReferencedAttachmentId
    ##   the refereced attachment id which specifies one attachment that is related 
    ##         to this @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def ReferencedAttachmentId(self) -> str:
        """
        Getter for property: (str) ReferencedAttachmentId
          the refereced attachment id which specifies one attachment that is related 
                to this @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink    
            
         
        """
        pass
    
    ## Setter for property: (str) ReferencedAttachmentId

    ##   the refereced attachment id which specifies one attachment that is related 
    ##         to this @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink    
    ##     
    ##  
    ## Setter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ReferencedAttachmentId.setter
    def ReferencedAttachmentId(self, referencedAttachmentId: str):
        """
        Setter for property: (str) ReferencedAttachmentId
          the refereced attachment id which specifies one attachment that is related 
                to this @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink    
            
         
        """
        pass
    
    ##  Recapture the snapshot 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ## <param name="bookmarkFileSpec"> (str) </param>
    ## <param name="imageFileSpec"> (str) </param>
    def RecaptureSnapshot(attachment: IssueAttachment, bookmarkFileSpec: str, imageFileSpec: str) -> None:
        """
         Recapture the snapshot 
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Issue::IssueBriefcase NXOpen::Issue::IssueBriefcase@endlink  synchronize builder  <br> To create a new instance of this class, use @link NXOpen::Issue::IssueBriefcase::CreateSynchronizeContentBuilder  NXOpen::Issue::IssueBriefcase::CreateSynchronizeContentBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class IssueBriefcaseSynchronizeBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Issue.IssueBriefcase</ja_class> synchronize builder """


    ##  Adds an part type @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink ,
    ##         only the added parts can be synchronized to server.
    ##         
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ## <param name="attachment"> (@link IssueAttachment NXOpen.Issue.IssueAttachment@endlink) </param>
    def AddPartAttachment(builder: IssueBriefcaseSynchronizeBuilder, attachment: IssueAttachment) -> None:
        """
         Adds an part type @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink ,
                only the added parts can be synchronized to server.
                
        """
        pass
    
    ##  Adds an part type @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink . 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ## <param name="attachment"> (@link IssueAttachment NXOpen.Issue.IssueAttachment@endlink) </param>
    def RemovePartAttachment(builder: IssueBriefcaseSynchronizeBuilder, attachment: IssueAttachment) -> None:
        """
         Adds an part type @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink . 
        """
        pass
    
##  Represents the Issue Briefcase object. 
## 
##   <br>  Created in NX10.0.0  <br> 

class IssueBriefcase(IssueList): 
    """ Represents the Issue Briefcase object. """


    ## Getter for property: (str) Location
    ##   the briefcase location  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def Location(self) -> str:
        """
        Getter for property: (str) Location
          the briefcase location  
            
         
        """
        pass
    
    ## Setter for property: (str) Location

    ##   the briefcase location  
    ##     
    ##  
    ## Setter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Location.setter
    def Location(self, folder: str):
        """
        Setter for property: (str) Location
          the briefcase location  
            
         
        """
        pass
    
    ##  Adds an @link NXOpen::Issue::IssueContent NXOpen::Issue::IssueContent@endlink  from an existing @link NXOpen::Issue::IssueContent NXOpen::Issue::IssueContent@endlink . 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ## <param name="issue"> (@link IssueContent NXOpen.Issue.IssueContent@endlink) </param>
    def AddIssue(briefcase: IssueBriefcase, issue: IssueContent) -> None:
        """
         Adds an @link NXOpen::Issue::IssueContent NXOpen::Issue::IssueContent@endlink  from an existing @link NXOpen::Issue::IssueContent NXOpen::Issue::IssueContent@endlink . 
        """
        pass
    
    ##  Closes @link NXOpen::Issue::IssueBriefcase NXOpen::Issue::IssueBriefcase@endlink . 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    @staticmethod
    def Close(briefcase: IssueBriefcase) -> None:
        """
         Closes @link NXOpen::Issue::IssueBriefcase NXOpen::Issue::IssueBriefcase@endlink . 
        """
        pass
    
    ##  Creates an @link NXOpen::Issue::IssueBriefcaseSynchronizeBuilder NXOpen::Issue::IssueBriefcaseSynchronizeBuilder@endlink  
    ##  @return builder (@link IssueBriefcaseSynchronizeBuilder NXOpen.Issue.IssueBriefcaseSynchronizeBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    def CreateSynchronizeContentBuilder(briefcase: IssueBriefcase) -> IssueBriefcaseSynchronizeBuilder:
        """
         Creates an @link NXOpen::Issue::IssueBriefcaseSynchronizeBuilder NXOpen::Issue::IssueBriefcaseSynchronizeBuilder@endlink  
         @return builder (@link IssueBriefcaseSynchronizeBuilder NXOpen.Issue.IssueBriefcaseSynchronizeBuilder@endlink): .
        """
        pass
    
    ##  Removes an @link NXOpen::Issue::IssueContent NXOpen::Issue::IssueContent@endlink . 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ## <param name="issue"> (@link IssueContent NXOpen.Issue.IssueContent@endlink) </param>
    def RemoveIssue(briefcase: IssueBriefcase, issue: IssueContent) -> None:
        """
         Removes an @link NXOpen::Issue::IssueContent NXOpen::Issue::IssueContent@endlink . 
        """
        pass
    
    ##  Saves all @link NXOpen::Issue::IssueContent NXOpen::Issue::IssueContent@endlink s. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    @staticmethod
    def Save(briefcase: IssueBriefcase) -> None:
        """
         Saves all @link NXOpen::Issue::IssueContent NXOpen::Issue::IssueContent@endlink s. 
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Issue::IssueContent NXOpen::Issue::IssueContent@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Issue::IssueManager::CreateIssueContentBuilder  NXOpen::Issue::IssueManager::CreateIssueContentBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Title </term> <description> 
##  
## New Issue </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX8.5.0  <br> 

class IssueContentBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Issue.IssueContent</ja_class> builder """


    ## Getter for property: (str) AssignedUser
    ##   the assigned user   
    ##     
    ##  
    ## Getter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def AssignedUser(self) -> str:
        """
        Getter for property: (str) AssignedUser
          the assigned user   
            
         
        """
        pass
    
    ## Setter for property: (str) AssignedUser

    ##   the assigned user   
    ##     
    ##  
    ## Setter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @AssignedUser.setter
    def AssignedUser(self, assignedUser: str):
        """
        Setter for property: (str) AssignedUser
          the assigned user   
            
         
        """
        pass
    
    ## Getter for property: (str) Comment
    ##   the issue comment   
    ##     
    ##  
    ## Getter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Comment(self) -> str:
        """
        Getter for property: (str) Comment
          the issue comment   
            
         
        """
        pass
    
    ## Setter for property: (str) Comment

    ##   the issue comment   
    ##     
    ##  
    ## Setter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Comment.setter
    def Comment(self, comment: str):
        """
        Setter for property: (str) Comment
          the issue comment   
            
         
        """
        pass
    
    ## Getter for property: (str) DueDate
    ##   the due date   
    ##     
    ##  
    ## Getter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def DueDate(self) -> str:
        """
        Getter for property: (str) DueDate
          the due date   
            
         
        """
        pass
    
    ## Setter for property: (str) DueDate

    ##   the due date   
    ##     
    ##  
    ## Setter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @DueDate.setter
    def DueDate(self, dueDate: str):
        """
        Setter for property: (str) DueDate
          the due date   
            
         
        """
        pass
    
    ## Getter for property: (str) Priority
    ##   the issue priority   
    ##     
    ##  
    ## Getter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Priority(self) -> str:
        """
        Getter for property: (str) Priority
          the issue priority   
            
         
        """
        pass
    
    ## Setter for property: (str) Priority

    ##   the issue priority   
    ##     
    ##  
    ## Setter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Priority.setter
    def Priority(self, priority: str):
        """
        Setter for property: (str) Priority
          the issue priority   
            
         
        """
        pass
    
    ## Getter for property: (str) Status
    ##   the issue status   
    ##     
    ##  
    ## Getter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Status(self) -> str:
        """
        Getter for property: (str) Status
          the issue status   
            
         
        """
        pass
    
    ## Setter for property: (str) Status

    ##   the issue status   
    ##     
    ##  
    ## Setter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Status.setter
    def Status(self, status: str):
        """
        Setter for property: (str) Status
          the issue status   
            
         
        """
        pass
    
    ## Getter for property: (str) Title
    ##   the issue title   
    ##     
    ##  
    ## Getter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Title(self) -> str:
        """
        Getter for property: (str) Title
          the issue title   
            
         
        """
        pass
    
    ## Setter for property: (str) Title

    ##   the issue title   
    ##     
    ##  
    ## Setter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Title.setter
    def Title(self, title: str):
        """
        Setter for property: (str) Title
          the issue title   
            
         
        """
        pass
    
    ##  Adds an @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink  
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ## <param name="attachment"> (@link IssueAttachment NXOpen.Issue.IssueAttachment@endlink) </param>
    def AddAttachment(builder: IssueContentBuilder, attachment: IssueAttachment) -> None:
        """
         Adds an @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink  
        """
        pass
    
    ##  Returns all the @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink s 
    ##  @return attachments (@link IssueAttachment List[NXOpen.Issue.IssueAttachment]@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    @staticmethod
    def GetAllAttachments(builder: IssueContentBuilder) -> List[IssueAttachment]:
        """
         Returns all the @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink s 
         @return attachments (@link IssueAttachment List[NXOpen.Issue.IssueAttachment]@endlink): .
        """
        pass
    
    ##  Returns the @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink  with this attachment name 
    ##  @return attachment (@link IssueAttachment NXOpen.Issue.IssueAttachment@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ## <param name="attachmentName"> (str) </param>
    def GetAttachment(builder: IssueContentBuilder, attachmentName: str) -> IssueAttachment:
        """
         Returns the @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink  with this attachment name 
         @return attachment (@link IssueAttachment NXOpen.Issue.IssueAttachment@endlink): .
        """
        pass
    
    ##  Returns the editable user defined @link NXOpen::Issue::IssueProperty NXOpen::Issue::IssueProperty@endlink s 
    ##  @return properties (@link IssueProperty List[NXOpen.Issue.IssueProperty]@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    @staticmethod
    def GetEditableUserProperties(builder: IssueContentBuilder) -> List[IssueProperty]:
        """
         Returns the editable user defined @link NXOpen::Issue::IssueProperty NXOpen::Issue::IssueProperty@endlink s 
         @return properties (@link IssueProperty List[NXOpen.Issue.IssueProperty]@endlink): .
        """
        pass
    
    ##  Returns the value of @link NXOpen::Issue::IssueProperty NXOpen::Issue::IssueProperty@endlink  
    ##  @return propertyValue (str): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ## <param name="propertyName"> (str) </param>
    def GetPropertyValue(builder: IssueContentBuilder, propertyName: str) -> str:
        """
         Returns the value of @link NXOpen::Issue::IssueProperty NXOpen::Issue::IssueProperty@endlink  
         @return propertyValue (str): .
        """
        pass
    
    ##  Removes an @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink  
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ## <param name="attachment"> (@link IssueAttachment NXOpen.Issue.IssueAttachment@endlink) </param>
    def RemoveAttachment(builder: IssueContentBuilder, attachment: IssueAttachment) -> None:
        """
         Removes an @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink  
        """
        pass
    
    ##  Sets preview image 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ## <param name="attachment"> (@link IssueAttachment NXOpen.Issue.IssueAttachment@endlink) </param>
    def SetPreviewImage(builder: IssueContentBuilder, attachment: IssueAttachment) -> None:
        """
         Sets preview image 
        """
        pass
    
    ##  Sets the value of @link NXOpen::Issue::IssueProperty NXOpen::Issue::IssueProperty@endlink  
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ## <param name="propertyName"> (str) </param>
    ## <param name="propertyValue"> (str) </param>
    def SetPropertyValue(builder: IssueContentBuilder, propertyName: str, propertyValue: str) -> None:
        """
         Sets the value of @link NXOpen::Issue::IssueProperty NXOpen::Issue::IssueProperty@endlink  
        """
        pass
    
import NXOpen
##  Represents the Issue Issue object.  <br> To create a new instance of this class, use @link NXOpen::Issue::IssueManager::CreateIssueContent  NXOpen::Issue::IssueManager::CreateIssueContent @endlink  <br> 
## 
##   <br>  Created in NX8.5.0  <br> 

class IssueContent(NXOpen.NXObject): 
    """ Represents the Issue Issue object. """


    ## Getter for property: (str) AssignedUser
    ##   the assigned user   
    ##     
    ##  
    ## Getter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def AssignedUser(self) -> str:
        """
        Getter for property: (str) AssignedUser
          the assigned user   
            
         
        """
        pass
    
    ## Setter for property: (str) AssignedUser

    ##   the assigned user   
    ##     
    ##  
    ## Setter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @AssignedUser.setter
    def AssignedUser(self, assignedUser: str):
        """
        Setter for property: (str) AssignedUser
          the assigned user   
            
         
        """
        pass
    
    ## Getter for property: (str) Comment
    ##   the issue comment   
    ##     
    ##  
    ## Getter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Comment(self) -> str:
        """
        Getter for property: (str) Comment
          the issue comment   
            
         
        """
        pass
    
    ## Setter for property: (str) Comment

    ##   the issue comment   
    ##     
    ##  
    ## Setter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Comment.setter
    def Comment(self, comment: str):
        """
        Setter for property: (str) Comment
          the issue comment   
            
         
        """
        pass
    
    ## Getter for property: (str) DueDate
    ##   the due date   
    ##     
    ##  
    ## Getter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def DueDate(self) -> str:
        """
        Getter for property: (str) DueDate
          the due date   
            
         
        """
        pass
    
    ## Setter for property: (str) DueDate

    ##   the due date   
    ##     
    ##  
    ## Setter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @DueDate.setter
    def DueDate(self, dueDate: str):
        """
        Setter for property: (str) DueDate
          the due date   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsLocked
    ##   the lock state   
    ##     
    ##  
    ## Getter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def IsLocked(self) -> bool:
        """
        Getter for property: (bool) IsLocked
          the lock state   
            
         
        """
        pass
    
    ## Getter for property: (str) IssueId
    ##   the issue id   
    ##     
    ##  
    ## Getter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def IssueId(self) -> str:
        """
        Getter for property: (str) IssueId
          the issue id   
            
         
        """
        pass
    
    ## Getter for property: (@link IssueAttachment NXOpen.Issue.IssueAttachment@endlink) PreviewImage
    ##   the preview image   
    ##     
    ##  
    ## Getter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return IssueAttachment
    @property
    def PreviewImage(self) -> IssueAttachment:
        """
        Getter for property: (@link IssueAttachment NXOpen.Issue.IssueAttachment@endlink) PreviewImage
          the preview image   
            
         
        """
        pass
    
    ## Setter for property: (@link IssueAttachment NXOpen.Issue.IssueAttachment@endlink) PreviewImage

    ##   the preview image   
    ##     
    ##  
    ## Setter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @PreviewImage.setter
    def PreviewImage(self, previewImage: IssueAttachment):
        """
        Setter for property: (@link IssueAttachment NXOpen.Issue.IssueAttachment@endlink) PreviewImage
          the preview image   
            
         
        """
        pass
    
    ## Getter for property: (str) Priority
    ##   the issue priority   
    ##     
    ##  
    ## Getter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Priority(self) -> str:
        """
        Getter for property: (str) Priority
          the issue priority   
            
         
        """
        pass
    
    ## Setter for property: (str) Priority

    ##   the issue priority   
    ##     
    ##  
    ## Setter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Priority.setter
    def Priority(self, priority: str):
        """
        Setter for property: (str) Priority
          the issue priority   
            
         
        """
        pass
    
    ## Getter for property: (str) Status
    ##   the issue status   
    ##     
    ##  
    ## Getter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Status(self) -> str:
        """
        Getter for property: (str) Status
          the issue status   
            
         
        """
        pass
    
    ## Setter for property: (str) Status

    ##   the issue status   
    ##     
    ##  
    ## Setter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Status.setter
    def Status(self, status: str):
        """
        Setter for property: (str) Status
          the issue status   
            
         
        """
        pass
    
    ## Getter for property: (str) Title
    ##   the issue title   
    ##     
    ##  
    ## Getter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Title(self) -> str:
        """
        Getter for property: (str) Title
          the issue title   
            
         
        """
        pass
    
    ## Setter for property: (str) Title

    ##   the issue title   
    ##     
    ##  
    ## Setter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Title.setter
    def Title(self, title: str):
        """
        Setter for property: (str) Title
          the issue title   
            
         
        """
        pass
    
    ##  Adds an @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink  
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ## <param name="attachment"> (@link IssueAttachment NXOpen.Issue.IssueAttachment@endlink) </param>
    def AddAttachment(issue: IssueContent, attachment: IssueAttachment) -> None:
        """
         Adds an @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink  
        """
        pass
    
    ##  Closes the issue 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ## <param name="coseNote"> (str) </param>
    def Close(issue: IssueContent, coseNote: str) -> None:
        """
         Closes the issue 
        """
        pass
    
    ##  Discards the newly created issue which has not saved in external db yet 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    @staticmethod
    def DiscardIssue(issue: IssueContent) -> None:
        """
         Discards the newly created issue which has not saved in external db yet 
        """
        pass
    
    ##  Returns all the @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink s 
    ##  @return attachments (@link IssueAttachment List[NXOpen.Issue.IssueAttachment]@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    @staticmethod
    def GetAllAttachments(issue: IssueContent) -> List[IssueAttachment]:
        """
         Returns all the @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink s 
         @return attachments (@link IssueAttachment List[NXOpen.Issue.IssueAttachment]@endlink): .
        """
        pass
    
    ##  Returns the @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink  with this attachment name 
    ##  @return attachment (@link IssueAttachment NXOpen.Issue.IssueAttachment@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ## <param name="attachmentName"> (str) </param>
    def GetAttachment(issue: IssueContent, attachmentName: str) -> IssueAttachment:
        """
         Returns the @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink  with this attachment name 
         @return attachment (@link IssueAttachment NXOpen.Issue.IssueAttachment@endlink): .
        """
        pass
    
    ##  Returns the child @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink s 
    ##  @return attachments (@link IssueAttachment List[NXOpen.Issue.IssueAttachment]@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    @staticmethod
    def GetChildAttachments(issue: IssueContent) -> List[IssueAttachment]:
        """
         Returns the child @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink s 
         @return attachments (@link IssueAttachment List[NXOpen.Issue.IssueAttachment]@endlink): .
        """
        pass
    
    ##  Returns all the child @link NXOpen::Issue::IssueFolder NXOpen::Issue::IssueFolder@endlink s 
    ##  @return folders (@link IssueFolder List[NXOpen.Issue.IssueFolder]@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    @staticmethod
    def GetFolders(issue: IssueContent) -> List[IssueFolder]:
        """
         Returns all the child @link NXOpen::Issue::IssueFolder NXOpen::Issue::IssueFolder@endlink s 
         @return folders (@link IssueFolder List[NXOpen.Issue.IssueFolder]@endlink): .
        """
        pass
    
    ##  Returns the @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink  with part type 
    ##  @return attachment (@link IssueAttachment NXOpen.Issue.IssueAttachment@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    @staticmethod
    def GetPartAttachment(issue: IssueContent) -> IssueAttachment:
        """
         Returns the @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink  with part type 
         @return attachment (@link IssueAttachment NXOpen.Issue.IssueAttachment@endlink): .
        """
        pass
    
    ##  Returns the @link NXOpen::Issue::IssueProperty NXOpen::Issue::IssueProperty@endlink  with this property name 
    ##  @return property (@link IssueProperty NXOpen.Issue.IssueProperty@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ## <param name="propertyName"> (str) </param>
    def GetProperty(issue: IssueContent, propertyName: str) -> IssueProperty:
        """
         Returns the @link NXOpen::Issue::IssueProperty NXOpen::Issue::IssueProperty@endlink  with this property name 
         @return property (@link IssueProperty NXOpen.Issue.IssueProperty@endlink): .
        """
        pass
    
    ##  Returns the value of @link NXOpen::Issue::IssueProperty NXOpen::Issue::IssueProperty@endlink  
    ##  @return propertyValue (str): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ## <param name="propertyName"> (str) </param>
    def GetPropertyValue(issue: IssueContent, propertyName: str) -> str:
        """
         Returns the value of @link NXOpen::Issue::IssueProperty NXOpen::Issue::IssueProperty@endlink  
         @return propertyValue (str): .
        """
        pass
    
    ##  Returns the user definded @link NXOpen::Issue::IssueProperty NXOpen::Issue::IssueProperty@endlink s 
    ##  @return properties (@link IssueProperty List[NXOpen.Issue.IssueProperty]@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    @staticmethod
    def GetUserProperties(issue: IssueContent) -> List[IssueProperty]:
        """
         Returns the user definded @link NXOpen::Issue::IssueProperty NXOpen::Issue::IssueProperty@endlink s 
         @return properties (@link IssueProperty List[NXOpen.Issue.IssueProperty]@endlink): .
        """
        pass
    
    ##  Returns whether the issue is checked out  
    ##  @return A tuple consisting of (isCheckOut, user). 
    ##  - isCheckOut is: bool.
    ##  - user is: str.

    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    @staticmethod
    def IsCheckedOut(issue: IssueContent) -> Tuple[bool, str]:
        """
         Returns whether the issue is checked out  
         @return A tuple consisting of (isCheckOut, user). 
         - isCheckOut is: bool.
         - user is: str.

        """
        pass
    
    ##  Returns whether the issue is closed 
    ##  @return isClosed (bool): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    @staticmethod
    def IsClosed(issue: IssueContent) -> bool:
        """
         Returns whether the issue is closed 
         @return isClosed (bool): .
        """
        pass
    
    ##  Returns whether the issue is read only 
    ##  @return isReadOnly (bool): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    @staticmethod
    def IsReadOnly(issue: IssueContent) -> bool:
        """
         Returns whether the issue is read only 
         @return isReadOnly (bool): .
        """
        pass
    
    ##  Loads the @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink s 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    @staticmethod
    def LoadAttachments(issue: IssueContent) -> None:
        """
         Loads the @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink s 
        """
        pass
    
    ##  Reloads all the @link NXOpen::Issue::IssueProperty NXOpen::Issue::IssueProperty@endlink s 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    @staticmethod
    def ReloadProperties(issue: IssueContent) -> None:
        """
         Reloads all the @link NXOpen::Issue::IssueProperty NXOpen::Issue::IssueProperty@endlink s 
        """
        pass
    
    ##  Removes an @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink  
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ## <param name="attachment"> (@link IssueAttachment NXOpen.Issue.IssueAttachment@endlink) </param>
    def RemoveAttachment(issue: IssueContent, attachment: IssueAttachment) -> None:
        """
         Removes an @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink  
        """
        pass
    
    ##  Signs off the current workflow task with decision 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ## <param name="reviewDecision"> (str) </param>
    ## <param name="comment"> (str) </param>
    def Review(issue: IssueContent, reviewDecision: str, comment: str) -> None:
        """
         Signs off the current workflow task with decision 
        """
        pass
    
    ##  Saves the changes to issue server 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    @staticmethod
    def SaveChanges(issue: IssueContent) -> None:
        """
         Saves the changes to issue server 
        """
        pass
    
    ##  Sends the issue to workflow process 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ## <param name="workflowTemplate"> (str) </param>
    def SendToWorkflow(issue: IssueContent, workflowTemplate: str) -> None:
        """
         Sends the issue to workflow process 
        """
        pass
    
    ##  Sets the value of @link NXOpen::Issue::IssueProperty NXOpen::Issue::IssueProperty@endlink  
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ## <param name="propertyName"> (str) </param>
    ## <param name="propertyValue"> (str) </param>
    def SetPropertyValue(issue: IssueContent, propertyName: str, propertyValue: str) -> None:
        """
         Sets the value of @link NXOpen::Issue::IssueProperty NXOpen::Issue::IssueProperty@endlink  
        """
        pass
    
import NXOpen
##  Represents the Issue Folder object. 
## 
##   <br>  Created in NX8.5.0  <br> 

class IssueFolder(NXOpen.NXObject): 
    """ Represents the Issue Folder object. """


    ##  Represents the possible folder types
    ##              for a @link NXOpen::Issue::IssueFolder NXOpen::Issue::IssueFolder@endlink .
    ##         
    ##  Problem items type     
    class Type(Enum):
        """
        Members Include: <ProblemItems> <ImpactedItems> <ReferenceItems> <ImplementedBy> <IssueImage> <IssueFixedImage> <SnapshotBeforeFix> <SnapshotAfterFix> <ValidationResults>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> IssueFolder.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link IssueFolder.Type NXOpen.Issue.IssueFolder.Type@endlink) FolderType
    ##   the folder type   
    ##     
    ##  
    ## Getter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return IssueFolder.Type
    @property
    def FolderType(self) -> IssueFolder.Type:
        """
        Getter for property: (@link IssueFolder.Type NXOpen.Issue.IssueFolder.Type@endlink) FolderType
          the folder type   
            
         
        """
        pass
    
    ##  Adds an @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink  
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ## <param name="attachment"> (@link IssueAttachment NXOpen.Issue.IssueAttachment@endlink) </param>
    def AddAttachment(folder: IssueFolder, attachment: IssueAttachment) -> None:
        """
         Adds an @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink  
        """
        pass
    
    ##  Returns the child @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink s 
    ##  @return attachments (@link IssueAttachment List[NXOpen.Issue.IssueAttachment]@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    @staticmethod
    def GetAttachments(folder: IssueFolder) -> List[IssueAttachment]:
        """
         Returns the child @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink s 
         @return attachments (@link IssueAttachment List[NXOpen.Issue.IssueAttachment]@endlink): .
        """
        pass
    
    ##  Removes an @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink  
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ## <param name="attachment"> (@link IssueAttachment NXOpen.Issue.IssueAttachment@endlink) </param>
    def RemoveAttachment(folder: IssueFolder, attachment: IssueAttachment) -> None:
        """
         Removes an @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink  
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Issue::IssueListCollection NXOpen::Issue::IssueListCollection@endlink   <br> To obtain an instance of this class, refer to @link NXOpen::Issue::IssueManager  NXOpen::Issue::IssueManager @endlink  <br> 
## 
##   <br>  Created in NX8.5.0  <br> 

class IssueListCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a <ja_class>NXOpen.Issue.IssueListCollection</ja_class> """


    ##  Finds the @link NXOpen::Issue::IssueList NXOpen::Issue::IssueList@endlink  with the given name.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return list (@link IssueList NXOpen.Issue.IssueList@endlink):  @link NXOpen::Issue::IssueList NXOpen::Issue::IssueList@endlink  with this name. .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ##  The name of the @link NXOpen::Issue::IssueList NXOpen::Issue::IssueList@endlink . 
    def FindObject(session: IssueListCollection, name: str) -> IssueList:
        """
         Finds the @link NXOpen::Issue::IssueList NXOpen::Issue::IssueList@endlink  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         @return list (@link IssueList NXOpen.Issue.IssueList@endlink):  @link NXOpen::Issue::IssueList NXOpen::Issue::IssueList@endlink  with this name. .
        """
        pass
    
import NXOpen
##  Represents the Issue List object. 
## 
##   <br>  Created in NX8.5.0  <br> 

class IssueList(NXOpen.NXObject): 
    """ Represents the Issue List object. """


    ##  Changes the config of @link NXOpen::Issue::IssueList NXOpen::Issue::IssueList@endlink  
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ##  The saved query name 
    def ChangeConfig(list: IssueList, queryName: str, criteriaTitles: List[str], criteriaValues: List[str]) -> None:
        """
         Changes the config of @link NXOpen::Issue::IssueList NXOpen::Issue::IssueList@endlink  
        """
        pass
    
    ##  Discards the modified @link NXOpen::Issue::IssueContent NXOpen::Issue::IssueContent@endlink s 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    @staticmethod
    def DiscardChanges(list: IssueList) -> None:
        """
         Discards the modified @link NXOpen::Issue::IssueContent NXOpen::Issue::IssueContent@endlink s 
        """
        pass
    
    ##  Returns whether the list exists in database 
    ##  @return exists (bool): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    @staticmethod
    def ExistsInDatabase(list: IssueList) -> bool:
        """
         Returns whether the list exists in database 
         @return exists (bool): .
        """
        pass
    
    ##  Returns all the @link NXOpen::Issue::IssueContent NXOpen::Issue::IssueContent@endlink s 
    ##  @return issues (@link IssueContent List[NXOpen.Issue.IssueContent]@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    @staticmethod
    def GetIssues(list: IssueList) -> List[IssueContent]:
        """
         Returns all the @link NXOpen::Issue::IssueContent NXOpen::Issue::IssueContent@endlink s 
         @return issues (@link IssueContent List[NXOpen.Issue.IssueContent]@endlink): .
        """
        pass
    
    ##  Reloads the @link NXOpen::Issue::IssueContent NXOpen::Issue::IssueContent@endlink s 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    @staticmethod
    def ReloadIssues(list: IssueList) -> None:
        """
         Reloads the @link NXOpen::Issue::IssueContent NXOpen::Issue::IssueContent@endlink s 
        """
        pass
    
    ##  Resets the config of @link NXOpen::Issue::IssueList NXOpen::Issue::IssueList@endlink  
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    @staticmethod
    def ResetConfig(list: IssueList) -> None:
        """
         Resets the config of @link NXOpen::Issue::IssueList NXOpen::Issue::IssueList@endlink  
        """
        pass
    
    ##  Saves the modified @link NXOpen::Issue::IssueContent NXOpen::Issue::IssueContent@endlink s 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    @staticmethod
    def SaveChanges(list: IssueList) -> None:
        """
         Saves the modified @link NXOpen::Issue::IssueContent NXOpen::Issue::IssueContent@endlink s 
        """
        pass
    
    ##  Saves the config of @link NXOpen::Issue::IssueList NXOpen::Issue::IssueList@endlink  to server 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    @staticmethod
    def SaveConfig(list: IssueList) -> None:
        """
         Saves the config of @link NXOpen::Issue::IssueList NXOpen::Issue::IssueList@endlink  to server 
        """
        pass
    
    ##  Sets the related parts of @link NXOpen::Issue::IssueList NXOpen::Issue::IssueList@endlink  
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ## <param name="parts"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    def SetRelatedParts(list: IssueList, parts: List[NXOpen.NXObject]) -> None:
        """
         Sets the related parts of @link NXOpen::Issue::IssueList NXOpen::Issue::IssueList@endlink  
        """
        pass
    
import NXOpen
##  Contains the collection objects for creating and iterating over issue objects.  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX8.5.0  <br> 

class IssueManager(NXOpen.Object): 
    """ Contains the collection objects for creating and iterating over issue objects. """


    ##  Represents the possible issue site modes.
    ##         
    ##  Teamcenter community mode 
    class Mode(Enum):
        """
        Members Include: <TeamcenterCommunity> <Teamcenter> <Briefcase>
        """
        TeamcenterCommunity: int
        Teamcenter: int
        Briefcase: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> IssueManager.Mode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the possible issue object states.
    ##         
    ##  Original state 
    class State(Enum):
        """
        Members Include: <Original> <Created> <Modified> <Removed>
        """
        Original: int
        Created: int
        Modified: int
        Removed: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> IssueManager.State:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link IssueManager.Mode NXOpen.Issue.IssueManager.Mode@endlink) CurrentMode
    ##   the current mode   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.2.  This functionality is no longer supported.  <br> 

    ## @return IssueManager.Mode
    @property
    def CurrentMode(self) -> IssueManager.Mode:
        """
        Getter for property: (@link IssueManager.Mode NXOpen.Issue.IssueManager.Mode@endlink) CurrentMode
          the current mode   
            
         
        """
        pass
    
    ## Setter for property: (@link IssueManager.Mode NXOpen.Issue.IssueManager.Mode@endlink) CurrentMode

    ##   the current mode   
    ##     
    ##  
    ## Setter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.2.  This functionality is no longer supported.  <br> 

    @CurrentMode.setter
    def CurrentMode(self, mode: IssueManager.Mode):
        """
        Setter for property: (@link IssueManager.Mode NXOpen.Issue.IssueManager.Mode@endlink) CurrentMode
          the current mode   
            
         
        """
        pass
    
    ## Getter for property: (@link IssueSite NXOpen.Issue.IssueSite@endlink) CurrentSite
    ##   the current @link NXOpen::Issue::IssueSite NXOpen::Issue::IssueSite@endlink    
    ##     
    ##  
    ## Getter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return IssueSite
    @property
    def CurrentSite(self) -> IssueSite:
        """
        Getter for property: (@link IssueSite NXOpen.Issue.IssueSite@endlink) CurrentSite
          the current @link NXOpen::Issue::IssueSite NXOpen::Issue::IssueSite@endlink    
            
         
        """
        pass
    
    ##  Returns the @link NXOpen::Issue::IssueListCollection NXOpen::Issue::IssueListCollection@endlink  instance 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @link IssueListCollection NXOpen.Issue.IssueListCollection@endlink
    @property
    def IssueListCollection() -> IssueListCollection:
        """
         Returns the @link NXOpen::Issue::IssueListCollection NXOpen::Issue::IssueListCollection@endlink  instance 
        """
        pass
    
    ##  Creates a @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink  for Snapshot 
    ##  @return attachObj (@link IssueAttachment NXOpen.Issue.IssueAttachment@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    @staticmethod
    def CaptureAndCreateAttachmentForSnapshot() -> IssueAttachment:
        """
         Creates a @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink  for Snapshot 
         @return attachObj (@link IssueAttachment NXOpen.Issue.IssueAttachment@endlink): .
        """
        pass
    
    ##  Connects to issue server and returns the @link NXOpen::Issue::IssueSite NXOpen::Issue::IssueSite@endlink  
    ##  @return site (@link IssueSite NXOpen.Issue.IssueSite@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.2.  This functionality is no longer supported.  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## <param name="siteUrl"> (str) </param>
    ## <param name="userName"> (str) </param>
    ## <param name="password"> (str) </param>
    def Connect(siteUrl: str, userName: str, password: str) -> IssueSite:
        """
         Connects to issue server and returns the @link NXOpen::Issue::IssueSite NXOpen::Issue::IssueSite@endlink  
         @return site (@link IssueSite NXOpen.Issue.IssueSite@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink  for BookMark 
    ##  @return attachObj (@link IssueAttachment NXOpen.Issue.IssueAttachment@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    def CreateAttachmentForBookMark() -> IssueAttachment:
        """
         Creates a @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink  for BookMark 
         @return attachObj (@link IssueAttachment NXOpen.Issue.IssueAttachment@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink  for ScreenImage 
    ##  @return attachObj (@link IssueAttachment NXOpen.Issue.IssueAttachment@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    def CreateAttachmentForScreenImage() -> IssueAttachment:
        """
         Creates a @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink  for ScreenImage 
         @return attachObj (@link IssueAttachment NXOpen.Issue.IssueAttachment@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink  for Sanpshot 
    ##  @return attachment (@link IssueAttachment NXOpen.Issue.IssueAttachment@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ##  The bookmark file 
    def CreateAttachmentForSnapshot(bookmarkFileSpec: str, imageFileSpec: str, name: str) -> IssueAttachment:
        """
         Creates a @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink  for Sanpshot 
         @return attachment (@link IssueAttachment NXOpen.Issue.IssueAttachment@endlink): .
        """
        pass
    
    ##  Creates an @link NXOpen::Issue::IssueBriefcase NXOpen::Issue::IssueBriefcase@endlink . 
    ##  @return briefcase (@link IssueBriefcase NXOpen.Issue.IssueBriefcase@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ##  The briefcase name 
    def CreateBriefcase(briefcaseName: str, filePath: str) -> IssueBriefcase:
        """
         Creates an @link NXOpen::Issue::IssueBriefcase NXOpen::Issue::IssueBriefcase@endlink . 
         @return briefcase (@link IssueBriefcase NXOpen.Issue.IssueBriefcase@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink  
    ##  @return attachment (@link IssueAttachment NXOpen.Issue.IssueAttachment@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## <param name="fileSpec"> (str) </param>
    ## <param name="name"> (str) </param>
    ## <param name="type"> (@link IssueAttachment.Type NXOpen.Issue.IssueAttachment.Type@endlink) </param>
    def CreateIssueAttachment(fileSpec: str, name: str, type: IssueAttachment.Type) -> IssueAttachment:
        """
         Creates a @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink  
         @return attachment (@link IssueAttachment NXOpen.Issue.IssueAttachment@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Issue::IssueContent NXOpen::Issue::IssueContent@endlink  
    ##  @return issue (@link IssueContent NXOpen.Issue.IssueContent@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## <param name="list"> (@link IssueList NXOpen.Issue.IssueList@endlink) </param>
    def CreateIssueContent(list: IssueList) -> IssueContent:
        """
         Creates a @link NXOpen::Issue::IssueContent NXOpen::Issue::IssueContent@endlink  
         @return issue (@link IssueContent NXOpen.Issue.IssueContent@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Issue::IssueContentBuilder NXOpen::Issue::IssueContentBuilder@endlink  
    ##  @return builder (@link IssueContentBuilder NXOpen.Issue.IssueContentBuilder@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## <param name="issue"> (@link IssueContent NXOpen.Issue.IssueContent@endlink) </param>
    def CreateIssueContentBuilder(issue: IssueContent) -> IssueContentBuilder:
        """
         Creates a @link NXOpen::Issue::IssueContentBuilder NXOpen::Issue::IssueContentBuilder@endlink  
         @return builder (@link IssueContentBuilder NXOpen.Issue.IssueContentBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Issue::SnapshotSubsetBuilder NXOpen::Issue::SnapshotSubsetBuilder@endlink  
    ##  @return builder (@link SnapshotSubsetBuilder NXOpen.Issue.SnapshotSubsetBuilder@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## <param name="subsetPart"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateIssueSnapshotSubsetBuilder(subsetPart: NXOpen.Part) -> SnapshotSubsetBuilder:
        """
         Creates a @link NXOpen::Issue::SnapshotSubsetBuilder NXOpen::Issue::SnapshotSubsetBuilder@endlink  
         @return builder (@link SnapshotSubsetBuilder NXOpen.Issue.SnapshotSubsetBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Issue::SnapshotWorksetBuilder NXOpen::Issue::SnapshotWorksetBuilder@endlink  
    ##  @return builder (@link SnapshotWorksetBuilder NXOpen.Issue.SnapshotWorksetBuilder@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## <param name="issue"> (@link IssueContent NXOpen.Issue.IssueContent@endlink) </param>
    def CreateIssueSnapshotWorksetBuilder(issue: IssueContent) -> SnapshotWorksetBuilder:
        """
         Creates a @link NXOpen::Issue::SnapshotWorksetBuilder NXOpen::Issue::SnapshotWorksetBuilder@endlink  
         @return builder (@link SnapshotWorksetBuilder NXOpen.Issue.SnapshotWorksetBuilder@endlink): .
        """
        pass
    
    ##  Disconnects from issue server 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.2.  This functionality is no longer supported.  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    @staticmethod
    def Disconnect() -> None:
        """
         Disconnects from issue server 
        """
        pass
    
    ##  Gets the modified state of @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink  
    ##  @return state (@link IssueManager.State NXOpen.Issue.IssueManager.State@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## <param name="attachment"> (@link IssueAttachment NXOpen.Issue.IssueAttachment@endlink) </param>
    @staticmethod
    def GetAttachmentState(attachment: IssueAttachment) -> IssueManager.State:
        """
         Gets the modified state of @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink  
         @return state (@link IssueManager.State NXOpen.Issue.IssueManager.State@endlink): .
        """
        pass
    
    ##  Gets the modified state of @link NXOpen::Issue::IssueContent NXOpen::Issue::IssueContent@endlink  
    ##  @return state (@link IssueManager.State NXOpen.Issue.IssueManager.State@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## <param name="issue"> (@link IssueContent NXOpen.Issue.IssueContent@endlink) </param>
    @staticmethod
    def GetIssueState(issue: IssueContent) -> IssueManager.State:
        """
         Gets the modified state of @link NXOpen::Issue::IssueContent NXOpen::Issue::IssueContent@endlink  
         @return state (@link IssueManager.State NXOpen.Issue.IssueManager.State@endlink): .
        """
        pass
    
    ##  Gets the modified state of @link NXOpen::Issue::IssueProperty NXOpen::Issue::IssueProperty@endlink  
    ##  @return state (@link IssueManager.State NXOpen.Issue.IssueManager.State@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## <param name="property"> (@link IssueProperty NXOpen.Issue.IssueProperty@endlink) </param>
    @staticmethod
    def GetPropertyState(property: IssueProperty) -> IssueManager.State:
        """
         Gets the modified state of @link NXOpen::Issue::IssueProperty NXOpen::Issue::IssueProperty@endlink  
         @return state (@link IssueManager.State NXOpen.Issue.IssueManager.State@endlink): .
        """
        pass
    
    ##  Gets the current working @link NXOpen::Issue::IssueList NXOpen::Issue::IssueList@endlink  
    ##  @return list (@link IssueList NXOpen.Issue.IssueList@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetWorkingList() -> IssueList:
        """
         Gets the current working @link NXOpen::Issue::IssueList NXOpen::Issue::IssueList@endlink  
         @return list (@link IssueList NXOpen.Issue.IssueList@endlink): .
        """
        pass
    
    ##  Opens an @link NXOpen::Issue::IssueBriefcase NXOpen::Issue::IssueBriefcase@endlink  .
    ##  @return list (@link IssueBriefcase NXOpen.Issue.IssueBriefcase@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ##  The briefcase file path 
    @staticmethod
    def OpenBriefcase(filePath: str) -> IssueBriefcase:
        """
         Opens an @link NXOpen::Issue::IssueBriefcase NXOpen::Issue::IssueBriefcase@endlink  .
         @return list (@link IssueBriefcase NXOpen.Issue.IssueBriefcase@endlink): .
        """
        pass
    
    ##  Sets the current working @link NXOpen::Issue::IssueList NXOpen::Issue::IssueList@endlink  
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## <param name="list"> (@link IssueList NXOpen.Issue.IssueList@endlink) </param>
    @staticmethod
    def SetWorkingList(list: IssueList) -> None:
        """
         Sets the current working @link NXOpen::Issue::IssueList NXOpen::Issue::IssueList@endlink  
        """
        pass
    
import NXOpen
##  Represents the Issue Property object. 
## 
##   <br>  Created in NX8.5.0  <br> 

class IssueProperty(NXOpen.NXObject): 
    """ Represents the Issue Property object. """


    ##  Represents the possible property types.
    ##              for a @link NXOpen::Issue::IssueProperty NXOpen::Issue::IssueProperty@endlink .
    ##         
    ##  Text type 
    class Type(Enum):
        """
        Members Include: <Text> <Note> <User> <Choice> <Url> <Boolean> <Date> <Number> <Integer> <Point3D> <Vector3D>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> IssueProperty.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) IsReadOnly
    ##   whether the property is read only   
    ##     
    ##  
    ## Getter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def IsReadOnly(self) -> bool:
        """
        Getter for property: (bool) IsReadOnly
          whether the property is read only   
            
         
        """
        pass
    
    ## Getter for property: (str) StringValue
    ##   the string value   
    ##     
    ##  
    ## Getter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def StringValue(self) -> str:
        """
        Getter for property: (str) StringValue
          the string value   
            
         
        """
        pass
    
    ## Getter for property: (@link IssueProperty.Type NXOpen.Issue.IssueProperty.Type@endlink) ValueType
    ##   the property type   
    ##     
    ##  
    ## Getter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return IssueProperty.Type
    @property
    def ValueType(self) -> IssueProperty.Type:
        """
        Getter for property: (@link IssueProperty.Type NXOpen.Issue.IssueProperty.Type@endlink) ValueType
          the property type   
            
         
        """
        pass
    
    ##  Returns the choices  
    ##  @return choices (List[str]): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    @staticmethod
    def GetChoices(property: IssueProperty) -> List[str]:
        """
         Returns the choices  
         @return choices (List[str]): .
        """
        pass
    
    ##  Returns the default choice  
    ##  @return defaultChoice (str): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    @staticmethod
    def GetDefaultChoice(property: IssueProperty) -> str:
        """
         Returns the default choice  
         @return defaultChoice (str): .
        """
        pass
    
import NXOpen
##  Represents the Issue Site object. 
## 
##   <br>  Created in NX8.5.0  <br> 

class IssueSite(NXOpen.NXObject): 
    """ Represents the Issue Site object. """


    ##  Creates an @link NXOpen::Issue::IssueList NXOpen::Issue::IssueList@endlink  
    ##  @return list (@link IssueList NXOpen.Issue.IssueList@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ##  The list name 
    def CreateList(site: IssueSite, listName: str, queryName: str, criteriaTitles: List[str], criteriaValues: List[str]) -> IssueList:
        """
         Creates an @link NXOpen::Issue::IssueList NXOpen::Issue::IssueList@endlink  
         @return list (@link IssueList NXOpen.Issue.IssueList@endlink): .
        """
        pass
    
    ##  Gets the @link NXOpen::Issue::IssueList NXOpen::Issue::IssueList@endlink  for quick search 
    ##  @return list (@link IssueList NXOpen.Issue.IssueList@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    @staticmethod
    def GetQuickSearchList(site: IssueSite) -> IssueList:
        """
         Gets the @link NXOpen::Issue::IssueList NXOpen::Issue::IssueList@endlink  for quick search 
         @return list (@link IssueList NXOpen.Issue.IssueList@endlink): .
        """
        pass
    
    ##  Returns whether the site is connected 
    ##  @return isConnected (bool): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    @staticmethod
    def IsConnected(site: IssueSite) -> bool:
        """
         Returns whether the site is connected 
         @return isConnected (bool): .
        """
        pass
    
    ##  Removes an @link NXOpen::Issue::IssueList NXOpen::Issue::IssueList@endlink  
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ## <param name="list"> (@link IssueList NXOpen.Issue.IssueList@endlink) </param>
    def RemoveList(site: IssueSite, list: IssueList) -> None:
        """
         Removes an @link NXOpen::Issue::IssueList NXOpen::Issue::IssueList@endlink  
        """
        pass
    
import NXOpen
import NXOpen.Assemblies
##  Used to create or edit issue snapshot subset.  <br> To create a new instance of this class, use @link NXOpen::Issue::IssueManager::CreateIssueSnapshotSubsetBuilder  NXOpen::Issue::IssueManager::CreateIssueSnapshotSubsetBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class SnapshotSubsetBuilder(NXOpen.Builder): 
    """ Used to create or edit issue snapshot subset. """


    ##  The option specifying which kinds of issue snapshot subset should be created. 
    ##  Problem Subset 
    class ContextType(Enum):
        """
        Members Include: <Problem> <Impacted> <Reference>
        """
        Problem: int
        Impacted: int
        Reference: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SnapshotSubsetBuilder.ContextType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link SnapshotSubsetBuilder.ContextType NXOpen.Issue.SnapshotSubsetBuilder.ContextType@endlink) Context
    ##   the context indicating the issue snapshot subset type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return SnapshotSubsetBuilder.ContextType
    @property
    def Context(self) -> SnapshotSubsetBuilder.ContextType:
        """
        Getter for property: (@link SnapshotSubsetBuilder.ContextType NXOpen.Issue.SnapshotSubsetBuilder.ContextType@endlink) Context
          the context indicating the issue snapshot subset type.  
             
         
        """
        pass
    
    ## Setter for property: (@link SnapshotSubsetBuilder.ContextType NXOpen.Issue.SnapshotSubsetBuilder.ContextType@endlink) Context

    ##   the context indicating the issue snapshot subset type.  
    ##      
    ##  
    ## Setter License requirements: nx_issue_mgmt ("NX Issue Tracking")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Context.setter
    def Context(self, context: SnapshotSubsetBuilder.ContextType):
        """
        Setter for property: (@link SnapshotSubsetBuilder.ContextType NXOpen.Issue.SnapshotSubsetBuilder.ContextType@endlink) Context
          the context indicating the issue snapshot subset type.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Assemblies.SelectComponentList NXOpen.Assemblies.SelectComponentList@endlink) SelectParts
    ##   the select parts which will be collected into issue snapshot subset.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Assemblies.SelectComponentList
    @property
    def SelectParts(self) -> NXOpen.Assemblies.SelectComponentList:
        """
        Getter for property: (@link NXOpen.Assemblies.SelectComponentList NXOpen.Assemblies.SelectComponentList@endlink) SelectParts
          the select parts which will be collected into issue snapshot subset.  
             
         
        """
        pass
    
import NXOpen
##  
##     Used to create or edit issue snapshot workset which is a container to hold all the corresponding 
##     parts to represent an issue.
##       <br> To create a new instance of this class, use @link NXOpen::Issue::IssueManager::CreateIssueSnapshotWorksetBuilder  NXOpen::Issue::IssueManager::CreateIssueSnapshotWorksetBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class SnapshotWorksetBuilder(NXOpen.Builder): 
    """ 
    Used to create or edit issue snapshot workset which is a container to hold all the corresponding 
    parts to represent an issue.
     """


    ## Getter for property: (@link SnapshotSubsetBuilder NXOpen.Issue.SnapshotSubsetBuilder@endlink) ImpactedSubset
    ##   the impactedSubset containing the impacted parts.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return SnapshotSubsetBuilder
    @property
    def ImpactedSubset(self) -> SnapshotSubsetBuilder:
        """
        Getter for property: (@link SnapshotSubsetBuilder NXOpen.Issue.SnapshotSubsetBuilder@endlink) ImpactedSubset
          the impactedSubset containing the impacted parts.  
             
         
        """
        pass
    
    ## Getter for property: (@link SnapshotSubsetBuilder NXOpen.Issue.SnapshotSubsetBuilder@endlink) ProblemSubset
    ##   the problemSubset containing the problem parts.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return SnapshotSubsetBuilder
    @property
    def ProblemSubset(self) -> SnapshotSubsetBuilder:
        """
        Getter for property: (@link SnapshotSubsetBuilder NXOpen.Issue.SnapshotSubsetBuilder@endlink) ProblemSubset
          the problemSubset containing the problem parts.  
             
         
        """
        pass
    
    ## Getter for property: (@link SnapshotSubsetBuilder NXOpen.Issue.SnapshotSubsetBuilder@endlink) ReferenceSubset
    ##   the referenceSubset containing the reference parts.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return SnapshotSubsetBuilder
    @property
    def ReferenceSubset(self) -> SnapshotSubsetBuilder:
        """
        Getter for property: (@link SnapshotSubsetBuilder NXOpen.Issue.SnapshotSubsetBuilder@endlink) ReferenceSubset
          the referenceSubset containing the reference parts.  
             
         
        """
        pass
    
## @package NXOpen.Issue
## Classes, Enums and Structs under NXOpen.Issue namespace

##  @link IssueAttachmentType NXOpen.Issue.IssueAttachmentType @endlink is an alias for @link IssueAttachment.Type NXOpen.Issue.IssueAttachment.Type@endlink
IssueAttachmentType = IssueAttachment.Type


##  @link IssueFolderType NXOpen.Issue.IssueFolderType @endlink is an alias for @link IssueFolder.Type NXOpen.Issue.IssueFolder.Type@endlink
IssueFolderType = IssueFolder.Type


##  @link IssueManagerMode NXOpen.Issue.IssueManagerMode @endlink is an alias for @link IssueManager.Mode NXOpen.Issue.IssueManager.Mode@endlink
IssueManagerMode = IssueManager.Mode


##  @link IssueManagerState NXOpen.Issue.IssueManagerState @endlink is an alias for @link IssueManager.State NXOpen.Issue.IssueManager.State@endlink
IssueManagerState = IssueManager.State


##  @link IssuePropertyType NXOpen.Issue.IssuePropertyType @endlink is an alias for @link IssueProperty.Type NXOpen.Issue.IssueProperty.Type@endlink
IssuePropertyType = IssueProperty.Type


##  @link SnapshotSubsetBuilderContextType NXOpen.Issue.SnapshotSubsetBuilderContextType @endlink is an alias for @link SnapshotSubsetBuilder.ContextType NXOpen.Issue.SnapshotSubsetBuilder.ContextType@endlink
SnapshotSubsetBuilderContextType = SnapshotSubsetBuilder.ContextType


