import yaml


class Tools:
    def read_yaml(self, file_path):
        with open(file_path, encoding='utf-8') as f:
            datas = yaml.safe_load(f)
        return datas

    def write_yaml(self, file_path, content):
        with open(file_path, "w", encoding="UTF-8") as f:
            yaml.dump(content, f)

    def get_init_data(self, key, file_path):
        datas = self.read_yaml(file_path)
        datas[key] += 1
        self.write_yaml(file_path, datas)
        return datas[key]


if __name__ == '__main__':
    t = Tools()
    file_path = "init_datas_count.yaml"
    wework_api_path = "wework_api.yaml"
    datas = t.read_yaml(wework_api_path)
    print(datas)

    # a = t.get_init_data("group_count", file_path)
    # print(a)
