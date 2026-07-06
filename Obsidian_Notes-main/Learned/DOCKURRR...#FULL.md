# Docker Commands Guide: Stages 1-5

## Complete Reference with Explanations & Common Confusions Clarified

---

## **STAGE 1: Installation & First Steps**

### Installation Verification

```bash
# Check Docker version and verify installation
docker version
# Shows client and server (daemon) versions

# Get detailed system information
docker info
# Shows containers, images, storage driver, etc.

# Test Docker installation with a minimal container
docker run hello-world
# Downloads hello-world image (if not present) and runs it
# This validates: image pull → container creation → execution → exit
```

---

## **STAGE 2: Core Container Management**

### 🔴 **CONFUSION ALERT: `docker run` vs `docker start`**

**The Key Difference:**

- `docker run` = **CREATE** a new container from an image + START it
- `docker start` = **START** an existing (stopped) container

```bash
# SCENARIO 1: First time running
docker run nginx
# Creates NEW container from nginx image AND starts it

# SCENARIO 2: Container already exists but is stopped
docker start my-container
# Just starts the existing container (no new container created)
```

**Think of it like this:**

- `docker run` = Buying a new car and driving it
- `docker start` = Starting a car you already own

---

### Running Containers

```bash
# Basic run (foreground, blocks terminal)
docker run nginx
# Container runs in foreground, you see logs, can't use terminal

# Detached mode (background) - MOST COMMON
docker run -d nginx
# -d = detached (runs in background)
# Returns container ID, terminal is free
# Container keeps running even if you close terminal

# With port mapping - CRUCIAL FOR WEB APPS
docker run -d -p 8080:80 nginx
# -p HOST_PORT:CONTAINER_PORT
# Maps port 8080 on your machine to port 80 inside container
# Access via localhost:8080 in browser

# With custom name (easier to reference)
docker run -d -p 8080:80 --name my-web nginx
# --name = give it a memorable name instead of random ID
# Now you can use 'my-web' in other commands

# Interactive mode (for exploring)
docker run -it my-web bash
# -i = interactive (keep STDIN open)
# -t = allocate pseudo-TTY (terminal)
# Together = you get a shell inside the container
# Use this for: testing, debugging, running CLI apps

# Combining flags - REAL WORLD EXAMPLE
docker run -d -p 3000:3000 --name my-app -e NODE_ENV=production my-node-app
# -d = background
# -p = port mapping
# --name = custom name
# -e = environment variable
```

### 🔴 **CONFUSION ALERT: Port Mapping**

```bash
# Format: -p HOST:CONTAINER
docker run -p 8080:80 nginx

# HOST PORT (8080) = What you type in browser (localhost:8080)
# CONTAINER PORT (80) = Where app listens INSIDE container

# Common mistake:
docker run -p 80:8080 nginx  # WRONG if nginx listens on 80
# This maps host 80 → container 8080, but nginx uses port 80!

# Correct:
docker run -p 8080:80 nginx  # RIGHT
# Browser: localhost:8080 → nginx on container port 80
```

---

### Viewing Containers

```bash
# List RUNNING containers only
docker ps
# Shows: CONTAINER ID, IMAGE, STATUS, PORTS, NAMES

# List ALL containers (running + stopped)
docker ps -a
# -a = all (includes exited/stopped containers)
# This is crucial for finding containers you've stopped

# Filter by status
docker ps -a --filter "status=exited"
# Shows only stopped containers
```

### 🔴 **CONFUSION ALERT: Why don't I see my container?**

```bash
# You ran:
docker run ubuntu
# Container starts and IMMEDIATELY exits (no process to keep it alive)

# To see it:
docker ps -a
# It's there, but STATUS = Exited

# Why? Ubuntu image has no long-running process
# Fix: Give it a command
docker run -d ubuntu sleep infinity
# Now it runs forever (or until you stop it)
```

---

### Container Lifecycle Management

```bash
# STOP a running container (graceful shutdown)
docker stop my-web
# Sends SIGTERM (allows 10 sec for cleanup)
# Then sends SIGKILL if still running
# Container still exists, just stopped

# START a stopped container
docker start my-web
# Restarts the same container (same ID, same data)

# RESTART a container
docker restart my-web
# Equivalent to: stop + start

# KILL a container (force stop, immediate)
docker kill my-web
# Sends SIGKILL immediately (no graceful shutdown)
# Use when 'stop' doesn't work
```

