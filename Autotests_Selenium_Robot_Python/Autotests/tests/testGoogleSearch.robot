*** Settings ***
Library  Selenium2Library
Suite Setup     Open Browser    ${URL}   ${BROWSER}
Suite Teardown  Close All Browsers

*** Variables ***
${URL}              https://www.google.com/
${BROWSER}          Chrome
${search_form}      xpath=//form[@action='/search']
${search_input}     xpath=//input[@name='q']
${search_value}     GeForce1650
${search_result}    xpath=//a[@href="https://www.nvidia.com/ru-ru/geforce/graphics-cards/gtx-1650/"]

*** Test Cases ***
Google Search
    Wait Until Element Is Visible  ${search_form}
    Wait Until Element Is Visible  ${search_input}
    Input Text      ${search_input}   ${EMPTY}
    Input Text      ${search_input}   ${search_value}
    Submit Form
    Wait Until Element Is Visible   ${search_result}
    Element Should Be Visible   ${search_result}