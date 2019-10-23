
# Description

The objective of this project is to sort bits and pieces that usually go in the bin. By "bits and pieces" I mean screws and nuts. These items are  usually disposed because the time taken to sort them is more expensive than the actual value of the items.
One of the biggest challenges of this project is the amount of different items that are required to be detected. E.g: There are mainly 10 different screw diameters each with at least 10 different lengths; added to that there are several types of screw heads also there are different types of nuts. These many variants represents a big challenge in the vision inspection application. 

The other big challenge is the design and implementation of a gripper that is able pick both screws and nuts

## HMI
the fronted of the application was developed using python PyQT5 which binds the vision inspection system and the pick and place system. The front end is developed using Designer and the bindings are done using python 3

## Vision
From the vision inspection the weapon of choice is OpenCV using python as a scripting language. the version is CV2.

## Pick And Place System
The pick and place machine is controlled using GRBL platform. This system receives positions from the application and drives the robot around.The mechanical system was designed using solid works. The components of the rig were recycled and some of them 3d printed. The electrical drivers of the motors were developed using Arduino and a CNC arduino shield Keyestudio UNO CNC Kit V3.


# To Do is To Be 

	
ItemNo|Description|status
--- | --- | ---
1|Add Serial port Handler to the application| InProgress
2|Add initial information to the MD file| Closed
3|Add Pictures| Open
4|Add more details about the application| Open
5|Timer to get machine status| Closed
6|Buttons to move the picker| Closed
7|Add settings| Open
8|Add message parser t show current position| Open
9|Timer to get machine status| Open
10|Buttons to move the picker| Open
11|Add settings| Open
12|Segregate sytem in several scripts, 1 for rig, 1 for vision, 1 for settings| Open
--- | --- | ---

---

### Cheatsheet
#### Git

Command | Description
--- | --- 
git fetch | gets the remote status of the repository
git status | display the local current status of the repository
git pull | updates changes in the local repository
git add . | updates (adds, removes) files and infor from local to remote repository
git commit -m "" | Commits the changes and allows for a message to be updated
git push origin master| Pushes changes to remote repository
