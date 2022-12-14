#ifndef NXOpen_FEATURES_CURVEFINDERBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_CURVEFINDERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_CurveFinderBuilder.ja
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
#include <NXOpen/Features_CurveFinderBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        class CurveFinderBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class NXObject;
    class ScCollector;
    class SelectDisplayableObjectList;
    class SelectNXObject;
    namespace Features
    {
        class _CurveFinderBuilderBuilder;
        class CurveFinderBuilderImpl;
        /** Represents a collection of curves and their relationships to other curves in the model 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  CurveFinderBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            private: CurveFinderBuilderImpl * m_curvefinderbuilder_impl;
            private: friend class  _CurveFinderBuilderBuilder;
            protected: CurveFinderBuilder();
            public: ~CurveFinderBuilder();
            /**Returns  the curve collector 
             <br>  @deprecated Deprecated in NX10.0.0.  This is for pre NX10 usage, do not use this method. <br>  

             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX10.0.0.  This is for pre NX10 usage, do not use this method.") NXOpen::ScCollector * CurveSection
            (
            );
            /**Returns  the curve and point collector 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * CurvePointList
            (
            );
            /** Adds curves to collector 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void SelectCurves
            (
                const std::vector<NXOpen::NXObject *> & curves /** curves */ 
            );
            /** Removes curves from collector 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void DeselectCurves
            (
                const std::vector<NXOpen::NXObject *> & curves /** curves */ 
            );
            /** Selects entity for symmetry reference 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void SelectSymmetryReference
            (
                NXOpen::NXObject * symmetryReference /** symmetryreference */ 
            );
            /** Deselect entity for symmetry reference 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void DeselectSymmetryReference
            (
                NXOpen::NXObject * symmetryReference /** symmetryreference */ 
            );
            /** Adds tangent relations of the last curves added to curve collector 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void AddTangent
            (
            );
            /** Removes tangent relations of the last curves added to curve collector 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void RemoveTangent
            (
            );
            /** Adds parallel relations of the last curves added to curve collector 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void AddParallel
            (
            );
            /** Removes parallel relations of the last curves added to curve collector 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void RemoveParallel
            (
            );
            /** Adds offset relations of the last curves added to curve collector 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void AddOffset
            (
            );
            /** Removes offset relations of the last curves added to curve collector 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void RemoveOffset
            (
            );
            /** Adds coincident vertex relations of the last vertexes added to curve collector 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void AddCoincident
            (
            );
            /** Removes coincident vertex relations of the last vertexes added to curve collector 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void RemoveCoincident
            (
            );
            /** Adds vertex on curve relations of the last curves added to curve collector 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void AddVertexOnCurve
            (
            );
            /** Removes vertex on curve relations of the last curves added to curve collector 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void RemoveVertexOnCurve
            (
            );
            /** Adds chamfer relations of the last curves added to curve collector 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void AddChamfer
            (
            );
            /** Removes chamfer relations of the last curves added to curve collector 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void RemoveChamfer
            (
            );
            /** Adds conlinear relations of the last curves added to curve collector 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void AddConlinear
            (
            );
            /** Removes conlinear relations of the last curves added to curve collector 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void RemoveConlinear
            (
            );
            /** Adds concentric relations of the last curves added to curve collector 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void AddConcentric
            (
            );
            /** Removes concentric relations of the last curves added to curve collector 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void RemoveConcentric
            (
            );
            /** Adds equal radius relations of the last curves added to curve collector 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void AddEqualRadius
            (
            );
            /** Removes equal radius relations of the last curves added to curve collector 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void RemoveEqualRadius
            (
            );
            /** Add symmetric relations of the last curves added to curve collector 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void AddSymmetric
            (
                int planeType /** planetype */ 
            );
            /** Removes symmetric relations of the last curves added to curve collector 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void RemoveSymmetric
            (
                int planeType /** planetype */ 
            );
            /**Returns  a value that indicates which symmetric option is 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: int SymmetryOption
            (
            );
            /**Sets  a value that indicates which symmetric option is 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void SetSymmetryOption
            (
                int symmetryOption /** symmetryoption */ 
            );
            /**Returns  the symmetry line reference 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObject * SymmetryReference
            (
            );
            /**Returns  a value that indicates whether relation recognition is enabled 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool UseCurveFinder
            (
            );
            /**Sets  a value that indicates whether relation recognition is enabled 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void SetUseCurveFinder
            (
                bool curveBrowseEnabled /** curvebrowseenabled */ 
            );
            /** Finds relation curves 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void FindRelationCurve
            (
                const std::vector<NXOpen::NXObject *> & selectedCurves /** selectedcurves */ 
            );
            /**Returns  a value that indicates whether add tangent relation recognition for the last curves added to curve collector 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool TangentEnabled
            (
            );
            /**Sets  a value that indicates whether add tangent relation recognition for the last curves added to curve collector 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void SetTangentEnabled
            (
                bool tangentEnabled /** tangentenabled */ 
            );
            /**Returns  a value that indicates whether add concentric relation recognition for the last curves added to curve collector 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool ConcentricEnabled
            (
            );
            /**Sets  a value that indicates whether add concentric relation recognition for the last curves added to curve collector 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void SetConcentricEnabled
            (
                bool concentricEnabled /** concentricenabled */ 
            );
            /**Returns  a value that indicates whether add collinear relation recognition for the last curves added to curve collector 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool CollinearEnabled
            (
            );
            /**Sets  a value that indicates whether add collinear relation recognition for the last curves added to curve collector 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void SetCollinearEnabled
            (
                bool collinearEnabled /** collinearenabled */ 
            );
            /**Returns  a value that indicates whether add equal radius recognition for the last curves added to curve collector 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool EqualRadiusEnabled
            (
            );
            /**Sets  a value that indicates whether add equal radius recognition for the last curves added to curve collector 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void SetEqualRadiusEnabled
            (
                bool equalRadiusEnabled /** equalradiusenabled */ 
            );
            /**Returns  a value that indicates whether add symmetric relation recognition for the last curves added to curve collector 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool SymmetricEnabled
            (
            );
            /**Sets  a value that indicates whether add symmetric relation recognition for the last curves added to curve collector 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void SetSymmetricEnabled
            (
                bool symmetricEnabled /** symmetricenabled */ 
            );
            /**Returns  a value that indicates whether add parallel relation recognition for the last curves added to curve collector 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool ParallelEnabled
            (
            );
            /**Sets  a value that indicates whether add parallel relation recognition for the last curves added to curve collector 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void SetParallelEnabled
            (
                bool parallelEnabled /** parallelenabled */ 
            );
            /**Returns  a value that indicates whether add offset relation recognition for the last curves added to curve collector 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool OffsetEnabled
            (
            );
            /**Sets  a value that indicates whether add offset relation recognition for the last curves added to curve collector 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void SetOffsetEnabled
            (
                bool offsetEnabled /** offsetenabled */ 
            );
            /**Returns  a value that indicates whether add coincident vertex relation recognition for the last curves added to curve collector 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool CoincidentVertexEnabled
            (
            );
            /**Sets  a value that indicates whether add coincident vertex relation recognition for the last curves added to curve collector 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void SetCoincidentVertexEnabled
            (
                bool coincidentVertexEnabled /** coincidentvertexenabled */ 
            );
            /**Returns  a value that indicates whether add vertex on curve relation recognition for the last vertexes added to the collector 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool VertexOnCurveEnabled
            (
            );
            /**Sets  a value that indicates whether add vertex on curve relation recognition for the last vertexes added to the collector 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void SetVertexOnCurveEnabled
            (
                bool vertexOnCurveEnabled /** vertexoncurveenabled */ 
            );
            /**Returns  a value that indicates whether add chamfer relation recognition for the last curves added to curve collector 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool ChamferEnabled
            (
            );
            /**Sets  a value that indicates whether add chamfer relation recognition for the last curves added to curve collector 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void SetChamferEnabled
            (
                bool chamferEnabled /** chamferenabled */ 
            );
            /**Returns  a value that indicates which find scope option is 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: int FindScopeOption
            (
            );
            /**Sets  a value that indicates which find scope option is 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void SetFindScopeOption
            (
                int scopeOption /** scopeoption */ 
            );
            /** Finds relation curves in the scope 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void FindScopeCurve
            (
                const std::vector<NXOpen::NXObject *> & selectedCurves /** selectedcurves */ 
            );
            /** Close the VTK interaction and Remove all nodes from the Engine 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void RemoveEngineNodes
            (
            );
            /** ReStore all nodes from the Engine On Undo 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void RestoreEngineNodes
            (
            );
            /**Returns  a value that indicates what kind of relations are needed to recognize 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: int RelationScope
            (
            );
            /**Sets  a value that indicates what kind of relations are needed to recognize 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void SetRelationScope
            (
                int relationScope /** relationscope */ 
            );
            /** Set the distance Tolerance for loop Recognization 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void SetDistanceTolerance
            (
                double distanceTolerance /** distancetolerance */ 
            );
            /** Remove all the included constraint 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void RemoveIncludedConstraints
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
