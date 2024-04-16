# Assignment 4
A multi-user chat distributed system with utilization of Python Socket and Thread. 

## Table of Contents
- [Overall System Architecture](#overall-system-architecture)
- [Technologies Used](#technologies-used)
- [Solutions to Design Challenges](#solutions-to-design-challenges)
- [Demonstration Video](#demonstration-video)

## Overall System Architecture 
![Overall System Architecture](https://github.com/Software-Cakes/Assignment-4/assets/117486461/ce8344c2-e423-46d7-9449-5356429b870d)


## Technologies Used
To create the multi-user chat distributed system, Python3 Socket and Thread were implemented and utilized in server.py and client.py because 1) socket programming enables to connection between two distinctive nodes in the interconnected network for communication purposes while 2) thread is the execution of small, functioning program sequence independent from the primary operating system. 


## Solutions to Design Challenges
1. Heterogeneity: The developed source code utilized socket programming and thread. Both implementations enable the software to run on disparate oeprating systems within different environments because sockets enables commmunication between different interconnected nodes in the network; thus, achieving multi-user communication. Furthermore, the provided codes can be written in different languages as long as they retain the fundamental operations. 
2. Openness: The server and clients communicate via TCP sockets, reliable and secure software structures within the network node of computers when handling incoming and outbound connections. Since TCP is widely supported by various systems, it thus facilitates interoperability between different systems as long as the codes are in use. 
3. Security: While the developed source code for the given assignment has weak security, the implementation of socket.accept() serves as simple acceptance of a requested client communication connection.
4. Scalability: Built with the purpose to handle large quantity of clients communicating with one another, the presented code has considerbly good scalability. However, future iterations can further strengthen the distributed system's scalability capabilities.  
5. Failure Handling: To ensure the program, especially for the server, to handle failures, error commands were implemented to inform connected users the unavailability of certain task requests. For example, a connected user inputs a channel name that does not exist. The system will analyze the given input and determine of its existence. Finding that the provided channel name input does not exist within its dictionary, it informs him/her about the error and reasons. 
6. Transparency: The program offers transparency, albeit at a simplistic level, by simplifying the complexity of the distributed system through an intuitive user interface reminiscent of vintage multi-user chat platforms. The main menu presents a range of commands, granting users autonomy to execute various actions. For instance, John Doe can initiate a private chat with Jane Doe by typing "/private" and hitting "Enter," establishing a direct messaging channel between them. If Jane Doe needs to leave the system temporarily but wishes to resume the conversation later, both parties can coordinate their next steps. They might agree to reconvene in a new channel at a specified time. When the agreed-upon time arrives, Jane Doe creates the new communication channel, and John Doe joins it to continue their interaction.


## Demonstration Video
[link]
