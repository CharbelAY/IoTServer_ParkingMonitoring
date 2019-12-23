# IoTServer_ParkingMonitoring

CAN BE ACCESSED ON localhost:8000


docker images to list all images
docker container ls -a to list all containers
docker rm container_id to remove the container then you can remove the images 
docker rmi image_id to remove image


-u is used in the CMD docker file so that the print functions are not stored in a buffer and released at the end when closing the server. Instead each time print is called the console will get the printed data

host is 0.0.0.0
Port forwarding can only connect to a single destination—but you can change where the server process is listening. You do this by listening on 0.0.0.0, which means “listen on all interfaces”
check https://pythonspeed.com/articles/docker-connection-refused/

To build image docker build -t parking-monitor .

To run the container with port mapping docker run -p 8000:8000 parking-monitor 

