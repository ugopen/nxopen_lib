// Copyright (c) Microsoft Corporation. All rights reserved.
var bValidating = false;

//SET DIRECTION FUNCTION*************************************
//***********************************************************
function setDirection()
{
	if (document.dir == "rtl")
	{
		
		//SET CONTENT FRAME FLOW FOR RTL*********************
		//***************************************************
		var CatcHERa = document.all.tags("LI");
		var CatcHERb = document.all.tags("DIV");
		var CatcHERc = document.all.tags("SPAN");
		var CatcHERd = document.all.tags("INPUT");
		var CatcHERe = document.all.tags("TABLE");
		var CatcHERf = document.all.tags("BUTTON");
		var CatcHERg = document.all.tags("SELECT");
		var CatcHERh = document.all.tags("OBJECT");
		
		if (CatcHERa != null)
		{
		  for (var i = 0; i < CatcHERa.length; i++)
		  {
            if (CatcHERa[i].className.toLowerCase() == "list")
			{
			  CatcHERa[i].style.left = "0px";
			  CatcHERa[i].style.right = "-15px";
			}
		  }
		}
		
		if (CatcHERb != null)
		{
		  for (var i = 0; i < CatcHERb.length; i++)
		  {
            if (CatcHERb[i].className.toLowerCase() == "vertline")
			{
			  CatcHERb[i].style.left = "0px";
			  CatcHERb[i].style.right = "0px";
			}
            if (CatcHERb[i].className.toLowerCase() == "itemtextradiob")
			{
			  CatcHERb[i].style.left = "0px";
			  CatcHERb[i].style.right = "25px";
			}
            if (CatcHERb[i].className.toLowerCase() == "itemtextradioindenta")
			{
			  CatcHERb[i].style.left = "0px";
			  CatcHERb[i].style.right = "30px";
			}
            if (CatcHERb[i].className.toLowerCase() == "itemtextradioindentb")
			{
			  CatcHERb[i].style.left = "0px";
			  CatcHERb[i].style.right = "42px";
			}
            if (CatcHERb[i].className.toLowerCase() == "itemtextcheckboxa")
			{
			  CatcHERb[i].style.left = "0px";
			  CatcHERb[i].style.right = "15px";
			}
            if (CatcHERb[i].className.toLowerCase() == "itemtextcheckboxb")
			{
			  CatcHERb[i].style.left = "0px";
			  CatcHERb[i].style.right = "25px";
			}
            if (CatcHERb[i].className.toLowerCase() == "itemtextcheckboxindentb")
			{
			  CatcHERb[i].style.left = "0px";
			  CatcHERb[i].style.right = "42px";
			}
		  }
		}
		
		if (CatcHERc != null)
		{
		  for (var i = 0; i < CatcHERc.length; i++)
		  {
            if (CatcHERc[i].className.toLowerCase() == "vertline1")
			{
			  CatcHERc[i].style.left = "0px";
			  CatcHERc[i].style.right = "-1px";
			}
            if (CatcHERc[i].className.toLowerCase() == "itemtextindent")
			{
			  CatcHERc[i].style.left = "0px";
			  CatcHERc[i].style.right = "17px";
			}
		  }
		}
		
		if (CatcHERd != null)
		{
		  for (var i = 0; i < CatcHERd.length; i++)
		  {
            if (CatcHERd[i].className.toLowerCase() == "radio")
			{
			  CatcHERd[i].style.left = "0px";
			  CatcHERd[i].style.right = "6px";
			}
            if (CatcHERd[i].className.toLowerCase() == "checkbox")
			{
			  CatcHERd[i].style.marginLeft = "0px";
			  CatcHERd[i].style.marginRight = "-4px";
			}
            if (CatcHERd[i].className.toLowerCase() == "checkboxa")
			{
			  CatcHERd[i].style.marginLeft = "0px";
			  CatcHERd[i].style.marginRight = "10px";
			}
            if (CatcHERd[i].className.toLowerCase() == "sidebtn")
			{
			  CatcHERd[i].style.left = "0px";
			  CatcHERd[i].style.right = "9px";
			}
            if (CatcHERd[i].className.toLowerCase() == "sidebtn2")
			{
			  CatcHERd[i].style.left = "0px";
			  CatcHERd[i].style.right = "9px";
			}
            if (CatcHERd[i].className.toLowerCase() == "sidebtnb")
			{
			  CatcHERd[i].style.left = "0px";
			  CatcHERd[i].style.right = "9px";
			}
            if (CatcHERd[i].className.toLowerCase() == "checkboxindent")
			{
			  CatcHERd[i].style.marginLeft = "0px";
			  CatcHERd[i].style.marginRight = "23px";
			}
            if (CatcHERd[i].className.toLowerCase() == "radioindent")
			{
			  CatcHERd[i].style.marginLeft = "0px";
			  CatcHERd[i].style.marginRight = "23px";
			}
            if (CatcHERd[i].className.toLowerCase() == "radioindenta")
			{
			  CatcHERd[i].style.marginLeft = "0px";
			  CatcHERd[i].style.marginRight = "9px";
			}
            if (CatcHERd[i].className.toLowerCase() == "comment")
			{
			  CatcHERd[i].style.left = "0px";
			  CatcHERd[i].style.right = "8px";
			}
		  }
		}
		
		if (CatcHERe != null)
		{
		  for (var i = 0; i < CatcHERe.length; i++)
		  {
            if (CatcHERe[i].className.toLowerCase() == "linktextselected")
			{
			  CatcHERe[i].style.left = "0px";
			  CatcHERe[i].style.right = "10px";
			}
            if (CatcHERe[i].className.toLowerCase() == "linktextselectedindent")
			{
			  CatcHERe[i].style.left = "0px";
			  CatcHERe[i].style.right = "16px";
			}
            if (CatcHERe[i].className.toLowerCase() == "linktext")
			{
			  CatcHERe[i].style.left = "0px";
			  CatcHERe[i].style.right = "10px";
			}
            if (CatcHERe[i].className.toLowerCase() == "linktextindent")
			{
			  CatcHERe[i].style.left = "0px";
			  CatcHERe[i].style.right = "16px";
			}
		  }
		}
		
		if (CatcHERf != null)
		{
		  for (var i = 0; i < CatcHERf.length; i++)
		  {
            if (CatcHERf[i].className.toLowerCase() == "buttonclass")
			{
			  CatcHERf[i].style.marginLeft = "0px";
			  CatcHERf[i].style.marginRight = "8px";
			}
		  }
		}
		
		if (CatcHERg != null)
		{
		  for (var i = 0; i < CatcHERg.length; i++)
		  {
            if (CatcHERg[i].className.toLowerCase() == "sidebtn")
			{
			  CatcHERg[i].style.left = "0px";
			  CatcHERg[i].style.right = "9px";
			}
            if (CatcHERg[i].className.toLowerCase() == "sidebtn2")
			{
			  CatcHERg[i].style.left = "0px";
			  CatcHERg[i].style.right = "17px";
			}
            if (CatcHERg[i].className.toLowerCase() == "sidebtn2a")
			{
			  CatcHERg[i].style.left = "0px";
			  CatcHERg[i].style.right = "25px";
			}
            if (CatcHERg[i].className.toLowerCase() == "sidebtn2b")
			{
			  CatcHERg[i].style.left = "0px";
			  CatcHERg[i].style.right = "8px";
			}
		  }
		}
		
		if (CatcHERh != null)
		{
		  for (var i = 0; i < CatcHERh.length; i++)
		  {
            if (CatcHERh[i].className.toLowerCase() == "itemtext")
			{
			  CatcHERh[i].style.left = "0px";
			  CatcHERh[i].style.right = "8px";
			}
		  }
		}
		
		//SET INTRODUCTION FRAME FLOW FOR RTL****************
		//***************************************************
		
		//SET INTRODUCTION SUBHEADING TEXT ALIGNMENT*********
		document.all("SUBHEAD").style.marginLeft = "0px";
		document.all("SUBHEAD").style.marginRight = "10px";
		
		//SET INTRODUCTION IMAGE ALIGNMENT*******************
		document.all("IMAGE_TABLE").style.textAlign = "left";
	}
}

