from testerFirst import tester
from test_sales_guy import test_sales_guy


z = tester("http://localhost:8069/")

z.processRole()


z = test_sales_guy("http://localhost:8069/")

z.processRole()