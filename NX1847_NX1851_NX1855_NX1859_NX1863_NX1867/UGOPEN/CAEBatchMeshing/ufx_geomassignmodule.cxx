/*****************************************************************************
**
** ufx_geomassignmodule.cxx
**
** Description:
**    Main file for the mesh control assignment application. 
**
*


**
*****************************************************************************/

/* ============================
        Includes needed
   ============================ */
#include <uf_defs.h>
#include <string.h>
#include <ctype.h>
#include <stdarg.h>
#include <map>

#include <uf.h>
#include <uf_obj.h>
#include <uf_sf.h>
#include <ufx_geomassignmodule.hxx>

#include <NXOpen/CAE_CAEBody.hxx>
#include <NXOpen/CAE_CAEFace.hxx>
#include <NXOpen/CAE_CAEEdge.hxx>
#include <NXOpen/CAE_MeshControl.hxx>
#include <NXOpen/CAE_MeshControlBuilder.hxx>
#include <NXOpen/CAE_MeshControlCollection.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/NXObjectManager.hxx>
#include <NXOpen/SelectNXObjectList.hxx>

using namespace std;
using namespace NXOpen;

struct nxstring_less:
    public std::binary_function<NXString,NXString,bool>
{
    bool operator()(const NXString &lhs,const NXString &rhs) const
    {
        const char*pl = lhs.GetText();
        const char*pr = rhs.GetText();

       return ( strcmp( pl,pr ) < 0 );
            
    }

};

typedef multimap<NXOpen::NXString, tag_t, nxstring_less> StlStringTagMultiMap; 

multimap<NXOpen::NXString, tag_t, nxstring_less>::iterator it;
multimap<NXOpen::NXString, tag_t, nxstring_less>::iterator assingit;

StlStringTagMultiMap mMeshControlInfo;/* Mesh control definition map contains name and tag_t mesh control definition */
StlStringTagMultiMap mAssignedMeshControlInfo;/* On assigned mesh controls are stored into this map */

static bool MeshControlAssignment(CAE::FEModel *fEModel1, 
                                  CAE::MeshControl *meshControl1, 
                                  std::vector<NXObject *>objects, 
                                  bool usefiltertoggleonly);

static void upper_to_lower_case ( NXString *strString);

static void write_info_fprintf(bool        fToConsole, 
                               FILE       *fp,             /* I   : File to print*/
                               const char *format_string,  /* I   */
                               ...                         /* I   */ );

geomAssignment::geomAssignment( void )
{
}

geomAssignment::~geomAssignment()
{
}