//SET POTENTIALLY DISABLED TABS FOR MOUSEOVER****************
//***********************************************************

function MouseOver(obj)
{

	if ((obj == null) || (typeof(obj) == "undefined"))
		return;
	
	else if ((obj.id != "DatSupBtn") || (obj.id != "BrowseBtn"))
	{
		obj.className = "activelink";
	}
	
	else if (obj.id == "DBSupport")
	{
		if (window.external.FindSymbol("APP_TYPE_DLG"))
		{ 
			obj.className = "inactivelink"; 
		}
	}
	
	else if ((obj.id == "CompoundDoc") || (obj.id == "DocTemp"))
	{
		if ((!window.external.FindSymbol("DOCVIEW")) || (window.external.IsSymbolDisabled("DOCVIEW")))
		{ 
			obj.className = "inactivelink";
		}
	} 
	else if (obj.id == "Notifications")
	{
		if (!GENERATE_FILTER.checked) 
		{ 
			obj.className = "inactivelink"; 
		}
	}
	else if (obj.id == "DatSupBtn")
	{
		if ((DB_VIEW_WITH_FILE.checked) || (DB_VIEW_NO_FILE.checked))
		{
			DatSupBtn.disabled = false;
			sdstitle.disabled = false;
		}
		
		else if ((!DB_VIEW_WITH_FILE.checked) && (!DB_VIEW_NO_FILE.checked))
		{
			DatSupBtn.disabled = true;
			sdstitle.disabled = true;
		}
	}
}

