# Mission to Mars

![mission_to_mars](D:/RICE_CAMP_DATA/RICEHOU201906DATA1/HW/12-Web-Scraping-and-Document-Databases/Images/mission_to_mars.png)

 

## Method of Approach

The first step in a project like this is to organize it.  This is called setting up an interface, defining what needs to done in order to finish the task.  Although there is not a formal way to do that using what I know now with Python, the idea is still useful.  So what I have done here, is read over the instructions and broken it down so that I set up a blank project with all of the components I will need to fill in.   I am conceptually thinking in terms of view, view-model and model  (MVVM) for this type of project.  What this means is that I can separate work on each of the major components of the project, so they are not dependent upon one another, although they will be linked together.  I can set up the final output , the 'view' component, so that all I need do is fill in the blanks later once I have finished the' view-model' component, aka business logic.  The 'model' is MongoDB in this case, and that is how the data will be stored. (The view-model links the view to the model more or less)

My approach to this is to define, via VS Code all of the components, including this README, as a git project, HW12 and then start working on each component.  I will work on the things that I know best, first, getting them out of the way, and work my way through the list.  I will use Jupyter to test and play with the necessary python code and then incorporate what is needed into VS Code.

The following shows  how this MVVM pattern works.

### MondgoDB  (The Model)

First, I note of all the expected returns from the scraping and created a Mongo DB, and a Mongo collection called Mdata with all the expected values.  I tested with bogus data to make sure that the various functions  worked.

### View Logic  (The View)



#### FLASK App.py

#### index.html

### SCRAPING LOGIC  (The View-Model) ###

This is the View-Model phase.  In this part I set up the business logic necessary to scrape each of the required web pages.  I expect this to take the most amount of time because it is what I am least familiar with, and that is why I reserve it for last.

For this, I use *Jupyter Lab* to test all my code.  I also test the MongoDB code in Jupyter.  I find it useful to use Jupyter for code testing, and then integrating whatever production code I want to use into VS Code.  

### BRINGING IT ALL TOGETHER 

## CONCLUSION ##

![](C:\Users\kevin\Desktop\HW12\static\MarsNewsCaster.jpeg)



This approach was quite useful on this project.  It helped me to keep all of the the different tasks fairly well organized so that I was not confused with competing needs in order to complete the task.  

This assignment ranks an 'A' in terms of bringing different skills together to accomplish a real-world kind of task.



