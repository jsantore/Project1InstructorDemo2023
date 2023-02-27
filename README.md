# Project1InstructorDemo2023
This is a demo of the Comp490/Comp530 project 

It is current as of sprint 3 for the undergraduates and Graduate Students

This solution works on my form:
https://jsantore.wufoo.com/forms/cubes-project-proposal-submission/

To run the project, run main.py

This will give you a command line choice to update the data or run the GUI

If you update the data it will hit the wufoo form and use your API key

you need your secrets.py to be in the form
wufoo_key = 'YoUr-KeY-pUt-hErE'

Currently, I am using the Grad approach of running the GUI from a server
If I was running the server from a free linode/heroku/digital ocean, 
I would have put the DisplayWufooWindow.data_url into secrets as well

For undergrads, follow the comment in DisplayWufooWindow.get_data and 
replace the contents of that function with the code from
cubes-api.get_data() instead.


To run the server run
-  uvicorn cubes-api:app --reload