//SET POTENTIALLY DISABLED TABS FOR MOUSEOUT*****************
//***********************************************************
function MouseOut(obj)
{

	if ((obj == null) || (typeof(obj) == "undefined"))
		return;
	
	else if (obj.id == "DBSupport")
	{
	
		if (obj.className == "")
		{
			obj.className = ""
		}
		
		else
		{
			obj.className = "activelink"; 
		}
		
		if (window.external.FindSymbol("APP_TYPE_DLG")) 
		{ 
			obj.className = "inactivelink"; 
		}
	}
	
	else if ((obj.id == "CompoundDoc") || (obj.id == "DocTemp"))
	{
	
		if (obj.className == "")
		{
			obj.className = ""
		}
		
		else
		{
			obj.className = "activelink"; 
		}
		
		if ((!window.external.FindSymbol("DOCVIEW")) || (window.external.IsSymbolDisabled("DOCVIEW")))
		{ 
			obj.className = "inactivelink";
		}
	} 
	
	else if (obj.id == "Notifications")
	{
	
		if (obj.className == "")
		{
			obj.className = ""
		}
		
		else
		{
			obj.className = "activelink"; 
		}
		
		if (!window.external.FindSymbol("GENERATE_FILTER")) 
		{
			obj.className = "inactivelink";
		}
	}
	
	else if (obj.id == "DatSupBtn")
	{
	
		if ((DB_VIEW_WITH_FILE.checked) || (DB_VIEW_NO_FILE.checked))
		{
			DatSupBtn.disabled = false;
			sdstitle.disabled = false;
		}
		
		else if ((!DB_VIEW_WITH_FILE.checked) && (!DB_VIEW_NO_FILE.checked))
		{
			DatSupBtn.disabled = true;
			sdstitle.disabled = true;
		}
	}	
	
	else if (obj.id == "ServerOptions")
	{
	
		if (obj.className == "")
		{
			obj.className = ""
		}
		
		else
		{
			obj.className = "activelink"; 
		}
		
		if ((!window.external.FindSymbol("GENERATE_ISAPI")) && (!window.external.FindSymbol("COMBINE_PROJECTS")))
		{ 
			obj.className = "inactivelink"; 
		}
	}
	
	else if (obj.id == "AppOptions")
	{
		if (obj.className == "")
		{
			obj.className = ""
		}
		
		else
		{
			obj.className = "activelink"; 
		}
		
		if ((!window.external.FindSymbol("GENERATE_APP")) && (!window.external.FindSymbol("COMBINE_PROJECTS")))
		{
			obj.className = "inactivelink";
		}
	}
	
	else if (obj.id == "BrowseBtn")
	{
		obj.disabled = true;
		
		if ((GENERATE_ISAPI.checked) && (GENERATE_ISAPI.disabled == false))
		{
			obj.disabled = false;
		}
	}	
}

