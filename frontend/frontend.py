import tkinter as tk
import tkinter.font as tkFont

class Frontend:
    def __init__(self, root):
        #setting title
        root.title("Welcome to computerization!")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        font_type = tkFont.Font(family='Times',size=10)

        project_selection_label=tk.Label(root)
        project_selection_label["cursor"] = "trek"
        project_selection_label["disabledforeground"] = "#6c1f1f"
        project_selection_label["font"] = font_type
        project_selection_label["fg"] = "#333333"
        project_selection_label["justify"] = "left"
        project_selection_label["text"] = "Please type your project name."
        project_selection_label["relief"] = "flat"
        project_selection_label.place(x=40,y=20,width=244,height=34)

        project_selection_text=tk.Entry(root)
        project_selection_text["borderwidth"] = "1px"
        project_selection_text["font"] = font_type
        project_selection_text["fg"] = "#333333"
        project_selection_text["justify"] = "center"
        project_selection_text["text"] = ""
        project_selection_text.place(x=310,y=30,width=266,height=30)

        env_selection_label=tk.Label(root)
        env_selection_label["font"] = font_type
        env_selection_label["fg"] = "#333333"
        env_selection_label["justify"] = "center"
        env_selection_label["text"] = "Do you want to run locally or on Browser stack?"
        env_selection_label.place(x=30,y=50,width=272,height=35)

        locally_rb=tk.Radiobutton(root)
        locally_rb["font"] = font_type
        locally_rb["fg"] = "#333333"
        locally_rb["justify"] = "center"
        locally_rb["text"] = "Locally"
        locally_rb.place(x=70,y=160,width=85,height=25)
        locally_rb["command"] = self.locally_rb_command

        browser_stack_rb=tk.Radiobutton(root)
        browser_stack_rb["font"] = font_type
        browser_stack_rb["fg"] = "#333333"
        browser_stack_rb["justify"] = "center"
        browser_stack_rb["text"] = "Browser Stack"
        browser_stack_rb.place(x=400,y=160,width=160,height=30)
        browser_stack_rb["command"] = self.browser_stack_rb_command

        chrome_cb=tk.Checkbutton(root)
        chrome_cb["font"] = font_type
        chrome_cb["fg"] = "#333333"
        chrome_cb["justify"] = "center"
        chrome_cb["text"] = "Chrome"
        chrome_cb.place(x=40,y=180,width=70,height=25)
        chrome_cb["offvalue"] = "0"
        chrome_cb["onvalue"] = "1"
        chrome_cb["command"] = self.chrome_cb_command

        fire_fox_cb=tk.Checkbutton(root)
        fire_fox_cb["font"] = font_type
        fire_fox_cb["fg"] = "#333333"
        fire_fox_cb["justify"] = "center"
        fire_fox_cb["text"] = "Firefox"
        fire_fox_cb.place(x=130,y=180,width=70,height=25)
        fire_fox_cb["offvalue"] = "0"
        fire_fox_cb["onvalue"] = "1"
        fire_fox_cb["command"] = self.fire_fox_cb_command

        edge_cb=tk.Checkbutton(root)
        edge_cb["font"] = font_type
        edge_cb["fg"] = "#333333"
        edge_cb["justify"] = "center"
        edge_cb["text"] = "Edge"
        edge_cb.place(x=30,y=210,width=70,height=25)
        edge_cb["offvalue"] = "0"
        edge_cb["onvalue"] = "1"
        edge_cb["command"] = self.edge_cb_command

        bs_user_name_text=tk.Entry(root)
        bs_user_name_text["borderwidth"] = "1px"
        bs_user_name_text["font"] = font_type
        bs_user_name_text["fg"] = "#333333"
        bs_user_name_text["justify"] = "center"
        bs_user_name_text["text"] = "Provide BS username"
        bs_user_name_text.place(x=370,y=190,width=211,height=30)

        bs_access_key_text=tk.Entry(root)
        bs_access_key_text["borderwidth"] = "1px"
        bs_access_key_text["font"] = font_type
        bs_access_key_text["fg"] = "#333333"
        bs_access_key_text["justify"] = "center"
        bs_access_key_text["text"] = "Provide BS Access Key"
        bs_access_key_text.place(x=370,y=230,width=209,height=30)

        bs_native_url_text=tk.Entry(root)
        bs_native_url_text["borderwidth"] = "1px"
        bs_native_url_text["font"] = font_type
        bs_native_url_text["fg"] = "#333333"
        bs_native_url_text["justify"] = "center"
        bs_native_url_text["text"] = "Provide native URL"
        bs_native_url_text.place(x=370,y=290,width=209,height=30)

        kind_text_lb=tk.Label(root)
        kind_text_lb["font"] = font_type
        kind_text_lb["fg"] = "#333333"
        kind_text_lb["justify"] = "center"
        kind_text_lb["text"] = "What kind of test it is?"
        kind_text_lb.place(x=20,y=80,width=157,height=33)

        opera_cb=tk.Checkbutton(root)
        opera_cb["font"] = font_type
        opera_cb["fg"] = "#333333"
        opera_cb["justify"] = "center"
        opera_cb["text"] = "Opera"
        opera_cb.place(x=130,y=210,width=70,height=25)
        opera_cb["offvalue"] = "0"
        opera_cb["onvalue"] = "1"
        opera_cb["command"] = self.opera_cb_command

        api_rb=tk.Radiobutton(root)
        api_rb["font"] = font_type
        api_rb["fg"] = "#333333"
        api_rb["justify"] = "center"
        api_rb["text"] = "Api"
        api_rb.place(x=20,y=120,width=95,height=30)
        api_rb["command"] = self.api_rb_command

        mobile_native_rb=tk.Radiobutton(root)
        mobile_native_rb["font"] = font_type
        mobile_native_rb["fg"] = "#333333"
        mobile_native_rb["justify"] = "center"
        mobile_native_rb["text"] = "Mobile Native App"
        mobile_native_rb.place(x=140,y=120,width=145,height=30)
        mobile_native_rb["command"] = self.mobile_native_rb_command

        web_site_rb=tk.Radiobutton(root)
        web_site_rb["font"] = font_type
        web_site_rb["fg"] = "#333333"
        web_site_rb["justify"] = "center"
        web_site_rb["text"] = "Website"
        web_site_rb.place(x=310,y=120,width=85,height=25)
        web_site_rb["command"] = self.web_site_rb_command

        mobile_site_rb=tk.Radiobutton(root)
        mobile_site_rb["font"] = font_type
        mobile_site_rb["fg"] = "#333333"
        mobile_site_rb["justify"] = "center"
        mobile_site_rb["text"] = "Mobile site "
        mobile_site_rb.place(x=440,y=120,width=85,height=25)
        mobile_site_rb["command"] = self.mobile_site_rb_command

        run_btn=tk.Button(root)
        run_btn["bg"] = "#5fb878"
        run_btn["font"] = font_type
        run_btn["fg"] = "#000000"
        run_btn["justify"] = "center"
        run_btn["text"] = "Run"
        run_btn.place(x=50,y=420,width=150,height=30)
        run_btn["command"] = self.run_btn_command

        cancel_btn=tk.Button(root)
        cancel_btn["bg"] = "#efefef"
        cancel_btn["font"] = font_type
        cancel_btn["fg"] = "#000000"
        cancel_btn["justify"] = "center"
        cancel_btn["text"] = "Cancel"
        cancel_btn.place(x=290,y=420,width=141,height=30)
        cancel_btn["command"] = self.cancel_btn_command

        bs_username_lb=tk.Label(root)
        bs_username_lb["font"] = font_type
        bs_username_lb["fg"] = "#333333"
        bs_username_lb["justify"] = "center"
        bs_username_lb["text"] = "Username"
        bs_username_lb.place(x=280,y=190,width=70,height=25)

        bs_accesskey_lb=tk.Label(root)
        bs_accesskey_lb["font"] = font_type
        bs_accesskey_lb["fg"] = "#333333"
        bs_accesskey_lb["justify"] = "center"
        bs_accesskey_lb["text"] = "Access Key"
        bs_accesskey_lb.place(x=280,y=230,width=70,height=25)

        bs_native_app_url_lb=tk.Label(root)
        bs_native_app_url_lb["font"] = font_type
        bs_native_app_url_lb["fg"] = "#333333"
        bs_native_app_url_lb["justify"] = "center"
        bs_native_app_url_lb["text"] = "native app url"
        bs_native_app_url_lb.place(x=280,y=280,width=75,height=25)

    def locally_rb_command(self):       
        print("command")


    def browser_stack_rb_command(self):
        print("command")


    def chrome_cb_command(self):
        print("command")


    def fire_fox_cb_command(self):
        print("command")


    def edge_cb_command(self):
        print("command")


    def opera_cb_command(self):
        print("command")


    def api_rb_command(self):
        print("command")


    def mobile_native_rb_command(self):
        print("command")


    def web_site_rb_command(self):
        print("command")


    def mobile_site_rb_command(self):
        print("command")


    def run_btn_command(self):
        print("command")


    def cancel_btn_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = Frontend(root)
    root.mainloop()
    
