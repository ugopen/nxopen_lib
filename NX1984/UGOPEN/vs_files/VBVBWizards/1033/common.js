//
// Copyright (c) Microsoft Corporation 2001-2002. All rights reserved.
//

var vsViewKindPrimary           = "{00000000-0000-0000-0000-000000000000}";
var vsViewKindDebugging         = "{7651A700-06E5-11D1-8EBD-00A0C90F26EA}";
var vsViewKindCode              = "{7651A701-06E5-11D1-8EBD-00A0C90F26EA}";
var vsViewKindDesigner          = "{7651A702-06E5-11D1-8EBD-00A0C90F26EA}";
var vsViewKindTextView          = "{7651A703-06E5-11D1-8EBD-00A0C90F26EA}";
var vsWindowKindSolutionExplorer= "{3AE79031-E1BC-11D0-8F78-00A0C9110057}";

var GUID_ItemType_PhysicalFolder= "{6BB5F8EF-4483-11D3-8BCF-00C04F8EC28C}";
var GUID_ItemType_VirtualFolder = "{6BB5F8F0-4483-11D3-8BCF-00C04F8EC28C}";
var GUID_ItemType_PhysicalFile  = "{6BB5F8EE-4483-11D3-8BCF-00C04F8EC28C}";

var vsWizardAddSubProject       = "{0F90E1D2-4999-11D1-B6D1-00A0C90F2744}";


function CreateVSProject(strProjectName, strProjectExt, strProjectPath, strTemplateFile)
{
    var solution = dte.Solution;
    var strSolutionName = "";

    if (wizard.FindSymbol("CLOSE_SOLUTION"))
    {
        solution.Close();
        strSolutionName = wizard.FindSymbol("VS_SOLUTION_NAME");
        if (strSolutionName.length)
        {
            var strSolutionPath = strProjectPath.substr(0, strProjectPath.length - strProjectName.length);
            solution.Create(strSolutionPath, strSolutionName);
        }
    }

    var strProjectFile = strProjectName + strProjectExt;

    var oTarget = wizard.FindSymbol("TARGET");
    var project;

    if (wizard.FindSymbol("WIZARD_TYPE") == vsWizardAddSubProject)
    {
        var prjItem = oTarget.AddFromTemplate(strTemplateFile, strProjectPath+"\\"+strProjectFile);
        project = prjItem.SubProject;
    }
    else
    {
        project = oTarget.AddFromTemplate(strTemplateFile, strProjectPath, strProjectFile);
    }
    return project;
}

function AddFileToVSProject(strItemName, selProj, selObj, strTemplateFile, bValidate)
{
    fso = new ActiveXObject("Scripting.FileSystemObject");
    AddBaseNameToWizard("SAFE_ITEM_NAME", strItemName, ".");

    if( bValidate )
    {
        var strSafeName = wizard.FindSymbol( "SAFE_ITEM_NAME" );
        if( !wizard.ValidateCLRIdentifier( strSafeName, false ))
        {
            strSafeName = "_" + strSafeName;
            wizard.AddSymbol("SAFE_ITEM_NAME", strSafeName);
        }
    }

    var isReferenceExpanded;
    if(selProj != null) 
        isReferenceExpanded = IsReferenceExpanded(selProj);

    // Get project item for selObj collection
    var folder = selObj.parent;

    var strURL = folder.Properties("URL").Value;
    if (strURL.length > 0) //if a web project
        var strProjectPath = folder.Properties("LocalPath");
    else
        var strProjectPath = folder.Properties("FullPath");

    var strItemFile = strProjectPath + strItemName;

    var fsoTemporaryFolder = 2;
    var tFolder = fso.GetSpecialFolder(fsoTemporaryFolder);
    var strTempName = fso.GetTempName();
    var strTempFile = tFolder.Path + "\\" + strTempName;
    SafeDeleteFile(fso, strTempFile);
    
    wizard.RenderTemplate(strTemplateFile, strTempFile, false);
    var item = folder.ProjectItems.AddFromTemplate(strTempFile, strItemName );
    SafeDeleteFile(fso, strTempFile);

    if(selProj != null)
    {
        if(isReferenceExpanded == true)
 	    ExpandReferencesNode(selProj);
        else
            CollapseReferencesNode(selProj);
    }

    return item;
}

function AddDependentFileToVSProject(strItemName, projectItem, strTemplateFilePath)
{
    fso = new ActiveXObject("Scripting.FileSystemObject");
    
    var fsoTemporaryFolder = 2;
    var tFolder = fso.GetSpecialFolder(fsoTemporaryFolder);
    var strTempName = fso.GetTempName();
    var strTempFile = tFolder.Path + "\\" + strTempName;
    SafeDeleteFile(fso, strTempFile);
    
    wizard.RenderTemplate(strTemplateFilePath, strTempFile, false);
    var item = projectItem.ProjectItems.AddFromTemplate(strTempFile, strItemName);
    SafeDeleteFile(fso, strTempFile);
    
    return item;
}

function AddBaseNameToWizard( strName, strValue, strDelim )
{
    var strLegalItemName;
    var nIndex = strValue.lastIndexOf(strDelim);
    if( nIndex > 0 )
        strLegalItemName = strValue.substr(0, nIndex);
    else
        strLegalItemName = strValue;
    wizard.AddSymbol(strName, CreateLegalIdentifier(strLegalItemName));
}

function SafeDeleteFile( fso, strFilespec )
{
	if (fso.FileExists(strFilespec))
	{
		var tmpFile = fso.GetFile(strFilespec);
		tmpFile.Delete();
	}
}

function GetDependentFileName(strMainFileName, strMainExtension, strDependentExtension)
{
    var strDependentFileName = strMainFileName;
    
    // If main file name is Something.vb, the dependent file name will be Something.resx
    // Otherwise, if main file name is Something.ext, the dependent file name will be Something.ext.resx.
    
    if (strMainFileName.toLowerCase().lastIndexOf(strMainExtension.toLowerCase()) == 
        strMainFileName.length - strMainExtension.length)
    {
        strDependentFileName = strMainFileName.substring(0, strMainFileName.length - strMainExtension.length) +
            strDependentExtension;
    }
    else 
    {
        strDependentFileName = strMainFileName + strDependentExtension;
    }
    
    return strDependentFileName;
}

