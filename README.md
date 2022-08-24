# ml_project_scratch

Create github repository and clone it. Copy repo link and run

```
git clone <repo link>
```

```
conda create -p venv python==3.7 -y
```

```
conda activate venv/
```

Create requirements.txt file and write module name
```
pip install -r requirements.txt
```
```
git add .
```
```
git status
```
```
git commit -m "message"
```
```
git push origin main
```
To check origin variable
```
git remote -v
```

For ci cd with heroku we need:
Heroku email
Heroku api key -> settings -> api key
Heroku app name

Build docker image
```
docker build -t <image_name>:<tagname> . 
```

To list docker images
```
docker images
```
```
docker run -p 5000:5000 -e PORT=5000 <image_id>
```
Check running container
```
docker ps
```
Stop Docker Image:
```
docker stop <container_id>

Create folder structure .github\workflows\main.yaml


====================================================================

1. Create Housing Folder and create __init__.py file
Create setup.py file
-e . will install all local libraries which we will create inside housing folder
add -e . at last inside requirements.txt file . setup.py is mandatory for -e .

2. Inside housing folder create subfolders - component , config , entity , logger , 
exception , pipeline. Now create __init__.py inside each folder