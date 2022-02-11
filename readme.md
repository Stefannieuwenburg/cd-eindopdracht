#### CD Project ####

### Logging in to cloud.digitalocean.com ###
i have managed to create a Droplet on the cloud server after do some online video info explain how to make it ant how to do your key code up ant running for safe log in to the system whit bash terminal ssh root@0.0.0.0.0

I’ve managed to create a continuous development pipeline through the use of a VPS (droplet @ digitalocean), nginx, python, flask and gunicorn. 
A commit made in this repository will execute a series of commands through the SSH connection I’ve configured in github. I have another SSH link, specifically made for without the use of Github - for me to check if all steps in the workflow have been done correctly.
While building the pipeline I’ve encountered numeral issues, so I narrowed down the top three issues I faced:

### Gunicorn ######
Gunicorn was my biggest hurdle in the whole process. Even after successfully running the flask application on the VPS, gunicorn refused to identify the application. 
The solution was to learn to ‘read more ant dive in to it’. 

### SSH connection ######
Creating a valid SSH connection between github and the VPS served a lot more complications than i whas thinking befor. 

### Nginx / app.service #####
In the linux terminal the format of an error is less descriptive than I would have hoped for. 
A simple error code gave me hours of headaches, as I couldn’t figure out yet that error-200 simply meant that I had misspelled a directory somewhere. Through the use of ‘jounalctl -xe’. ‘systemctl status app.service’ and google, I got the answers to those errors.

Stefan Nieuwenburg