### 🔴 **CONFUSION ALERT: `stop` vs `kill` vs `rm`**

```bash
# STOP = pause the container (can restart later)
docker stop my-web
# Container status: Exited
# Data inside: PRESERVED
# Can restart: YES

# KILL = force stop immediately
docker kill my-web
# Same as stop but no grace period
# Use for frozen containers

# RM = DELETE the container permanently
docker rm my-web
# Container status: GONE
# Data inside: LOST (unless using volumes)
# Can restart: NO (it doesn't exist anymore)

# Common workflow:
docker stop my-web   # Stop it
docker rm my-web     # Delete it
# Or in one command:
docker rm -f my-web  # Force remove (stops + deletes)
```

---

### Interacting with Running Containers

```bash
# Execute command in running container
docker exec my-web ls /usr/share/nginx/html
# Runs 'ls' command inside 'my-web' container
# Shows files then exits

# Get interactive shell (like SSH)
docker exec -it my-web bash
# -it = interactive terminal
# Now you're "inside" the container
# Type 'exit' to leave

# For Alpine-based images (no bash)
docker exec -it my-web sh
# Alpine uses 'sh' instead of 'bash'

# View container logs
docker logs my-web
# Shows stdout/stderr from container

# Follow logs in real-time
docker logs -f my-web
# -f = follow (like 'tail -f')
# Press Ctrl+C to stop following

# Show only last 100 lines
docker logs --tail 100 my-web
```

### 🔴 **CONFUSION ALERT: `docker run` vs `docker exec`**

```bash
# RUN = Create NEW container and execute command
docker run ubuntu echo "hello"
# Creates new container → runs echo → exits → container stops

# EXEC = Execute command in EXISTING running container
docker exec my-container echo "hello"
# Runs echo in already-running container
# Container keeps running after command finishes

# Common pattern:
docker run -d --name web nginx         # Start container
docker exec -it web bash               # Get shell in running container
```

---

### Cleanup

```bash
# Remove a stopped container
docker rm my-web
# Must be stopped first (or use -f flag)

# Force remove (even if running)
docker rm -f my-web
# Stops and removes in one command

# Remove an image
docker rmi nginx
# Removes the nginx image from your system
# Can't remove if containers are using it

# Remove all stopped containers
docker container prune
# Interactive confirmation required
# Frees up disk space

# Remove all unused images
docker image prune
# Removes dangling images (no tags)

# Remove unused images, containers, networks, volumes
docker system prune
# The nuclear option
# Add -a to remove ALL unused images (not just dangling)

# See disk usage
docker system df
# Shows how much space images/containers/volumes use
```

### 🔴 **CONFUSION ALERT: `prune` vs `rm`**

```bash
# RM = Remove SPECIFIC item
docker rm container_name       # Remove one container
docker rmi image_name         # Remove one image

# PRUNE = Remove ALL unused items of a type
docker container prune        # Remove ALL stopped containers
docker image prune           # Remove ALL dangling images
docker system prune          # Remove EVERYTHING unused

# Be careful with prune!
docker system prune -a --volumes
# Deletes: stopped containers, unused images, unused volumes
# Can't undo this!
```

---

## **STAGE 3: Building Images**

### Dockerfile Basics

```dockerfile
# Use a base image
FROM node:18-alpine
# FROM = starting point (usually an OS + runtime)
# alpine = lightweight version (~5MB vs ~900MB for full node)

# Set working directory inside container
WORKDIR /app
# All subsequent commands run from /app
# Creates directory if it doesn't exist

# Copy files from host to container
COPY package.json .
# COPY <source on host> <destination in container>
# '.' means current WORKDIR (/app)

# Run command during IMAGE BUILD (not container runtime)
RUN npm install
# Executes during 'docker build'
# Installs dependencies into the image
# Results are saved in image layers

# Copy application code
COPY . .
# Copies everything from build context to /app

# Document which port the app uses
EXPOSE 3000
# Does NOT publish the port (just documentation)
# You still need -p flag when running container

# Command to run when container STARTS
CMD ["node", "server.js"]
# Runs when you 'docker run' the image
# Can only have ONE CMD per Dockerfile
```

