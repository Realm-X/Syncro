import customtkinter as ctk
import sys

def login(username_entry, password_entry, root):
    C_password = 'test123'
    C_username = 'test'
    username = username_entry.get()
    password = password_entry.get()

    if username == C_username and password == C_password:

        print(f"Logging in with Username: {username} and Password: {password}")
        root.withdraw()
        root.after(2000, root.withdraw())
        home_page()
        return

    else : 
        print("Wrong developer username or password.....")


def home_page():
    home = ctk.CTk()
    home.title("Syncro - Home")
    home.geometry("1050x650")
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    main_frame = ctk.CTkFrame(home, corner_radius=15, fg_color="#2B2B2B")
    main_frame.pack(pady=50, padx=50, fill="both", expand=True)

    label = ctk.CTkLabel(main_frame, text="Welcome to Syncro Dashboard 🚀",
                         font=ctk.CTkFont(size=24, weight="bold"), text_color="white")
    label.pack(pady=20)

    def view_devices():
        print("🔍 Viewing connected devices...")

    def sync_now():
        print("🔄 Syncing data...")

    def settings():
        print("⚙️ Opening settings...")

    def logout():
        print("🚪 Logging out...")
        home.after(2000, lambda: [home.destroy(), sys.exit()])

        

    btn1 = ctk.CTkButton(main_frame, text="View Connected Devices", command=view_devices,
                         fg_color="#1E90FF", hover_color="#1C86EE", font=ctk.CTkFont(size=16))
    btn1.pack(pady=15)

    btn2 = ctk.CTkButton(main_frame, text="Sync Now", command=sync_now,
                         fg_color="#32CD32", hover_color="#2E8B57", font=ctk.CTkFont(size=16))
    btn2.pack(pady=15)

    btn3 = ctk.CTkButton(main_frame, text="Device Settings", command=settings,
                         fg_color="#FFA500", hover_color="#FF8C00", font=ctk.CTkFont(size=16))
    btn3.pack(pady=15)

    btn4 = ctk.CTkButton(main_frame, text="Logout", command=logout,
                         fg_color="#FF4500", hover_color="#CD3700", font=ctk.CTkFont(size=16))
    btn4.pack(pady=25)

    home.mainloop()

    

def signup():
    print("Redirecting to sign-up page...")

def create_syncro_login():
    ctk.set_appearance_mode("dark")  
    ctk.set_default_color_theme("dark-blue")  

  
    root = ctk.CTk()
    root.title("Syncro - Welcome Back!")
    root.geometry("1050x650")

    main_frame = ctk.CTkFrame(root, corner_radius=15, fg_color="#2B2B2B")
    main_frame.pack(pady=50, padx=50, fill="both", expand=True)

    label = ctk.CTkLabel(main_frame, text="Welcome to Syncro!",
                         font=ctk.CTkFont(size=24, weight="bold"), text_color="white")
    label.pack(pady=20)

    sub_label = ctk.CTkLabel(main_frame, text="Let's get connected 🚀",
                             font=ctk.CTkFont(size=16), text_color="#D3D3D3")
    sub_label.pack(pady=5)

    username_label = ctk.CTkLabel(main_frame, text="Username", font=ctk.CTkFont(size=14), text_color="white")
    username_label.pack(pady=10)
    username_entry = ctk.CTkEntry(main_frame, placeholder_text="Enter your username", fg_color="#333333", text_color="white")
    username_entry.pack(pady=10)

    password_label = ctk.CTkLabel(main_frame, text="Password", font=ctk.CTkFont(size=14), text_color="white")
    password_label.pack(pady=10)
    password_entry = ctk.CTkEntry(main_frame, placeholder_text="Enter your password", show="*", fg_color="#333333", text_color="white")
    password_entry.pack(pady=10)

    login_button = ctk.CTkButton(main_frame, text="Login",
                                 command=lambda: login(username_entry, password_entry, root),
                                 fg_color="#1E90FF", hover_color="#1C86EE", font=ctk.CTkFont(size=16, weight="bold"))
    login_button.pack(pady=20)

    signup_label = ctk.CTkLabel(main_frame, text="Don't have an account?", font=ctk.CTkFont(size=12), text_color="white")
    signup_label.pack(pady=5)

    signup_button = ctk.CTkButton(main_frame, text="Sign up", command=signup,
                                  fg_color="#FF6347", hover_color="#FF4500", font=ctk.CTkFont(size=14), width=120)
    signup_button.pack(pady=5)

    root.mainloop()
