#*PiPedal*
Two 'interrupt' events run this system, which functions like
a state machine to some extent. The first is when an external
button is pressed, or **stomped** (hence the name, StompBox). 
============================================================
```
<ISR_1:>
AUDIO IN: Analog audio signal is converted into digital 
quantities, and sampled into the system continuously
```
============================================================
```
<ISR_2:>
STOMP_2: On the second stomp the audio is no longer being 
sampled, and is instead immediately dumped into a file and 
played back through a speaker (this has to be done extremely 
fast or it will 'feel' off beat to the musician). 
```
============================================================