### 🔴 **CONFUSION ALERT: `RUN` vs `CMD` vs `ENTRYPOINT`**

```dockerfile
# RUN = Execute during IMAGE BUILD
RUN npm install
# Happens when you build image
# Results are baked into the image

# CMD = Default command when CONTAINER STARTS
CMD ["npm", "start"]
# Happens when you run container
# Can be overridden: docker run my-image npm test

# ENTRYPOINT = Command that ALWAYS runs
ENTRYPOINT ["node"]
CMD ["server.js"]
# Container always runs 'node'
# But you can change the argument: docker run my-image app.js
# Result: runs 'node app.js' instead of 'node server.js'

# Simple rule:
# RUN = build time
# CMD/ENTRYPOINT = runtime
```

---

### Building Images

```bash
# Build image from Dockerfile in current directory
docker build .
# '.' = build context (current directory)
# Creates unnamed image

# Build with tag (name + version)
docker build -t my-app:v1 .
# -t = tag
# Format: name:version
# 'latest' is default if no version specified

# Build with multiple tags
docker build -t my-app:v1 -t my-app:latest .
# One image, multiple names

# Specify different Dockerfile
docker build -f Dockerfile.prod -t my-app:prod .
# -f = file
# Useful when you have Dockerfile.dev, Dockerfile.prod, etc.

# Build with build arguments
docker build --build-arg NODE_ENV=production -t my-app .
# Pass variables to Dockerfile using ARG instruction

# View build history (layers)
docker history my-app
# Shows each layer, size, creation time
```

### 🔴 **CONFUSION ALERT: Build Context**

```bash
# What is the dot?
docker build -t my-app .
#                      ^ This dot!

# The dot = build context = files Docker can access
# Everything in current directory (and subdirectories)
# Gets sent to Docker daemon before build starts

# Common mistake:
cd /
docker build -t my-app .
# Tries to send YOUR ENTIRE HARD DRIVE to Docker! 

# Solution: Build from project directory
cd /path/to/project
docker build -t my-app .

# Or specify path:
docker build -t my-app /path/to/project
```

### .dockerignore File

```bash
# Create .dockerignore in project root
# Works like .gitignore

# Example .dockerignore:
node_modules
.git
.env
*.log
.DS_Store

# Why? Makes builds faster and images smaller
# node_modules can be 100MB+
# You'll RUN npm install anyway
```

---

## **STAGE 4: Volumes & Networking**

### Volumes (Data Persistence)

```bash
# Create a named volume
docker volume create my-data
# Creates managed volume (stored in Docker's area)

# List volumes
docker volume ls
# Shows all volumes

# Inspect volume
docker volume inspect my-data
# Shows mount point, driver, creation date

# Use volume with container
docker run -d -v my-data:/data postgres
# -v volume_name:container_path
# Data in /data persists even if container deleted

# Remove volume
docker volume rm my-data
# Can't remove if container is using it

# Remove unused volumes
docker volume prune
```

### 🔴 **CONFUSION ALERT: Volumes vs Bind Mounts**

```bash
# NAMED VOLUME (managed by Docker)
docker run -v my-data:/app/data my-app
# 'my-data' is a volume name
# Docker manages where it's stored
# Good for: databases, production

# BIND MOUNT (specific host path)
docker run -v /home/user/code:/app my-app
# '/home/user/code' is absolute path on host
# Maps specific folder directly
# Good for: development (live code updates)

# How to tell the difference:
# Volume: short name (my-data)
# Bind mount: starts with / or ./ (absolute/relative path)

# Development pattern:
docker run -v $(pwd):/app -p 3000:3000 my-app
# $(pwd) = current directory
# Edit code on host → changes appear in container
# Great for hot-reload during development
```

### Volume Examples

```bash
# Database with persistent data
docker run -d \
  --name postgres-db \
  -v pgdata:/var/lib/postgresql/data \
  -e POSTGRES_PASSWORD=secret \
  postgres
# Even if you delete container, data in 'pgdata' volume persists

# Development with live code reload
docker run -d \
  -v $(pwd):/app \
  -p 3000:3000 \
  --name dev-app \
  node:18-alpine \
  npm run dev
# Changes to local files immediately reflected in container
```

