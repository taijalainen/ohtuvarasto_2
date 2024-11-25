*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User    jottainkin    98998kiiu

*** Test Cases ***
Register With Valid Username And Password
    Input New Command And Create User    huhheliiini    veteleekoiraakuonoon6
    Create User    huhheliini    veteleekoiraakuonoon6
    Output Should Contain    New user registered

Register With Already Taken Username And Valid Password
    [Documentation]    Yritetään luoda käyttäjä, jonka nimi on jo olemassa.
    Input New Command And Create User     kyllikkhirvi    kyllikinoma78
    Input New Command And Create User     kyllikkhirvi    kyllikinoma78
    Output Should Contain    UserError: Username already exists! 
    


Register With Too Short Username And Valid Password
    Input New Command And Create User     aa    validpassword123
    Output Should Contain    Username must be at least 3 characters and contain only letters a-z
 
Register With Enough Long But Invalid Username And Valid Password
    Input New Command And Create User     invalid!username    validpassword123
    Output Should Contain    Username must be at least 3 characters and contain only letters a-z

Register With Valid Username And Too Short Password
    Input New Command And Create User     validuser    short
    Output Should Contain    Password must include characters other than letters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command And Create User     validuserion    StrongPassword
    Output Should Contain    New user registered

*** Keywords ***

Input New Command And Create User
    [Arguments]    ${username}    ${password}
    Input New Command
    Input Credentials    ${username}    ${password}
    #Create User    ${username}    ${password}
