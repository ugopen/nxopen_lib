#ifndef NXOpen_MECHANICALROUTING_PATHSTOCKPREFERENCEBUILDER_HXX_INCLUDED
#define NXOpen_MECHANICALROUTING_PATHSTOCKPREFERENCEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     MechanicalRouting_PathStockPreferenceBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_mechanicalrouting_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace MechanicalRouting
    {
        class PathStockPreferenceBuilder;
    }
    class Expression;
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class NXObject;
    namespace MechanicalRouting
    {
        class _PathStockPreferenceBuilderBuilder;
        class PathStockPreferenceBuilderImpl;
        /** Assigns stocks to segments based on user's criteria and the current default stock.  
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_MECHANICALROUTINGEXPORT  PathStockPreferenceBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            /** Determines the type of stock being assigned. */
            public: enum AssignStockType
            {
                AssignStockTypeStock/** Default stock type.            */,
                AssignStockTypeOverstock/** Overstock stock type.           */
            };

            /** Determines the type of sub stock being assigned. This is only valid when Stock type is 'Stock' */
            public: enum AssignStockSubType
            {
                AssignStockSubTypeStock/** Default stock subtype.             */,
                AssignStockSubTypeSpaceReservation/** Space Reservation stock subtype.   */
            };

            /** Determines how to choose which stock to assign. 
             <br>  @deprecated Deprecated in NX11.0.1.  Use @link NXOpen::MechanicalRouting::PathStockPreferenceBuilder::StockMethod NXOpen::MechanicalRouting::PathStockPreferenceBuilder::StockMethod@endlink  instead. <br>  
            */
            public: enum NX_DEPRECATED("Deprecated in NX11.0.1.  Use NXOpen::MechanicalRouting::PathStockPreferenceBuilder::StockMethod instead.") AssignMethod
            {
                AssignMethodNone/** No Stock. */,
                AssignMethodFromStartObject/** Finds a stock based off of the
                                                                               default stock and the object selected by the user. */,
                AssignMethodCircular/** User specified diameter, creates round
                                                                               space reservation stock. */,
                AssignMethodRectangular/** User specified values, creates rectangular
                                                                               space reservation stock. */,
                AssignMethodFlatOval/** User specified values, creates flat_oval 
                                                                                   space reservation stock. */,
                AssignMethodSpecifiedStock/** Stock selected from Specify Item dialog */
            };

            /** Determines how to choose which stock to assign. */
            public: enum StockMethod
            {
                StockMethodNone/** No Stock. */,
                StockMethodSpecifiedStock/** Stock selected from Specify Item dialog */
            };

            /** Determines how to choose which space reservation to assign. */
            public: enum SpaceReservationMethod
            {
                SpaceReservationMethodNone/** No Stock. */,
                SpaceReservationMethodFromStartObject/** Finds a stock based off of the
                                                                               default stock and the object selected by the user. */,
                SpaceReservationMethodCircular/** User specified diameter, creates round
                                                                               space reservation stock. */,
                SpaceReservationMethodRectangular/** User specified values, creates rectangular
                                                                               space reservation stock. */,
                SpaceReservationMethodFlatOval/** User specified values, creates flat_oval 
                                                                                   space reservation stock. */,
                SpaceReservationMethodSpecifiedSpaceReservation/** sp selected from Specify Item dialog */
            };

            private: PathStockPreferenceBuilderImpl * m_pathstockpreferencebuilder_impl;
            private: friend class  _PathStockPreferenceBuilderBuilder;
            protected: PathStockPreferenceBuilder();
            public: ~PathStockPreferenceBuilder();
            /**Returns  the type of stock being assigned. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::MechanicalRouting::PathStockPreferenceBuilder::AssignStockType StockType
            (
            );
            /**Sets  the type of stock being assigned. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetStockType
            (
                NXOpen::MechanicalRouting::PathStockPreferenceBuilder::AssignStockType stockType /** stock type */ 
            );
            /**Returns  the type of stock being assigned. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::MechanicalRouting::PathStockPreferenceBuilder::AssignStockSubType StockSubType
            (
            );
            /**Sets  the type of stock being assigned. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetStockSubType
            (
                NXOpen::MechanicalRouting::PathStockPreferenceBuilder::AssignStockSubType stockType /** stock type */ 
            );
            /**Returns  the method to determine which stock to assign. 
             <br>  @deprecated Deprecated in NX11.0.1.  Use @link NXOpen::MechanicalRouting::PathStockPreferenceBuilder::StockMethodType NXOpen::MechanicalRouting::PathStockPreferenceBuilder::StockMethodType@endlink  instead. <br>  

             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NX_DEPRECATED("Deprecated in NX11.0.1.  Use NXOpen::MechanicalRouting::PathStockPreferenceBuilder::StockMethodType instead.") NXOpen::MechanicalRouting::PathStockPreferenceBuilder::AssignMethod AssignStockMethod
            (
            );
            /**Sets  the method to determine which stock to assign. 
             <br>  @deprecated Deprecated in NX11.0.1.  Use @link NXOpen::MechanicalRouting::PathStockPreferenceBuilder::SetStockMethodType NXOpen::MechanicalRouting::PathStockPreferenceBuilder::SetStockMethodType@endlink  instead. <br>  

             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NX_DEPRECATED("Deprecated in NX11.0.1.  Use NXOpen::MechanicalRouting::PathStockPreferenceBuilder::SetStockMethodType instead.") void SetAssignStockMethod
            (
                NXOpen::MechanicalRouting::PathStockPreferenceBuilder::AssignMethod method /** method */ 
            );
            /**Returns  the method to determine which stock to assign. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::MechanicalRouting::PathStockPreferenceBuilder::StockMethod StockMethodType
            (
            );
            /**Sets  the method to determine which stock to assign. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetStockMethodType
            (
                NXOpen::MechanicalRouting::PathStockPreferenceBuilder::StockMethod method /** method */ 
            );
            /**Returns  the method to determine which space reservation to assign. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::MechanicalRouting::PathStockPreferenceBuilder::SpaceReservationMethod SpaceReservationMethodType
            (
            );
            /**Sets  the method to determine which space reservation to assign. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetSpaceReservationMethodType
            (
                NXOpen::MechanicalRouting::PathStockPreferenceBuilder::SpaceReservationMethod method /** method */ 
            );
            /**Returns  the start object to use for the 
                        @link NXOpen::MechanicalRouting::PathStockPreferenceBuilder::SpaceReservationMethodFromStartObject NXOpen::MechanicalRouting::PathStockPreferenceBuilder::SpaceReservationMethodFromStartObject@endlink  
                        method of stock assignment.  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::NXObject * StartObject
            (
            );
            /**Sets  the start object to use for the 
                        @link NXOpen::MechanicalRouting::PathStockPreferenceBuilder::SpaceReservationMethodFromStartObject NXOpen::MechanicalRouting::PathStockPreferenceBuilder::SpaceReservationMethodFromStartObject@endlink  
                        method of stock assignment.  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetStartObject
            (
                NXOpen::NXObject * startObject /** start object */ 
            );
            /**Returns  the diameter value to use for the 
                        @link NXOpen::MechanicalRouting::PathStockPreferenceBuilder::SpaceReservationMethodCircular NXOpen::MechanicalRouting::PathStockPreferenceBuilder::SpaceReservationMethodCircular@endlink  
                        method of stock assignment.  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Expression * Diameter
            (
            );
            /**Sets  the diameter value to use for the 
                        @link NXOpen::MechanicalRouting::PathStockPreferenceBuilder::SpaceReservationMethodCircular NXOpen::MechanicalRouting::PathStockPreferenceBuilder::SpaceReservationMethodCircular@endlink  
                        method of stock assignment.  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetDiameter
            (
                NXOpen::Expression * diameter /** diameter */ 
            );
            /**Returns  the height value to use for the  @link 
                        NXOpen::MechanicalRouting::PathStockPreferenceBuilder::SpaceReservationMethodRectangular 
                        NXOpen::MechanicalRouting::PathStockPreferenceBuilder::SpaceReservationMethodRectangular@endlink  
                        method of stock assignment.  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Expression * RectangularHeight
            (
            );
            /**Returns  the Width value to use for the  @link 
                        NXOpen::MechanicalRouting::PathStockPreferenceBuilder::SpaceReservationMethodRectangular 
                        NXOpen::MechanicalRouting::PathStockPreferenceBuilder::SpaceReservationMethodRectangular@endlink  
                        method of stock assignment    
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Expression * RectangularWidth
            (
            );
            /**Returns  the height value to use for the  @link 
                        NXOpen::MechanicalRouting::PathStockPreferenceBuilder::SpaceReservationMethodFlatOval 
                        NXOpen::MechanicalRouting::PathStockPreferenceBuilder::SpaceReservationMethodFlatOval@endlink  
                        method of stock assignment.  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Expression * FlatOvalHeight
            (
            );
            /**Returns  the Width value to use for the  @link 
                        NXOpen::MechanicalRouting::PathStockPreferenceBuilder::SpaceReservationMethodFlatOval 
                        NXOpen::MechanicalRouting::PathStockPreferenceBuilder::SpaceReservationMethodFlatOval@endlink  
                        method of stock assignment    
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Expression * FlatOvalWidth
            (
            );
            /** Sets the identifier of the classification object associated with the part to place 
             <br>  @deprecated Deprecated in NX11.0.1.  Use @link NXOpen::MechanicalRouting::PathStockPreferenceBuilder::SetClassificationObjectIdentifierForStock NXOpen::MechanicalRouting::PathStockPreferenceBuilder::SetClassificationObjectIdentifierForStock@endlink  instead. <br>  

             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NX_DEPRECATED("Deprecated in NX11.0.1.  Use NXOpen::MechanicalRouting::PathStockPreferenceBuilder::SetClassificationObjectIdentifierForStock instead.") void SetClassificationObjectIdentifier
            (
                const NXString & classificationObjectId /** classificationobjectid */ 
            );
            /** Sets the identifier of the classification object associated with the part to place 
             <br>  @deprecated Deprecated in NX11.0.1.  Use @link NXOpen::MechanicalRouting::PathStockPreferenceBuilder::SetClassificationObjectIdentifierForStock NXOpen::MechanicalRouting::PathStockPreferenceBuilder::SetClassificationObjectIdentifierForStock@endlink  instead. <br>  

             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            void SetClassificationObjectIdentifier
            (
                const char * classificationObjectId /** classificationobjectid */ 
            );
            /** Get the identifier of the classification object associated with the stock part to place 
                        NOTE: Client should NOT free the returned string  @return  
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXString GetClassificationObjectIdentifierForStock
            (
            );
            /** Sets the identifier of the classification object associated with the stock part to place 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetClassificationObjectIdentifierForStock
            (
                const NXString & classificationObjectId /** classificationobjectid */ 
            );
            /** Sets the identifier of the classification object associated with the stock part to place 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            void SetClassificationObjectIdentifierForStock
            (
                const char * classificationObjectId /** classificationobjectid */ 
            );
            /** Get the file specification of the stock part to place 
                        NOTE: Client should NOT free the returned string  @return  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXString GetFileSpecificationOfStockToPlace
            (
            );
            /** Sets the file specification of the stock part to place 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetFileSpecificationOfStockToPlace
            (
                const NXString & filename /** filename */ 
            );
            /** Sets the file specification of the stock part to place 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            void SetFileSpecificationOfStockToPlace
            (
                const char * filename /** filename */ 
            );
            /** Get the identifier of the classification object associated with the space reservation part to place 
                         NOTE: Client should NOT free the returned string  @return  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXString GetClassificationObjectIdentifierForSpaceReservation
            (
            );
            /** Sets the identifier of the classification object associated with the space reservation part to place 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetClassificationObjectIdentifierForSpaceReservation
            (
                const NXString & classificationObjectId /** classificationobjectid */ 
            );
            /** Sets the identifier of the classification object associated with the space reservation part to place 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            void SetClassificationObjectIdentifierForSpaceReservation
            (
                const char * classificationObjectId /** classificationobjectid */ 
            );
            /** Get the file specification of the space reservation part to place 
                        NOTE: Client should NOT free the returned string  @return  
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXString GetFileSpecificationOfSpaceReservationToPlace
            (
            );
            /** Sets the file specification of the space reservation part to place 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetFileSpecificationOfSpaceReservationToPlace
            (
                const NXString & filename /** filename */ 
            );
            /** Sets the file specification of the space reservation part to place 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            void SetFileSpecificationOfSpaceReservationToPlace
            (
                const char * filename /** filename */ 
            );
            /** Validate whether the inputs to the component are sufficient for 
                        commit to be called.  If the component is not in a state to commit
                        then an exception is thrown.  For example, if the component requires
                        you to set some property, this method will throw an exception if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful 
             <br>  Created in NX3.0.1.  <br>  
             <br> License requirements : None */
            public: virtual bool Validate
            (
            );
        };
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
