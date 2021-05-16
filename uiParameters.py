from ui import *

# UI
panel = Panel()
runButton = Button("Run")

connections = TextUI("SPRING POSITIONS", (Width-180, 120), (255, 255, 255))
connections.fontSize = 30
verticalText = TextUI("Vertical: ", (Width-245, 180), (255, 255, 255))
horizontalText = TextUI("Horizontal: ", (Width-245, 220), (255, 255, 255))
diagonal1Text = TextUI("Diagonal-1: ", (Width-245, 260), (255, 255, 255))
diagonal2Text = TextUI("Diagonal-2: ", (Width-245, 300), (255, 255, 255))
showpointText = TextUI("show Point: ", (Width-245, 350), (255, 255, 255))
positionText = TextUI("PARAMETERS", (Width-180, 400), (255, 255, 255))
positionText.fontSize = 30
rowsText = TextUI("Cols: ",(Width-280, 440),(255, 255, 255))
colsText = TextUI("Rows: ",(Width-140, 440),(255, 255, 255) )
radiusText = TextUI("point-radius: ",(Width-240, 500),(255, 255, 255))
thicknessText = TextUI("line-thickness: ",(Width-240, 530),(255, 255, 255) )
spacingText = TextUI("point-spacing: ",(Width-240, 560),(255, 255, 255) )

toggleVertical = ToggleButton((Width-160, 170), 20, 20, True)
toggleHorizontal = ToggleButton((Width-160, 210), 20, 20, True)
toggleDiagonal1 = ToggleButton((Width-160, 250), 20, 20, False)
toggleDiagonal2 = ToggleButton((Width-160, 290), 20, 20, False)
showPoint = ToggleButton((Width-160, 340), 20, 20, True)

rowsInput = DigitInput(20, (Width-250, 420), 80, 40)
colsInput = DigitInput(10, (Width-110, 420), 80, 40)

radiusInput = DigitInput(3, (Width-160, 480), 80, 30)
thicknessInput = DigitInput(3, (Width-160, 515), 80, 30)
spacingInput = DigitInput(20, (Width-160, 550), 80, 30)
