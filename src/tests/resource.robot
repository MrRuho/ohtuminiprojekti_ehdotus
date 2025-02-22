*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Input Add New File For Test Citations
    Input  4
    Input  Testfile

Input Add Book Citation Command
    Input  1

Input Add Article Citation Command
    Input  2

Input Add Inproceedings Citation Command
    Input  3

Input Create New BibTex File Command
    Input  4

Input Book Reference
    [Arguments]  ${title}  ${author}  ${year}  ${publisher}  ${address}
    Input  ${title}
    Input  ${author}
    Input  ${year}
    Input  ${publisher}
    Input  ${address}

Input Article Reference
    [Arguments]  ${title}  ${author}  ${year}  ${journal}  ${volume}  ${pages}
    Input  ${title}
    Input  ${author}
    Input  ${year}
    Input  ${journal}
    Input  ${volume}
    Input  ${pages}
    Run Application

Input Inproceedings Reference
    [Arguments]  ${title}  ${author}  ${year}  ${booktitle}
    Input  ${title}
    Input  ${author}
    Input  ${year}
    Input  ${booktitle}
    Run Application

Input New BibTex Filename
    [Arguments]  ${filename}
    Input  ${filename}

Input Summarize Written Citations Command
    Input  5