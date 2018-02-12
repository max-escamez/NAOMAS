# NAOMAS

Goal : Make Nao recognize objects and bring them back in a specific order

Nao should be able to : 

-Learn and differentiate several different objects by size, color and shape

-Approach them, grab them and bring them back

-Change his mind if he spots another object that should be brought first (Multi-Agent components)

As of today, Nao is simulated using Choregraphe. A virtual world is provided by Webots. 
The two software work together to create a virtual representation of Nao's behaviour and learning
abilities in the real world. After successful virtual testing, an actual Nao will be used to 
test his behaviour in the real world.


## Recognizing Objects

The module ALVideoDevice make use of NAO's cameras. Nao is able to learn then recognize objects 
with the ALVisionRecognition sub-module. This can be done with a virtual robot in a virtual world.


How to connect Choregraphe and Webots together :

http://doc.aldebaran.com/2-1/software/webots/webots_index.html#webots

ALVideoDevice performances and limitations :

http://doc.aldebaran.com/2-1/naoqi/vision/alvideodevice.html

ALVisionRecognition documentation :

http://doc.aldebaran.com/2-1/naoqi/vision/alvisionrecognition.html#alvisionrecognition

How to teach Nao to recognize objects :

http://doc.aldebaran.com/1-14/software/choregraphe/tutos/recognize_objects.html

## Entering Motion / Picking up


## Changing Mind

All the Multi-Agent part will be here