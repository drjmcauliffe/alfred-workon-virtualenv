# alfred-workon-virtualenv
Workflow to list and start python virtualenvs (assumes you and have virtualenv and virtualenvwrapper installed). 

* Type 'ven' to see a list of python virtualenvs (located by default under ~/.virtualenvs) 
* Select one and action it to have it activate in a new terminal or tab
* If you know the virtualenv you want just start typing the name after a space after the 'ven'
* Modifiers (for now I'm using and assuming use of .zsh - I'll make this more generic sometime soon) :
  * alt : open the project code folder (assumes PROJECT_HOME set)
  * ctrl : open the virtualenv folder where python and packages are installed
  * shift : show installed packages for selected virtualenv and copies them to the clipboard (assumes WORKON_HOME is set as is usual with virtualenvwrapper)
  * cmd : copy installed packages for selected virtualenv to the clipboard.

And that's it for now.
