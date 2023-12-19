import os,json

class Config():
    
    def __init__(self) -> None:
        # カテゴリー情報を管理するJson
        self.category_info = os.path.join(os.getcwd(), 'category_info.json')

    def get_json_info(self):
        with open(self.category_info, mode='r', encoding='utf-8') as json_file:
            return json.load(json_file)
    
    def set_json_info(self, category_key, category_value):
        try:
            # jsonファイルの読み込み
            with open(self.category_info,'r', encoding='cp932') as json_file:
                json_data = json.load(json_file)
                json_data[category_key] = category_value
            # jsonファイルの更新
            with open(self.category_info, 'w', encoding='cp932') as json_file:
                json.dump(json_data, json_file, indent=4)
        except:
            print('jsonファイル更新失敗しました。')

    def del_json_info(self, category_value):
        try:
            # jsonファイルの読み込み
            with open(self.category_info,'r', encoding='cp932') as json_file:
                json_data = json.load(json_file)
                keys = [k for k, v in json_data.items() if v== category_value]
                if not keys is None:
                    for k in keys:
                        del(json_data[k])
                        
            # jsonファイルの更新
            with open(self.category_info, 'w', encoding='cp932') as json_file:
                json.dump(json_data, json_file, indent=4)
        except:
            print('jsonファイル更新失敗しました。')

    def initial_json(self):
        json_data = {
            "category_01": "生活"
        }
        with open(self.category_info, 'w', encoding='cp932') as json_file:
                json.dump(json_data, json_file, indent=4)

if __name__ == '__main__':
    ins = Config()
    ins.initial_json()
    print(ins.get_json_info())
    ins.set_json_info('category_02','学校')
    d = list(ins.get_json_info().values())
    print(d)