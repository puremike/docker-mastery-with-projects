print("    ____        _   _                  _    ")
print("   |  _ \\ _   _| |_| |__   ___  _ __  / \\   ")
print("   | |_) | | | | __| '_ \\ / _ \\| '_ \\/  /   ")
print("   |  __/| |_| | |_| | | | (_) | | | /\\_/    ")
print("   |_|    \\__, |\\__|_| |_|\\___/|_| |_(_)    ")
print("          |___/                             ")
print("                                            ")
print("             -- Python --                   ")


# Developer: Hey there, Captain DevOps! To run this application without Docker, simply execute:
#            python python-app.py
#            I trust that you can take it from here and work your container magic. Smooth sailing!


# With Docker (Running the application inside docker containers):
# docker run -v "C:\Users\ADMIN\Desktop\docker-course\lesson-starter-projects\01-starter-code:/app/" --name my-py-run python:latest python /app/python-app.py
# OR
# docker run --rm -v "C:\Users\ADMIN\Desktop\docker-course\lesson-starter-projects\01-starter-code:/app/" --name my-py-run python:latest python /app/python-app.py - will remove the container after it has run it