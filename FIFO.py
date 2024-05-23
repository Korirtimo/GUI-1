import tkinter as tk
import time

def fifo(page_reference_sequence, number_of_frames):
    page_table = []  # Represents the frames in memory
    page_faults = 0
    animation_steps = []

    for page_reference in page_reference_sequence:
        animation_steps.append((list(page_table), page_reference, page_reference not in page_table))
        if page_reference not in page_table:
            if len(page_table) == number_of_frames:
                # Remove the oldest page (first-in) if the frames are full
                page_table.pop(0)
            # Add the new page (first-in) to the frames
            page_table.append(page_reference)
            page_faults += 1

    return page_faults, animation_steps

def animate_algorithm():
    page_reference_sequence = list(map(int, input_entry.get().split()))
    number_of_frames = int(frames_entry.get())

    total_page_faults, animation_steps = fifo(page_reference_sequence, number_of_frames)

    for step, (frames, page_reference, page_fault) in enumerate(animation_steps):
        draw_step(frames, page_reference, page_fault)
        root.update()
        time.sleep(1)  # Adjust the sleep duration to control animation speed

    result_label.config(text=f"Total Page Faults (FIFO): {total_page_faults}")

def draw_step(frames, page_reference, page_fault):
    canvas.delete("all")

    canvas.create_text(50, 20, text="Frames", font=("Helvetica", 12))
    for i, frame in enumerate(frames):
        canvas.create_rectangle(20 + i * 40, 40, 60 + i * 40, 80, fill="lightblue")
        canvas.create_text(40 + i * 40, 60, text=str(frame), font=("Helvetica", 12))

    canvas.create_text(150, 20, text="Page Reference", font=("Helvetica", 12))
    canvas.create_rectangle(140, 40, 180, 80, fill="lightgreen")
    canvas.create_text(160, 60, text=str(page_reference), font=("Helvetica", 12))

    canvas.create_text(270, 20, text="Page Fault", font=("Helvetica", 12))
    if page_fault:
        canvas.create_rectangle(260, 40, 300, 80, fill="red")
        canvas.create_text(280, 60, text="Yes", font=("Helvetica", 12))
    else:
        canvas.create_rectangle(260, 40, 300, 80, fill="green")
        canvas.create_text(280, 60, text="No", font=("Helvetica", 12))

# Create a GUI window
root = tk.Tk()
root.title("FIFO Page Replacement Algorithm")

# Create input fields and labels
input_label = tk.Label(root, text="Enter Page Reference Sequence (space-separated):")
input_label.pack()
input_entry = tk.Entry(root)
input_entry.pack()

frames_label = tk.Label(root, text="Enter Number of Frames:")
frames_label.pack()
frames_entry = tk.Entry(root)
frames_entry.pack()

calculate_button = tk.Button(root, text="Animate FIFO Algorithm", command=animate_algorithm)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Create a canvas for visualization
canvas = tk.Canvas(root, width=400, height=100)
canvas.pack()

# Start the GUI main loop
root.mainloop()
