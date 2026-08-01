from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class SessionManager(NXOpen.Object): 
    """  Represents a Session Manager class  """
    def GetSubscriptionManager() -> SubscriptionMgr:
        """
         Returns a new NXOpen.CollaborationApplication.SubscriptionMgr object 
         Returns subscriptionManager ( SubscriptionMgr NXOpen.Collabor): .
        """
        pass
import NXOpen
class SubscriptionMgr(NXOpen.TransientObject): 
    """  Represents a Subscription Manager class.  """
    @property
    def FollowPartsOnLoadFlag(self) -> bool:
        """
        Getter for property: (bool) FollowPartsOnLoadFlag
         Returns the property that controls whether the parts are automatically followed on load.  
             
         
        """
        pass
    @FollowPartsOnLoadFlag.setter
    def FollowPartsOnLoadFlag(self, followPartsOnLoadFlag: bool):
        """
        Setter for property: (bool) FollowPartsOnLoadFlag
         Returns the property that controls whether the parts are automatically followed on load.  
             
         
        """
        pass
    def UpdateSubscription(self, displayNames: List[str]) -> None:
        """
         Set the objects for receiving activity notifications.
        """
        pass