---

### Networking

```bash
# List networks
docker network ls
# Shows: bridge (default), host, none

# Create custom network
docker network create my-network
# Creates bridge network

# Inspect network
docker network inspect my-network
# Shows connected containers, subnet, gateway

# Run container on specific network
docker run -d --name web --network my-network nginx

# Connect running container to network
docker network connect my-network my-container

# Disconnect from network
docker network disconnect my-network my-container

# Remove network
docker network rm my-network
# Can't remove if containers are connected
```

### 🔴 **CONFUSION ALERT: Container Communication**

```bash
# WRONG WAY (doesn't work)
docker run -d --name api my-api
docker run -d --name web my-web
# These containers can't talk to each other by name

# RIGHT WAY (same network)
docker network create app-network
docker run -d --name api --network app-network my-api
docker run -d --name web --network app-network my-web
# Now 'web' can access 'api' by name: http://api:3000

# Inside web container, you can:
curl http://api:3000/users
# DNS resolution works automatically on same network

# Default bridge network vs custom network:
# Default bridge: containers can't use names, only IPs
# Custom network: containers can use names (DNS)
```

---

## **STAGE 5: Docker Compose**

### 🔴 **MAJOR CONFUSION ALERT: `up/down` vs `start/stop`**

```bash
# UP = Create + Start everything
docker compose up
# 1. Creates networks
# 2. Creates volumes
# 3. Builds images (if needed)
# 4. Creates containers
# 5. Starts containers

# DOWN = Stop + Remove everything
docker compose down
# 1. Stops containers
# 2. Removes containers
# 3. Removes networks
# Default: keeps volumes and images

# START = Start existing stopped containers
docker compose start
# Only starts containers (no creation)
# Use after 'docker compose stop'

# STOP = Stop containers (but don't remove)
docker compose stop
# Containers still exist, just stopped
# Can 'docker compose start' them later

# SUMMARY:
# up/down = full lifecycle (create/destroy)
# start/stop = just pause/resume
```

### Docker Compose Commands

```bash
# Start services (foreground)
docker compose up
# Shows logs from all services
# Blocks terminal
# Ctrl+C stops everything

# Start services (background)
docker compose up -d
# -d = detached
# Returns control to terminal
# Most common for development

# Build images before starting
docker compose up --build
# Forces rebuild even if images exist
# Use when Dockerfile changes

# Start specific service
docker compose up -d api
# Only starts 'api' service (and dependencies)

# Stop services
docker compose stop
# Graceful shutdown
# Containers still exist

# Start stopped services
docker compose start
# Resumes containers that were stopped

# Restart services
docker compose restart
# stop + start

# Stop and remove containers, networks
docker compose down
# Deletes containers and networks
# Keeps volumes and images

# Remove everything including volumes
docker compose down -v
# -v = volumes
# WARNING: Deletes database data!

# Remove everything including images
docker compose down --rmi all
# Removes all images used by services
```

### Viewing & Debugging

```bash
# View running services
docker compose ps
# Shows status of services defined in compose.yaml

# View logs
docker compose logs
# Shows logs from all services

# Follow logs in real-time
docker compose logs -f
# -f = follow (live updates)

# Logs for specific service
docker compose logs -f api
# Only shows logs from 'api' service

# Execute command in running service
docker compose exec api bash
# Opens shell in 'api' service container
# Service must be running

# Run one-off command in new container
docker compose run api npm test
# Creates NEW container, runs command, exits
# Use for: migrations, tests, scripts
```

### 🔴 **CONFUSION ALERT: `exec` vs `run`**

```bash
# EXEC = command in RUNNING service container
docker compose exec api npm test
# Service 'api' must be already running
# Uses existing container
# Fast

# RUN = command in NEW container
docker compose run api npm test
# Creates temporary container
# Runs command
# Container is removed after (unless --rm=false)
# Slower but more isolated

# When to use exec:
# - Quick debugging
# - Access running service
# - Check logs, files, processes

# When to use run:
# - Database migrations
# - One-time scripts
# - Testing without affecting running service
```

---

### Basic compose.yaml Structure

