import cv2 as cv

capture = cv.VideoCapture(r"C:\Users\yunus\Downloads\capture.mp4")

height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
count = capture.get(cv.CAP_PROP_FRAME_COUNT)
fps = capture.get(cv.CAP_PROP_FPS)
print(height, width, count, fps)

fourcc = cv.VideoWriter_fourcc(*'mp4v')  # Codec belirleyin, 'mp4v' kullanabilirsiniz
out = cv.VideoWriter(r"C:\Users\yunus\Downloads\output.mp4", fourcc, fps, (int(width), int(height)))

while True:
    ret, frame = capture.read()
    if ret is True:
        cv.imshow("video", frame)
        out.write(frame)
        c = cv.waitKey(30)
        if c == 27:
            break
    else:
        break

capture.release()
out.release()
cv.destroyAllWindows()

height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
count = capture.get(cv.CAP_PROP_FRAME_COUNT)
fps = capture.get(cv.CAP_PROP_FPS)
print(height, width, count, fps)

fourcc = cv.VideoWriter_fourcc(*'mp4v')  # Codec belirleyin, 'mp4v' kullanabilirsiniz
out = cv.VideoWriter(r"C:\Users\yunus\Downloads\output.mp4", fourcc, fps, (int(width), int(height)))

while True: 
    ret, frame = capture.read() 
    if ret is True:
        cv.imshow("video", frame)
        out.write(frame)
        c = cv.waitKey(30)
        if c == 27:
            break
    else:
        break

capture.release()
out.release()
cv.destroyAllWindows()