function MouseOutEx(obj)
{

	if ((obj == null) || (typeof(obj) == "undefined"))
		return;
	
	else if (obj.id == "DocTemp")
	{
	
		if (obj.className == "")
		{
			obj.className = ""
		}
		
		else
		{
			obj.className = "activelink"; 
		}
		
		if ((!window.external.FindSymbol("DOCVIEW")) || (window.external.IsSymbolDisabled("DOCVIEW")))
		{ 
			obj.className = "inactivelink";
		}
	} 
}

/******************************************************************************
 Description: OnKeyPress event handler for HTML pages
******************************************************************************/
function OnPress()
{
	// get outermost window for new UI with frames
	var oDefault = window;
	while (oDefault != oDefault.parent)
		oDefault = oDefault.parent;

	var bPreviousTab = false;

	if (event.keyCode != 0)
	{
		if (!event.repeat)
		{
			switch(event.keyCode)
			{
				// Enter
				case 13:
					if (event.srcElement.className && (event.srcElement.className.toLowerCase() == "activelink" || event.srcElement.className.toLowerCase() == "inactivelink"))
					{
						event.cancelBubble = true;
						event.srcElement.click();
						break;
					}
					if (event.srcElement.type == null ||
						(event.srcElement.type && event.srcElement.type.toLowerCase() != "button"))
						oDefault.FinishBtn.click();
					break;

				// Backspace		
				case 8:
					if (event.srcElement.type == null ||
						(event.srcElement.type && event.srcElement.type.toLowerCase() != "text"))
						event.returnValue = false;
					break;
					
				// Escape
				case 27:
					oDefault.CancelBtn.click();
					break;
			}
		}
	}
}

