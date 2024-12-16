



















    def login_screen(self):
        self.clear_screen()
        
        tk.Label(self.root, text="Quiz Pak Tirta", font=("Times New Roman", 18)).pack(pady=10)

        tk.Label(self.root, text="Username").pack()
        self.input_username = tk.Entry(self.root)
        self.input_username.pack()

        tk.Label(self.root, text="Password").pack()
        self.input_password = tk.Entry(self.root, show="0")
        self.input_password.pack()

        tk.Button(self.root, text="Sign In", command=self.sign_in).pack(pady=5)
        tk.Button(self.root, text="Sign Up", command=self.sign_up_screen).pack()




































    def sign_in(self):
        username = self.input_username.get()
        password = self.input_password.get()

        if username in self.users and self.users[username]["password"] == password:
            self.current_user = username
            if self.users[username]["mode"] == "teacher":
                self.teacher_dashboard()
            else:
                self.student_dashboard()
        else:
            messagebox.showerror("Error", "Invalid username or password")