function CreateLegalIdentifier(strName)
{
    var nLen = strName.length;
    var strLegalName = "";
    var cChar = strName.charAt(0);
    switch(cChar)
    {
        case "0":
        case "1":
        case "2":
        case "3":
        case "4":
        case "5":
        case "6":
        case "7":
        case "8":
        case "9":
            strLegalName += "_";
            break;
    }
    for (nCntr = 0; nCntr < nLen; nCntr++)
    {
        cChar = strName.charAt(nCntr);
        switch(cChar)
        {
            case " ":
            case "~":
            case "&":
            case "'":
            case "#":
            case "!":
            case "@":
            case "$":
            case "%":
            case "^":
            case "(":
            case ")":
            case "-":
            case "+":
            case "=":
            case "{":
            case "}":
            case "[":
            case "]":
            case ";":
            case ",":
            case "`":
            case ".":
                strLegalName += "_";
                break;
            default:
                strLegalName += cChar;
                break;
        }
    }
    return strLegalName;
}

function ReplaceDots(strName)
{
    var nLen = strName.length;
    var strLegalName = "";
    for (nCntr = 0; nCntr < nLen; nCntr++)
    {
        var cChar = strName.charAt(nCntr);
        if (cChar == ".")
                strLegalName += "_";
        else
                strLegalName += cChar;
    }
    return strLegalName;
}


function AddNamespaceSymbolToWizard(dtex, wizardx, selObj) 
{
    var parent = selObj.Parent;
    var kind = parent.Kind;
    if(kind == GUID_ItemType_PhysicalFolder)
    {
        wizardx.AddSymbol("NAMESPACE", parent.Properties("DefaultNamespace").Value);
    }
    else
    {
        wizardx.AddSymbol("NAMESPACE", parent.Properties("RootNamespace").Value);
    }
}


function AddDefaultClientScriptToWizard(dtex, wizardx, selProj)
{
    var prjScriptLang = selProj.Properties("DefaultClientScript").Value;
    // 0 = JScript
    // 1 = VBScript
    if(prjScriptLang == 0)
    {
        wizardx.AddSymbol("DEFAULT_CLIENT_SCRIPT", "JavaScript");
    }
    else
    {
        wizardx.AddSymbol("DEFAULT_CLIENT_SCRIPT", "VBScript");
    }
}

function AddDefaultTargetSchemaToWizard(dtex, wizardx, selProj)
{
    var prjTargetSchema = selProj.Properties("DefaultTargetSchema").Value;
    // 0 = IE3/Nav4
    // 1 = IE5
    // 2 = Nav4
    if(prjTargetSchema == 0)
    {
        wizardx.AddSymbol("DEFAULT_TARGET_SCHEMA", "http://schemas.microsoft.com/intellisense/ie3-2nav3-0");
    }
    else if( prjTargetSchema == 1)
    {
        wizardx.AddSymbol("DEFAULT_TARGET_SCHEMA", "http://schemas.microsoft.com/intellisense/ie5");
    }
    else
    {
        wizardx.AddSymbol("DEFAULT_TARGET_SCHEMA", "http://schemas.microsoft.com/intellisense/nav4-0");
    }
}

function AddDefaultDefaultHTMLPageLayoutToWizard(dtex, wizardx, selProj)
{
    var prjPageLayout = selProj.Properties("DefaultHTMLPageLayout").Value;
    // 0 = FlowLayout
    // 1 = GridLayout
    if(prjPageLayout == 0)
    {
        wizardx.AddSymbol("DEFAULT_HTML_LAYOUT", "FlowLayout");
    }
    else
    {
        wizardx.AddSymbol("DEFAULT_HTML_LAYOUT", "GridLayout");
    }
}
function AddDefaultWebFormsPropertiesToWizard(dtex, wizardx, selProj)
{
    AddDefaultClientScriptToWizard(dtex, wizardx, selProj);
    AddDefaultTargetSchemaToWizard(dtex, wizardx, selProj);
    AddDefaultDefaultHTMLPageLayoutToWizard(dtex, wizardx, selProj);
}


function IsReferenceExpanded(oProj)
{
    UIItem = GetUIReferencesNode(oProj);
    if( UIItem != null )
        return UIItem.Expanded;
}		

function ExpandReferencesNode(oProj)
{
    UIItem = GetUIReferencesNode(oProj);
    if( UIItem != null )
        UIItem.Expanded = true;
}

function CollapseReferencesNode(oProj)
{
    UIItem = GetUIReferencesNode(oProj);
    if( UIItem != null )
        UIItem.Expanded = false;
}

function GetUIReferencesNode(oProj)
{
    var L_strREferencesNode_Text = "References"; // This string needs to be localized
    var UIItemX = null;

    UIItemX = GetUIItem( oProj, L_strREferencesNode_Text);
    if( UIItemX )
        return UIItemX.UIHierarchyItems;
    else
        return null;
}

//
// Return the parent of the input hierarchy item. The parent may be a folder, 
// or a superproject or the solution.
//
function getParent(obj)
{
    var parent = obj.Collection.parent;
    //
    // is obj a project ?
    //
    if( parent == dte )
    {
        //
        // is obj a sub-project ?
        //
        if( IsSubProject(obj) )
        {                
            parent = obj.ParentProjectItem.Collection.parent;
        }
        else
        {
            //
            // obj is a top-level project
            //
            parent = null;
        }
    }
    return parent;    
}

function IsSubProject(oProj)
{
    try
    {
        var Parent = oProj.ParentProjectItem;
        if(Parent)
            return true;
        return false;
    }
    catch(e)
    {
        return false;
    }
}

