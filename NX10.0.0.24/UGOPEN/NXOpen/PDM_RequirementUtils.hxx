#ifndef NXOpen_PDM_REQUIREMENTUTILS_HXX_INCLUDED
#define NXOpen_PDM_REQUIREMENTUTILS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PDM_RequirementUtils.ja
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
#include <NXOpen/PDM_TracelinkQuery.hxx>
#include <NXOpen/TaggedObject.hxx>
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
        class RequirementUtils;
    }
    class Session;
    namespace PDM
    {
        class TracelinkQuery;
    }
    namespace PDM
    {
        class RequirementUtilsImpl;
        /** Collection of PDM utility methods  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
         <br>  Created in NX6.0.3.  <br>  
        */
        class NXOPENCPP_PDMEXPORT  RequirementUtils
        {
            private: RequirementUtilsImpl * m_requirementutils_impl;
            private: NXOpen::Session* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit RequirementUtils(NXOpen::Session *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~RequirementUtils();
            /** Returns a Tracelink query object  @return   
             <br>  Created in NX6.0.3.  <br>  
             <br> License requirements : None */
            public: NXOpen::PDM::TracelinkQuery * NewTracelinkQuery
            (
            );
            /** Creates Trace Links from @link NXOpen::Validate::Requirement NXOpen::Validate::Requirement@endlink s to @link NXOpen::Part NXOpen::Part@endlink s
                    For the input requirement_item_numbers:
                    In case of Default Domain: it is Teamcenter item ID.
                    In case of non-Default Domain: it is the multifield key.
                    e.g.  %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                    And the encoded part filename would be containing the MFK.
                    
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void CreateTraceLinks
            (
                std::vector<NXString> & requirementItemNumbers /** requirement multifield key */,
                std::vector<NXString> & requirementRevisions /** requirement item revisions. Must be same size as the item number array */,
                std::vector<NXString> & parts /** part CLI names   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Removes Trace Links between @link NXOpen::Validate::Requirement NXOpen::Validate::Requirement@endlink s and @link NXOpen::Part NXOpen::Part@endlink s
                    For the input requirement_item_numbers:
                    In case of Default Domain: it is Teamcenter item ID.
                    In case of non-Default Domain: it is the multifield key.
                    e.g.  %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                    And the encoded part filename would be containing the MFK.
                    
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void RemoveTraceLinks
            (
                std::vector<NXString> & requirementItemNumbers /** requirement multifield Key */,
                std::vector<NXString> & requirementRevisions /** requirement item revisions. Must be same size as the item number array */,
                std::vector<NXString> & parts /** part CLI names   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
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