void geomAssignment::mesh_control_processing_module( FILE *batchmesher_logger_file, tag_t partTag, CAE::FEModel *fEModel1, int nCAEBodies, tag_t *CAEBodies_p )
{
    int  type, mainType, subType;
    std::vector<NXObject::AttributeInformation> info1;
    std::vector<NXOpen::NXObject::AttributeInformation>::iterator attrInfoItr;
    type = UF_caemisc_type;
    tag_t meshcontrol = NULL_TAG;  

    std::vector<CAE::CAEBody *> CAEbodies1;

    pair<multimap<NXOpen::NXString, tag_t, nxstring_less>::iterator,multimap<NXOpen::NXString, tag_t, nxstring_less>::iterator> ret;
    pair<multimap<NXOpen::NXString, tag_t, nxstring_less>::iterator,multimap<NXOpen::NXString, tag_t, nxstring_less>::iterator> assignret;

    write_info_fprintf(true, batchmesher_logger_file, " \n\n");
    write_info_fprintf(true, batchmesher_logger_file, "Mesh Control Geometry Assignment \n");
    write_info_fprintf(true, batchmesher_logger_file, "================================ \n");

    write_info_fprintf(true, batchmesher_logger_file, "   Name(s) of Mesh Control Definition(s):\n");
    /* 1. Cycle through all the mesh control definitons in the current FEM produced from the TEMPLATE provided */ 
    UF_OBJ_cycle_objs_in_part( partTag, type, &meshcontrol ); 

    while ( meshcontrol != NULL_TAG )
    {
        UF_OBJ_ask_type_and_subtype(meshcontrol, &mainType, &subType);
        
        if (subType == UF_caemisc_edge_density_subtype ||
            subType == UF_caemisc_face_density_subtype ||
            subType == UF_caemisc_mapped_hole_subtype ||
            subType == UF_caemisc_fillet_density_subtype ||
            subType == UF_caemisc_cylinder_density_subtype ||
            subType == UF_caemisc_boundary_layer_subtype )
        {
            CAE::MeshControl *meshControl1(dynamic_cast<CAE::MeshControl *>((NXObject *)NXObjectManager::Get(meshcontrol)));

            if (meshControl1 == nullptr)
                continue;

            /*2. Obtain the CUSTOM NAME of each definition in the current FEM */
            NXString namemc = (meshControl1->Name()).GetLocaleText();

            /*2.1 If the user has not provide with a custom name, then query the default IDENTIFIER of this definition */
            if (strcmp(namemc.GetText(), "") == 0)
                namemc = (meshControl1->JournalIdentifier()).GetLocaleText();

            upper_to_lower_case(&namemc);

            /*3. Store the name/identifier and the respective tag_t of meshcontrol in a MULTI MAP */
            if (strcmp(namemc.GetText(), "") != 0)
                mMeshControlInfo.insert(std::make_pair(namemc, meshcontrol));

            write_info_fprintf(true, batchmesher_logger_file, "/t/t%s\n", namemc.GetLocaleText());

            UF_OBJ_cycle_objs_in_part(partTag, type, &meshcontrol);
        }
        else
        {
            UF_OBJ_cycle_objs_in_part(partTag, type, &meshcontrol);
        }
       
    }

    write_info_fprintf(true, batchmesher_logger_file, " \n\n");
    write_info_fprintf(true, batchmesher_logger_file, " Geomtery Assignment\n");
    write_info_fprintf(true, batchmesher_logger_file, " ===================\n");
    /*4. If we find any definitons inside the fem, module continues to the next step */
    if ( mMeshControlInfo.size() > 0)
    {
        /*5. Identify all the bodies in Current FEM and cyle through them */
        for ( int n=0; n<nCAEBodies; n++)         
        {
            int nCAEFaces = 0;
            tag_t *CAEFaces_p = NULL;

            NXObject *bodyObj = (NXObject *)NXObjectManager::Get( CAEBodies_p[n] );                

            CAE::CAEBody *cAEBody1(dynamic_cast<CAE::CAEBody *>(bodyObj));

            /*6. Identify all the FACES in te current BODY */
            UF_SF_body_ask_faces( CAEBodies_p[n], &nCAEFaces, &CAEFaces_p);  

            for ( int m=0; m < nCAEFaces; m++ )
            {
                /*7. Cycle through all the faces and identify name of each face */
                NXObject *faceObj = (NXObject *)NXObjectManager::Get( CAEFaces_p[m] );

                CAE::CAEFace *cAEFace1(dynamic_cast<CAE::CAEFace *>(faceObj));

                NXString caeFaceName = (cAEFace1->Name());

                 upper_to_lower_case (&caeFaceName);
                /*8. Find out if this FACE NAME matches with any NAMES in mesh control defnitions MAP*/
                ret = mMeshControlInfo.equal_range(caeFaceName);

                /*9. if a match is found and if respective defnition is not edge density type,
                     the name and macthed defnition is stored into a second multi map, which tracks only assigned controls.
                      Also this face will be assigned to this definition.*/ 
                for (it=ret.first; it!=ret.second; ++it)
                {
                    UF_OBJ_ask_type_and_subtype ((*it).second, &mainType, &subType );

                    if ( subType == UF_caemisc_edge_density_subtype )
                    {
                        continue;
                    }
                    else
                    {
                        bool added2;
                        CAE::MeshControl *meshControl1(dynamic_cast<CAE::MeshControl *>((NXObject *)NXObjectManager::Get( (*it).second )));
                        std::vector<NXObject *> objects1(1);
                        objects1[0] = cAEFace1;

                        added2 = MeshControlAssignment(fEModel1, meshControl1, objects1, false);                           

                        NXString namemc = (meshControl1->Name());

                        if (added2)
                        {
                            write_info_fprintf(true, batchmesher_logger_file, " \t\t Mesh Definition %s is assigned to face %s.\n",namemc.GetLocaleText(),caeFaceName.GetLocaleText());
                            mAssignedMeshControlInfo.insert(std::make_pair(namemc,(*it).second));
                        }
                        else
                            write_info_fprintf(true, batchmesher_logger_file, " \t\t Mesh Definition %s failed to be assigned to face %s.\n",namemc.GetLocaleText(),caeFaceName.GetLocaleText());
                    }

                }

            }

            int nCAEEdges = 0;
            tag_t *CAEEdges_p = NULL;

            /*10. Cycle through all the edges and identify name of each edge */
            UF_SF_body_ask_edges( CAEBodies_p[n], &nCAEEdges, &CAEEdges_p);

            for ( int p=0; p < nCAEEdges; p++ )
            {
                NXObject *edgeObj = (NXObject *)NXObjectManager::Get( CAEEdges_p[p]);                 
                CAE::CAEEdge *cAEEdge1(dynamic_cast<CAE::CAEEdge *>(edgeObj));

                /*11. Find out if this EDGE NAME matches with any NAMES in mesh control defnitions MAP*/
                NXString caeEdgeName = (cAEEdge1->Name());
                upper_to_lower_case (&caeEdgeName);
                ret = mMeshControlInfo.equal_range(caeEdgeName);

                /*12. if a match is found and if respective definition is not face density type,
                     the name and matched definition is stored into a second multi map, which tracks only assigned controls. 
                     Also this edge will be assigned to this definition. */ 
                for (it=ret.first; it!=ret.second; ++it)
                {
                    UF_OBJ_ask_type_and_subtype ((*it).second, &mainType, &subType );

                    if ( subType == UF_caemisc_face_density_subtype )
                    {
                        continue;
                    }
                    else
                    {

                        bool added2;
                        CAE::MeshControl *meshControl1(dynamic_cast<CAE::MeshControl *>((NXObject *)NXObjectManager::Get( (*it).second )));
                        std::vector<NXObject *> objects1(1);
                        objects1[0] = cAEEdge1;

                        added2 = MeshControlAssignment(fEModel1, meshControl1, objects1, false);                           

                            NXString namemc = (meshControl1->Name());

                        if (added2)
                        {                            
                            mAssignedMeshControlInfo.insert(std::make_pair(namemc,(*it).second));
                            write_info_fprintf(true, batchmesher_logger_file, " \t\t Mesh Definition %s is assigned to edge %s.\n",namemc.GetLocaleText(),caeEdgeName.GetLocaleText());
                            upper_to_lower_case (&namemc);
                            mAssignedMeshControlInfo.insert(std::make_pair(namemc,(*it).second));                            
                        } 
                        else
                            write_info_fprintf(true, batchmesher_logger_file, " \t\t Mesh Definition %s failed to be assigned to edge %s.\n",namemc.GetLocaleText(),caeEdgeName.GetLocaleText());
                    }

                }  

                NXString caeBodyName = (cAEBody1->Name());
                upper_to_lower_case (&caeBodyName);
                ret = mMeshControlInfo.equal_range(caeBodyName);

                /*13. Find out if this BODY NAME matches with any NAMES in mesh control defnitions MAP. If a match is found,
                the name and matched definition is stored into a second multi map, which tracks only assigned controls.
                Also this body will be assigned to this definition.*/ 
                for (it=ret.first; it!=ret.second; ++it)
                {
                    bool added2;
                    CAE::MeshControl *meshControl1(dynamic_cast<CAE::MeshControl *>((NXObject *)NXObjectManager::Get( (*it).second )));
                    std::vector<NXObject *> objects1(1);
                    objects1[0] = cAEBody1;

                    added2 = MeshControlAssignment(fEModel1, meshControl1, objects1, false);                           

                    NXString namemc = (meshControl1->Name());

                    if (added2)
                    {
                        mAssignedMeshControlInfo.insert(std::make_pair(namemc,(*it).second));
                        write_info_fprintf(true, batchmesher_logger_file, " \t\t Mesh Definition %s is assigned to body %s.\n",namemc.GetLocaleText(),caeBodyName.GetLocaleText());
                        upper_to_lower_case (&namemc);
                        mAssignedMeshControlInfo.insert(std::make_pair(namemc,(*it).second));                        
                    } 
                    else
                        write_info_fprintf(true, batchmesher_logger_file, " \t\t Mesh Definition %s failed to be assigned to body %s.\n",namemc.GetLocaleText(),caeBodyName.GetLocaleText());
                }

            }
        }
    }

    /*14. Cycle through the mesh control definition map (NOT assigned mesh control map)*/
    bool matchfound = false;
    it=mMeshControlInfo.begin();
    while ( it != mMeshControlInfo.end() )
    {
        /*15.Identify if there is a name that matches in the Assigned mesh control multi map */
        assignret = mAssignedMeshControlInfo.equal_range((*it).first);
        for (assingit=assignret.first; assingit!=assignret.second; ++assingit)
        {
            matchfound = true;

            /*16. Also if tag_t matches in assigned mesh control, we continue to next iteration,
                  but if we find that it does not then we identify if this mesh control defintion is a type 
                  that has a filter toggle and if this toggle is turned on then we assign the this control to all bodies*/  
            if ( (*it).second == (*assingit).second )
            {
                continue;
            }
            else
            {
                bool added2; 
                CAE::MeshControl *meshControl1(dynamic_cast<CAE::MeshControl *>((NXObject *)NXObjectManager::Get( (*assingit).second )));
                std::vector<NXObject *> objects1(nCAEBodies);

                for ( int n=0; n<nCAEBodies; n++)         
                {
                    NXObject *bodyObj = (NXObject *)NXObjectManager::Get( CAEBodies_p[n] );
                    CAE::CAEBody *cAEBody1(dynamic_cast<CAE::CAEBody *>(bodyObj));
                    objects1[n] = cAEBody1;
                }

                added2 = MeshControlAssignment(fEModel1, meshControl1, objects1, true);  

                if (added2)
                {
                    
                    write_info_fprintf(true, batchmesher_logger_file, " \t\t Mesh Definition %s is assigned to all the bodies.\n",((*it).first).GetLocaleText());
                }
                else
                    write_info_fprintf(true, batchmesher_logger_file, " \t\t Mesh Definition %s failed to be assigned to all the bodies.\n",((*it).first).GetLocaleText());
            }
        }
        
        /* 15.1 if the name doesn't match with any names in Assigned mesh control map, then 
                module identifies if the respective control definition of type that has a filter toggle 
                and if this toggle is turned on then we assign the this control to all bodies*/     
        if( !matchfound )
        {
                bool added2;
                CAE::MeshControl *meshControl1(dynamic_cast<CAE::MeshControl *>((NXObject *)NXObjectManager::Get( (*it).second )));
                std::vector<NXObject *> objects1(nCAEBodies);

                for ( int n=0; n<nCAEBodies; n++)         
                {
                    NXObject *bodyObj = (NXObject *)NXObjectManager::Get( CAEBodies_p[n] );
                    CAE::CAEBody *cAEBody1(dynamic_cast<CAE::CAEBody *>(bodyObj));                    
                    objects1[n] = cAEBody1;
                }

                added2 = MeshControlAssignment(fEModel1, meshControl1, objects1, true);

                if (added2)
                {
                    
                    write_info_fprintf(true, batchmesher_logger_file, " \t\t Mesh Definition %s is assigned to all the bodies.\n",((*it).first).GetLocaleText());
                }
                else
                    write_info_fprintf(true, batchmesher_logger_file, " \t\t Mesh Definition %s failed to be assigned to all the bodies.\n",((*it).first).GetLocaleText());
         
        }
        matchfound = false;
        ++it;
    }
} 

