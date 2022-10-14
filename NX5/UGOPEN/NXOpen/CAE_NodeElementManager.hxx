#ifndef NXOpen_CAE_NODEELEMENTMANAGER_HXX_INCLUDED
#define NXOpen_CAE_NODEELEMENTMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_NodeElementManager.ja
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
        class NodeElementManager;
    }
    namespace CAE
    {
        class FEModel;
    }
    namespace CAE
    {
        class ElementConnectivityBuilder;
    }
    namespace CAE
    {
        class ElementCreateBuilder;
    }
    namespace CAE
    {
        class ElementDeleteBuilder;
    }
    namespace CAE
    {
        class ElementExtrudeBuilder;
    }
    namespace CAE
    {
        class ElementModifyLabelBuilder;
    }
    namespace CAE
    {
        class ElementProjectBuilder;
    }
    namespace CAE
    {
        class ElementReflectBuilder;
    }
    namespace CAE
    {
        class ElementRevolveBuilder;
    }
    namespace CAE
    {
        class ElementSplitBuilder;
    }
    namespace CAE
    {
        class ElementTranslateBuilder;
    }
    namespace CAE
    {
        class NodeAlignBuilder;
    }
    namespace CAE
    {
        class NodeCreateBuilder;
    }
    namespace CAE
    {
        class NodeDeleteBuilder;
    }
    namespace CAE
    {
        class NodeModifyLabelBuilder;
    }
    namespace CAE
    {
        class NodeModifyLocationBuilder;
    }
    namespace CAE
    {
        class NodeReflectBuilder;
    }
    namespace CAE
    {
        class NodeRotateBuilder;
    }
    namespace CAE
    {
        class NodeTranslateBuilder;
    }
    namespace CAE
    {
        class NodesBetweenNodesBuilder;
    }
    namespace CAE
    {
        class NodesOnCurveBuilder;
    }
    namespace CAE
    {
        /**  @brief  Provides method for creating  builder for 
            node element operation commands in a fem part  

           <br> To obtain an instance of this class, refer to @link CAE::FEModel CAE::FEModel@endlink  <br> */
        class NXOPENCPPEXPORT NodeElementManager
        {
            private: NXOpen::CAE::FEModel* m_owner;
            public: explicit NodeElementManager(NXOpen::CAE::FEModel *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /** Creates a builder for nodes on curve command @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::NodesOnCurveBuilder * CreateNodesOnCurveBuilder
            (
            );
            /** Creates a builder for node rotate command @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::NodeRotateBuilder * CreateNodeRotateBuilder
            (
            );
            /** Creates a builder for node translate command @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::NodeTranslateBuilder * CreateNodeTranslateBuilder
            (
            );
            /** Creates a builder for node align command @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::NodeAlignBuilder * CreateNodeAlignBuilder
            (
            );
            /** Creates a builder for node modify label command @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::NodeModifyLabelBuilder * CreateNodeModifyLabelBuilder
            (
            );
            /** Creates a builder for element modify label command @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::ElementModifyLabelBuilder * CreateElementModifyLabelBuilder
            (
            );
            /** Creates a builder for node between nodes command @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::NodesBetweenNodesBuilder * CreateNodesBetweenNodesBuilder
            (
            );
            /** Creates a builder for node delete command @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::NodeDeleteBuilder * CreateNodeDeleteBuilder
            (
            );
            /** Creates a builder for element create command @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::ElementCreateBuilder * CreateElementCreateBuilder
            (
            );
            /** Creates a builder for element extrude command @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::ElementExtrudeBuilder * CreateElementExtrudeBuilder
            (
            );
            /** Creates a builder for element revolve command @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::ElementRevolveBuilder * CreateElementRevolveBuilder
            (
            );
            /** Creates a builder for element split command @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::ElementSplitBuilder * CreateElementSplitBuilder
            (
            );
            /** Creates a builder for node create command @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::NodeCreateBuilder * CreateNodeCreateBuilder
            (
            );
            /** Creates a builder for node modify location command @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::NodeModifyLocationBuilder * CreateNodeModifyLocationBuilder
            (
            );
            /** Creates a builder for element project command @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::ElementProjectBuilder * CreateElementProjectBuilder
            (
            );
            /** Creates a builder for element delete command @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::ElementDeleteBuilder * CreateDeleteElementBuilder
            (
            );
            /** Creates a builder for element translate command @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::ElementTranslateBuilder * CreateElementTranslateBuilder
            (
            );
            /** Creates a builder for Node reflect command @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::NodeReflectBuilder * CreateNodeReflectBuilder
            (
            );
            /** Creates a builder for element reflect command @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::ElementReflectBuilder * CreateElementReflectBuilder
            (
            );
            /** Creates a builder for element connectivity command @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::ElementConnectivityBuilder * CreateElementConnectivityBuilder
            (
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif