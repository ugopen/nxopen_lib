//MeasureAreaBetweenPointsCore

// Mandatory UF Includes
#include <uf.h>
#include <uf_object_types.h>

// Internal Includes
#include <NXOpen/ListingWindow.hxx>
#include <NXOpen/NXMessageBox.hxx>
#include <NXOpen/UI.hxx>

// Internal+External Includes
#include <NXOpen/Annotations.hxx>
#include <NXOpen/Assemblies_Component.hxx>
#include <NXOpen/Assemblies_ComponentAssembly.hxx>
#include <NXOpen/Body.hxx>
#include <NXOpen/BodyCollection.hxx>
#include <NXOpen/Face.hxx>
#include <NXOpen/Line.hxx> 
#include <NXOpen/Point.hxx>
#include <NXOpen/NXException.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/Session.hxx>
#include <NXOpen/Features_CustomAttribute.hxx>
#include <NXOpen/Features_CustomTagArrayAttribute.hxx>
#include <NXOpen/Features_CustomExpressionAttribute.hxx>
#include <NXOpen/Features_CustomFeature.hxx>
#include <NXOpen/Features_CustomFeatureClass.hxx>
#include <NXOpen/Features_CustomFeatureClassManager.hxx>
#include <NXOpen/Features_CustomFeatureCreateFeatureGeometryEvent.hxx>
#include <NXOpen/Features_CustomFeatureData.hxx>
#include <NXOpen/Features_CustomFeatureInformationEvent.hxx>
#include <NXOpen/Features_CustomIntegerAttribute.hxx>
#include <NXOpen/Features_CustomLogicalAttribute.hxx>
#include <NXOpen/Features_CustomTagAttribute.hxx>
#include <NXOpen/Features_Feature.hxx>
#include <NXOpen/Features_FeatureCollection.hxx>
#include <NXOpen/Features_CustomAttributeCollection.hxx>
#include <NXOpen/UnitCollection.hxx>
#include <NXOpen/Unit.hxx>
#include <NXOpen/ExpressionCollection.hxx>
#include <NXOpen/Expression.hxx>
#include <math.h>

// Std C++ Includes
#include <iostream>
#include <sstream>

using namespace NXOpen;
using std::string;
using std::exception;
using std::stringstream;
using std::endl;
using std::cout;
using std::cerr;

//Utility functions

NXOpen::Vector3d  VectorBetwenPoints(NXOpen::Point3d &startPoint, NXOpen::Point3d &endPoint)
{
    NXOpen::Vector3d vector;

    vector.X = endPoint.X - startPoint.X;
    vector.Y = endPoint.Y - startPoint.Y;
    vector.Z = endPoint.Z - startPoint.Z;

    return vector;
}

NXOpen::Vector3d VectorCrossProduct(NXOpen::Vector3d &vector1, NXOpen::Vector3d &vector2)
{
    NXOpen::Vector3d NormalVector;

    NormalVector.X = vector1.Y*vector2.Z - vector1.Z*vector2.Y;
    NormalVector.Y = -vector1.X*vector2.Z + vector1.Z*vector2.X;
    NormalVector.Z = vector1.X*vector2.Y - vector1.Y*vector2.X;

    return NormalVector;
}

// area3D_Polygon(): compute the area of a 3D planar polygon
//  Input:  int n = the number of vertices in the polygon
//          Point* V = an array of n+1 points in a 2D plane with V[n]=V[0]
//          Point N = a normal vector of the polygon's plane
//  Return: the (float) area of the polygon
double area3D_Polygon(int n, NXOpen::Point3d *V, NXOpen::Vector3d N)
{
    double area = 0;
    double an, ax, ay, az; // abs value of normal and its coords
    int  coord;           // coord to ignore: 1=x, 2=y, 3=z
    int  i, j, k;         // loop indices

    if (n < 3) return 0;  // a degenerate polygon

    // select largest abs coordinate to ignore for projection
    ax = (N.X>0 ? N.X : -N.X);    // abs x-coord
    ay = (N.Y > 0 ? N.Y : -N.Y);    // abs y-coord
    az = (N.Z > 0 ? N.Z : -N.Z);    // abs z-coord

    coord = 3;                    // ignore z-coord
    if (ax > ay) {
        if (ax > az) coord = 1;   // ignore x-coord
    }
    else if (ay > az) coord = 2;  // ignore y-coord

    // compute area of the 2D projection
    switch (coord) {
    case 1:
        for (i = 1, j = 2, k = 0; i < n; i++, j++, k++)
        {
            j = j == n ? 0 : j;
            area += (V[i].Y * (V[j].Z - V[k].Z));
        }
        break;
    case 2:
        for (i = 1, j = 2, k = 0; i < n; i++, j++, k++)
        {
            j = j == n ? 0 : j;
            area += (V[i].Z * (V[j].X - V[k].X));
        }
        break;
    case 3:
        for (i = 1, j = 2, k = 0; i < n; i++, j++, k++)
        {
            j = j == n ? 0 : j;
            area += (V[i].X * (V[j].Y - V[k].Y));
        }
        break;

    }
    switch (coord) {    // wrap-around term
    case 1:
        area += (V[0].Y * (V[1].Z - V[n - 1].Z));
        break;
    case 2:
        area += (V[0].Z * (V[1].X - V[n - 1].X));
        break;
    case 3:
        area += (V[0].X * (V[1].Y - V[n - 1].Y));
        break;
    }

    // scale to get area before projection
    an = sqrt(ax*ax + ay*ay + az*az); // length of normal vector
    switch (coord) {
    case 1:
        area *= (an / (2 * N.X));
        break;
    case 2:
        area *= (an / (2 * N.Y));
        break;
    case 3:
        area *= (an / (2 * N.Z));
    }

    area = area < 0 ? -area : area;

    return area;
}


bool ArePointsCoplaner(std::vector<NXOpen::TaggedObject*> pointsVec)
{
    std::vector<NXOpen::Point3d>point3dVec;

    if (pointsVec.size() < 4)
    {
        return true;
    }

    for (int i = 0; i < pointsVec.size(); ++i)
    {
        NXOpen::Point* point = dynamic_cast<NXOpen::Point*>(pointsVec[i]);

        point3dVec.push_back(point->Coordinates());
    }

    NXOpen::Vector3d v1 = VectorBetwenPoints(point3dVec[0], point3dVec[1]);
    NXOpen::Vector3d v2 = VectorBetwenPoints(point3dVec[0], point3dVec[2]);

    NXOpen::Vector3d vCross = VectorCrossProduct(v1, v2);

    for (int i = 3; i < point3dVec.size(); ++i)
    {
        NXOpen::Vector3d vi0 = VectorBetwenPoints(point3dVec[0], point3dVec[i]);

        double det = vi0.X* vCross.X - vi0.Y* (-vCross.Y) + vi0.Z* vCross.Z;

        det = det < 0.0 ? -det : det;

        if (det > 0.01)
        {
            return false;
        }
    }
    return true;
}

static int GetPolygonArea(Features::CustomTagArrayAttribute *points, double* area)
{
    std::vector<NXOpen::TaggedObject*> pointsVec = points->GetValues();
    
    *area =  0.0;

    if (pointsVec.size() < 3)
    {
        return 1;
    }
    if (!ArePointsCoplaner(pointsVec))
    {
        return 2;
    }

    std::vector<NXOpen::Point3d>point3dVec;

    for (int i = 0; i < pointsVec.size(); ++i)
    {
        NXOpen::Point* point = dynamic_cast<NXOpen::Point*>(pointsVec[i]);

        point3dVec.push_back(point->Coordinates());
    }
    NXOpen::Vector3d vector1 = VectorBetwenPoints(point3dVec[1], point3dVec[0]);

    NXOpen::Vector3d vector2 = VectorBetwenPoints(point3dVec[1], point3dVec[2]);

    NXOpen::Vector3d NormalVector = VectorCrossProduct(vector1, vector2);

    *area = area3D_Polygon((int)point3dVec.size(), &point3dVec[0], NormalVector);

    return 0;
}

//------------------------------------------------------------------------------
// NXOpen c++ test class 
//------------------------------------------------------------------------------
class MeasureAreaBetweenPointsCore
{
    // class members
public:
    static Session *theSession;
    static UI *theUI;

