import time
import tkinter
from OpenGL import GL
from pyopengltk import OpenGLFrame

class AppOgl(OpenGLFrame):
    def initgl(self):
        GL.glViewport(0, 0, self.width, self.height)
        GL.glClearColor(1.0, 1.0, 1.0, 1.0)
        self.start = time.time()
        self.nframes = 0

    def redraw(self):
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        tm = time.time() - self.start
        self.nframes += 1
        print("fps", self.nframes / tm, end="\r" )

def main():
    root = tkinter.Tk()
    app = AppOgl(root, width=400, height=280)
    app.pack(fill=tkinter.BOTH, expand=tkinter.YES)
    app.animate = 1
    app.after(100, app.printContext)
    app.mainloop()

if __name__=="__main__":
    main()