//
// get the UIHierarchyItem for the projectitem, sName. 
// If sName is empty, returns the UIHierarchyItem for the project
//
function GetUIItem( oProj, sName )
{
    try
    {
        if( sName != "" )
        {
            sSaveName = sName;
            sName = oProj.Name + "\\" + sSaveName;
        }
        else
        {
            sName = oProj.Name;
        }

        var parent = getParent( oProj );

        while( parent != null )
        {
            sSaveName = sName;
            sName = parent.Name + "\\" + sSaveName;
            parent = getParent( parent );

        }

        //
        // we have arrived at the top of the soltuion explorer hierarchy - return the sName index into the solution's UIHierarchyItem collection
        //
        var strSolutionName = dte.Solution.Properties("Name");
        var vsHierObject = dte.Windows.Item(vsWindowKindSolutionExplorer).Object;   
        return vsHierObject.GetItem( strSolutionName + "\\" + sName );
    }	
    catch(e)
    {
        return null;
    }
}

//
// Finds the file already exist on the project
//
function DoesFileExistInProj(oProj, sName )
{
    try
    {
        return oProj.ProjectItems.Item(sName);

    }	
    catch(e)
    {
        return null;
    }
}

function SetErrorInfo(error)
{
    if(error.description.length > 0)
    {
        wizard.SetErrorInfo(error.description, error.number & 0xFFFFFFFF);
    }
}

function ReportError( strErr )
{
    if( dte.SuppressUI == false )
    {
        wizard.ReportError(strErr);
    }
}

function ProjectIsARootWeb(strProjectPath)
{
    // Returns true if strProjectPath is a root web. Is does this by counting
    // the forward slashes. Web roots are of the form: http://server. Assuming
    // no trailing slash, a web root will have 2 forward slashes, non webroots will
    // have 3 or more slashes. 
    var nCntr = 0;
    var cSlashes = 0;
    var nLen = strProjectPath.length - 1;   // Ignore last character
    for (nCntr = 0; nCntr < nLen; nCntr++)
    {
        // Count the forward slashes
        if(strProjectPath.charAt(nCntr) == "/")
            cSlashes++;
    }
    
    if(cSlashes == 2)
        return true;
    return false;
}

