#ifndef NXOpen_PDM_EFFECTIVITYTABLEBUILDER_HXX_INCLUDED
#define NXOpen_PDM_EFFECTIVITYTABLEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PDM_EffectivityTableBuilder.ja
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
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/PDM_EffectivityTableBuilder.hxx>
#include <NXOpen/PDM_EffectivityTableRow.hxx>
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
        class EffectivityTableBuilder;
    }
    class CollaborativeDesign;
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace PDM
    {
        class EffectivityTableRow;
    }
    namespace PDM
    {
        class _EffectivityTableBuilderBuilder;
        class EffectivityTableBuilderImpl;
        /** Represents a builder class for effectivity configuration. 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_PDMEXPORT  EffectivityTableBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            private: EffectivityTableBuilderImpl * m_effectivitytablebuilder_impl;
            private: friend class  _EffectivityTableBuilderBuilder;
            protected: EffectivityTableBuilder();
            public: ~EffectivityTableBuilder();
            /** Gets the existing effectivity rows from effectivity table
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            public: void GetEffectivityRows
            (
                std::vector<NXOpen::PDM::EffectivityTableRow *> & effectivityRows /** effectivityrows */ 
            );
            /** Creates new effectivity row in @link NXOpen::PDM::EffectivityTableBuilder NXOpen::PDM::EffectivityTableBuilder@endlink  object  @return  newly created empty effectivity row 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            public: NXOpen::PDM::EffectivityTableRow * CreateNewEffectivityRow
            (
            );
            /** Adds the given effectivity row to @link NXOpen::PDM::EffectivityTableBuilder NXOpen::PDM::EffectivityTableBuilder@endlink  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            public: void AddEffectivityRow
            (
                NXOpen::PDM::EffectivityTableRow * effectivityRow /** effectivityrow */ 
            );
            /** Removes the given effectivity rows from @link NXOpen::PDM::EffectivityTableBuilder NXOpen::PDM::EffectivityTableBuilder@endlink  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            public: void RemoveEffectivityRows
            (
                const std::vector<NXOpen::PDM::EffectivityTableRow *> & effectivityRows /** effectivity rows to be removed*/
            );
            /** Updates this builder with new @link NXOpen::CollaborativeDesign NXOpen::CollaborativeDesign@endlink , validation basis formula and effectivity formulae to edit.
                        Effectivity formulae will be validated against provided validation basis formula.
                    
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            public: void UpdateBuilderDetails
            (
                NXOpen::CollaborativeDesign * cd /** cd */ ,
                const NXString & validationBasisFormula /** validationbasisformula */ ,
                const std::vector<NXString> & effectivityFormulae /** effectivityformulae */ 
            );
            /** Updates this builder with new @link NXOpen::CollaborativeDesign NXOpen::CollaborativeDesign@endlink , validation basis formula and effectivity formulae to edit.
                        Effectivity formulae will be validated against provided validation basis formula.
                    
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            void UpdateBuilderDetails
            (
                NXOpen::CollaborativeDesign * cd /** cd */ ,
                const char * validationBasisFormula /** validationbasisformula */ ,
                const std::vector<NXString> & effectivityFormulae /** effectivityformulae */ 
            );
            /** Commit the modified effectivity rows 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_4gd_integration ("4th Generation Design") */
            public: void Commit
            (
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
