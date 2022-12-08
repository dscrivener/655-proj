#this is the script for the server
sudo apt-get update
sudo apt-get install zip unzip #donwload unzipper
sudo apt-get install python3.6 #install python 3.6
sudo apt-get -y install python3-pip #install python3-pip
sudo -H pip3 install Flask #install flask 
sudo -H pip3 install pandas
sudo -H pip3 install Pillow
#sudo -H pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu --no-cache-dir #install torch
sudo -H pip3 install supervisor gunicorn
supervisord -c server.conf 

# #run the flask app
# cd ..
# python3 flask_app.py


