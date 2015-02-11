from lib.query import *
import unittest
import torndb

mysql_host = "localhost"
mysql_database = "f2e"
mysql_user = "manager"
mysql_password = "manager"

class QueryTestCase(unittest.TestCase):
    def setUp(self):
        try:
            self.db = torndb.Connection(
            mysql_host, mysql_database, 
            mysql_user,
            mysql_password
            )
        except Exception as error:
            print "db read failed"
            print type(error)    
        self.query = Query("topic", self.db)
        self.sqls = {
            "create": "INSERT INTO topic (title, content) VALUES (Hello, World)",
            "remove": "DELETE FROM topic WHERE title = 'Hello'",
            "update": "UPDATE topic SET title = 'shit' WHERE title = 'title'",
            "update_back": "UPDATE topic SET title = 'title' WHERE title = 'shit'",
            "retrieve": "SELECT title, content from topic" 
            }
                        
    def tearDown(self):
        self.query = None
        if self.db != None:
            self.db.close()
            
    def testQuery(self):
        sql = "select * from topic;"
        a = self.query.query(sql)
        self.assertEqual(3, len(a))
        
    def testPages(self):
        self.query.grasp(self.sqls["retrieve"])
        result = self.query.pages(1, 10)
        self.assertEqual(len(result['list']), 3)
    
def suite1():
    suite1 = unittest.TestSuite()
    suite1.addTest(QueryTestCase("testQuery"))
    suite1.addTest(QueryTestCase("testPages"))
    return suite1

if __name__ == "__main__":
    unittest.main(defaultTest = 'suite1')
        