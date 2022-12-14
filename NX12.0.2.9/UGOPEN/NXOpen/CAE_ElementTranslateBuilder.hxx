#ifndef NXOpen_CAE_ELEMENTTRANSLATEBUILDER_HXX_INCLUDED
#define NXOpen_CAE_ELEMENTTRANSLATEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ElementTranslateBuilder.ja
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
#include <NXOpen/CAE_ElementTypeBuilder.hxx>
#include <NXOpen/CAE_SelectElementsBuilder.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class ElementTranslateBuilder;
    }
    class Builder;
    namespace CAE
    {
        class ElementTypeBuilder;
    }
    namespace CAE
    {
        class SelectElementsBuilder;
    }
    class CoordinateSystem;
    class Direction;
    class Expression;
    class Point;
    namespace CAE
    {
        class _ElementTranslateBuilderBuilder;
        class ElementTranslateBuilderImpl;
        /**
            Represents a @link NXOpen::CAE::ElementTranslateBuilder NXOpen::CAE::ElementTranslateBuilder@endlink 
             <br> To create a new instance of this class, use @link NXOpen::CAE::NodeElementManager::CreateElementTranslateBuilder  NXOpen::CAE::NodeElementManager::CreateElementTranslateBuilder @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  ElementTranslateBuilder : public NXOpen::Builder
        {
            /** the copy types */
            public: enum CopyType
            {
                CopyTypeTranslateOnly/** translate without copying elements*/,
                CopyTypeCopyTranslate/** first copy elements then translate the copies */,
                CopyTypeElementCoat/** make 1D element using the existing nodes */
            };

            /** Translation method */
            public: enum MethodType
            {
                MethodTypeComponent/** translate by components  */,
                MethodTypeDirection/** translate along a vector */,
                MethodTypeElemNormal/** translate along element normal */,
                MethodTypePointToPoint/** translate by point to point */
            };

            /** Distance - specify whether the translation distance is per copy or total */
            public: enum DistanceType
            {
                DistanceTypePerCopy/** distance specified is for each copy */,
                DistanceTypeTotal/** distance specified is total translation distance */
            };

            /** Dimension of the elements to be created */
            public: enum ElemDimensionType
            {
                ElemDimensionTypeAny/** any element can be selected         */,
                ElemDimensionTypeBeam/** only beam elements can be selected  */,
                ElemDimensionTypeShell/** only shell elements can be selected */,
                ElemDimensionTypeSolid/** only solid elements can be selected */
            };

            /** Option to create a new mesh or add the new elements to an existing mesh */
            public: enum NewMeshType
            {
                NewMeshTypeCreate/** create a new mesh */,
                NewMeshTypeExisting/** add new elements to an existing mesh */
            };

            /**  Option to use label/increment or offset */
            public: enum LabelType
            {
                LabelTypeLabel/** specify start label and increment for new elements */,
                LabelTypeOffset/** offset labels of selected element to get new labels */
            };

            private: ElementTranslateBuilderImpl * m_elementtranslatebuilder_impl;
            private: friend class  _ElementTranslateBuilderBuilder;
            protected: ElementTranslateBuilder();
            public: ~ElementTranslateBuilder();
            /**Returns  the selected elements 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::SelectElementsBuilder * ElementSelection
            (
            );
            /**Returns  the element type builder.  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::ElementTypeBuilder * ElementType
            (
            );
            /**Returns  the number of copies to be created for each selected element 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: int NumCopy
            (
            );
            /**Sets  the number of copies to be created for each selected element 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetNumCopy
            (
                int numCopy /** num copy */ 
            );
            /**Returns  the method to be used for translating the selected elements 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::ElementTranslateBuilder::MethodType Method
            (
            );
            /**Sets  the method to be used for translating the selected elements 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetMethod
            (
                NXOpen::CAE::ElementTranslateBuilder::MethodType method /** method */ 
            );
            /**Returns  the coordinate system to be used for translating the selected elements 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CoordinateSystem * Csys
            (
            );
            /**Sets  the coordinate system to be used for translating the selected elements 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetCsys
            (
                NXOpen::CoordinateSystem * csys /** csys */ 
            );
            /**Returns  the vector along which the selected elements should be translated 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Direction * Vector
            (
            );
            /**Sets  the vector along which the selected elements should be translated 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetVector
            (
                NXOpen::Direction * vector /** vector */ 
            );
            /**Returns  the flip state from the builder 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: int FlipState
            (
            );
            /**Sets  the flip state from the builder 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetFlipState
            (
                int flipstate /** flipstate */ 
            );
            /**Returns  the distance option 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::ElementTranslateBuilder::DistanceType DistanceOption
            (
            );
            /**Sets  the distance option 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetDistanceOption
            (
                NXOpen::CAE::ElementTranslateBuilder::DistanceType distanceOption /** distance option */ 
            );
            /**Returns  the total distance for translation along a vector 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Distance
            (
            );
            /**Returns  the x component of distance for translation in a cartesian coordinate system 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * XDistance
            (
            );
            /**Returns  the y component of distance for translation in a cartesian coordinate system 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * YDistance
            (
            );
            /**Returns  the z component of distance for translation in a cartesian/cylindrical coordinate system 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * ZDistance
            (
            );
            /**Returns  the radial component of distance for translation in a cylindrical/spherical coordinate system 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * RDistance
            (
            );
            /**Returns  the theta angle for translation in a cylindrical/spherical coordinate system 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * TAngle
            (
            );
            /**Returns  the phi angle for translation in a spherical coordinate system 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * PAngle
            (
            );
            /**Returns  the dimension of the elements to be translated 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::ElementTranslateBuilder::ElemDimensionType ElementDimension
            (
            );
            /**Sets  the dimension of the elements to be translated 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetElementDimension
            (
                NXOpen::CAE::ElementTranslateBuilder::ElemDimensionType elementDimension /** element dimension */ 
            );
            /**Returns  the neutral name of the elements to be created 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXString NeutralName
            (
            );
            /**Sets  the neutral name of the elements to be created 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetNeutralName
            (
                const NXString & neutralName /** neutral name */ 
            );
            /**Sets  the neutral name of the elements to be created 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            void SetNeutralName
            (
                const char * neutralName /** neutral name */ 
            );
            /**Returns  the name of the mesh collector which will hold the new elements 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXString MeshCollectorName
            (
            );
            /**Sets  the name of the mesh collector which will hold the new elements 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetMeshCollectorName
            (
                const NXString & meshCollectorName /** mesh collector name */ 
            );
            /**Sets  the name of the mesh collector which will hold the new elements 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            void SetMeshCollectorName
            (
                const char * meshCollectorName /** mesh collector name */ 
            );
            /**Returns  the option to create a new mesh or add the new elements to an existing mesh  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::ElementTranslateBuilder::NewMeshType NewMeshOption
            (
            );
            /**Sets  the option to create a new mesh or add the new elements to an existing mesh  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetNewMeshOption
            (
                NXOpen::CAE::ElementTranslateBuilder::NewMeshType newMeshOption /** new mesh option */ 
            );
            /**Returns  the name of the mesh that will hold the new elements 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXString MeshName
            (
            );
            /**Sets  the name of the mesh that will hold the new elements 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetMeshName
            (
                const NXString & meshName /** mesh name */ 
            );
            /**Sets  the name of the mesh that will hold the new elements 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            void SetMeshName
            (
                const char * meshName /** mesh name */ 
            );
            /**Returns  the option to specify the start label and increment for the new elements OR 
                        specify an offset from the existing element labels 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::ElementTranslateBuilder::LabelType LabelOption
            (
            );
            /**Sets  the option to specify the start label and increment for the new elements OR 
                        specify an offset from the existing element labels 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetLabelOption
            (
                NXOpen::CAE::ElementTranslateBuilder::LabelType labelOption /** label option */ 
            );
            /**Returns  the start label for the new elements 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: int Label
            (
            );
            /**Sets  the start label for the new elements 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetLabel
            (
                int label /** label */ 
            );
            /**Returns  the increment in label for each new element 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: int Increment
            (
            );
            /**Sets  the increment in label for each new element 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetIncrement
            (
                int increment /** increment */ 
            );
            /**Returns  the offset to be used to generate new element labels 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: int Offset
            (
            );
            /**Sets  the offset to be used to generate new element labels 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetOffset
            (
                int offset /** offset */ 
            );
            /**Returns  the option which indicates whether mesh is exported to solver or not.
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool ExportMesh
            (
            );
            /**Sets  the option which indicates whether mesh is exported to solver or not.
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetExportMesh
            (
                bool fExportMesh /** fexportmesh */ 
            );
            /**Returns  the copy option .
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::ElementTranslateBuilder::CopyType CopyOption
            (
            );
            /**Sets  the copy option .
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetCopyOption
            (
                NXOpen::CAE::ElementTranslateBuilder::CopyType inCopyoption /** incopyoption */ 
            );
            /**Returns  the source point .
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * SourcePoint
            (
            );
            /**Sets  the source point .
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetSourcePoint
            (
                NXOpen::Point * sourcePoint /** sourcepoint */ 
            );
            /**Returns  the target point .
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * TargetPoint
            (
            );
            /**Sets  the target point .
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetTargetPoint
            (
                NXOpen::Point * targetPoint /** targetpoint */ 
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
