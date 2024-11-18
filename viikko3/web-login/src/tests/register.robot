*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  testi
    Set Password  asd123123
    Set Password Confirmation  asd123123
    Submit Registration
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Set Username  te
    Set Password  asd123123
    Set Password Confirmation  asd123123
    Submit Registration
    Registration Should Fail With Message  Invalid username

Register With Valid Username And Too Short Password
    Set Username  testi
    Set Password  asd1
    Set Password Confirmation  asd1
    Submit Registration
    Registration Should Fail With Message  Invalid password

Register With Valid Username And Invalid Password
    Set Username  testi
    Set Password  asdasdasd
    Set Password Confirmation  asdasdasd
    Submit Registration
    Registration Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  testi
    Set Password  asd123123
    Set Password Confirmation  asd12312
    Submit Registration
    Registration Should Fail With Message  Passwords do not match

Register With Username That Is Already In Use
    Set Username  ville
    Set Password  asd123123
    Set Password Confirmation  asd123123
    Submit Registration
    Registration Should Fail With Message  User with username ville already exists

Login After Successful Registration
    Set Username  testi
    Set Password  asd123123
    Set Password Confirmation  asd123123
    Submit Registration
    Click Link  Continue to main page
    Click Button  Logout
    Set Username  testi
    Set Password  asd123123
    Click Button  Login
    Main Page Should Be Open

Login After Failed Registration
    Set Username  t
    Set Password  asd123123
    Set Password Confirmation  asd123123
    Submit Registration
    Click Link  Login
    Set Username  t
    Set Password  asd123123
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Reset Application Create User And Go To Register Page
  Reset Application
  Create User  ville  asdasd123
  Go To Register Page

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Registration
    Click Button  Register

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}