// SIG // Begin signature block
// SIG // MIIj+gYJKoZIhvcNAQcCoIIj6zCCI+cCAQExDzANBglg
// SIG // hkgBZQMEAgEFADB3BgorBgEEAYI3AgEEoGkwZzAyBgor
// SIG // BgEEAYI3AgEeMCQCAQEEEBDgyQbOONQRoqMAEEvTUJAC
// SIG // AQACAQACAQACAQACAQAwMTANBglghkgBZQMEAgEFAAQg
// SIG // 4YdMNIXV59yR9PsfweZDIgJWtXFQwBnqn7Gz0v/1vnig
// SIG // gg2TMIIGETCCA/mgAwIBAgITMwAAAI6HkaRXGl/KPgAA
// SIG // AAAAjjANBgkqhkiG9w0BAQsFADB+MQswCQYDVQQGEwJV
// SIG // UzETMBEGA1UECBMKV2FzaGluZ3RvbjEQMA4GA1UEBxMH
// SIG // UmVkbW9uZDEeMBwGA1UEChMVTWljcm9zb2Z0IENvcnBv
// SIG // cmF0aW9uMSgwJgYDVQQDEx9NaWNyb3NvZnQgQ29kZSBT
// SIG // aWduaW5nIFBDQSAyMDExMB4XDTE2MTExNzIyMDkyMVoX
// SIG // DTE4MDIxNzIyMDkyMVowgYMxCzAJBgNVBAYTAlVTMRMw
// SIG // EQYDVQQIEwpXYXNoaW5ndG9uMRAwDgYDVQQHEwdSZWRt
// SIG // b25kMR4wHAYDVQQKExVNaWNyb3NvZnQgQ29ycG9yYXRp
// SIG // b24xDTALBgNVBAsTBE1PUFIxHjAcBgNVBAMTFU1pY3Jv
// SIG // c29mdCBDb3Jwb3JhdGlvbjCCASIwDQYJKoZIhvcNAQEB
// SIG // BQADggEPADCCAQoCggEBANCH1EIrfp3ZxnrUosPjFZLS
// SIG // U52VF8lSNvpUv6sQr+nJ58wmU8PCc79t1gDlANzpamc0
// SIG // MPYWF7QBpZV8i7mkLOaLO3n2Iwx5j/NS30ABHMLGA53r
// SIG // Wc9z6dhxOZvwziVZLdLJWwrvftYyDl10EgTsngRTpmsC
// SIG // Z/hNWYt34Csh4O/ApEUSzwN7A8Y5w9Qi3FVcd0L/nLLl
// SIG // VWdoui12an9mU0fVRwrMON6Ne5cZfYLQJviljuWh8F5k
// SIG // EOT56yfG8uAI0A3yZ8DY8i/7idoV+a4PPgCXB9ELPnDU
// SIG // d6tyeEGYB7gXzKKxX+y981Bno9eU8NKLVY9TppWT5rJm
// SIG // z8k3aORjx88CAwEAAaOCAYAwggF8MB8GA1UdJQQYMBYG
// SIG // CisGAQQBgjdMCAEGCCsGAQUFBwMDMB0GA1UdDgQWBBSr
// SIG // yNbtshXSqo7xzO1sOPdFStCKuzBSBgNVHREESzBJpEcw
// SIG // RTENMAsGA1UECxMETU9QUjE0MDIGA1UEBRMrMjMwMDEy
// SIG // K2IwNTBjNmU3LTc2NDEtNDQxZi1iYzRhLTQzNDgxZTQx
// SIG // NWQwODAfBgNVHSMEGDAWgBRIbmTlUAXTgqoXNzcitW2o
// SIG // ynUClTBUBgNVHR8ETTBLMEmgR6BFhkNodHRwOi8vd3d3
// SIG // Lm1pY3Jvc29mdC5jb20vcGtpb3BzL2NybC9NaWNDb2RT
// SIG // aWdQQ0EyMDExXzIwMTEtMDctMDguY3JsMGEGCCsGAQUF
// SIG // BwEBBFUwUzBRBggrBgEFBQcwAoZFaHR0cDovL3d3dy5t
// SIG // aWNyb3NvZnQuY29tL3BraW9wcy9jZXJ0cy9NaWNDb2RT
// SIG // aWdQQ0EyMDExXzIwMTEtMDctMDguY3J0MAwGA1UdEwEB
// SIG // /wQCMAAwDQYJKoZIhvcNAQELBQADggIBAESJAqxpU/PE
// SIG // trvUjGBT58psqElpZr6lmkGZOtid0lcCUWr6v5uW26Ym
// SIG // fQlW6NztJXV6pUdSqB5LFlPz7g+awwSVKcGChKRWMfyg
// SIG // ipGVtb9azqkBH2RGoebK8dd0e7+SCFFefDMCXlE7m+XY
// SIG // Ll8CTAmcGkPace3k2eei2nQsF63lDLUY9VQJ1L4cc80g
// SIG // e6T6yNvY2zqu+pDFo72VZa5GLVcpWNaS8GzaY/GPM6J+
// SIG // OHZe3fM17ayaO2KB0E4ZfEh8sAuPOMwtvNU5ZamVwQPi
// SIG // ksm5q9JXCqrcUgsuViej4piXV468qVluJJKOguIJc4LZ
// SIG // NYPMn3/RBI6IuOKag1iw1JrmMfqUR459puJOefPY02oz
// SIG // FlBw8UK7mAnp/8yVVVsIv5JSqAjE8ejx/0DX+Zo2nf26
// SIG // kIXSVT5QrUYf7yUMuJ46SARj73iYol0DDQLY3CCr5la1
// SIG // 3u8WZsPXVYIeT4J4yZ5UGhBgtxerQBORrrAZwZozne4y
// SIG // cs1lzE9GmC0PUWAefPv+2+gHeQf3oTM4/gma2497tjq9
// SIG // hYa4zLx9ATC3ex2pXRu9zE0X925HM9VA32rKLlG4tbnP
// SIG // wwTTO+Xj6RCM66e63qQuM2opLxRK6h7BIjg1BYXvwgQA
// SIG // DWvB2JYUSBWvflKwuGDEUrVKgreFKgBJKiaDJ1pB3r3V
// SIG // Zkm8C5x4cAm8MIIHejCCBWKgAwIBAgIKYQ6Q0gAAAAAA
// SIG // AzANBgkqhkiG9w0BAQsFADCBiDELMAkGA1UEBhMCVVMx
// SIG // EzARBgNVBAgTCldhc2hpbmd0b24xEDAOBgNVBAcTB1Jl
// SIG // ZG1vbmQxHjAcBgNVBAoTFU1pY3Jvc29mdCBDb3Jwb3Jh
// SIG // dGlvbjEyMDAGA1UEAxMpTWljcm9zb2Z0IFJvb3QgQ2Vy
// SIG // dGlmaWNhdGUgQXV0aG9yaXR5IDIwMTEwHhcNMTEwNzA4
// SIG // MjA1OTA5WhcNMjYwNzA4MjEwOTA5WjB+MQswCQYDVQQG
// SIG // EwJVUzETMBEGA1UECBMKV2FzaGluZ3RvbjEQMA4GA1UE
// SIG // BxMHUmVkbW9uZDEeMBwGA1UEChMVTWljcm9zb2Z0IENv
// SIG // cnBvcmF0aW9uMSgwJgYDVQQDEx9NaWNyb3NvZnQgQ29k
// SIG // ZSBTaWduaW5nIFBDQSAyMDExMIICIjANBgkqhkiG9w0B
// SIG // AQEFAAOCAg8AMIICCgKCAgEAq/D6chAcLq3YbqqCEE00
// SIG // uvK2WCGfQhsqa+laUKq4BjgaBEm6f8MMHt03a8YS2Avw
// SIG // OMKZBrDIOdUBFDFC04kNeWSHfpRgJGyvnkmc6Whe0t+b
// SIG // U7IKLMOv2akrrnoJr9eWWcpgGgXpZnboMlImEi/nqwhQ
// SIG // z7NEt13YxC4Ddato88tt8zpcoRb0RrrgOGSsbmQ1eKag
// SIG // Yw8t00CT+OPeBw3VXHmlSSnnDb6gE3e+lD3v++MrWhAf
// SIG // TVYoonpy4BI6t0le2O3tQ5GD2Xuye4Yb2T6xjF3oiU+E
// SIG // GvKhL1nkkDstrjNYxbc+/jLTswM9sbKvkjh+0p2ALPVO
// SIG // VpEhNSXDOW5kf1O6nA+tGSOEy/S6A4aN91/w0FK/jJSH
// SIG // vMAhdCVfGCi2zCcoOCWYOUo2z3yxkq4cI6epZuxhH2rh
// SIG // KEmdX4jiJV3TIUs+UsS1Vz8kA/DRelsv1SPjcF0PUUZ3
// SIG // s/gA4bysAoJf28AVs70b1FVL5zmhD+kjSbwYuER8ReTB
// SIG // w3J64HLnJN+/RpnF78IcV9uDjexNSTCnq47f7Fufr/zd
// SIG // sGbiwZeBe+3W7UvnSSmnEyimp31ngOaKYnhfsi+E11ec
// SIG // XL93KCjx7W3DKI8sj0A3T8HhhUSJxAlMxdSlQy90lfdu
// SIG // +HggWCwTXWCVmj5PM4TasIgX3p5O9JawvEagbJjS4NaI
// SIG // jAsCAwEAAaOCAe0wggHpMBAGCSsGAQQBgjcVAQQDAgEA
// SIG // MB0GA1UdDgQWBBRIbmTlUAXTgqoXNzcitW2oynUClTAZ
// SIG // BgkrBgEEAYI3FAIEDB4KAFMAdQBiAEMAQTALBgNVHQ8E
// SIG // BAMCAYYwDwYDVR0TAQH/BAUwAwEB/zAfBgNVHSMEGDAW
// SIG // gBRyLToCMZBDuRQFTuHqp8cx0SOJNDBaBgNVHR8EUzBR
// SIG // ME+gTaBLhklodHRwOi8vY3JsLm1pY3Jvc29mdC5jb20v
// SIG // cGtpL2NybC9wcm9kdWN0cy9NaWNSb29DZXJBdXQyMDEx
// SIG // XzIwMTFfMDNfMjIuY3JsMF4GCCsGAQUFBwEBBFIwUDBO
// SIG // BggrBgEFBQcwAoZCaHR0cDovL3d3dy5taWNyb3NvZnQu
// SIG // Y29tL3BraS9jZXJ0cy9NaWNSb29DZXJBdXQyMDExXzIw
// SIG // MTFfMDNfMjIuY3J0MIGfBgNVHSAEgZcwgZQwgZEGCSsG
// SIG // AQQBgjcuAzCBgzA/BggrBgEFBQcCARYzaHR0cDovL3d3
// SIG // dy5taWNyb3NvZnQuY29tL3BraW9wcy9kb2NzL3ByaW1h
// SIG // cnljcHMuaHRtMEAGCCsGAQUFBwICMDQeMiAdAEwAZQBn
// SIG // AGEAbABfAHAAbwBsAGkAYwB5AF8AcwB0AGEAdABlAG0A
// SIG // ZQBuAHQALiAdMA0GCSqGSIb3DQEBCwUAA4ICAQBn8oal
// SIG // mOBUeRou09h0ZyKbC5YR4WOSmUKWfdJ5DJDBZV8uLD74
// SIG // w3LRbYP+vj/oCso7v0epo/Np22O/IjWll11lhJB9i0ZQ
// SIG // VdgMknzSGksc8zxCi1LQsP1r4z4HLimb5j0bpdS1HXeU
// SIG // OeLpZMlEPXh6I/MTfaaQdION9MsmAkYqwooQu6SpBQyb
// SIG // 7Wj6aC6VoCo/KmtYSWMfCWluWpiW5IP0wI/zRive/DvQ
// SIG // vTXvbiWu5a8n7dDd8w6vmSiXmE0OPQvyCInWH8MyGOLw
// SIG // xS3OW560STkKxgrCxq2u5bLZ2xWIUUVYODJxJxp/sfQn
// SIG // +N4sOiBpmLJZiWhub6e3dMNABQamASooPoI/E01mC8Cz
// SIG // TfXhj38cbxV9Rad25UAqZaPDXVJihsMdYzaXht/a8/jy
// SIG // FqGaJ+HNpZfQ7l1jQeNbB5yHPgZ3BtEGsXUfFL5hYbXw
// SIG // 3MYbBL7fQccOKO7eZS/sl/ahXJbYANahRr1Z85elCUtI
// SIG // EJmAH9AAKcWxm6U/RXceNcbSoqKfenoi+kiVH6v7RyOA
// SIG // 9Z74v2u3S5fi63V4GuzqN5l5GEv/1rMjaHXmr/r8i+sL
// SIG // gOppO6/8MO0ETI7f33VtY5E90Z1WTk+/gFcioXgRMiF6
// SIG // 70EKsT/7qMykXcGhiJtXcVZOSEXAQsmbdlsKgEhr/Xmf
// SIG // wb1tbWrJUnMTDXpQzTGCFb8wghW7AgEBMIGVMH4xCzAJ
// SIG // BgNVBAYTAlVTMRMwEQYDVQQIEwpXYXNoaW5ndG9uMRAw
// SIG // DgYDVQQHEwdSZWRtb25kMR4wHAYDVQQKExVNaWNyb3Nv
// SIG // ZnQgQ29ycG9yYXRpb24xKDAmBgNVBAMTH01pY3Jvc29m
// SIG // dCBDb2RlIFNpZ25pbmcgUENBIDIwMTECEzMAAACOh5Gk
// SIG // Vxpfyj4AAAAAAI4wDQYJYIZIAWUDBAIBBQCggaowGQYJ
// SIG // KoZIhvcNAQkDMQwGCisGAQQBgjcCAQQwHAYKKwYBBAGC
// SIG // NwIBCzEOMAwGCisGAQQBgjcCARUwLwYJKoZIhvcNAQkE
// SIG // MSIEIBGgZSRc9Cqu/ojBB48jrfeTIw2HASJin8UwGsvH
// SIG // XUVSMD4GCisGAQQBgjcCAQwxMDAuoBSAEgBjAG8AbQBt
// SIG // AG8AbgAuAGoAc6EWgBRodHRwOi8vbWljcm9zb2Z0LmNv
// SIG // bTANBgkqhkiG9w0BAQEFAASCAQB9qcpTtreLyao7wgob
// SIG // NAUdxpdS4MetBJFlZpw/0UVc1HN5Y3yasVwy9UdASvHn
// SIG // KQk+n2csw1iFmfejB+iXl3qiS9jmNtRx8LLlBcvTPVyF
// SIG // prVuDKos8r+DB2J3gj0D5vnahiN3cVuyCxd/jjoVYhFA
// SIG // GhklG28lNFF+GkW/aXJXV9URD9JsSS6rIO3rGHviVAFr
// SIG // buc33SzDDTPAtNglIBmuA7O/N/HwRrGw3un07+/XVLhI
// SIG // SP8P2FZYxzW0a59ZeJlJlbj9iFSnF5syna7UeQVz6Qp+
// SIG // e9p7WxWqPrwKF9q2QJQsxoOvEj9EUEUIe52z1k1TeTlx
// SIG // AMMA0CTzi+8tyg6hoYITTTCCE0kGCisGAQQBgjcDAwEx
// SIG // ghM5MIITNQYJKoZIhvcNAQcCoIITJjCCEyICAQMxDzAN
// SIG // BglghkgBZQMEAgEFADCCAT0GCyqGSIb3DQEJEAEEoIIB
// SIG // LASCASgwggEkAgEBBgorBgEEAYRZCgMBMDEwDQYJYIZI
// SIG // AWUDBAIBBQAEIK9ZvP4kKVB/FrWSLxEQXICfWWM5YRpY
// SIG // 5yoWv0Dbgn1/AgZYl43wSz8YEzIwMTcwMjA5MDQyMDA1
// SIG // Ljc3MlowBwIBAYACAfSggbmkgbYwgbMxCzAJBgNVBAYT
// SIG // AlVTMRMwEQYDVQQIEwpXYXNoaW5ndG9uMRAwDgYDVQQH
// SIG // EwdSZWRtb25kMR4wHAYDVQQKExVNaWNyb3NvZnQgQ29y
// SIG // cG9yYXRpb24xDTALBgNVBAsTBE1PUFIxJzAlBgNVBAsT
// SIG // Hm5DaXBoZXIgRFNFIEVTTjo1ODQ3LUY3NjEtNEY3MDEl
// SIG // MCMGA1UEAxMcTWljcm9zb2Z0IFRpbWUtU3RhbXAgU2Vy
// SIG // dmljZaCCDtAwggZxMIIEWaADAgECAgphCYEqAAAAAAAC
// SIG // MA0GCSqGSIb3DQEBCwUAMIGIMQswCQYDVQQGEwJVUzET
// SIG // MBEGA1UECBMKV2FzaGluZ3RvbjEQMA4GA1UEBxMHUmVk
// SIG // bW9uZDEeMBwGA1UEChMVTWljcm9zb2Z0IENvcnBvcmF0
// SIG // aW9uMTIwMAYDVQQDEylNaWNyb3NvZnQgUm9vdCBDZXJ0
// SIG // aWZpY2F0ZSBBdXRob3JpdHkgMjAxMDAeFw0xMDA3MDEy
// SIG // MTM2NTVaFw0yNTA3MDEyMTQ2NTVaMHwxCzAJBgNVBAYT
// SIG // AlVTMRMwEQYDVQQIEwpXYXNoaW5ndG9uMRAwDgYDVQQH
// SIG // EwdSZWRtb25kMR4wHAYDVQQKExVNaWNyb3NvZnQgQ29y
// SIG // cG9yYXRpb24xJjAkBgNVBAMTHU1pY3Jvc29mdCBUaW1l
// SIG // LVN0YW1wIFBDQSAyMDEwMIIBIjANBgkqhkiG9w0BAQEF
// SIG // AAOCAQ8AMIIBCgKCAQEAqR0NvHcRijog7PwTl/X6f2mU
// SIG // a3RUENWlCgCChfvtfGhLLF/Fw+Vhwna3PmYrW/AVUycE
// SIG // MR9BGxqVHc4JE458YTBZsTBED/FgiIRUQwzXTbg4CLNC
// SIG // 3ZOs1nMwVyaCo0UN0Or1R4HNvyRgMlhgRvJYR4YyhB50
// SIG // YWeRX4FUsc+TTJLBxKZd0WETbijGGvmGgLvfYfxGwScd
// SIG // JGcSchohiq9LZIlQYrFd/XcfPfBXday9ikJNQFHRD5wG
// SIG // Pmd/9WbAA5ZEfu/QS/1u5ZrKsajyeioKMfDaTgaRtogI
// SIG // Neh4HLDpmc085y9Euqf03GS9pAHBIAmTeM38vMDJRF1e
// SIG // FpwBBU8iTQIDAQABo4IB5jCCAeIwEAYJKwYBBAGCNxUB
// SIG // BAMCAQAwHQYDVR0OBBYEFNVjOlyKMZDzQ3t8RhvFM2ha
// SIG // hW1VMBkGCSsGAQQBgjcUAgQMHgoAUwB1AGIAQwBBMAsG
// SIG // A1UdDwQEAwIBhjAPBgNVHRMBAf8EBTADAQH/MB8GA1Ud
// SIG // IwQYMBaAFNX2VsuP6KJcYmjRPZSQW9fOmhjEMFYGA1Ud
// SIG // HwRPME0wS6BJoEeGRWh0dHA6Ly9jcmwubWljcm9zb2Z0
// SIG // LmNvbS9wa2kvY3JsL3Byb2R1Y3RzL01pY1Jvb0NlckF1
// SIG // dF8yMDEwLTA2LTIzLmNybDBaBggrBgEFBQcBAQROMEww
// SIG // SgYIKwYBBQUHMAKGPmh0dHA6Ly93d3cubWljcm9zb2Z0
// SIG // LmNvbS9wa2kvY2VydHMvTWljUm9vQ2VyQXV0XzIwMTAt
// SIG // MDYtMjMuY3J0MIGgBgNVHSABAf8EgZUwgZIwgY8GCSsG
// SIG // AQQBgjcuAzCBgTA9BggrBgEFBQcCARYxaHR0cDovL3d3
// SIG // dy5taWNyb3NvZnQuY29tL1BLSS9kb2NzL0NQUy9kZWZh
// SIG // dWx0Lmh0bTBABggrBgEFBQcCAjA0HjIgHQBMAGUAZwBh
// SIG // AGwAXwBQAG8AbABpAGMAeQBfAFMAdABhAHQAZQBtAGUA
// SIG // bgB0AC4gHTANBgkqhkiG9w0BAQsFAAOCAgEAB+aIUQ3i
// SIG // xuCYP4FxAz2do6Ehb7Prpsz1Mb7PBeKp/vpXbRkws8LF
// SIG // Zslq3/Xn8Hi9x6ieJeP5vO1rVFcIK1GCRBL7uVOMzPRg
// SIG // Eop2zEBAQZvcXBf/XPleFzWYJFZLdO9CEMivv3/Gf/I3
// SIG // fVo/HPKZeUqRUgCvOA8X9S95gWXZqbVr5MfO9sp6AG9L
// SIG // MEQkIjzP7QOllo9ZKby2/QThcJ8ySif9Va8v/rbljjO7
// SIG // Yl+a21dA6fHOmWaQjP9qYn/dxUoLkSbiOewZSnFjnXsh
// SIG // bcOco6I8+n99lmqQeKZt0uGc+R38ONiU9MalCpaGpL2e
// SIG // Gq4EQoO4tYCbIjggtSXlZOz39L9+Y1klD3ouOVd2onGq
// SIG // BooPiRa6YacRy5rYDkeagMXQzafQ732D8OE7cQnfXXSY
// SIG // Ighh2rBQHm+98eEA3+cxB6STOvdlR3jo+KhIq/fecn5h
// SIG // a293qYHLpwmsObvsxsvYgrRyzR30uIUBHoD7G4kqVDmy
// SIG // W9rIDVWZeodzOwjmmC3qjeAzLhIp9cAvVCch98isTtoo
// SIG // uLGp25ayp0Kiyc8ZQU3ghvkqmqMRZjDTu3QyS99je/WZ
// SIG // ii8bxyGvWbWu3EQ8l1Bx16HSxVXjad5XwdHeMMD9zOZN
// SIG // +w2/XU/pnR4ZOC+8z1gFLu8NoFA12u8JJxzVs341Hgi6
// SIG // 2jbb01+P3nSISRIwggTaMIIDwqADAgECAhMzAAAAszm7
// SIG // 1BKTFan+AAAAAACzMA0GCSqGSIb3DQEBCwUAMHwxCzAJ
// SIG // BgNVBAYTAlVTMRMwEQYDVQQIEwpXYXNoaW5ndG9uMRAw
// SIG // DgYDVQQHEwdSZWRtb25kMR4wHAYDVQQKExVNaWNyb3Nv
// SIG // ZnQgQ29ycG9yYXRpb24xJjAkBgNVBAMTHU1pY3Jvc29m
// SIG // dCBUaW1lLVN0YW1wIFBDQSAyMDEwMB4XDTE2MDkwNzE3
// SIG // NTY1OFoXDTE4MDkwNzE3NTY1OFowgbMxCzAJBgNVBAYT
// SIG // AlVTMRMwEQYDVQQIEwpXYXNoaW5ndG9uMRAwDgYDVQQH
// SIG // EwdSZWRtb25kMR4wHAYDVQQKExVNaWNyb3NvZnQgQ29y
// SIG // cG9yYXRpb24xDTALBgNVBAsTBE1PUFIxJzAlBgNVBAsT
// SIG // Hm5DaXBoZXIgRFNFIEVTTjo1ODQ3LUY3NjEtNEY3MDEl
// SIG // MCMGA1UEAxMcTWljcm9zb2Z0IFRpbWUtU3RhbXAgU2Vy
// SIG // dmljZTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoC
// SIG // ggEBAJ42eXjeuC/MHUn9fikiWJr2Ylp7yzldveklaHAm
// SIG // d8soj1xvNY6raNcUqYB4Ag9qssERi19kp2s7RBL3l4qW
// SIG // hD3fqn9haaKIBs4J9InmhmZBhJQzwdYi81RYANo9Xv6w
// SIG // o4mmZ+yNPW7TLIF/aIvd5UhMQ8kObht+DQLGugVqWwLU
// SIG // DnsrDfOqV5OcEkPxBfJYLY741QZMTcbLK1G8yWSE8PaV
// SIG // apWwM1hT1A5udRUivrizzWBbBA0JXphdAAsLAHFyd6YR
// SIG // 4jLQ07bdqlUFg8aHQXw+GuoiFBAc6M7wkq7L+4x3oevE
// SIG // x9798fA8EDGm8H0SyGZalbEjJss19jQYS6kiubUCAwEA
// SIG // AaOCARswggEXMB0GA1UdDgQWBBTTXe3WW0qpaL5VZmRJ
// SIG // h3PrF/AicDAfBgNVHSMEGDAWgBTVYzpcijGQ80N7fEYb
// SIG // xTNoWoVtVTBWBgNVHR8ETzBNMEugSaBHhkVodHRwOi8v
// SIG // Y3JsLm1pY3Jvc29mdC5jb20vcGtpL2NybC9wcm9kdWN0
// SIG // cy9NaWNUaW1TdGFQQ0FfMjAxMC0wNy0wMS5jcmwwWgYI
// SIG // KwYBBQUHAQEETjBMMEoGCCsGAQUFBzAChj5odHRwOi8v
// SIG // d3d3Lm1pY3Jvc29mdC5jb20vcGtpL2NlcnRzL01pY1Rp
// SIG // bVN0YVBDQV8yMDEwLTA3LTAxLmNydDAMBgNVHRMBAf8E
// SIG // AjAAMBMGA1UdJQQMMAoGCCsGAQUFBwMIMA0GCSqGSIb3
// SIG // DQEBCwUAA4IBAQAiV3ujVO9S7REMoDNF5DZ9GHJuELMA
// SIG // z2V1Gfb1gosbquVJTEFce/9AO2gRa5aTVAVw4WzKAGNw
// SIG // OGsyzMybI8qI3yM7JHBDk1ni7fmpVW+nwxMgxQ5BMRwJ
// SIG // phXdRltC6YUZwXWzVpn8cIleq9uuypIIL6EbTwICbjhv
// SIG // tuDzaVDfnizJvMclLGnZtSavxDDupLOIwWu27IcS7eQU
// SIG // cgLEY2LBAOfKnLoTzZ55Q7imoSF7i16lFvrVXFKOK2Mg
// SIG // 1Rsi4EJhVVnwkNXLc7W6B3p3aW2Y1zeZa1nbbt7vqGC0
// SIG // NM9t0mZUUwyKmuAiEIzAwzCZ3eQ5MuSLmNoqNiD5TBlm
// SIG // zynLoYIDeTCCAmECAQEwgeOhgbmkgbYwgbMxCzAJBgNV
// SIG // BAYTAlVTMRMwEQYDVQQIEwpXYXNoaW5ndG9uMRAwDgYD
// SIG // VQQHEwdSZWRtb25kMR4wHAYDVQQKExVNaWNyb3NvZnQg
// SIG // Q29ycG9yYXRpb24xDTALBgNVBAsTBE1PUFIxJzAlBgNV
// SIG // BAsTHm5DaXBoZXIgRFNFIEVTTjo1ODQ3LUY3NjEtNEY3
// SIG // MDElMCMGA1UEAxMcTWljcm9zb2Z0IFRpbWUtU3RhbXAg
// SIG // U2VydmljZaIlCgEBMAkGBSsOAwIaBQADFQC++cH02g8V
// SIG // P/CQAwO+eKWa2orcuaCBwjCBv6SBvDCBuTELMAkGA1UE
// SIG // BhMCVVMxEzARBgNVBAgTCldhc2hpbmd0b24xEDAOBgNV
// SIG // BAcTB1JlZG1vbmQxHjAcBgNVBAoTFU1pY3Jvc29mdCBD
// SIG // b3Jwb3JhdGlvbjENMAsGA1UECxMETU9QUjEnMCUGA1UE
// SIG // CxMebkNpcGhlciBOVFMgRVNOOjRERTktMEM1RS0zRTA5
// SIG // MSswKQYDVQQDEyJNaWNyb3NvZnQgVGltZSBTb3VyY2Ug
// SIG // TWFzdGVyIENsb2NrMA0GCSqGSIb3DQEBBQUAAgUA3EXM
// SIG // TjAiGA8yMDE3MDIwODE2NTY0NloYDzIwMTcwMjA5MTY1
// SIG // NjQ2WjB3MD0GCisGAQQBhFkKBAExLzAtMAoCBQDcRcxO
// SIG // AgEAMAoCAQACAhJfAgH/MAcCAQACAhmuMAoCBQDcRx3O
// SIG // AgEAMDYGCisGAQQBhFkKBAIxKDAmMAwGCisGAQQBhFkK
// SIG // AwGgCjAIAgEAAgMW42ChCjAIAgEAAgMHoSAwDQYJKoZI
// SIG // hvcNAQEFBQADggEBAF3lQ3ZqLs5iAy6hIY4twbGxL2u8
// SIG // laxwaX3GCGXgZ+BqK32Cu4LyFV2bYz4wXa9UNrNUeb5X
// SIG // wYelD6A5yKq/fkBpkrIPobB+tIySkTb2n7urStJPV/lx
// SIG // hBXLmvyLAHvIPcJhybYEdLd0uJtufVYkZVPzPHYdb766
// SIG // EDL7MRE5YXxo8chKzs6doWtRH9Mi4dcezU3fl8d+hcqn
// SIG // 8j8vudGmV7LuPbJN9Ipu+/Y3BamtRiW9HCjF0P85MgXa
// SIG // Ae7wmxOhZd1brK5VYrjHsmPUPb6ApPKePFmDCyCGc9ru
// SIG // 1/z008lO1Lo/iJpz7lCIL2s1RfCo9SOS75zXgfw1aZHn
// SIG // ve7PyEUxggL1MIIC8QIBATCBkzB8MQswCQYDVQQGEwJV
// SIG // UzETMBEGA1UECBMKV2FzaGluZ3RvbjEQMA4GA1UEBxMH
// SIG // UmVkbW9uZDEeMBwGA1UEChMVTWljcm9zb2Z0IENvcnBv
// SIG // cmF0aW9uMSYwJAYDVQQDEx1NaWNyb3NvZnQgVGltZS1T
// SIG // dGFtcCBQQ0EgMjAxMAITMwAAALM5u9QSkxWp/gAAAAAA
// SIG // szANBglghkgBZQMEAgEFAKCCATIwGgYJKoZIhvcNAQkD
// SIG // MQ0GCyqGSIb3DQEJEAEEMC8GCSqGSIb3DQEJBDEiBCDi
// SIG // WpFpTTsRRhZaf6KUHefV5ZjZTkYFqKoXGPv7a/t8GTCB
// SIG // 4gYLKoZIhvcNAQkQAgwxgdIwgc8wgcwwgbEEFL75wfTa
// SIG // DxU/8JADA754pZraity5MIGYMIGApH4wfDELMAkGA1UE
// SIG // BhMCVVMxEzARBgNVBAgTCldhc2hpbmd0b24xEDAOBgNV
// SIG // BAcTB1JlZG1vbmQxHjAcBgNVBAoTFU1pY3Jvc29mdCBD
// SIG // b3Jwb3JhdGlvbjEmMCQGA1UEAxMdTWljcm9zb2Z0IFRp
// SIG // bWUtU3RhbXAgUENBIDIwMTACEzMAAACzObvUEpMVqf4A
// SIG // AAAAALMwFgQUtY2d4x2DjYB3B5UUCGDRhRdc5q4wDQYJ
// SIG // KoZIhvcNAQELBQAEggEATJ7/KDnyn3T93L3tgQduOzMM
// SIG // /QUVSYfx98X9KrkojyLBLAyp1X9ZV5IU+Rff+ReFR6W9
// SIG // QapFaTnMCGUG2fhM7d1FTW3YqVXQngXDTQm0RUU8RjIR
// SIG // qhV8C5XQ8lXn8PTabnWqKvOBSGeFO4ONcw3onJSG2H/1
// SIG // 6DRQDNYnv3v2lXnNsVxB4XRkRdkhCrbyhJFPQo6JiUB7
// SIG // uwuPghwH2jS66EeusEhoa8THh/BtQuzvbJs1xiUqTmkL
// SIG // UOj53x/sKQgD/uMF2TkGKFPWyeCmlT9g8Y8IzzhTelJ7
// SIG // 0D1IRlqiqv0nlcFaroxjIn36LgYdw/+U0UXVIgNIfDDB
// SIG // wurhC5dzIA==
// SIG // End signature block
