from tkinter import *
from PIL import ImageTk, Image
from dbfunctions import custom_query, create_all_tables, query_all_tables, populate_all_tables, exit, field, close_window, drop_all_tables, display_all_tables
from dbconnect import connection

class POSShoppers:
    def __init__(self, root):
        self.root = root
        self.root.title("Shoppers Drug Mart Point of Sale Database System")
        self.root.geometry("620x620")

        self.login = Frame(root)
        self.functions = Frame(root)
        self.functions = Frame(root, bg="black") 
        for frame in (self.login, self.functions):
            frame.grid(row=0, column=0, sticky="news")

        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        self.connection = None
        self.cursor = None

        self.init_login_page()
        self.init_functions()

        self.raise_frame(self.login)
        
        self.root.protocol("WM_DELETE_WINDOW", lambda: close_window(self))

    def raise_frame(self, frame):
        frame.tkraise()

    def init_login_page(self):
        for i in range(5):
            self.login.grid_rowconfigure(i, weight=1)
        self.login.grid_columnconfigure(0, weight=1)

        image = Image.open("POSShoppers_CPS510A9/logo.png") 
        image = image.resize((300, 250))
        img = ImageTk.PhotoImage(image)

        label = Label(self.login, image=img)
        label.image = img 
        label.grid(row=0, column=0, pady=5)

        self.login_message = Label(self.login, text="Enter CS Username and Password to Login")
        self.login_message.grid(row=1, column=0, pady=5)

        username = Frame(self.login)
        Label(username, text="Username").pack(side=LEFT, padx=5)
        self.username_input = Entry(username, width=30)
        self.username_input.pack(side=RIGHT, padx=5)
        username.grid(row=2, column=0, pady=1)

        password = Frame(self.login)
        Label(password, text="Password").pack(side=LEFT, padx=5)
        self.password_input = Entry(password, show="*", width=30)
        self.password_input.pack(side=RIGHT, padx=5)
        password.grid(row=3, column=0, pady=5)

        login = Button(self.login, text="Login", command=lambda:connection(self))
        login.grid(row=4, column=0, pady=10)
        
    #Initialize all the buttons and their functions
    def init_functions(self):
        for i in range(7):
            self.functions.grid_rowconfigure(i, weight=1)
        self.functions.grid_columnconfigure(0, weight=1)

        self.result = Text(self.functions, wrap=WORD, state=DISABLED, height=15, width=50)
        self.result.grid(row=0, column=0, padx=10, pady=10)

        self.input = Entry(self.functions, width=80) #Create an input field
        self.input.insert(0, "Enter a Query...")
        self.input.bind("<FocusIn>", lambda _: field(self))
        self.input.grid(row=1, column=0, padx=10, pady=5)
        
        #Buttons and attribute declaration
        Button(self.functions, text="Run Custom Query", width=50, command=lambda: custom_query(self)).grid(row=2, column=0, pady=5)
        Button(self.functions, text="Create All Tables", width=50, command=lambda: create_all_tables(self)).grid(row=3, column=0, pady=5)
        Button(self.functions, text="Populate All Tables", width=50, command=lambda: populate_all_tables(self)).grid(row=4, column=0, pady=5)
        Button(self.functions, text="Query All Tables", width=50, command=lambda: query_all_tables(self)).grid(row=5, column=0, pady=5)
        Button(self.functions, text="Drop All Tables", width=50, command=lambda: drop_all_tables(self)).grid(row=6, column=0, pady=5)
        Button(self.functions, text="Show All Tables", width=50, command=lambda: display_all_tables(self)).grid(row=7, column=0, pady=5)
        Button(self.functions, text="Exit", width=20, bg='red', command=lambda: exit(self)).grid(row=8, column=0, pady=10)

if __name__ == "__main__":
    root = Tk()
    app = POSShoppers(root)
    root.mainloop()