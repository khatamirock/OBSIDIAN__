

## 🔄 Lifecycle Commands

- **`docker run`**  
    Creates and starts a ==new container== from an image. You can also pass commands to run inside it.  
    _Example:_ 
```docker
docker build -t my_flsk-app:v1 .
// building with that name instead preevuild ones (like nginx or busybox or airflw)
```

``` cmd
docker run --name myapp nginx
docker run --name test busybox echo "hello"
docker run -d -p 5000:5000 --name flask_web my_flsk-app:v1
```

- **`docker start`**  
    Starts an ==existing (stopped) container==.  
    _Example:_ `docker start myapp`
    
- **`docker stop`**  
    Gracefully stops a running container (sends SIGTERM, then SIGKILL if needed).  
    _Example:_ `docker stop myapp`
    
- **`docker restart`**  
    Stops and then starts a container again. Useful for applying changes.  
    _Example:_ `docker restart myapp`
    
- **`docker kill`**  
    Immediately stops a container by sending SIGKILL (forceful termination).  
    _Example:_ `docker kill myapp`
    

---

## 👀 Viewing Processes

- **`docker ps`**  
    Lists only **running containers**.
    
- **`docker ps -a`**  
    Lists **all containers** (running, stopped, exited, created).
    

---

## 🧹 Cleanup Commands

- **`docker rm <container>`**
    Removes a container (==must be stopped== first unless you add `-f`).  
    _Example:_ `docker rm myapp`

- **`docker rmi <image>`**  
    Removes an image (only if no containers are using it).  
    _Example:_ `docker rmi nginx`

- **`docker system prune`**  
    Cleans up unused containers, networks, images, and optionally volumes.  
    _Example:_ `docker system prune -a`


---

## ⚙️ Crucial Flags

- **`-d` (Detached mode)**  
    Runs the container in the background.  
    _Example:_ `docker run -d nginx`
    
- **`-p` (Port mapping)**  
    Maps host ports to container ports. Format: `HostPort:ContainerPort`.  
    _Example:_ `docker run -p 8080:80 nginx`
    
- **`--name` (Naming containers)**  
    Assigns a custom name to the container.  
    _Example:_ `docker run --name webserver nginx`
    
- **`-it` (Interactive terminal)**  
    Combines `-i` (keep STDIN open) and `-t` (allocate a terminal).  
    Useful for shells inside containers.  
    _Example:_ `docker run -it ubuntu bash`
    

---

✅ With these commands and flags, you can handle the **full lifecycle** of containers: create, run, inspect, stop, clean up, and interact with them.

Would you like me to also create a **visual cheat sheet table** that organizes these commands and flags side by side for quick reference?