```yaml
# Version is optional in modern Compose
services:
  # Service name (you choose this)
  api:
    # Build from Dockerfile in ./api directory
    build: ./api
    # Or use image directly
    # image: node:18-alpine
    
    # Port mapping (same as -p flag)
    ports:
      - "3000:3000"  # host:container
    
    # Environment variables
    environment:
      - NODE_ENV=development
      - DB_HOST=database
    
    # Or use env file
    env_file:
      - .env
    
    # Volumes (same as -v flag)
    volumes:
      - ./api:/app        # bind mount
      - node_modules:/app/node_modules  # named volume
    
    # Depends on other services
    depends_on:
      - database
    
    # Custom network
    networks:
      - app-network
    
    # Restart policy
    restart: unless-stopped

  database:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: secret
    volumes:
      - pgdata:/var/lib/postgresql/data
    networks:
      - app-network

# Define volumes
volumes:
  pgdata:
  node_modules:

# Define networks
networks:
  app-network:
```

### 🔴 **CONFUSION ALERT: Service Names vs Container Names**

```yaml
services:
  api:  # This is the SERVICE name
    container_name: my-api-container  # This is the CONTAINER name
    image: my-api
```

```bash
# In Docker Compose commands, use SERVICE name:
docker compose logs api         # ✓ Correct
docker compose exec api bash    # ✓ Correct

# In regular Docker commands, use CONTAINER name:
docker logs my-api-container    # ✓ Correct
docker exec -it my-api-container bash  # ✓ Correct

# If no container_name specified, Docker creates one:
# Format: project-name_service-name_1
# Example: myapp_api_1

# Inside containers, use SERVICE name for DNS:
# From web service to api service:
curl http://api:3000  # ✓ Works (service name)
```

---

## **Quick Reference: Most Confusing Concepts**

### 1. Container Lifecycle Commands

```
docker run    = CREATE + START container
docker start  = START existing container
docker stop   = STOP running container
docker rm     = DELETE container
```

### 2. Docker Compose Lifecycle

```
docker compose up      = CREATE + START
docker compose down    = STOP + DELETE
docker compose start   = START existing
docker compose stop    = STOP (keep containers)
```

### 3. Port Mapping

```
-p 8080:80
   ↑    ↑
   |    └─ Container port (where app listens inside)
   └────── Host port (what you type in browser)
```

### 4. Volumes

```
-v my-data:/app/data     = Named volume (Docker managed)
-v /host/path:/app/data  = Bind mount (specific folder)
-v $(pwd):/app           = Current directory (development)
```

### 5. When Data Persists

```
docker stop   → Data preserved ✓
docker rm     → Data lost ✗ (unless using volumes)
docker down   → Data lost ✗ (unless using volumes)
docker down -v → Even volume data lost ✗
```

---

## **Common Error Solutions**

### "Port is already allocated"

```bash
# Find what's using the port
lsof -i :8080  # Mac/Linux
netstat -ano | findstr :8080  # Windows

# Use different port
docker run -p 8081:80 nginx  # Changed from 8080 to 8081
```

### "Cannot remove container, container is running"

```bash
# Stop first
docker stop my-container
docker rm my-container

# Or force remove
docker rm -f my-container
```

### "Cannot connect to Docker daemon"

```bash
# Start Docker Desktop (Mac/Windows)
# Or start Docker service (Linux)
sudo systemctl start docker
```

### "Image not found"

```bash
# Pull the image first
docker pull nginx

# Or just run (pulls automatically)
docker run nginx
```

### "Cannot remove image, image is being used"

```bash
# Remove containers using it first
docker ps -a  # Find containers
docker rm container_id

# Then remove image
docker rmi image_name
```

---

## **Development Workflow Cheat Sheet**

```bash
# 1. Start development environment
docker compose up -d

# 2. View logs
docker compose logs -f

# 3. Get shell in service
docker compose exec api bash

# 4. Run tests
docker compose exec api npm test

# 5. Restart after code changes (if needed)
docker compose restart api

# 6. Stop when done
docker compose down

# 7. Clean up everything
docker compose down -v
docker system prune -a
```

---

**Remember:** When in doubt, use `docker compose ps` to see what's running and `docker compose logs` to see what's happening!