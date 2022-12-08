# Image Classification

## GENI configuration and any public link: 
- Name of GENI slice: projectgvsf
- Rspec file: https://github.com/dscrivener/655-proj/blob/main/proj.xml
- Web interface: http://pcvm2-9.instageni.cenic.net:8000/
- Video demo: Need to add this.

## Reproduction 
The reproduction instructions below deploys the server and puts the model on 3 workers. This was the setup we used in our experimentation.
 - Use the RSPEC file to reserve the GENI resources.
 - SSH into the server and do the following:
    - Obtain the repository
    ```bash 
    wget https://github.com/dscrivener/655-proj/archive/refs/heads/main.zip
    ```
    - Unzip the codebase 
    ```bash 
    unzip main.zip
    ```
    If unzip is uninstalled, please run: 
    ```bash 
    sudo apt-get install unzip
    ```
    - Go to the project folder
    ```bash 
    cd 655-proj-main/
    ```

    - **At the file flask_app.py, change the server and the workers IP. For the server, the GENI should show the public available IP. For the workers, you can find them using ifconfig at each worker**

    - **At the file server.conf, change the directory entry (second line) to your current directory (655-proj-main directory). You can get your directory using the command pwd.**

    - Run the server shell script
    ```bash 
    sudo bash InstallScripts/ConfigureServer.sh
    ```

    - You can verify if the server is running using the following command:

    ```bash
    supervisorctl status
    ```

- SSH into workers 1, 2 and 3. Run the commands below on each worker.

- Obtain the repository
    ```bash 
    wget https://github.com/dscrivener/655-proj/archive/refs/heads/main.zip
    ```
    - Unzip the codebase 
    ```bash 
    unzip main.zip
    ```
    If unzip is uninstalled, please run: 
    ```bash 
    sudo apt-get install unzip
    ```

    - Go to the project folder
    ```bash 
    cd 655-proj-main/
    ```

    - **At the file worker_img.py, change the worker IP to the IP that your current worker IP. You can find this information using ifconfig.**

    - **At the file worker.conf, change the directory entry (second line) to your current directory (655-proj-main directory). You can get your directory using the command pwd.**

    - Run the server shell script
    ```bash 
    sudo bash InstallScripts/ConfigureWorker.sh
    ```

    - You can verify if the server is running using the following command:

    ```bash
    supervisorctl status
    ```

## Team members
- Abhinit Sati
- Gabriel Franco 
- Daniel Scrivener 
- Rahul Mitra