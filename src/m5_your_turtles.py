"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Tianxi He.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
ZACK= rg.SimpleTurtle('turtle')
ZACK.pen = rg.Pen('gray', 3)
ZACK.speed = 10
CHIGO = rg.SimpleTurtle('turtle')
CHIGO.pen = rg.Pen('white', 3)
CHIGO.left(90)
CHIGO.forward(100)
CHIGO.right(180)
CHIGO.speed = 10
nubleth=10
sizec=200
for k in range(5):
    ZACK.draw_regular_polygon(nubleth,100)
    nubleth=nubleth-1
    CHIGO.pen = rg.Pen('red', 3)
for g in range(5):
    CHIGO.pen = rg.Pen('white', 3)
    CHIGO.forward(70)
    CHIGO.pen = rg.Pen('red', 3)
    CHIGO.draw_circle(sizec)
    sizec=sizec-20
