#ifndef NXOpen_LINEDESIGNER_OPERATIONBUILDER_HXX_INCLUDED
#define NXOpen_LINEDESIGNER_OPERATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     LineDesigner_OperationBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/liblinedesigneropencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace LineDesigner
    {
        class OperationBuilder;
    }
    class Builder;
    class SelectDisplayableObject;
    class SelectDisplayableObjectList;
    namespace LineDesigner
    {
        class _OperationBuilderBuilder;
        class OperationBuilderImpl;
        /** use for cearting operation  <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateOperationBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateOperationBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        OperationType </td> <td> 
         
        Undefined </td> </tr> 

        <tr><td> 
         
        Time </td> <td> 
         
        0 </td> </tr> 

        </table>  

         <br>  Created in NX1876.0.0.  <br>  
        */
        class LINEDESIGNEROPENCPPEXPORT  OperationBuilder : public NXOpen::Builder
        {
            /** This enum have collection of all type of operation */
            public: enum Operation
            {
                OperationUndefined/** undefined */ ,
                OperationOperator/** operator */ ,
                OperationTooling/** tooling */ ,
                OperationSafety/** safety */ ,
                OperationConveyance/** conveyance */ ,
                OperationMHRobot/** mhrobot */ ,
                OperationGeoWeld/** geo weld */ ,
                OperationRespot/** respot */ ,
                OperationStudNutBolt/** stud nut bolt */ ,
                OperationRivetFDS/** rivet fds */ ,
                OperationScribing/** scribing */ ,
                OperationVision/** vision */ ,
                OperationLaserSpotWeld/** laser spot weld */ ,
                OperationMigWeld/** mig weld */ ,
                OperationSealingAdhesive/** sealing adhesive */ ,
                OperationLaserCut/** laser cut */ ,
                OperationHemming/** hemming */ ,
                OperationRobotHold/** robot hold */ 
            };

            private: OperationBuilderImpl * m_operationbuilder_impl;
            private: friend class  _OperationBuilderBuilder;
            protected: OperationBuilder();
            public: ~OperationBuilder();
            /**Returns  the select station 
             <br>  Created in NX1876.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObject * SelectStation
            (
            );
            /**Returns  the operation type 
             <br>  Created in NX1876.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::LineDesigner::OperationBuilder::Operation OperationType
            (
            );
            /**Sets  the operation type 
             <br>  Created in NX1876.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void SetOperationType
            (
                NXOpen::LineDesigner::OperationBuilder::Operation operationType /** operationtype */ 
            );
            /**Returns  the name 
             <br>  Created in NX1876.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Sets  the name 
             <br>  Created in NX1876.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the name 
             <br>  Created in NX1876.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            void SetName
            (
                const char * name /** name */ 
            );
            /**Returns  the time 
             <br>  Created in NX1876.0.0.  <br>  
             <br> License requirements : None */
            public: double Time
            (
            );
            /**Sets  the time 
             <br>  Created in NX1876.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void SetTime
            (
                double time /** time */ 
            );
            /**Returns  the select operation 
             <br>  Created in NX1876.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObject * SelectOperation
            (
            );
            /**Returns  the select resources 
             <br>  Created in NX1876.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * SelectResources
            (
            );
            /**Returns  the select features 
             <br>  Created in NX1876.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * SelectFeatures
            (
            );
            /**Returns  the select part 
             <br>  Created in NX1876.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * SelectPart
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
