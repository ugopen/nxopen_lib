/******************************************************************************
The next two functions (getNextPage, getPrevPage) are only run in the context of
the next/previous buttons, it is unknown if they will work in any other context.
******************************************************************************/

/******************************************************************************
 Description: method to determine the page the "Next" button should link to, given current
	settings (i.e. find the next non-disabled page).
 Returns: name (including .htm) of next page
******************************************************************************/
function getNextPage()
{
    var count = 0;
    var tab_array = new Array();
    var hit, previousLink, nextLink;
    var findTableTags = window.document.all.tags('TABLE');
    var nextPage;

    //SET PREVIOUS/NEXT BUTTON LINKS********************************
    // *************************************************************
    for (var i = 0; i < findTableTags.length; i++)
    {
        if (findTableTags[i].className.toLowerCase() == 'three')
        {
            var findTheDiv = findTableTags[i].all.tags('DIV');
            for (var ii = 0; ii < findTheDiv.length; ii++)
            {
                if ((findTheDiv[ii].className.toLowerCase() == 'link') || (findTheDiv[ii].className.toLowerCase() == 'linkselected'))
                {
                    count++;
                    if (findTheDiv[ii].className.toLowerCase() == 'linkselected')
                    {
                        hit = ii;
                        previous = ii - 1;
                        next = ii + 1;
                    }
                    var findTheSpan = findTheDiv[ii].all.tags('SPAN');
                    for (var iii = 0; iii < findTheSpan.length; iii++)
                    {
                        if ((findTheSpan[iii].className.toLowerCase() != 'vertline1') && (findTheSpan[iii].className.toLowerCase() != 'horiline1'))
                        {
                            if (!findTheSpan[iii].disabled && findTheSpan[iii].className.toLowerCase() == "activelink")
                            {
                                tab_array[ii] = findTheSpan[iii].id;
                            }
                            else
                            {
                                tab_array[ii] = null;
                            }
                        }
                    }
                }
            }
        }
    }
    nextPage = hit + 1;
    while (nextPage < tab_array.length)
        {
            if (tab_array[nextPage])
            {
                break;
            }
            else
            {
                nextPage++;
            }
        }
    if (nextPage >= tab_array.length)
        nextPage = hit;
    return tab_array[nextPage] + ".htm";
}

/******************************************************************************
 Description: method to determine the page the "Previous" button should link to, given current
	settings (i.e. find the previous non-disabled page).
 Returns: name (including .htm) of previous page
******************************************************************************/
function getPrevPage()
{
    var count = 0;
    var tab_array = new Array();
    var hit, previousLink, nextLink;
    var findTableTags = window.document.all.tags('TABLE');
    var prevPage;

    //SET PREVIOUS/NEXT BUTTON LINKS********************************
    // *************************************************************
    for (var i = 0; i < findTableTags.length; i++)
    {
        if (findTableTags[i].className.toLowerCase() == 'three')
        {
            var findTheDiv = findTableTags[i].all.tags('DIV');
            for (var ii = 0; ii < findTheDiv.length; ii++)
            {
                if ((findTheDiv[ii].className.toLowerCase() == 'link') || (findTheDiv[ii].className.toLowerCase() == 'linkselected'))
                {
                    count++;
                    if (findTheDiv[ii].className.toLowerCase() == 'linkselected')
                    {
                        hit = ii;
                        previous = ii - 1;
                        next = ii + 1;
                    }
                    var findTheSpan = findTheDiv[ii].all.tags('SPAN');
                    for (var iii = 0; iii < findTheSpan.length; iii++)
                    {
                        if ((findTheSpan[iii].className.toLowerCase() != 'vertline1') && (findTheSpan[iii].className.toLowerCase() != 'horiline1'))
                        {
                            if (!findTheSpan[iii].isDisabled && findTheSpan[iii].className.toLowerCase() == "activelink")
                            {
                                tab_array[ii] = findTheSpan[iii].id;
                            }
                            else
                            {
                                tab_array[ii] = null;
                            }
                        }
                    }
                }
            }
        }
    }
    prevPage = hit - 1;
    while (prevPage >= 0)
        {
            if (tab_array[prevPage])
            {
                break;
            }
            else
            {
                prevPage--;
            }
        }
    if (prevPage >= tab_array.length)
        prevPage = hit;
    return tab_array[prevPage] + ".htm";
}

