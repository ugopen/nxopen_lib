#ifndef NXOpen_GEOMETRICANALYSIS_ANALYSISOBJECTCOLLECTION_HXX_INCLUDED
#define NXOpen_GEOMETRICANALYSIS_ANALYSISOBJECTCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricAnalysis_AnalysisObjectCollection.ja
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
#include <iterator>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/GeometricAnalysis_SectionAnalysis_SectionAnalysisExBuilder.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_geometricanalysis_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace GeometricAnalysis
    {
        class AnalysisObjectCollection;
    }
    namespace GeometricAnalysis
    {
        class AnalysisManager;
    }
    namespace GeometricAnalysis
    {
        class AnalysisObject;
    }
    class DisplayableObject;
    namespace GeometricAnalysis
    {
        class AnalysisObjectCollectionEx;
    }
    namespace GeometricAnalysis
    {
        class CurveAnalysisCombsBuilder;
    }
    namespace GeometricAnalysis
    {
        class CurveAnalysisDisplay;
    }
    namespace GeometricAnalysis
    {
        class CurveAnalysisInflectionsBuilder;
    }
    namespace GeometricAnalysis
    {
        class CurveAnalysisPeaksBuilder;
    }
    namespace GeometricAnalysis
    {
        class CurveContinuityBuilder;
    }
    namespace GeometricAnalysis
    {
        class CurveCurvatureAnalysisBuilder;
    }
    namespace GeometricAnalysis
    {
        class DeviationGaugeBuilder;
    }
    namespace GeometricAnalysis
    {
        class DraftAnalysisBuilder;
    }
    namespace GeometricAnalysis
    {
        class FaceCurvatureAnalysisBuilder;
    }
    namespace GeometricAnalysis
    {
        class GapFlushness;
    }
    namespace GeometricAnalysis
    {
        class GapFlushnessBuilder;
    }
    namespace GeometricAnalysis
    {
        class HighlightLinesAnalysisBuilder;
    }
    namespace GeometricAnalysis
    {
        class LocalRadiusAnalysis;
    }
    namespace GeometricAnalysis
    {
        class LocalRadiusAnalysisBuilder;
    }
    namespace GeometricAnalysis
    {
        namespace SectionAnalysis
        {
            class SectionAnalysisBuilder;
        }
    }
    namespace GeometricAnalysis
    {
        namespace SectionAnalysis
        {
            class SectionAnalysisExBuilder;
        }
    }
    namespace GeometricAnalysis
    {
        namespace SectionAnalysis
        {
            class SectionAnalysisExObject;
        }
    }
    namespace GeometricAnalysis
    {
        class SectionAnalysisObject;
    }
    namespace GeometricAnalysis
    {
        class SurfaceAnalysisDisplay;
    }
    namespace GeometricAnalysis
    {
        class SurfaceContinuityAnalysisBuilder;
    }
    namespace GeometricAnalysis
    {
        class SurfaceIntersectionBuilder;
    }
    namespace GeometricAnalysis
    {
        class AnalysisObjectCollectionImpl;
        /** Create a AnalysisObjectCollection  <br> To obtain an instance of this class, refer to @link NXOpen::GeometricAnalysis::AnalysisManager  NXOpen::GeometricAnalysis::AnalysisManager @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_GEOMETRICANALYSISEXPORT  AnalysisObjectCollection : public NXOpen::TaggedObjectCollection
        {
            private: AnalysisObjectCollectionImpl * m_analysisobjectcollection_impl;
            private: NXOpen::GeometricAnalysis::AnalysisManager* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit AnalysisObjectCollection(NXOpen::GeometricAnalysis::AnalysisManager *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~AnalysisObjectCollection();
            /** Iterator for accessing the contents of the collection. */
            //lint -sem(NXOpen::GeometricAnalysis::AnalysisObjectCollection::iterator::copy,initializer)
            class iterator : public std::iterator<std::forward_iterator_tag, NXOpen::GeometricAnalysis::AnalysisObject *>
            {
            public:
                /** Default constructor */
                iterator() : m_context(nullptr), m_current(NULL_TAG)
                {
                    // coverity[uninit_member]
                } //lint !e1401 m_state is not initialized
                /// \cond NX_NO_DOC
                explicit iterator(NXOpen::GeometricAnalysis::AnalysisObjectCollection *context) : m_context(context), m_current(NULL_TAG)
                {
                    // coverity[uninit_member]
                }//lint !e1401 m_state is not initialized
                /// \endcond
                /** Copy constructor */
                iterator(const iterator &other): m_context(nullptr), m_current(NULL_TAG)
                {
                    copy(other);
                }
                /** Copy constructor */
                iterator &operator =(const iterator &other)
                {
                    if (&other != this)
                        copy(other);
                    return *this;
                }
                /** Tests if the iterator objects on the left side and the right side of the operator are equal. */
                bool operator ==(const iterator &other) const
                {
                    return m_current == other.m_current && m_context == other.m_context;
                }
                /** Tests if the iterator objects on the left side and the right side of the operator are not equal. */
                bool operator !=(const iterator &other) const
                {
                    return !operator == (other);
                }
                /** Return the element currently pointed to by the iterator. */
                NXOPENCPP_GEOMETRICANALYSISEXPORT  value_type operator * () const;
                /** Points the iterator to next element. */
                iterator & operator ++()
                {
                    next();
                    return *this;
                }
                /** Points the iterator to next element. */
                iterator operator ++(int)
                {
                    iterator tmp(*this);
                    ++*this;
                    return tmp;
                }
            private:
                void copy(const iterator &other)
                {
                    m_context = other.m_context;
                    m_current = other.m_current;
                    for (int i = 0; i < sizeof(m_state)/sizeof(m_state[0]); i++)
                         m_state[i] = other.m_state[i];
                }
                NXOPENCPP_GEOMETRICANALYSISEXPORT  void next();
                NXOpen::GeometricAnalysis::AnalysisObjectCollection *m_context;
                tag_t m_current;
                unsigned int m_state[8];
            };
            /** Returns an iterator addressing the first element. */
            iterator begin();
            /** Returns an iterator addressing one past the last element. */
            iterator end()
            {
                return iterator(this);
            }
            /** Creates a gap and flushness builder  @return  Gap and Flushness builder 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::GeometricAnalysis::GapFlushnessBuilder * CreateGapFlushnessBuilder
            (
                NXOpen::GeometricAnalysis::GapFlushness * gfaoObject /** Gap and Flushness  */
            );
            /** Creates a surface continuity analysis builder  @return  Surface Continuity Analysis builder 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : gateway ("UG GATEWAY") */
            public: NXOpen::GeometricAnalysis::SurfaceContinuityAnalysisBuilder * CreateSurfaceContinuityAnalysisBuilder
            (
                NXOpen::DisplayableObject * scaoObject /** Surface Continuity Analysis */
            );
            /** Creates a curve curvature analysis builder  @return  Curve Curvature Analysis builder 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : gateway ("UG GATEWAY") */
            public: NXOpen::GeometricAnalysis::CurveCurvatureAnalysisBuilder * CreateCurveCurvatureAnalysisBuilder
            (
                NXOpen::DisplayableObject * caaoObject /**Curve Curvature Analysis */
            );
            /** Creates a curve analysis combs builder  @return  Curve analysis Combs Builder
             <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveCurvatureAnalysis NXOpen::GeometricAnalysis::CurveCurvatureAnalysis@endlink . <br>  

             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NX_DEPRECATED("Deprecated in NX8.5.0.  Use NXOpen::GeometricAnalysis::CurveCurvatureAnalysis.") NXOpen::GeometricAnalysis::CurveAnalysisCombsBuilder * CreateCurveAnalysisCombsBuilder
            (
            );
            /** Creates a curve analysis inflections builder  @return  Curve analysis Inflections Builder 
             <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveCurvatureAnalysis NXOpen::GeometricAnalysis::CurveCurvatureAnalysis@endlink . <br>  

             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NX_DEPRECATED("Deprecated in NX8.5.0.  Use NXOpen::GeometricAnalysis::CurveCurvatureAnalysis.") NXOpen::GeometricAnalysis::CurveAnalysisInflectionsBuilder * CreateCurveAnalysisInflectionsBuilder
            (
            );
            /** Creates a curve analysis peaks builder  @return  Curve analysis Peaks Builder 
             <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveCurvatureAnalysis NXOpen::GeometricAnalysis::CurveCurvatureAnalysis@endlink . <br>  

             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NX_DEPRECATED("Deprecated in NX8.5.0.  Use NXOpen::GeometricAnalysis::CurveCurvatureAnalysis.") NXOpen::GeometricAnalysis::CurveAnalysisPeaksBuilder * CreateCurveAnalysisPeaksBuilder
            (
            );
            /** Creates a Highlight Lines Analysis builder  @return  Highlight Lines Analysis builder 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
            public: NXOpen::GeometricAnalysis::HighlightLinesAnalysisBuilder * CreateHighlightLinesAnalysisBuilder
            (
                NXOpen::DisplayableObject * hpaoObject /** Highlight Lines Analysis object */
            );
            /** Creates a Section Analysis object builder  @return  Section Analysis builder 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
            public: NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder * CreateSectionAnalysisBuilder
            (
                NXOpen::GeometricAnalysis::SectionAnalysisObject * msaoObject /** Section Analysis object */
            );
            /** Creates a Section Analysis builder of a new version @return  Section Analysis builder 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
            public: NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder * CreateSectionAnalysisExBuilder
            (
                NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExObject * csaoObject /** Section Analysis object */
            );
            /** Creates a  Deviation Gauge Builder  @return  DeviationGauge builder 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::GeometricAnalysis::DeviationGaugeBuilder * CreateDeviationGaugeBuilder
            (
                NXOpen::DisplayableObject * ddaoObject /** DDAO  */
            );
            /** Creates a Curve Continuity Builder  @return  Curve Continuity AO builder 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : gateway ("UG GATEWAY") */
            public: NXOpen::GeometricAnalysis::CurveContinuityBuilder * CreateCurveContinuityBuilder
            (
                NXOpen::DisplayableObject * ccaoObject /** CCAO */
            );
            /** Creates a surface intersection  builder  @return  surface intersection builder 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
            public: NXOpen::GeometricAnalysis::SurfaceIntersectionBuilder * CreateSurfaceIntersectionBuilder
            (
                NXOpen::DisplayableObject * siaoObject /**surface intersection */
            );
            /** Creates a draft analysis builder  @return  draft analysis builder 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
            public: NXOpen::GeometricAnalysis::DraftAnalysisBuilder * CreateDraftAnalysisBuilder
            (
                NXOpen::DisplayableObject * daoObject /** DAO */
            );
            /** Creates a @link NXOpen::GeometricAnalysis::LocalRadiusAnalysisBuilder NXOpen::GeometricAnalysis::LocalRadiusAnalysisBuilder@endlink  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricAnalysis::LocalRadiusAnalysisBuilder * CreateLocalRadiusAnalysisBuilder
            (
                NXOpen::GeometricAnalysis::LocalRadiusAnalysis * lrao /** lrao */ 
            );
            /** Creates a face curvature analysis builder  @return  face curvature analysis builder 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
            public: NXOpen::GeometricAnalysis::FaceCurvatureAnalysisBuilder * CreateFaceCurvatureAnalysisBuilder
            (
                NXOpen::DisplayableObject * fcaoObject /** FCAO */
            );


            /** Returns object for displaying curve analysis information 
             <br>  Created in NX3.0.0.  <br>  
            */
            public: NXOpen::GeometricAnalysis::CurveAnalysisDisplay *CurveAnalysisDisplayObject();
            /** Returns object for displaying surface analysis information 
             <br>  Created in NX3.0.0.  <br>  
            */
            public: NXOpen::GeometricAnalysis::SurfaceAnalysisDisplay *SurfaceAnalysisDisplayObject();
            /** Returns the AnalysisObjectCollectionEx instance belonging to this part 
             <br>  Created in NX11.0.0.  <br>  
            */
            public: NXOpen::GeometricAnalysis::AnalysisObjectCollectionEx *AnalysisObjectsEx();
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