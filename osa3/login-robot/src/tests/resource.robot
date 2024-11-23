*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Input Login Command
    Input  login

Input Credentials
    [Arguments]  ${username}  ${password}
    Input  ${username}
    Input  ${password}
    Run Application

Should Raise Error
    [Arguments]    ${expected_error}
    Run Keyword And Expect Error    ${expected_error}    Input Credentials    kalle    123

    
