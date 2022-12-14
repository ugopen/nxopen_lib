#ifndef NXOpen_CAE_LAMINATEMETASOLBUILDER_HXX_INCLUDED
#define NXOpen_CAE_LAMINATEMETASOLBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_LaminateMetaSolBuilder.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/CAE_LaminateMetaSolBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class LaminateMetaSolBuilder;
    }
    class Builder;
    namespace CAE
    {
        class _LaminateMetaSolBuilderBuilder;
        /** Represents a @link CAE::LaminateMetaSol CAE::LaminateMetaSol@endlink  builder  <br> To create a new instance of this class, use @link CAE::SimSimulation::CreateLaminateMetaSolBuilder CAE::SimSimulation::CreateLaminateMetaSolBuilder@endlink  <br> 
        Default values:
        Index: True
        InputType: SolverShellStressResultant
        Margin: False
        PlyStrain: False
        PlyStress: False
        */
        class NXOPENCPPEXPORT LaminateMetaSolBuilder : public Builder
        {

            public: enum MyInputType
            {
                MyInputTypeSolverShellStressResultant/** solver shell stress resultant */ ,
                MyInputTypeSolverPlyStressesandStrains/** solver ply stressesand strains */ 
            };

            private: friend class  _LaminateMetaSolBuilderBuilder;
            protected: LaminateMetaSolBuilder();
            /**Returns  the metasol name  <br> License requirements : None */
            public: NXString MetasolName
            (
            );
            /**Sets  the metasol name  <br> License requirements : nx_lam_composites ("Laminate Composites") */
            public: void SetMetasolName
            (
                const NXString & metasolName /** metasolname */ 
            );
            /**Returns  the solution list  <br> License requirements : None */
            public: int RefSolIndex
            (
            );
            /**Sets  the solution list  <br> License requirements : nx_lam_composites ("Laminate Composites") */
            public: void SetRefSolIndex
            (
                int index /** index */ 
            );
            /**Returns  the input type  <br> License requirements : None */
            public: NXOpen::CAE::LaminateMetaSolBuilder::MyInputType InputType
            (
            );
            /**Sets  the input type  <br> License requirements : nx_lam_composites ("Laminate Composites") */
            public: void SetInputType
            (
                NXOpen::CAE::LaminateMetaSolBuilder::MyInputType inputType /** inputtype */ 
            );
            /**Returns  the ply stresses  <br> License requirements : None */
            public: bool PlyStress
            (
            );
            /**Sets  the ply stresses  <br> License requirements : nx_lam_composites ("Laminate Composites") */
            public: void SetPlyStress
            (
                bool plyStress /** plystress */ 
            );
            /**Returns  the ply strains  <br> License requirements : None */
            public: bool PlyStrain
            (
            );
            /**Sets  the ply strains  <br> License requirements : nx_lam_composites ("Laminate Composites") */
            public: void SetPlyStrain
            (
                bool plyStrain /** plystrain */ 
            );
            /**Returns  the indices  <br> License requirements : None */
            public: bool Index
            (
            );
            /**Sets  the indices  <br> License requirements : nx_lam_composites ("Laminate Composites") */
            public: void SetIndex
            (
                bool index /** index */ 
            );
            /**Returns  the margins  <br> License requirements : None */
            public: bool Margin
            (
            );
            /**Sets  the margins  <br> License requirements : nx_lam_composites ("Laminate Composites") */
            public: void SetMargin
            (
                bool margin /** margin */ 
            );
            /** the margins  @return   <br> License requirements : None */
            public: int GetSelectedResultSet
            (
                int index /** index */ 
            );
            public: void SetSelectedResultSet
            (
                int index /** index */ ,
                int selectedResultSet /** selected result set */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
