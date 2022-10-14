#ifndef NXOpen_ROUTINGCOMMON_ROUTINGMANAGER_HXX_INCLUDED
#define NXOpen_ROUTINGCOMMON_ROUTINGMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     RoutingCommon_RoutingManager.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_routingcommon_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace RoutingCommon
    {
        class RoutingManager;
    }
    class Session;
    namespace Assemblies
    {
        class Component;
    }
    class BasePart;
    class Part;
    namespace Routing
    {
        class ControlPoint;
    }
    namespace Routing
    {
        class Port;
    }
    namespace RoutingCommon
    {
        class BuilderFactory;
    }
    namespace RoutingCommon
    {
        class InsulationService;
    }
    namespace RoutingCommon
    {
        class RoutingManagerImpl;
        /** Represents an @link NXOpen::RoutingCommon::RoutingManager NXOpen::RoutingCommon::RoutingManager@endlink  object.   <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_ROUTINGCOMMONEXPORT  RoutingManager
        {
            private: RoutingManagerImpl * m_routingmanager_impl;
            private: NXOpen::Session* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit RoutingManager(NXOpen::Session *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            private: static RoutingManager* theRoutingManager;
            /** Returns the RoutingManager object for the running session which serves as the 'gateway' class for the application API.  
                References to all other objects in this API are obtained either directly or indirectly via methods and properties on this class.  
                Platform Session should be initialized using 'GetSession' method from NXOpen API prior to this call.  
            */
            public: static RoutingManager* GetRoutingManager(NXOpen::Session *owner);
            public: ~RoutingManager();
            /** Checks if the part is a route system assembly   @return  Returns true if the part is a routed system designer part. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool IsRouteSystemAssembly
            (
                NXOpen::Part * part /** the part that is to checked */
            );

            /// \cond NX_NO_DOC 
            /** Checks if the part is a shape component part   @return  Returns true if the part is a routed system designer part. 
             <br>  @deprecated Deprecated in NX1980.0.0.  This method is no longer required. Use IsStockComponentPart, IsInsulationComponentPart instead <br>  

             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NX_DEPRECATED("Deprecated in NX1980.0.0.  This method is no longer required. Use IsStockComponentPart, IsInsulationComponentPart instead") bool IsShapeComponentPart
            (
                NXOpen::BasePart * part /** the base part that is to checked */
            );

            /// \endcond 
            /** Checks if the part is a reusable component part   @return  Returns true if the part is a routed system designer part. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool IsReusableComponentPart
            (
                NXOpen::BasePart * part /** the base part that is to checked */
            );
            /** Makes a component a reusable component for Routed System Designer provided the component is not already a Routed System Designer component. 
                    It is recommended to check @link NXOpen::RoutingCommon::RoutingManager::IsReusableComponentPart NXOpen::RoutingCommon::RoutingManager::IsReusableComponentPart@endlink  before calling this API  @return  Returns true if the component was made reusable. It can return false even in cases where the component was already reusable. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool MakeComponentReusable
            (
                NXOpen::Assemblies::Component * component /** The component to which the reuse behavior is to added if needed */
            );
            /** Performs Detach Operation on rcp  @return  Returns true if the detach operation is performed. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool PerformDetachOperationOnRcp
            (
                NXOpen::Routing::ControlPoint * rcp /** the selected Routing Control Point occurrence*/
            );
            /** Performs Detach Operation on port @return  Returns true if the detach operation is performed. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool PerformDetachOperationOnPort
            (
                NXOpen::Routing::Port * port /** the selected Port occurrence or prototype*/
            );
            /** Checks if the part is a stock component part  @return  Returns true if the part is a Routed System Designer part. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool IsStockComponentPart
            (
                NXOpen::BasePart * part /** the base part that is to checked */
            );
            /** Checks if the part is a insulation component part @return  Returns true if the part is a Routed System Designer part. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool IsInsulationComponentPart
            (
                NXOpen::BasePart * part /** the base part that is to checked */
            );
            /** Stores given discipline within the routing assembly part so that the same discipline can be restored upon reopening the assembly.
                        Only in Routed System Assmebly part, @link RoutingManager::IsRouteSystemAssembly RoutingManager::IsRouteSystemAssembly@endlink , discipline can be saved.
                        If discipline is not found in application view, it is considered invalid. Invalid discipline is not saved.
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool StoreReuseLibraryDisciplineWithinPart
            (
                NXOpen::Part * part /** the routing assembly part  */,
                const NXString & discipline /** Name of the discipline */
            );
            /** Stores given discipline within the routing assembly part so that the same discipline can be restored upon reopening the assembly.
                        Only in Routed System Assmebly part, @link RoutingManager::IsRouteSystemAssembly RoutingManager::IsRouteSystemAssembly@endlink , discipline can be saved.
                        If discipline is not found in application view, it is considered invalid. Invalid discipline is not saved.
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            bool StoreReuseLibraryDisciplineWithinPart
            (
                NXOpen::Part * part /** the routing assembly part  */,
                const char * discipline /** Name of the discipline */
            );
            /** Stores given specification within the routing assembly part so that the same specification can be restored upon reopening the assembly.
                        Only in Routed System Assmebly part, @link RoutingManager::IsRouteSystemAssembly RoutingManager::IsRouteSystemAssembly@endlink , specification can be saved.
                        If specification is not found in current discipline, it is considered invalid. Invalid specification is not saved.
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool StoreReuseLibrarySpecificationWithinPart
            (
                NXOpen::Part * part /** the routing assembly part  */,
                const NXString & specification /** Name of the specification */
            );
            /** Stores given specification within the routing assembly part so that the same specification can be restored upon reopening the assembly.
                        Only in Routed System Assmebly part, @link RoutingManager::IsRouteSystemAssembly RoutingManager::IsRouteSystemAssembly@endlink , specification can be saved.
                        If specification is not found in current discipline, it is considered invalid. Invalid specification is not saved.
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            bool StoreReuseLibrarySpecificationWithinPart
            (
                NXOpen::Part * part /** the routing assembly part  */,
                const char * specification /** Name of the specification */
            );
            /** Returns saved discipline and specification from the given part. Only Routed System Assembly part can 
                        have discipline and specification saved in it. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void GetSavedDisciplineAndSpecificationFromThePart
            (
                NXOpen::Part * part /** the routing assembly part  */,
                NXString* discipline /** Name of the discipline */,
                NXString* specification /** Name of the specification */
            );
            /** Sets saved discipline and specification from the given part as active. Only Routed System Assembly part can
                        have discipline and specification saved in it. If saved discipline or specification is no longer valid, the method
                        returns failure status. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void RestoreDisciplineAndSpecificationFromThePart
            (
                NXOpen::Part * part /** the routing assembly part  */,
                bool* disciplineSuccess /** disciplinesuccess */ ,
                bool* specificationSuccess /** specificationsuccess */ 
            );


            /**  Returns a @link NXOpen::RoutingCommon::BuilderFactory NXOpen::RoutingCommon::BuilderFactory@endlink  object.  Use this object
                         to create specific routing builders.
                    
             <br>  Created in NX1847.0.0.  <br>  
            */
            public: NXOpen::RoutingCommon::BuilderFactory *BuilderFactory();
            /**  Returns a @link NXOpen::RoutingCommon::InsulationService NXOpen::RoutingCommon::InsulationService@endlink  object.  Use this object
                         for specific Routing  Insulation service
                    
             <br>  Created in NX1847.0.0.  <br>  
            */
            public: NXOpen::RoutingCommon::InsulationService *InsulationService();
        }; //lint !e1712 default constructor not defined for class  

    }
}

#ifdef _MSC_VER
#pragma warning(pop)
#endif
#ifdef __GNUC__
#ifndef NX_NO_GCC_DEPRECATION_WARNINGS
#pragma GCC diagnostic warning "-Wdeprecated-declarations"
#endif
#endif

#undef EXPORTLIBRARY
#endif