#ifndef NXOpen_PDM_IATTRIBUTEGROUPOWNER_HXX_INCLUDED
#define NXOpen_PDM_IATTRIBUTEGROUPOWNER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PDM_IAttributeGroupOwner.ja
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
#include <NXOpen/libnxopencpp_pdm_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace PDM
    {
        class IAttributeGroupOwner;
    }
    namespace PDM
    {
        class AttributeGroup;
    }
    namespace PDM
    {
        class AttributeGroupDescription;
    }
    namespace PDM
    {
        class AttributeGroupReviseBuilder;
    }
    namespace PDM
    {
        /** An interface class for objects that own attribute groups. 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_PDMEXPORT  IAttributeGroupOwner
        {
            virtual void EnsureVtableExists() {}
            public: virtual ~IAttributeGroupOwner() {}
            /** Creates an attribute group for a @link NXOpen::PDM::IAttributeGroupOwner NXOpen::PDM::IAttributeGroupOwner@endlink , based on an attribute
                    group type.  An attribute group type is represented by an @link NXOpen::PDM::AttributeGroupDescription NXOpen::PDM::AttributeGroupDescription@endlink .
                 @return  The new attribute group. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: virtual NXOpen::PDM::AttributeGroup * Create
            (
                NXOpen::PDM::AttributeGroupDescription * attributeGroupDescription /** attributegroupdescription */ 
            ) = 0;
            /** Creates a @link NXOpen::PDM::AttributeGroupReviseBuilder NXOpen::PDM::AttributeGroupReviseBuilder@endlink  object.  The builder creates a
                    revision for each attribute group in the input list of existing attribute groups.  @return   
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: virtual NXOpen::PDM::AttributeGroupReviseBuilder * CreateAttributeGroupReviseBuilder
            (
                const std::vector<NXOpen::PDM::AttributeGroup *> & attributeGroups /** attributegroups */ 
            ) = 0;
            /** Returns the @link NXOpen::PDM::AttributeGroup NXOpen::PDM::AttributeGroup@endlink  objects owned by this object.  @return   
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: virtual std::vector<NXOpen::PDM::AttributeGroup *> GetAttributeGroups
            (
            ) = 0;
            /** Returns the @link NXOpen::PDM::AttributeGroupDescription NXOpen::PDM::AttributeGroupDescription@endlink  objects representing the attribute
                    group types supported by this object.  @return   
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: virtual std::vector<NXOpen::PDM::AttributeGroupDescription *> GetAttributeGroupDescriptions
            (
            ) = 0;
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