/*****************************************************************************
 Description: OnKeyDown event handler for HTML pages.
******************************************************************************/
function OnKey()
{
	//Get outermost window
	var oDefault = window;
	while (oDefault != oDefault.parent)
		oDefault = oDefault.parent;

	var bPreviousTab = false;

	if (event.keyCode != 0)
	{
		if (!event.repeat)
		{
			switch(event.keyCode)
			{
				// Enter key for <SELECT>, other controls handled in OnPress()
				case 13:
					if (event.srcElement.type && event.srcElement.type.substr(0,6).toLowerCase() == "select")
						oDefault.FinishBtn.click();
					break;
					
				// Escape key for <SELECT>, other controls handled in OnPress()
				case 27:
					if (event.srcElement.type && event.srcElement.type.substr(0,6).toLowerCase() == "select")
						oDefault.CancelBtn.click();
					break;

				//F1
				case 112:
					oDefault.HelpBtn.click();
					break;
					
				case 65:
				case 70:
				case 78:
					{
						if (event.ctrlKey)
							event.returnValue = false;
					}
					
					break;
					
				//Case for 33,9,34 have to be in this order
				//Page Up
				case 33:
					bPreviousTab = true;
					
				//Tab
				case 9:
					if (event.shiftKey)
						bPreviousTab = true;
						
				//Page Down
				case 34:
					if (event.ctrlKey && oDefault.tab_array != null && oDefault.tab_array.length > 1)
					{
						for (i = 0; i < oDefault.tab_array.length; i++)
						{
							if ((oDefault.tab_array[i].className.toLowerCase() == "activelink") || (oDefault.tab_array[i].className.toLowerCase() == "inactivelink"))
							{
								var j = 0;
								
								if (bPreviousTab)
								{
									j = i - 1;
									while (j != i)
									{
										if (j < 0)
										{
											j = oDefault.tab_array.length - 1;
										}
										if ((oDefault.tab_array[j].className.toLowerCase() == "activelink") || (oDefault.tab_array[j].className.toLowerCase() == "inactivelink"))
										{
											j--;
										}
										else
										{
											break;
										}
									}
									while ((oDefault.tab_array[j].className.toLowerCase() == "") || (oDefault.tab_array[j].className.toLowerCase() == "inactivelink"))
									{
										if (j == 0)
										{
											break;
										}
										if (oDefault.tab_array[j - 1].className.toLowerCase() == "inactivelink")
										{
											j--;
										}
										else
										{
											break;
										}
									}
									if (j == 0)
									{
										j = oDefault.tab_array.length - 1;
									}
									else
									{
										j = j - 1;
									}
								}
								else
								{
									j = i + 1;
									while (j != i)
									{
										if (j >= oDefault.tab_array.length)
										{
											j = 0;
										}
										if ((oDefault.tab_array[j].className.toLowerCase() == "activelink") || (oDefault.tab_array[j].className.toLowerCase() == "inactivelink"))
										{
											j++;
										}
										else
										{
											break;
										}
									}
									while ((oDefault.tab_array[j].className.toLowerCase() == "") || (oDefault.tab_array[j].className.toLowerCase() == "inactivelink"))
									{
										if (j == oDefault.tab_array.length - 1)
										{
											break;
										}
										if (oDefault.tab_array[j + 1].className.toLowerCase() == "inactivelink")
										{
											j++;
										}
										else
										{
											break;
										}
									}
									if (j == oDefault.tab_array.length - 1)
									{
										j = 0;
									}
									else
									{
										j = j + 1;
									}
								}
								//Prevent double notification when we pop up an error
								event.cancelBubble = true;
								oDefault.tab_array[j].click();
								break;
							}
						}
					}
					break;
							
				//Alt-Left arrow
				case 37:
					if (event.altKey)
						event.returnValue = false;
					break;
					
				//Alt-Right arrow
				case 39:					
					if (event.altKey)
						event.returnValue = false;
					break;

				default:
					break;				
			}
		}
	}
}

/******************************************************************************
 Description: KeyDown event handler for WizCombo control
    nKeyCode: Ascii code for key
******************************************************************************/
function OnWizComboKeyDown(nKeyCode)
{
	// Get outermost window
	var oDefault = window;
	while (oDefault != oDefault.parent)
		oDefault = oDefault.parent;

	switch(nKeyCode)
	{
		// Enter
		case 13:
			oDefault.FinishBtn.click();
			break;
			
		// Escape
		case 27:
			oDefault.CancelBtn.click();
			break;

		// F1
		case 112:
			oDefault.HelpBtn.click();
			break;
	}
}

//DO MOUSEOVER***********************************************
//***********************************************************
function MouseOverActiveText()
{
  	var e = window.event.srcElement;
	
	if (e && e.className && e.className.toLowerCase() == "activelink")
		{
		  e.className = "activelink2";
		}
}

//DO MOUSEOUT************************************************
//***********************************************************
function MouseOutActiveText()
{
  	var e = window.event.srcElement;
	
	if (e && e.className && e.className.toLowerCase() == "activelink2")
		{
		  e.className = "activelink";
		}
}


//SET MOUSEOVERS AND MOUSOUTS********************************
//***********************************************************
document.onmouseover = MouseOverActiveText;
document.onmouseout = MouseOutActiveText;

/******************************************************************************
 Description: Called from the wizards html script when 'Finish' is clicked. This
              function in turn calls the wizard control's Finish().
    document: HTML document object
******************************************************************************/
function OnWizFinish(document)
{
	document.body.style.cursor='wait';
	try
	{
		window.external.Finish(document, "ok");
	}
	catch(e)
	{
		document.body.style.cursor='default';
		if (e.description.length != 0)
			SetErrorInfo(e);
		return e.number;
	}
}
