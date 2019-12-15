from unittest import TestCase
from mock import patch
import jsearch as mymodule


class TestAskUser(TestCase):
    #test display search terms
    @patch('builtins.input')
    def test_display_search_terms(self, m_input):
        m_input.side_effect = ['Any', '2']
        mymodule.main()

    #test search users with search term _id and value 1
    @patch('builtins.input')
    def test_display_search_user(self, m_input):
        m_input.side_effect = ['Any', '1', '1', '_id', '1']
        mymodule.main()

    #test search users with search term _id and value 1000 which doesn't exist
    @patch('builtins.input')
    def test_display_search_user_1(self, m_input):
        m_input.side_effect = ['Any', '1', '1', '_id', '1000']
        mymodule.main()

    #test search users with search term _idx which doesn't exit
    @patch('builtins.input')
    def test_display_search_user_2(self, m_input):
        m_input.side_effect = ['Any', '1', '1', '_idx','_id','1']
        mymodule.main()

    #test search tickets with search term _id and value 436bf9b0-1147-4c0a-8439-6f79833bff5b
    @patch('builtins.input')
    def test_display_search_ticket(self, m_input):
        m_input.side_effect = ['Any', '1', '2', '_id', '436bf9b0-1147-4c0a-8439-6f79833bff5b']
        mymodule.main()

    #test search organizations with search term _id and value 101
    @patch('builtins.input')
    def test_display_search_organization(self, m_input):
        m_input.side_effect = ['Any', '1', '2', '_id', '101']
        mymodule.main()

if __name__ == '__main__':
    unittest.main()        
