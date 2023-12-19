import ttkbootstrap as tb
from tkinter import *
from tkinter.filedialog import askopenfilename # tkinter.filedialogモジュールのaskopenfilenameメソッドをインポート
from app_config import Config
import datetime

 
 # tk.Frameを継承したApplicationクラスを作成
class Application(tb.Frame):
    def __init__(self, master=None):
        super().__init__(master)
 
        # ウィンドウの設定
        # self.master.geometry('1200x600+600+600')
        self.font = ("Meiryo", "14")
        self.option_add("*TCombobox*Listbox.Font", self.font)
        self.option_add("*TEntry.Font", self.font)
        self.style = tb.Style()

        # ui初期化
        self.initial_ui()
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
            self.clear_ui()
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
        # file
        self.file_menu = tb.Menu(self, tearoff=0, font=self.font) # 大項目「ファイル」を生成、切り取り線をオフに
        self.menu_bar.add_cascade(label="File", menu=self.file_menu) # 大項目「ファイル」を配置
        self.file_menu.add_command(label="Create new lesson", command=self.create_new_lesson) # 小項目「新規作成」に処理を割り当て
        self.file_menu.add_command(label="Open exit lesson", command=OpenFile) # 小項目「開く」に処理を割り当て
        self.file_menu.add_separator() # セパレーターを追加
        self.file_menu.add_command(label="End Application", command=root.quit) # 小項目「終了」に処理を割り当て

        # settings
        self.settings_menu = tb.Menu(self, tearoff=0, font=self.font)
        self.menu_bar.add_cascade(label='Settings', menu=self.settings_menu)
        self.settings_menu.add_command(label='Add Catgory', command=self.SetCategory)
        self.settings_menu.add_command(label='Del Category', command=self.DelCategory)
        

        # Help
        self.help_menu = tb.Menu(self, tearoff=0, font=self.font) # 大項目「ヘルプ」を生成、切り取り線をオフに
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu) # 大項目「ヘルプ」を配置
        self.help_menu.add_command(label="About", command=About) # 小項目に処理を割り当て
    
    def initial_ui(self):
        self.bt00 = self.bt01 = self.bt02 = tb.Button()
        self.label1 = self.e_label = self.label_result = tb.Label()
        self.cb = tb.Combobox()
        self.entry = tb.Entry()
       
    def clear_ui(self):
        ui_list = [self.bt00, 
                   self.label1,
                   self.cb,
                   self.entry,
                   self.e_label,
                   self.bt01,
                   self.bt02,
                   self.label_result]
       
        for ui in ui_list:
            try:
                ui.destroy()
            except:
                pass
       
    def combobox_func(self, event):
        v = self.cb.get()
        print(v)
    
    def del_category(self):
        v = self.cb.get()
        ins = Config()
        ins.del_json_info(v)
        # 削除画面を更新する
        self.DelCategory()

    def add_categories(self):
        cate_name = datetime.datetime.now().strftime('cate_%Y%m%d%H%M%S')
        cate_val = self.entry.get()
        ins = Config()
        ins.set_json_info(category_key=cate_name, category_value=cate_val)
        self.label_result['text'] = '[' + cate_val + ']の追加が完了しました。'
        self.label_result.pack()

    def DelCategory(self):
        self.clear_ui()
        v = tb.StringVar()
        cate = Config()
        # カテゴリを取得
        cate_data = list(cate.get_json_info().values())
        self.cb = tb.Combobox(
            self, textvariable=v, 
            values=cate_data, width=10, height=10,font=("", 20, "underline"))
        self.cb.set(cate_data[0])
        self.cb.bind('<<ComboboxSelected>>', self.combobox_func)
        
        self.cb.pack()
        # Button
        self.bt02 = tb.Button(text='DEL', bootstyle='danger', command=self.del_category)
        self.bt02.pack()
        self.style.configure('danger.TButton', font=self.font)   

    def SetCategory(self):
        self.clear_ui()
        # label
        self.e_label = Label(text='category:', font=self.font)
        self.e_label.pack()
        # Entry
        self.entry = tb.Entry(bootstyle='info')
        self.entry.pack()
        self.style.configure('info.TEntry', font=('Helvetica', 32))
        # Button
        self.bt01 = tb.Button(text='ADD', bootstyle='info', command=self.add_categories)
        self.bt01.pack()
        self.style.configure('info.TButton', font=('arial', 20))

        # message
        self.label_result = tb.Label(bootstyle="success", font=self.font)
        # self.label_result.pack()


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
        self.clear_ui()
        self.bt00 = tb.Button(self, text='dark', bootstyle='dark')
        self.bt00.pack(side='left', padx=5, pady=5)

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
