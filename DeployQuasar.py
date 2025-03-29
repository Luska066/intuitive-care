import os
import subprocess
from time import sleep

subprocess.run([""], cwd=os.getcwd(), check=True)

install_command = [
    "curl", "-o-",
    "https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh",
    "|", "bash"
]

directory = os.getcwd()+"/intuitive-front"
subprocess.run(install_command, cwd=directory, check=True, shell=True)
subprocess.run("nvm install 22", cwd=directory, check=True, shell=True)
subprocess.run("nvm use 22", cwd=directory, check=True, shell=True)
subprocess.run("npm run build", cwd=directory, check=True, shell=True)
subprocess.run("apt-get install http-server", cwd=directory, check=True, shell=True)
subprocess.run("npm install pm2 -g", cwd=directory, check=True, shell=True)
subprocess.run("cd intuitive-front/", cwd=directory, check=True, shell=True)
subprocess.run("http-server -p 8080", cwd=directory, check=True, shell=True)
subprocess.run("pm2 start http-server --name quasar-app -- -p 8080", cwd=directory, check=True, shell=True)




