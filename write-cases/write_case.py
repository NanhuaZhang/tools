import re
import argparse


class BaseWrite(object):

    def __init__(self, module_type, tag):
        self.__module_type = module_type
        self.__tag = tag
        self.tab = '    '
        self.annotation = '''        """

        :return:
        """'''

    @property
    def module_type(self):
        return self.__module_type

    @staticmethod
    def get_base_nodes(interface_type):
        base_nodes = []
        for base_node in dir(interface_type):
            if base_node[0] == '_' and base_node[1] != '_':
                base_nodes.append(base_node)
        return base_nodes

    def get_methods(self, base_node: type):
        self_class = self.__module_type.__getattribute__(base_node)
        methods = [x for x in dir(self_class) if re.match('[a-z]+_[a-z]+', x) is not None]
        return methods

    def write_import_packages(self):
        with open('./test_%s.py' % self.__module_type.__name__.split('.')[-1], 'w') as f:
            f.write("# -*- coding: utf-8 -*-\n")
            f.write("import unittest\n")
            f.write("from util import tag\n\n\n")
        f.close()

    def write_base_test_cases(self, tag):
        with open('./test_%s.py' % self.__module_type.__name__.split('.')[-1], 'a') as f:
            f.write("@tag.%s\n" % tag)
            f.write("class BaseTestCase(unittest.TestCase):\n")
            f.write(self.tab + "@classmethod\n")
            f.write(self.tab + "def setUpClass(cls):\n")
            f.write(self.tab + self.tab + "pass\n\n\n")
        f.close()

    def write_cases(self, methods: list):
        with open('./test_%s.py' % self.__module_type.__name__.split('.')[-1], 'a') as f:
            for method in methods:
                name = "Test" + "".join([a.capitalize() for a in method.split("_")])
                f.write("class " + name + "(BaseTestCase):\n")
                f.write(self.tab + "def test_" + method + "(self):\n")
                f.write(self.annotation + '\n')
                f.write(self.tab + self.tab + "pass\n\n\n")
        f.close()


class MyArgParse(object):
    @property
    def args(self):
        return self.get_args()

    @property
    def tag(self):
        return self.args.tag

    @property
    def name(self):
        return self.args.name

    @property
    def fromlist(self):
        return self.args.fromlist

    @staticmethod
    def get_args():
        parser = argparse.ArgumentParser(description="""write cases.
        we can use it like this :
        python hh.py -n wosai.sqb.biz.merchant_service -f MerchantServiceClient-t finance
        """)
        parser.add_argument('-n', "--name", type=str,
                            help="the name of imported package. eg: wosai.sqb.biz.finance_backend")
        parser.add_argument('-f', "--fromlist", type=str,
                            help="the RPCTreeClient which we want. eg: FinanceBackendClient")
        parser.add_argument('-t', "--tag", type=str,
                            help="the tag which we want use. eg: finance")
        return parser.parse_args()


class WriteCase(BaseWrite):
    def __init__(self, module_type, tag):
        super(WriteCase, self).__init__(module_type, tag)

    def run(self):
        nodes = self.get_base_nodes(self.module_type)
        self.write_import_packages()
        self.write_base_test_cases(MyArgParse().tag)
        for node in nodes:
            self.write_cases(self.get_methods(node))


if __name__ == '__main__':
    my_arg_parse = MyArgParse()

    try:
        # import the package we need
        filename = __import__(my_arg_parse.name, fromlist=[my_arg_parse.fromlist])
    except (ImportError,):
        print("do not meet the requirements for wosai package!")
    test = WriteCase(filename, my_arg_parse.tag)
    test.run()
