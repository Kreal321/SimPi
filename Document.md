## JSON between client and server format
```
{
    data: int/string/array
    type: int
}
```
### Type 0: server message
Display on screen

### Type 1: client message
Start/Suspend/Resume/Stop actions of SimPi

### Type 2: simpi config queue
Queue of actions 

### Type 3: Multi-client management
The number of current connected clients


## SimPi Queue Options
```
{
    type: int
    options: int/string/array
}
```
1. Start
Start `type: 10`
Click to start `type: 11`

2. Suspend
Suspend `type: 20`
Click to suspend `type: 21`

3. Resume 
Resume `type: 30`
Click to resume `type: 31`

4. Stop
Stop `type: 40`
Click to resume `type: 31`

5. Wait
Wait X mins `type: 5`

6. Turn on Source
7. Turn off Source
8. If Statement