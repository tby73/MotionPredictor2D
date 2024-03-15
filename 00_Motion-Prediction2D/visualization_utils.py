import cv2

class Display:
    def __init__(self):
        pass
    
    def BoundingBox(image, x, y, w, h, color: tuple, thickness):
        cv2.rectangle(image, (x, y), (x + w, y + h), color=color, thickness=thickness)

        # upper left
        cv2.line(image, (x - 30, y - 20), (x + 20, y - 20), color=color, thickness=thickness)
        cv2.line(image, (x - 30, y - 20), (x - 30, y + 10), color=color, thickness=thickness)

        # upper right
        cv2.line(image, ((x + w) - 20, y - 20), ((x + w) + 30, y - 20), color=color, thickness=thickness)
        cv2.line(image, ((x + w) + 30, y - 20), ((x + w) + 30, y + 10), color=color, thickness=thickness)

        # down right
        cv2.line(image, ((x + w) - 20, (y + h) + 20), ((x + w) + 30, (y + h) + 20), color=color, thickness=thickness)
        cv2.line(image, ((x + w) + 30, (y + h) + 20), ((x + w) + 30, (y + h) - 10), color=color, thickness=thickness)

        # down left
        cv2.line(image, (x - 30, (y + h) + 20), (x + 30, (y + h) + 20), color=color, thickness=thickness)
        cv2.line(image, (x - 30, (y + h) + 20), (x - 30, (y + h) - 10), color=color, thickness=thickness)

    def BoundingBoxwithInfo(image, text, scale, x, y, w, h, color: tuple, thickness):
        cv2.rectangle(image, (x, y), (x + w, y + h), color=color, thickness=thickness)
        cv2.putText(image, text, (x, y - 45), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=scale, color=color, thickness=thickness)
        
        # upper left
        cv2.line(image, (x - 30, y - 20), (x + 20, y - 20), color=color, thickness=thickness)
        cv2.line(image, (x - 30, y - 20), (x - 30, y + 10), color=color, thickness=thickness)

        # upper right
        cv2.line(image, ((x + w) - 20, y - 20), ((x + w) + 30, y - 20), color=color, thickness=thickness)
        cv2.line(image, ((x + w) + 30, y - 20), ((x + w) + 30, y + 10), color=color, thickness=thickness)

        # down right
        cv2.line(image, ((x + w) - 20, (y + h) + 20), ((x + w) + 30, (y + h) + 20), color=color, thickness=thickness)
        cv2.line(image, ((x + w) + 30, (y + h) + 20), ((x + w) + 30, (y + h) - 10), color=color, thickness=thickness)

        # down left
        cv2.line(image, (x - 30, (y + h) + 20), (x + 30, (y + h) + 20), color=color, thickness=thickness)
        cv2.line(image, (x - 30, (y + h) + 20), (x - 30, (y + h) - 10), color=color, thickness=thickness)

    def BoundingBoxwithMultilineInfo(image, lines, text: list, scale, x, y, w, h, color: tuple, thickness):
        cv2.rectangle(image, (x, y), (x + w, y + h), color=color, thickness=thickness)

        if lines == 2:
            cv2.putText(image, text[0], (x, y - 65), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=scale, color=color, thickness=thickness)
            cv2.putText(image, text[1], (x, y - 45), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=scale, color=color, thickness=thickness)
        elif lines == 3:
            cv2.putText(image, text[0], (x, y - 85), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=scale, color=color, thickness=thickness)
            cv2.putText(image, text[1], (x, y - 65), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=scale, color=color, thickness=thickness)
            cv2.putText(image, text[2], (x, y - 45), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=scale, color=color, thickness=thickness)
        
        # upper left
        cv2.line(image, (x - 30, y - 20), (x + 20, y - 20), color=color, thickness=thickness)
        cv2.line(image, (x - 30, y - 20), (x - 30, y + 10), color=color, thickness=thickness)

        # upper right
        cv2.line(image, ((x + w) - 20, y - 20), ((x + w) + 30, y - 20), color=color, thickness=thickness)
        cv2.line(image, ((x + w) + 30, y - 20), ((x + w) + 30, y + 10), color=color, thickness=thickness)

        # down right
        cv2.line(image, ((x + w) - 20, (y + h) + 20), ((x + w) + 30, (y + h) + 20), color=color, thickness=thickness)
        cv2.line(image, ((x + w) + 30, (y + h) + 20), ((x + w) + 30, (y + h) - 10), color=color, thickness=thickness)

        # down left
        cv2.line(image, (x - 30, (y + h) + 20), (x + 30, (y + h) + 20), color=color, thickness=thickness)
        cv2.line(image, (x - 30, (y + h) + 20), (x - 30, (y + h) - 10), color=color, thickness=thickness)

    def BoundingBoxwithDirectionVector(image, direction_coordinate: tuple, x, y, w, h, color: tuple, thickness, draw=True):
        if draw:
            cv2.rectangle(image, (x, y), (x + w, y + h), color=color, thickness=thickness)

            # upper left
            cv2.line(image, (x - 30, y - 20), (x + 20, y - 20), color=color, thickness=thickness)
            cv2.line(image, (x - 30, y - 20), (x - 30, y + 10), color=color, thickness=thickness)

            # upper right
            cv2.line(image, ((x + w) - 20, y - 20), ((x + w) + 30, y - 20), color=color, thickness=thickness)
            cv2.line(image, ((x + w) + 30, y - 20), ((x + w) + 30, y + 10), color=color, thickness=thickness)

            # down right
            cv2.line(image, ((x + w) - 20, (y + h) + 20), ((x + w) + 30, (y + h) + 20), color=color, thickness=thickness)
            cv2.line(image, ((x + w) + 30, (y + h) + 20), ((x + w) + 30, (y + h) - 10), color=color, thickness=thickness)

            # down left
            cv2.line(image, (x - 30, (y + h) + 20), (x + 30, (y + h) + 20), color=color, thickness=thickness)
            cv2.line(image, (x - 30, (y + h) + 20), (x - 30, (y + h) - 10), color=color, thickness=thickness)

            # center circle
            center_point = (int(x + w / 2), int(y + h / 2))
            cv2.circle(image, center_point, 5, color, cv2.FILLED)

            # arrow
            cv2.arrowedLine(image, center_point, direction_coordinate, color, thickness)

            return center_point
        else:
            return (int(x + w / 2), int(y + h / 2))