    MeasureAreaBetweenPointsCore();
    ~MeasureAreaBetweenPointsCore();
    
    static int preUpdateCallBack(NXOpen::Features::CustomFeaturePreUpdateEvent* event);
    static int createGeometryCallBack(NXOpen::Features::CustomFeatureCreateFeatureGeometryEvent* event);
    static int modifyGeometryCallBack(NXOpen::Features::CustomFeatureModifyFeatureGeometryEvent* event);
    static int postUpdateCallBack(NXOpen::Features::CustomFeaturePostUpdateEvent* event);
    static int informationCallBack(NXOpen::Features::CustomFeatureInformationEvent* event);
    
    void print(const NXString &);
    void print(const string &);
    void print(const char*);

private:
    Part *workPart, *displayPart;
    NXMessageBox *mb;
    ListingWindow *lw;
};

//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session *(MeasureAreaBetweenPointsCore::theSession) = NULL;
UI *(MeasureAreaBetweenPointsCore::theUI) = NULL;

//------------------------------------------------------------------------------
// Constructor 
//------------------------------------------------------------------------------
MeasureAreaBetweenPointsCore::MeasureAreaBetweenPointsCore()
{

    // Initialize the NX Open C++ API environment
    MeasureAreaBetweenPointsCore::theSession = NXOpen::Session::GetSession();
    MeasureAreaBetweenPointsCore::theUI = UI::GetUI();
    mb = theUI->NXMessageBox();
    lw = theSession->ListingWindow();

    workPart = theSession->Parts()->Work();
    displayPart = theSession->Parts()->Display();

    NXOpen::Features::CustomFeatureClassManager * mgr = theSession->CustomFeatureClassManager();

    NXOpen::Features::CustomFeatureClass* cfClass = mgr->GetClassFromName("NXOpen::CustomFeature::MeasureAreaBetweenPoints");

    // Registration of callback functions
    cfClass->AddPreUpdateHandler(make_callback(&MeasureAreaBetweenPointsCore::preUpdateCallBack));
    cfClass->AddCreateFeatureGeometryHandler(make_callback(&MeasureAreaBetweenPointsCore::createGeometryCallBack));
    cfClass->AddModifyFeatureGeometryHandler(make_callback(&MeasureAreaBetweenPointsCore::modifyGeometryCallBack));
    cfClass->AddPostUpdateHandler(make_callback(&MeasureAreaBetweenPointsCore::postUpdateCallBack));

    cfClass->AddInformationHandler(make_callback(&MeasureAreaBetweenPointsCore::informationCallBack));
    
}

//------------------------------------------------------------------------------
// Destructor
//------------------------------------------------------------------------------
MeasureAreaBetweenPointsCore::~MeasureAreaBetweenPointsCore()
{
}

//------------------------------------------------------------------------------
// Print string to listing window or stdout
//------------------------------------------------------------------------------
void MeasureAreaBetweenPointsCore::print(const NXString &msg)
{
    if(! lw->IsOpen() ) lw->Open();
    lw->WriteLine(msg);
}
void MeasureAreaBetweenPointsCore::print(const string &msg)
{
    if(! lw->IsOpen() ) lw->Open();
    lw->WriteLine(msg);
}
void MeasureAreaBetweenPointsCore::print(const char * msg)
{
    if(! lw->IsOpen() ) lw->Open();
    lw->WriteLine(msg);
}


int MeasureAreaBetweenPointsCore::preUpdateCallBack(NXOpen::Features::CustomFeaturePreUpdateEvent* event)
{
    return 0;
}



