# Natural Language Translation Example using Google Service

In order to get started using google translate there are steps for
setup.


### How to get started using this api.

Navigate to the link

* <https://cloud.google.com>

![](images/g1.png)

This is the homepage for Google cloud. Will need to activate your
console with a Google account and billing.

Google offers a free trial of up to $300 of language translation to
test. After activation of account, you will want to click console in
the top right.

![](images/g2.png)

Here is the console for all google projects.  The next step is to make
a new project by selecting the dropdown at the top left.

The project creation page will look like this:

![](images/g3.png)

Then, click create new project.

![](images/g4.png)

Give your project a title.

The dashboard will automatically update to use your new project, If
not, select your project at the top left.

From here we need to activate the api for language translation.
Select the api tab in the sidebar to the left.

![](images/g5.png)


From here you can click the enable apis and services tab at the top

![](images/g6.png)


Scroll down to machine learning. Here you will see a cloud translation
api.  Click the api and enable it.

![](images/g7.png)


![](images/g8.png)

The api is now enabled, and you will see it on your dashboard.

For each project you will have to enable credentials. this is a vital
part to the continuation of the project.

on the tab to the left you will see credentials. here we are going to
click create service account.

![](images/g9.png)

The next step is to title your service account.
You will proceed and click the role owner. 

this step is to decide what role each user has in the terms of the
project. owners typically have access to most resources so we are
going to select that one.


![](images/g10.png)

After the creation of the service account you will be prompted to
download the json private key.


![](images/g11.png)

This private key will be placed in your Downloads folder.  it is a
very important piece of information. When creating this private key
make sure to download as a json format.

In the command line you must create a virtual enviroment for the
location of this project

```bash
$ python3.10 -m venv ~/ENV3
$ source ~/ENV3/bin/activate
```

You will need to give this private key a GOOGLE_CREDENTIALS_PATH. This is a very important step.

```bash
$ export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"
```

Example:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/service-account-file.json"
```

In order to use the client library for Natural language translation
you will need to install some packages


```
pip install google-cloud-translate==2.0.1
```

or
```
pip install -r requirments.txt
```


From here you should have a linked api-key with a service account, and
will be ready to use some examples of natural language programming.


An example for a small natural language program is showcased in
[snippets.py](../snippets.py).


Documentation for getting started in the command line can be found in
[CLI Start](README-cli.md).



