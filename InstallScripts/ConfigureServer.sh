#this is the script for the server
sudo apt-get install zip unzip #donwload unzipper
sudo apt update
sudo apt-get install python3.6 #install python 3.6
sudo apt-get -y install python3-pip #install python3-pip
sudo pip3 install Flask #install flask 
sudo pip3 install pandas
sudo pip3 install Pillow
sudo pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu --no-cache-dir #install torch

#run the flask app
cd ..
python3 flask_app.py


