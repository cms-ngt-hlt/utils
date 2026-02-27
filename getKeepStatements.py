#! /usr/bin/env python3

import argparse

def get_read_branch_names(xml_path):
    """
    Open a framework job report XML file and return a list of keep statements
    with all the collections that have been read from the input files.

    If the ReadBranches element looks like

        <ReadBranches>
        <Branch Name="FEDRawDataCollection_rawDataCollector__LHC." ReadCount="2926"/>
        </ReadBranches>

    this function would return [ 'keep FEDRawDataCollection_rawDataCollector__LHC' ].
    """
    import xml.etree.ElementTree as ET

    tree = ET.parse(xml_path)
    root = tree.getroot()

    read_branches = root.find("ReadBranches")
    if read_branches is None:
        return []

    branch_names = []
    for branch in read_branches.findall("Branch"):
        name = branch.get("Name")
        if name:
            branch_names.append(name.rstrip("."))  # remove trailing dot(s)

    return branch_names


if __name__ == "__main__":
    # read xml path from command line argument
    parser = argparse.ArgumentParser(description='Get keep statements from a framework job report XML file.')
    parser.add_argument('--xml', default="jobReport.xml", help='Path to the framework job report XML file')
    args = parser.parse_args()

    branches = get_read_branch_names(args.xml)
    keep_statements = [f"\'keep {branch}\'," for branch in branches]
    # Remove the last character
    if keep_statements:
        keep_statements[-1] = keep_statements[-1].rstrip(',')
    print('\n'.join(keep_statements))
