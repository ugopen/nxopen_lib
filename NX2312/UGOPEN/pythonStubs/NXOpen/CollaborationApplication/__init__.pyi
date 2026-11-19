from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##   @brief  Represents a Session Manager class  
## 
##    <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class SessionManager(NXOpen.Object): 
    """ <summary> Represents a Session Manager class </summary> """


    ##  Returns a new @link NXOpen::CollaborationApplication::SubscriptionMgr NXOpen::CollaborationApplication::SubscriptionMgr@endlink  object 
    ##  @return subscriptionManager (@link SubscriptionMgr NXOpen.CollaborationApplication.SubscriptionMgr@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_mu_notifications (" NX Multi-User Notifications")
    @staticmethod
    def GetSubscriptionManager() -> SubscriptionMgr:
        """
         Returns a new @link NXOpen::CollaborationApplication::SubscriptionMgr NXOpen::CollaborationApplication::SubscriptionMgr@endlink  object 
         @return subscriptionManager (@link SubscriptionMgr NXOpen.CollaborationApplication.SubscriptionMgr@endlink): .
        """
        pass
    
import NXOpen
##   @brief  Represents a Subscription Manager class.  
## 
##   
## 
##   <br>  Created in NX1926.0.0  <br> 

class SubscriptionMgr(NXOpen.TransientObject): 
    """ <summary> Represents a Subscription Manager class. </summary> """


    ## Getter for property: (bool) FollowPartsOnLoadFlag
    ##   the property that controls whether the parts are automatically followed on load.  
    ##      
    ##  
    ## Getter License requirements: nx_mu_notifications (" NX Multi-User Notifications")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def FollowPartsOnLoadFlag(self) -> bool:
        """
        Getter for property: (bool) FollowPartsOnLoadFlag
          the property that controls whether the parts are automatically followed on load.  
             
         
        """
        pass
    
    ## Setter for property: (bool) FollowPartsOnLoadFlag

    ##   the property that controls whether the parts are automatically followed on load.  
    ##      
    ##  
    ## Setter License requirements: nx_mu_notifications (" NX Multi-User Notifications")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @FollowPartsOnLoadFlag.setter
    def FollowPartsOnLoadFlag(self, followPartsOnLoadFlag: bool):
        """
        Setter for property: (bool) FollowPartsOnLoadFlag
          the property that controls whether the parts are automatically followed on load.  
             
         
        """
        pass
    
    ##  Set the objects for receiving activity notifications.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_mu_notifications (" NX Multi-User Notifications")
    ## 
    ## <param name="displayNames"> (List[str]) </param>
    def UpdateSubscription(mgr: SubscriptionMgr, displayNames: List[str]) -> None:
        """
         Set the objects for receiving activity notifications.
        """
        pass
    
## @package NXOpen.CollaborationApplication
## Classes, Enums and Structs under NXOpen.CollaborationApplication namespace

