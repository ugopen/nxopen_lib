#ifndef NXOpen_CAE_LAMINATEPLYGROUP_HXX_INCLUDED
#define NXOpen_CAE_LAMINATEPLYGROUP_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_LaminatePlyGroup.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class LaminatePlyGroup;
    }
    namespace CAE
    {
        class LaminatePlyCollection;
    }
    namespace CAE
    {
        class _LaminatePlyGroupBuilder;
        /**  @brief  Represents one ply group in a laminate layup 

          */
        class NXOPENCPPEXPORT LaminatePlyGroup : public TaggedObject
        {
            /** Used to specify the kind of linked group created */
            public: enum Link
            {
                LinkNone/** not a linked group */,
                LinkRepeat/** same ply layup */,
                LinkSymm/** symmetric layup */,
                LinkAnti/** symmetric layup with reversed angles */,
                LinkRev/** same layup with reversed angles */
            };

            private: friend class  _LaminatePlyGroupBuilder;
            protected: LaminatePlyGroup();
            /**Returns  the definition rule for the PlyGroup  <br> License requirements : nx_lam_composites ("Laminate Composites") */
            public: NXOpen::CAE::LaminatePlyGroup::Link LinkType
            (
            );
            /**Returns  the group name  <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Sets  the group name  <br> License requirements : nx_lam_composites ("Laminate Composites") */
            public: void SetName
            (
                const NXString & name /** group name */
            );


            private: NXOpen::CAE::LaminatePlyCollection *plies;
            /** Returns the Ply collection of this group */
            public: NXOpen::CAE::LaminatePlyCollection *Plies()
            {
                return plies;
            }
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif