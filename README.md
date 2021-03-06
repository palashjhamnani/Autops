# Autops

<br>

Autops is a Python/Django web application that helps automate IT infrastructure operations for teams.

<h3>Why the name Autops?</h3>

It is simply to signify <b>Automation</b> of <b>Operations</b> required by IT infrastructure teams. 

<h3>Project Background</h3>

This project was started by me in 2015 as a personal side project in an attempt to learn full stack web development through Django and combine a set of python scripts into a web app that IT operation teams could use to accomplish repetitive release management and sys admin tasks remotely, without logging in to Windows and Linux servers. Functionality can be easily extended if required since the design is object oriented. Bootstrap has been used to keep it compatible with mobile browsers, so the support teams can resolve issues without access to laptops (provided they have VPN on phone). 

Technology Stack:

<ul>
  <li>Python</li>
  <li>Django</li>
  <li>Bootstrap</li>
  <li>Ajax</li>
  <li>WMI</li>
  <li>SQLite</li>
</ul>

Below are some of the screenshots from a running instance of Autops.

<br>

The initial Login/Registration page. 

<br>

![](https://raw.githubusercontent.com/palashjhamnani/Autops/master/autops/about/Picture6.png)

<br>

The profile page, where personal information can be updated.

<br>

![](https://raw.githubusercontent.com/palashjhamnani/Autops/master/autops/about/Picture1.png)

<br>

A sample page for a windows server, where multiple services can be added to be controlled. Apart from usual service control, reboot, etc, other services can be added through WMI API (<a href="https://docs.microsoft.com/en-us/windows/win32/wmisdk/about-wmi">Windows Management Instrumentation</a>) and Autops can be extended. Load balancing of that particular server can be managed as well, if the load balancer API is available (In case of Radware it is).

<br>

![](https://raw.githubusercontent.com/palashjhamnani/Autops/master/autops/about/Picture3.png)

<br>

A sample page for a Linux server, where multiple tasks can be added as blocks of scripts to be executed on remote machines. Paramiko is being used internally to execute these commands.

<br>

![](https://raw.githubusercontent.com/palashjhamnani/Autops/master/autops/about/Picture5.png)

<br>
<br>

This is a simple application, written with a purpose to learn full stack web development using Python and Django.
