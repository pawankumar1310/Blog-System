# Blog System
Blogs are a type of website. The only real difference between a blog and other types of website is that blogs are updated on a regular basis with new content,
which is displayed in reverse chronological order (new blog posts first).

# About Project
In this project, we have authors, articles, readers, comments.Author and Reader can register and changepassword itself.Author can add blog and Reader can like a blog, comment on a blog, follow their favourite author and also can view all their followed author.

## Features
 - **Feature #1** (Authors / Reader Registration)
     -  Author and Reader can register itself.
 - **Feature #2** (Authors / Reader Reset password)
     - Author and Reader can reset password.
 - **Feature #3** (Add the article)
     - Author can add the article. 
 - **Feature #4** (Read the article)
     - Guest, as well as registered reader can read the article.
 - **Feature #5** (Add a comment)
    - Reader can add upto 3 comments in a particular article.
 - **Feature #6** (Add a like)
    - Reader can like a particular article.
 - **Feature #7** (View liked articles)
    - Reader can view their liked articles.
 - **Feature #8** (Follow author)
   - Reader can follow their favorite author.
 - **Feature #9** (View followed author)
   - Reader can view all their followed author.
 - **Feature #10** (Notification on new article publish)
   - Reader can receive the notification when their followed author publishes any new article.
 - **Frontend / Template :**
      -  **Registration screen (for Author and Reader)**
         - **Author Screens :**
            - After login author can view only their published / unpublished articles.
            - Author can add new article, set the publish date and time, or simple save article as draft / 
              unpublished state.
            - Author can edit any article, it's attributes, and make article publish / unpublished.
            - Author can also open any article for reading like a normal reader.
         - **Reader Screens :**
            - After login reader can view all the published article by all authors.
            - Reader can search through and article by title or by author's name.
            - Reader can navigate to their liked article from the top nav bar.
            - Reader can navigate to their followed author from the top nav bar. (There they will see all the 
               published article by that author)
            - Reader can like any article and can add upto 3 comments in any of the article.
          - **Guest Reader Screens :**
            - Guest user can just navigate and read all the published article. They can neither like / comment on 
              any article, nor they can add any author as a favorite.
   
   - [Refer all the article attribute in this link](https://betterprogramming.pub/5-habits-of-highly-ineffective-remote-workers-a9f5f87f3118)
     
### Tech Stack
 - Python, Django,Html, CSS, Bootstrap

## Output
![Blog_sytem](https://user-images.githubusercontent.com/72221154/147220820-4c1b9d94-4ddf-41f2-88a3-f7fa23cdab5a.png)

## Acknowledgements/Prerequisites
- **Python IDE**
   - [VS Code (Visual Studio Code)](https://code.visualstudio.com/docs/?dv=win)
   - Install following extensions : -
       - Python
       - Code runer
- [Download Python and Install](https://www.python.org/downloads/)
- python.exe path must be set in 'path' environment variable
- For more details link are given below:-
  - [How to download Python and Pycharm](https://www.youtube.com/watch?v=mbryl4MZJms&ab_channel=Telusko)
  - [Download Pycharm](https://www.jetbrains.com/pycharm/download/#section=windows)


### Some Basic Commands ###
- To check python latest version: `` python --version ``
- To check pip: `` pip --version `` 
- To check all packages in your system: `` pip freeze ``
- To check Django install in your sytem or not,type: `` django-admin --version ``
- To install requirements.txt file, type : ``pip install -r requirements.txt``
- [How to protect your Django secret key using the .env file](https://www.youtube.com/watch?v=myqfTX9ZbTs&ab_channel=CodeBand)
     - [How to protect your Django secret key using the .env file official website](https://pypi.org/project/python-decouple/)

### Initial setup to build Django Project ###
- First we need to create a virtual environment.Using a virtual environment avoids installing Django into a global python environment and we will have exact control over the libraries used in an application.
    - **Step-1:-** Create a project folder on file system like 'Project-django' and open inside VS code.
    - **Step-2:-** Install django in Separate environment.
- We can create virtual environment two ways.
- **First way (Open CMD or Terminal)**
    1. Install virtual environment wrapper :  `` pip install virtualenvwrapper-win ``
    2. Create a new virtual environment : `` mkvirtualenv Env_Name `` Example : ``mkvirtualenv blog_env``
    3. To activate virtual environment : `` workon Env_Name `` Example : ``workon blog_env``
    4. Install Django : `` pip install django ``
    - [How to setup virtual environment for Django project](https://www.youtube.com/watch?v=F_xWv0Q_dLE&ab_channel=GeekyShows)
    - Using this, virtual environment is install in your default working directory(C Drive).In **Envs** folder virtual environment(Env_Name) is present.
    - **Note : -** In terminal virtual environment not seen.In CMD virtual environment see after activate it.To deactivate virtual environment simply type `` deactivate`` and to delete virtual environement ,type ``rmvirtualenv Env_Name`` and Uninstall django,type ``pip uninstall django``
    
 - **Another way to create virtual environment (Open terminal or CMD)**
    1. Create a new virtual environment: `` python -m venv Env_Name ``
    2. To activate virtual environment: `` Env_Name\Scripts\activate.bat`` But on Unix or MacOS: ``source Env_Name/bin/activate`` 
    3. Install Django : `` pip install django ``
      - [How to setup virtual environment for Django project](https://www.youtube.com/watch?v=APOPm01BVrk&ab_channel=CoreySchafer)
      - Using this way, virtual environment is install in your current directory.
      - **Note : -** In terminal virtual environment not seen.In CMD virtual environment see after activate it.To deactivate virtual environment simply type `` deactivate`` and to delete virtual environement ,type ``rmdir Env_Name /s`` and Uninstall django,type ``pip uninstall django``

### After Initial setup ###
 1. Activate virtual environment : `` workon Env_Name``
 2. Create Django Project : `` django-admin startproject PROJECT_NAME``
 3. Create Django Application : `` python manage.py startapp APPLICATION_NAME ``
 4. Install your application in ``settings.py `` file.
 5. Run the sever : `` python manage.py runserver ``
 6. Open website in browser at ``http://localhost:8000`` or admin at ``http://localhost:8000/admin``
 7. Quit the server : ``ctrl+c``
 - Whenever you edit your model fields (adding a new one, changing an existing one or altering any of the arguments it takes) then you should always run migrations.
 ``python manage.py makemigrations <app>`` : Create the migrations (generate the SQL commands).
 - ``python manage.py migrate`` : Run the migrations (execute the SQL commands).
 - To create super user, type : ``python manage.py createsuperuser``