int MeasureAreaBetweenPointsCore::createGeometryCallBack(NXOpen::Features::CustomFeatureCreateFeatureGeometryEvent* event)
{
    Session *theSession = Session::GetSession();

    NXOpen::Part *workPart(theSession->Parts()->Work());

    // Create attributes
    NXOpen::Features::FeatureCollection *featureCollection = workPart->Features();
    NXOpen::Features::CustomAttributeCollection *attribCollection = featureCollection->CustomAttributeCollection();

    NXOpen::Features::CustomFeature *cfFeature = event->GetCustomFeature();

    NXOpen::Features::CustomFeatureData* cfData = cfFeature->FeatureData();

    if (cfData->HasCustomAttribute("Points", NXOpen::Features::CustomAttribute::TypeTagVla))
    {
        Features::CustomTagArrayAttribute *points = cfData->CustomTagArrayAttributeByName("Points");

        double areaValue;
        int error = GetPolygonArea(points, &areaValue);

        if (cfData->HasCustomAttribute("Area", NXOpen::Features::CustomAttribute::TypeExpression))
        {
            Features::CustomExpressionAttribute* expAttrib = cfData->CustomExpressionAttributeByName("Area");
            NXOpen::Expression *areaexp = expAttrib->Value();

            areaexp->SetValue(areaValue);
        }
        else
        {
            NXOpen::Unit *unit0(dynamic_cast<NXOpen::Unit *>(workPart->UnitCollection()->FindObject("SquareMilliMeter")));
            NXOpen::Expression *areaexp = workPart->Expressions()->CreateSystemExpressionWithUnits("0", unit0);

            areaexp->SetValue(areaValue);

            std::vector<NXOpen::Features::CustomAttribute::Property> attrProp;

            attrProp.push_back(NXOpen::Features::CustomAttribute::Property::PropertyIsOutputAttribute);

            attrProp.push_back(NXOpen::Features::CustomAttribute::Property::PropertyIsOwnedAttribute);

            std::vector<NXOpen::Features::CustomAttribute*> attrs(0);

            Features::CustomExpressionAttribute* area = attribCollection->CreateCustomExpressionAttribute("Area", attrProp);

            area->SetValue(areaexp);

            attrs.push_back(area);

            cfData->AddCustomAttributes(attrs);
        }
        if (error == 1)
        {
            cfFeature->LogDiagnostic(error, "Too few point to calculate area, at least 3 points are required", NXOpen::Features::Feature::DiagnosticType::DiagnosticTypeWarning);
            event->SetErrorCode(error);
        }
        else if (error == 2)
        {
            cfFeature->LogDiagnostic(error, "Selected points are not coplanar", NXOpen::Features::Feature::DiagnosticType::DiagnosticTypeWarning);
            event->SetErrorCode(error);
        }
    }

    return 0;
}

int MeasureAreaBetweenPointsCore::modifyGeometryCallBack(NXOpen::Features::CustomFeatureModifyFeatureGeometryEvent* event)
{
    return 0;
}

int MeasureAreaBetweenPointsCore::postUpdateCallBack(NXOpen::Features::CustomFeaturePostUpdateEvent* event)
{
    return 0;
}

int MeasureAreaBetweenPointsCore::informationCallBack(NXOpen::Features::CustomFeatureInformationEvent* event)
{
    NXString string = "This is custom information \n \t\t Custom feature has not yet implemented custom code to show custom information";
    event->SetInformation(string);
    return 0;
}

//------------------------------------------------------------------------------
// Entry point(s) for unmanaged internal NXOpen C/C++ programs
//------------------------------------------------------------------------------
//  Explicit Execution
extern "C" DllExport void ufusr( char *parm, int *returnCode, int rlen )
{
    try
    {
        // Create NXOpen C++ class instance
        MeasureAreaBetweenPointsCore *theMeasureAreaBetweenPointsCore;
        theMeasureAreaBetweenPointsCore = new MeasureAreaBetweenPointsCore();
        delete theMeasureAreaBetweenPointsCore;
    }
    catch (const NXException& e1)
    {
        UI::GetUI()->NXMessageBox()->Show("NXException", NXOpen::NXMessageBox::DialogTypeError, e1.Message());
    }
    catch (const exception& e2)
    {
        UI::GetUI()->NXMessageBox()->Show("Exception", NXOpen::NXMessageBox::DialogTypeError, e2.what());
    }
    catch (...)
    {
        UI::GetUI()->NXMessageBox()->Show("Exception", NXOpen::NXMessageBox::DialogTypeError, "Unknown Exception.");
    }
}


//------------------------------------------------------------------------------
// Unload Handler
//------------------------------------------------------------------------------
extern "C" DllExport int ufusr_ask_unload()
{
    return (int)NXOpen::Session::LibraryUnloadOptionAtTermination;
}
