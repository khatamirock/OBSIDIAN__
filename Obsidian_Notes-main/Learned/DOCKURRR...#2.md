1. docker compose up/down
```
docker compose down
```
- **What it does**: It stops the containers **and then deletes them**. It also deletes the virtual network it created for your project.
- **What stays**: Your **Volumes** (your database data) and your **Images** (the built code).
- **Resume with**: 
    ```
    docker compose up
    ```
    
     (because the containers are gone, you have to "bring them up" again).
- **Analogy**: It's like **shutting down your computer and unplugging the power**. The files on your hard drive (volumes) are safe, but the "running instance" is totally gone.
1. docker compose start/stop
	- **What it does**: It tells the processes inside the containers to stop.
	- **What stays**: Everything. The container still exists, the internal IP addresses are reserved, and the network is still there.
	- **Resume with**: 
    
    ```
     docker compose start
    ```
	- ==**Analogy**: It's like **putting your laptop to sleep**. Everything is exactly where you left it when you wake it up.==
