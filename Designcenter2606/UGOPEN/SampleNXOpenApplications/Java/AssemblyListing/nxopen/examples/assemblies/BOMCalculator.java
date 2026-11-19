/*==================================================================================================
                               Copyright 2026 Siemens
====================================================================================================

    NOTE:  Designcenter Development provides programming examples for illustration only.
    Designcenter Development assumes you are familiar with the programming language
    demonstrated in these examples, and the tools used to create and debug NXOpen
    programs. GTAC support professionals can help explain the functionality of
    a particular procedure, but neither GTAC nor Designcenter Development will modify
    these examples to provide added functionality or construction procedures.

File description:

    A Java class that implements an example of the BOM Calculator for Assembly Listing.


==================================================================================================*/

package nxopen.examples.assemblies;

import java.rmi.RemoteException;
import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

import nxopen.NXException;
import nxopen.assemblies.Component;

/**
 * @author pesumner
 * An implementation of IComponentFunctor that creates a BOM for the assembly
 */
public class BOMCalculator implements IComponentFunctor {

    private Map<String, BOMPair> bomMap;
    
    public BOMCalculator() {
        bomMap = new HashMap<String, BOMPair>();
    }
    
    public void execute(Component c) {
        try {
            String name = c.name();
            int count = 0;
            if (bomMap.containsKey(name)) {
                BOMPair bomEntry = (BOMPair) bomMap.get(name);
                bomEntry.incrementCount();
            }
            else {
                count = 1;
                BOMPair bomEntry = new BOMPair(c, count);
                bomMap.put(name, bomEntry);
            }
        } catch (NXException nxEx) {
            nxEx.printStackTrace();
        } catch (RemoteException ex) {
            ex.printStackTrace();
        }
    }

    public Collection getBOMTable() {
        return bomMap.values();
    }
}
