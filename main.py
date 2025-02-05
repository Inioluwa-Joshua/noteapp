import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import font
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from speech_to_text import recognize_speech
from database import save_note, update_note, delete_note, get_notes, get_note_by_id

class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Note App with Speech-to-Text")
        self.root.geometry("900x500")
        self.selected_note_id = None

        # Apply Professional Theme
        self.root.configure(bg="#f4f4f4")  # Light gray background

        # Left Sidebar (Note History)
        self.left_frame = tk.Frame(self.root, width=300, bg="#333", padx=10, pady=10)  # Dark theme
        self.left_frame.pack(side="left", fill="y")

        self.history_label = tk.Label(self.left_frame, text="📜 Notes", font=("Arial", 14, "bold"), bg="#333", fg="white")
        self.history_label.pack(pady=5)

        self.search_entry = tk.Entry(self.left_frame, font=("Arial", 12))
        self.search_entry.pack(padx=5, pady=5, fill="x")
        self.search_entry.bind("<KeyRelease>", self.search_notes)

        self.note_listbox = tk.Listbox(self.left_frame, height=20, width=40, font=("Arial", 12), bg="#444", fg="white")
        self.note_listbox.pack(padx=5, pady=5, fill="both")
        self.load_notes()
        self.note_listbox.bind("<<ListboxSelect>>", self.load_selected_note)

        # Right Frame (Editor)
        self.right_frame = tk.Frame(self.root, bg="#444")
        self.right_frame.pack(side="right", expand=True, fill="both")

        self.text_area = tk.Text(self.right_frame, wrap="word", font=("Arial", 12), bg="white", fg="black")
        self.text_area.pack(expand=True, fill="both", padx=10, pady=10)

        # Formatting Buttons
        self.format_frame = tk.Frame(self.right_frame, bg="#444")
        self.format_frame.pack(pady=5)

        tk.Button(self.format_frame, text="B", font=("Arial", 12, "bold"), command=self.make_bold).pack(side="left", padx=5)
        tk.Button(self.format_frame, text="I", font=("Arial", 12, "italic"), command=self.make_italic).pack(side="left", padx=5)
        tk.Button(self.format_frame, text="U", font=("Arial", 12, "underline"), command=self.make_underline).pack(side="left", padx=5)

        # Buttons
        self.speech_button = tk.Button(self.right_frame, text="🎙️ Speech to Text", command=self.speech_to_text, font=("Arial", 12), bg="#007BFF", fg="black")
        self.speech_button.pack(pady=5)

        self.save_db_button = tk.Button(self.right_frame, text="💾 Save Note", command=self.save_or_update_note, font=("Arial", 12), bg="#28a745", fg="black")
        self.save_db_button.pack(pady=5)

        self.delete_button = tk.Button(self.right_frame, text="🗑️ Delete Note", command=self.delete_selected_note, font=("Arial", 12), bg="#dc3545", fg="black")
        self.delete_button.pack(pady=5)

        self.export_button = tk.Button(self.right_frame, text="📄 Export as PDF", command=self.export_to_pdf, font=("Arial", 12), bg="#17a2b8", fg="white")
        self.export_button.pack(pady=5)

        # Audio Listening Indicator
        self.listening_label = tk.Label(self.right_frame, text="", font=("Arial", 12, "bold"), fg="red")
        self.listening_label.pack()

    def load_notes(self):
        """Loads all saved notes into the listbox"""
        self.note_listbox.delete(0, tk.END)
        self.notes = get_notes()
        for note in self.notes:
            note_id, content = note
            display_text = content[:30] + "..." if len(content) > 30 else content
            self.note_listbox.insert(tk.END, f"{note_id}: {display_text}")

    def load_selected_note(self, event):
        """Loads selected note into editor"""
        try:
            selection = self.note_listbox.get(self.note_listbox.curselection())
            self.selected_note_id = selection.split(":")[0]
            note_content = get_note_by_id(self.selected_note_id)
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, note_content)
        except IndexError:
            pass  # Ignore empty selections

    def save_or_update_note(self):
        """Saves new note or updates existing one"""
        content = self.text_area.get(1.0, tk.END).strip()
        if content:
            if self.selected_note_id:
                update_note(self.selected_note_id, content)
                messagebox.showinfo("Success", "Note updated successfully!")
            else:
                save_note(content)
                messagebox.showinfo("Success", "Note saved successfully!")
            self.load_notes()

    def delete_selected_note(self):
        """Deletes selected note"""
        if self.selected_note_id:
            delete_note(self.selected_note_id)
            messagebox.showinfo("Success", "Note deleted successfully!")
            self.selected_note_id = None
            self.text_area.delete(1.0, tk.END)
            self.load_notes()

    def search_notes(self, event):
        """Filters notes based on search input"""
        query = self.search_entry.get().lower()
        self.note_listbox.delete(0, tk.END)
        for note_id, content in self.notes:
            if query in content.lower():
                display_text = content[:30] + "..." if len(content) > 30 else content
                self.note_listbox.insert(tk.END, f"{note_id}: {display_text}")

    def speech_to_text(self):
        """Converts speech to text with visual indicator."""
        self.listening_label.config(text="🎤 Listening...")
        self.root.update()
        text = recognize_speech()
        self.listening_label.config(text="")
        self.text_area.insert(tk.END, text + "\n")

    def make_bold(self):
        """Applies bold formatting to selected text"""
        self.text_area.tag_add("bold", "sel.first", "sel.last")
        self.text_area.tag_configure("bold", font=("Arial", 12, "bold"))

    def make_italic(self):
        """Applies italic formatting to selected text"""
        self.text_area.tag_add("italic", "sel.first", "sel.last")
        self.text_area.tag_configure("italic", font=("Arial", 12, "italic"))

    def make_underline(self):
        """Applies underline formatting to selected text"""
        self.text_area.tag_add("underline", "sel.first", "sel.last")
        self.text_area.tag_configure("underline", font=("Arial", 12, "underline"))
    
    
    def export_to_pdf(self):
        content = self.text_area.get(1.0, tk.END).strip()
        if content:
            pdf_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
            if pdf_path:
                try:
                    c = canvas.Canvas(pdf_path, pagesize=letter)
                    width, height = letter
                    margin = 1 * inch  # Add margins
                    line_height = 14   # Adjust line spacing

                    # Create a text object for better formatting
                    text_object = c.beginText()
                    text_object.setTextOrigin(margin, height - margin)
                    text_object.setFont("Helvetica", 12)

                    # Handle multi-line text
                    for line in content.split("\n"):
                        text_object.textLine(line)

                    c.drawText(text_object)
                    c.save()
                    messagebox.showinfo("Success", "Note exported as PDF!")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to export PDF: {e}")
                
if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()
