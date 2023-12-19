import ttkbootstrap as tb
from tkinter import *
from tkinter.filedialog import askopenfilename # tkinter.filedialogモジュールのaskopenfilenameメソッドをインポート

 
 # tk.Frameを継承したApplicationクラスを作成
class Application(tb.Frame):
    def __init__(self, master=None):
        super().__init__(master)
 
        # ウィンドウの設定
        # self.master.geometry('1200x600+600+600')
        self.font = ("Meiryo", "14")
 
        # 実行内容
        self.pack() # メインフレームを配置
        self.create_menu() # 下記で定義しているcreate_menuメソッドを実行
        self.create_welcome() # 下記で定義しているcreate_widgetメソッドを実行
        self.place_window_center()
 
    # create_menuメソッドを定義
    def create_menu(self):
        # メニューバー用の関数
        def OpenFile():
            file_name = askopenfilename() # インポートしたtkinter.filedialogモジュールのaskopenfilenameメソッドを代入
            print(file_name)
        def About():
            try:
                self.label1.destroy()
                self.b8.destroy()
            except:
                pass
            self.label1 = tb.Label(self, text='''
            This application will help you to study English.
            このアプリケーションはあなたの英語の学習を助けます。
            这个应用程序会帮助您学习英文''',
            font=self.font)
            self.label1.pack(side='left', padx=5)
            # print("このアプリはhogehogeなアプリです")

        self.menu_bar = tb.Menu(self, font=self.font)
        root.config(menu=self.menu_bar)
       
        # メニュー上部文字サイズの変更は難しい
        self.file_menu = tb.Menu(self, tearoff=0, font=self.font) # 大項目「ファイル」を生成、切り取り線をオフに
        self.menu_bar.add_cascade(label="File", menu=self.file_menu) # 大項目「ファイル」を配置
        self.file_menu.add_command(label="Create new lesson", command=self.create_new_lesson) # 小項目「新規作成」に処理を割り当て
        self.file_menu.add_command(label="Open exit lesson", command=OpenFile) # 小項目「開く」に処理を割り当て
        self.file_menu.add_separator() # セパレーターを追加
        self.file_menu.add_command(label="End Application", command=root.quit) # 小項目「終了」に処理を割り当て

        self.help_menu = tb.Menu(self, tearoff=0, font=self.font) # 大項目「ヘルプ」を生成、切り取り線をオフに
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu) # 大項目「ヘルプ」を配置
        self.help_menu.add_command(label="About", command=About) # 小項目に処理を割り当て
 
    # create_widgetメソッドを定義
    def create_welcome(self):
        # label1ウィジェット
        self.label1 = tb.Label(self,text='''
        Welcome!!!
        ようこそ！
        欢迎您！
        ''',
        font=self.font)
        self.label1.pack(side='left')
    
    # 新しいレッスンを作成する
    def create_new_lesson(self):
        try:
            # 実行順番が重要
            self.label1.destroy()
            self.b8.destroy()
        except:
            pass
        
        self.b8 = tb.Button(self, text='dark', bootstyle='dark')
        self.b8.pack(side='left', padx=5, pady=5)

    def place_window_center(self):
        """Position the toplevel in the center of the screen. Does not
        account for titlebar height."""
        w = 1200
        h = 600
        self.update_idletasks()
        w_height = self.winfo_height()
        w_width = self.winfo_width()
        s_height = self.winfo_screenheight()
        s_width = self.winfo_screenwidth()
        xpos = (s_width - w) // 2
        ypos = (s_height - h) // 2
        self.master.geometry(f'{w}x{h}+{xpos}+{ypos}')
 
if __name__ == "__main__":
    root = tb.Window(title='Study English Helper', themename='darkly')
    app = Application(master=root)
    app.mainloop()