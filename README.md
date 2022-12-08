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
    - Run the server shell script
    ```bash 
    sudo bash 655-proj-main/InstallScripts/ConfigureServer.sh
    ```

- SSH into workers 2, 3 and 5. Run the commands below on each worker. 
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
    - Run the worker shell script
    ```bash 
    sudo bash 655-proj-main/InstallScripts/ConfigureWorker.sh
    ```


## Team members
- Abhinit Sati
- Gabriel Franco 
- Daniel Scrivener 
- Rahul Mitra