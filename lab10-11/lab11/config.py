from configparser import ConfigParser

def load_config(filename = 'database.ini', section = 'postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    config = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            config[item[0]] = item[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')

    return config

if __name__ == '__main__':
    config = load_config()
    print(config)