import cv2
import pandas as pd

# Step 1: Load the image and the color dataset
img_path = r'C:\Users\svsak\AI_COLOR_DETECTOR\test_image.png' # Change this to your image name
img = cv2.imread(img_path)

# Reading the CSV file with pandas
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv(r'C:\Users\svsak\AI_COLOR_DETECTOR\colors.csv', names=index, header=None)

# Global variables for state
clicked = False
r = g = b = xpos = ypos = 0

# Step 2: Function to find the closest color name
def get_color_name(R, G, B):
    minimum = 10000
    for i in range(len(csv)):
        # Calculate mathematical distance between the clicked color and the CSV list
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname

# Step 3: Mouse Callback - Captures the X, Y coordinates on double-click
def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, xpos, ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        # Get BGR values from the pixel
        b, g, r = img[y, x]
        b, g, r = int(b), int(g), int(r)

# Step 4: Execution Loop
# --- Updated Step 4 for Beautiful Fullscreen ---

# 1. Get your screen resolution (standard HD)
screen_width = 1920
screen_height = 1080

# 2. Resize the image to fit the screen BEFORE showing it
img = cv2.resize(img, (screen_width, screen_height))

cv2.namedWindow('Color Detector', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('Color Detector', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.setMouseCallback('Color Detector', draw_function)

while True:
    cv2.imshow("Color Detector", img)
    
    if clicked:
        # Draw a clean, centered top bar for the text
        # (x1, y1) to (x2, y2)
        cv2.rectangle(img, (0, 0), (screen_width, 80), (b, g, r), -1)
        
        # Get color name
        text = get_color_name(r, g, b) + f'  [R={r} G={g} B={b}]'
        
        # Determine text color for readability
        text_color = (0, 0, 0) if (r + g + b >= 600) else (255, 255, 255)
        
        # Put centered text with a cleaner font scale
        cv2.putText(img, text, (50, 55), cv2.FONT_HERSHEY_DUPLEX, 1.5, text_color, 2, cv2.LINE_AA)
        
        clicked = False

    if cv2.waitKey(20) & 0xFF == 27: # Press Esc to exit
        break

cv2.destroyAllWindows()
