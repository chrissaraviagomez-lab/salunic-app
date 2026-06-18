import tkinter as tk
from tkinter import Canvas
import time

class SplashScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#ffffff")
        self.controller = controller
        self.parent = parent
        
        self.canvas = Canvas(
            self,
            width=375,
            height=812,
            bg="#ffffff",
            highlightthickness=0
        )
        self.canvas.pack()
        
        self.animation_frame = 0
        self.circles = []
        
        self.create_background()
        self.create_logo()
        self.create_animated_circles()
        self.create_progress_bar()
        self.create_version_info()
        
        self.start_animation()
    
    def create_background(self):
        self.canvas.create_rectangle(
            0, 0, 375, 812,
            fill="#ffffff",
            outline=""
        )
        
        self.canvas.create_rectangle(
            0, 0, 375, 350,
            fill="#1565c0",
            outline=""
        )
    
    def create_logo(self):
        self.canvas.create_text(
            187, 250,
            text="SALUNIC",
            font=("Nunito", 48, "bold"),
            fill="#ffffff"
        )
        
        self.canvas.create_text(
            187, 290,
            text="Salud y Bienestar",
            font=("Nunito", 14),
            fill="#1565c0"
        )
    
    def create_animated_circles(self):
        circle_y = 150
        circle_radius = 8
        spacing = 30
        
        for i in range(5):
            x = 120 + (i * spacing)
            circle_id = self.canvas.create_oval(
                x - circle_radius, circle_y - circle_radius,
                x + circle_radius, circle_y + circle_radius,
                fill="#cccccc",
                outline=""
            )
            self.circles.append({
                'id': circle_id,
                'x': x,
                'y': circle_y,
                'radius': circle_radius,
                'index': i
            })
    
    def update_circles(self):
        colors = ["#cccccc", "#999999", "#1565c0", "#999999", "#cccccc"]
        
        for i, circle in enumerate(self.circles):
            offset = (self.animation_frame + i * 2) % 20
            
            if offset < 5:
                color = "#1565c0"
                scale = 1.0 + (offset / 5) * 0.3
            elif offset < 10:
                color = "#1565c0"
                scale = 1.3 - ((offset - 5) / 5) * 0.3
            else:
                color = "#cccccc"
                scale = 1.0
            
            radius = circle['radius'] * scale
            self.canvas.coords(
                circle['id'],
                circle['x'] - radius,
                circle['y'] - radius,
                circle['x'] + radius,
                circle['y'] + radius
            )
            self.canvas.itemconfig(circle['id'], fill=color)
    
    def create_progress_bar(self):
        self.progress_bg = self.canvas.create_rectangle(
            50, 400, 325, 410,
            fill="#e0e0e0",
            outline=""
        )
        
        self.progress_fill = self.canvas.create_rectangle(
            50, 400, 50, 410,
            fill="#1565c0",
            outline=""
        )
    
    def create_version_info(self):
        self.canvas.create_text(
            187, 750,
            text="Version 1.0.0",
            font=("Nunito", 10),
            fill="#999999"
        )
        
        self.canvas.create_text(
            187, 775,
            text="UNAN Managua 2026",
            font=("Nunito", 9),
            fill="#cccccc"
        )
    
    def start_animation(self):
        self.animate()
    
    def animate(self):
        self.animation_frame += 1
        self.update_circles()
        
        progress = min(100, self.animation_frame * 3.33)
        progress_width = 50 + (progress / 100) * 275
        self.canvas.coords(
            self.progress_fill,
            50, 400, progress_width, 410
        )
        
        if self.animation_frame < 30:
            self.after(50, self.animate)
        else:
            self.controller.show_screen("Inicio")
