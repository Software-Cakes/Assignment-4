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
To create the multi-user chat distributed system, Python3 Socket and Thread were implemented and utilized in server.py and client.py because socket programming enables to connection between two distinctive nodes in the interconnected network for communication purposes while thread is the execution of small, functioning program sequence independent from the primary operating system. 


## Solutions to Design Challenges
1. Heterogeneity: The developed source code utilized XML-RPC. Since it is a set of implementations that enable software running on disparate oeprating systems, running in different environments to make procedure calls over the Internet, the provided codes can be written in different languages as long as they retain the fundamental operations. 
2. Openness: The server and client based on the presented code communicate via HTTP, a standard and open protocol. Since XML-RPC protocol is widely supported by various systems, it thus facilitates interoperability between different systems as long as the codes are in use. 
3. Security: While the developed source code for the given assignment has weak security, the implementation of if-else serves as simple authentication and verification of the given inputs from the client.
4. Scalability: While the presented codes do not cover scalability, the non-functional requirement can be implemented in future iterations of the program to support large quantities of clients silmultaneously. 
5. Failure Handling: To ensure the program, especially for the server, to handle failures, the os module was implemented. Try and except are utilized throughout both source codes for server and client to handle invalid inputs. When an error occurs, an error message with elucidation on the occurred failure is printed to the client’s device. 
6. Transparency: The program achieves transparency, albeit at a simplistic level, by abstracting the remote procedure calls with the XML-RPC protocol. Thus, clients are unaware that they are calling procedures on a remote server when interacting with the system. 


## Demonstration Video
[link]