/* This local static routine controls the assignment of mesh control. */ 
bool MeshControlAssignment(CAE::FEModel *fEModel1, CAE::MeshControl *meshControl1, std::vector<NXObject *>objects, bool usefiltertoggleonly)
{
    bool added2 = false;    
    CAE::MeshControlBuilder *meshControlBuilder1;    

    meshControlBuilder1 = fEModel1->MeshControls()->CreateBuilder(meshControl1);
    if ( usefiltertoggleonly )
    {
        bool toggle;
        toggle = meshControlBuilder1->SelectionFilterToggle();
        if (toggle)
        {
            added2 = meshControlBuilder1->Selection()->Add(objects); 

            std::vector<CAE::MeshControl *> densities1;

            densities1 = meshControlBuilder1->CommitDensities();
           
        }
        meshControlBuilder1->Destroy();
    }
    else
    {
        added2 = meshControlBuilder1->Selection()->Add(objects); 

        std::vector<CAE::MeshControl *> densities1;

        densities1 = meshControlBuilder1->CommitDensities();

        meshControlBuilder1->Destroy();
    }
    
    return added2;
}

static void upper_to_lower_case ( NXString *strString)
{
    char tempStr[MAX_FSPEC_BUFSIZE];

    strcpy(tempStr,(*strString).GetLocaleText());
    int i = 0, ichar = 0, nchar = 0;

    nchar = (int)strlen (tempStr);

    for (i=0;i<nchar;i++)
    {
        ichar = tempStr[i];
        tempStr[i] = tolower(ichar);
    }

    *strString = NXString ( tempStr, NXString::Locale );
}