function initItems()
{
    try
    {
        if (PreviousBtn != null) return;
    }
    catch (e)
    {
    }

    var findTableTags = window.document.all.tags('TABLE');

    // Look over all tables and see if any has the class 'three'.
    // That's the class that this behavior was originally attached to.
    // If we don't find such a table, don't add the buttons
    var FoundTable = false;
    var i;
    for (i = 0; i < findTableTags.length; i++)
    {
        if (findTableTags[i].className.toLowerCase() == 'three')
        {
            FoundTable = true;
            break;
        }
    }
    if (!FoundTable) return;


    var count = 0;
    var hit, previous, next;
    var tab_array = new Array();
    var previousLink, nextLink;



    //FIND THE SELECTED TAB AND DYNAMICALLY COLOR THE BACKGROUND****
    // *************************************************************
    for (var i = 0; i < findTableTags.length; i++)
    {
        if ((findTableTags[i].className.toLowerCase() == 'linktextselected')|| (findTableTags[i].className.toLowerCase() == 'linktextselectedindent'))
        {
            var findTheSpan = findTableTags[i].all.tags('SPAN');

            for (var ii = 0; ii < findTheSpan.length; ii++)
            {
                findTheSpan[ii].style.padding = "4px";
                findTheSpan[ii].style.left = "-2px";
                findTheSpan[ii].style.backgroundColor = "InactiveBorder";
                findTheSpan[ii].style.lineHeight = "1.7em";
            }
        }
    }
    // *************************************************************


    //SET PREVIOUS/NEXT BUTTON LINKS********************************
    // *************************************************************
    for (var i = 0; i < findTableTags.length; i++)
    {
        if (findTableTags[i].className.toLowerCase() == 'three')
        {
            var findTheDiv = findTableTags[i].all.tags('DIV');
            for (var ii = 0; ii < findTheDiv.length; ii++)
            {
                if ((findTheDiv[ii].className.toLowerCase() == 'link') || (findTheDiv[ii].className.toLowerCase() == 'linkselected'))
                {
                    count++;
                    if (findTheDiv[ii].className.toLowerCase() == 'linkselected')
                    {
                        hit = ii;
                        previous = ii - 1;
                        next = ii + 1;
                    }
                }
            }
        }
    }
    if (previous > -1)
    {
        previousLink = "onClick=\"bValidating = true; try { if (!ValidateInput()) { bValidating = false; return; } } catch(e) { }; Next(document, getPrevPage());\"";
    }
    else
    {
        previousLink = "DISABLED";
    }

    if (next < count)
    {
        nextLink = "onClick=\"bValidating = true; try { if (!ValidateInput()) { bValidating = false; return; } } catch(e) { }; Next(document, getNextPage());\"";
    }
    else
    {
        nextLink = "DISABLED";
    }
    // *************************************************************



    //ADD PREVIOUS AND NEXT BUTTONS - 4 ROWS TO TABLE***************
    // *************************************************************
	var L_NextButtin_Text = "Next &gt;";
	var L_PrevButtin_Text = "&lt; Previous";

    var targetRow = findTableTags[findTableTags.length - 2].rows[2];
    targetRow.insertCell(2).innerHTML = "<BUTTON CLASS='BUTTONS' ID='PreviousBtn'" + previousLink + ">"+L_PrevButtin_Text+"</BUTTON>";
    targetRow.cells[2].vAlign = "MIDDLE";
    targetRow.cells[2].height = "23";
    targetRow.cells[2].width = "75";
    targetRow.insertCell(3).innerHTML = "&nbsp; ";
    targetRow.cells[3].vAlign = "MIDDLE";
    targetRow.cells[3].height = "23";
    targetRow.cells[3].width = "4";
    targetRow.insertCell(4).innerHTML = "<BUTTON CLASS='BUTTONS' ID='NextBtn' " + nextLink + ">"+L_NextButtin_Text+"</BUTTON>";
    targetRow.cells[4].vAlign = "MIDDLE";
    targetRow.cells[4].height = "23";
    targetRow.cells[4].width = "75";
    targetRow.insertCell(5).innerHTML = "&nbsp; ";
    targetRow.cells[5].vAlign = "MIDDLE";
    targetRow.cells[5].height = "23";
    targetRow.cells[5].width = "4";
    // *************************************************************



    //FIX BUTTON TABLE'S ROW SPANS**********************************
    // *************************************************************
    var targetRow1 = findTableTags[findTableTags.length - 2].rows[0];
    targetRow1.cells[0].colSpan = "12";

    var targetRow2 = findTableTags[findTableTags.length - 2].rows[1];
    targetRow2.cells[0].colSpan = "12";

    var targetRow3 = findTableTags[findTableTags.length - 2].rows[3];
    targetRow3.cells[0].colSpan = "12";
    // *************************************************************



    //FIND THE TABLES DRAWING HORIZONTAL RULES AND DELETE GRAY LINE*
    // *************************************************************
    var findTDTags = window.document.all.tags('TD');

    for (var i = 0; i < findTDTags.length; i++)
    {
        if (findTDTags[i].className.toLowerCase() == 'rule')
        {
            var findTheTD = findTDTags[i].all.tags('TD');

            for (var ii = 0; ii < findTheTD.length; ii++)
            {
                findTheTD[ii].style.backgroundColor = "Window";
            }
        }
    }
    // *************************************************************
}

// We might be invoked in a scenario (not inside IE) when this fails. Just ignore...
try
{
	initItems();
}
catch (e)
{
}
