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
    init_data = t.read_yaml(file_path)
    print(init_data)

    a = t.get_init_data("group_count", file_path)
    print(a)
