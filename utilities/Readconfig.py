import configparser

config = configparser.RawConfigParser()
config.read(r'C:\Users\Mr.PerSeCuToR\PycharmProjects\pythonProjectPractice\Configuration\config.ini')


class Readconfigs:

    @staticmethod
    def geturl(testname):
        return config.get('website', testname)





