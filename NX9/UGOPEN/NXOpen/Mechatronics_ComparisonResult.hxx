#ifndef NXOpen_MECHATRONICS_COMPARISONRESULT_HXX_INCLUDED
#define NXOpen_MECHATRONICS_COMPARISONRESULT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_ComparisonResult.ja
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
#include <NXOpen/Mechatronics_ComparisonResultBase.hxx>
#include <NXOpen/Mechatronics_ComparisonResultAttribute.hxx>
#include <NXOpen/Mechatronics_ComparisonResultElectricalPart.hxx>
#include <NXOpen/libnxopencpp_mechatronics_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Mechatronics
    {
        class ComparisonResult;
    }
    namespace Mechatronics
    {
        class ComparisonResultAttribute;
    }
    namespace Mechatronics
    {
        class ComparisonResultBase;
    }
    namespace Mechatronics
    {
        class ComparisonResultElectricalPart;
    }
    namespace Mechatronics
    {
        class LogicObject;
    }
    namespace Mechatronics
    {
    }
    namespace Mechatronics
    {
        class ComparisonResultImpl;
        /** Represents comparison result 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  ComparisonResult : public Mechatronics::ComparisonResultBase
        {
            /** Defines categories of comparison results */
            public: enum Category
            {
                CategoryCreate/** Create category */,
                CategoryUpdateAttributes/** Update Attributes category */,
                CategoryUpdateParts/** Update Parts category */,
                CategoryMove/** Move category */,
                CategoryDelete/** Delete category */,
                CategoryCreateConflict/** Conflict from Create category */,
                CategoryMoveConflict/** Conflict from Move category */,
                CategoryNotFoundConflict/** Conflict due to the original logical object was deleted */,
                CategoryNoAction/** No Action Required */
            };

            private: ComparisonResultImpl * m_comparisonresult_impl;
            /// \cond NX_NO_DOC 
            public: explicit ComparisonResult(void *ptr);
            /// \endcond 
            /** Frees the object from memory. After this method is called, it is illegal to use the object. In .NET, this method is automatically called when the object is deleted by the garbage collector. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: virtual ~ComparisonResult();
            /**Returns  the category from the comparison result 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Mechatronics::ComparisonResult::Category ResultCategory
            (
            );
            /**Sets  the category from the comparison result 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void SetResultCategory
            (
                NXOpen::Mechatronics::ComparisonResult::Category category /** Category of comparison result */
            );
            /**Returns  the name from the comparison result 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXString ResultName
            (
            );
            /**Returns  the type from the comparison result 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXString ResultType
            (
            );
            /**Returns  the logical object from the comparison result 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Mechatronics::LogicObject * LogicalObject
            (
            );
            /**Sets  the logical object from the comparison result 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void SetLogicalObject
            (
                NXOpen::Mechatronics::LogicObject * logicalObject /** Logical object of comparison result */
            );
            /**Returns  the conflict logical object from the comparison result 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Mechatronics::LogicObject * ConflictLogicalObject
            (
            );
            /**Sets  the conflict logical object from the comparison result 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void SetConflictLogicalObject
            (
                NXOpen::Mechatronics::LogicObject * conflictLogicalObject /** Conflict logical object of comparison result */
            );
            /** Gets a list of attributes from the comparison result 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void GetAttributes
            (
                std::vector<NXOpen::Mechatronics::ComparisonResultAttribute *> & attributes /** Array of attributes */
            );
            /** Gets a list of electrical parts from the comparison result 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void GetElectricalParts
            (
                std::vector<NXOpen::Mechatronics::ComparisonResultElectricalPart *> & electricalParts /** Array of electrical parts */
            );
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