static void write_info_fprintf(bool        fToConsole, 
                               FILE       *fp,             /* I   : File to print*/
                               const char *format_string,  /* I   */
                               ...                         /* I   */
                              )
{
    va_list variable_list;
    
    
    if ( fToConsole )
    {
#if UF_UG_BATCH_MESH__SCREEN_DUMP_ON
        /* ====== #define flag ====== */
        va_start(variable_list, format_string);
        vprintf(format_string, variable_list);
        va_end(variable_list);
#endif
    }
    if ( fp!=NULL)
    {
        va_start(variable_list, format_string);
        vfprintf(fp, format_string, variable_list);
        va_end(variable_list);
    }

    if (fp!=NULL)
        fflush(fp);
}

// Turn this on if there is need of assignment by properties. 
// The below routine is intended to filter geomtery by string property(ies). 
#if 0
            {
            for ( int m=0; m < nCAEFaces; m++ )
            {
                NXObject *faceObj = (NXObject *)NXObjectManager::Get( CAEFaces_p[m] );

                CAE::CAEFace *cAEFace1(dynamic_cast<CAE::CAEFace *>(faceObj));
                info1 = cAEFace1->GetAttributeTitlesByType(NXObject::AttributeTypeString);
                for( attrInfoItr = info1.begin(); attrInfoItr < info1.end(); ++attrInfoItr )
                {
                    NXString faceStringAttr = (*attrInfoItr).Title.GetText();

                    ret = mMeshControlInfo.equal_range(faceStringAttr);

                    for (it=ret.first; it!=ret.second; ++it)
                    {
                        UF_OBJ_ask_type_and_subtype ((*it).second, &mainType, &subType );

                        if ( subType == UF_caemisc_edge_density_subtype )
                        {
                            continue;
                        }
                        else
                        {
                            bool added2;
                            CAE::MeshControl *meshControl1(dynamic_cast<CAE::MeshControl *>((NXObject *)NXObjectManager::Get( (*it).second )));
                            std::vector<NXObject *> objects1(1);
                            objects1[0] = cAEFace1;

                            added2 = MeshControlAssignment(fEModel1, meshControl1, objects1, false);                           
                          
                            if (added2)
                            {
                                NXString namemc = (meshControl1->Name());
                                mAssignedMeshControlInfo.insert(std::make_pair(namemc,(*it).second));
                            }
                           
                        }

                    }
                }
            }

            int nCAEEdges = 0;
            tag_t *CAEEdges_p = NULL;

            UF_SF_body_ask_edges( CAEBodies_p[n], &nCAEEdges, &CAEEdges_p);

            for ( int p=0; p < nCAEEdges; p++ )
            {
                NXObject *edgeObj = (NXObject *)NXObjectManager::Get( CAEEdges_p[p]);                 
                CAE::CAEEdge *cAEEdge1(dynamic_cast<CAE::CAEEdge *>(edgeObj));
                info1 = cAEEdge1->GetAttributeTitlesByType(NXObject::AttributeTypeString);
                for( attrInfoItr = info1.begin(); attrInfoItr < info1.end(); ++attrInfoItr )
                {
                    NXString edgeStringAttr = (*attrInfoItr).Title.GetText();

                    ret = mMeshControlInfo.equal_range(edgeStringAttr);

                    for (it=ret.first; it!=ret.second; ++it)
                    {
                        UF_OBJ_ask_type_and_subtype ((*it).second, &mainType, &subType );

                        if ( subType == UF_caemisc_face_density_subtype )
                        {
                            continue;
                        }
                        else
                        {
                            
                            bool added2;
                            CAE::MeshControl *meshControl1(dynamic_cast<CAE::MeshControl *>((NXObject *)NXObjectManager::Get( (*it).second )));
                            std::vector<NXObject *> objects1(1);
                            objects1[0] = cAEEdge1;

                            added2 = MeshControlAssignment(fEModel1, meshControl1, objects1, false);                           
                          
                            if (added2)
                            {
                                NXString namemc = (meshControl1->Name());
                                mAssignedMeshControlInfo.insert(std::make_pair(namemc,(*it).second));
                            }                            
                        }

                    }
                }
            }
        }
    }
# endif



