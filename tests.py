import unittest
from flask_jsonrpc.proxy import ServiceProxy
from app import app
import multiprocessing
import time


class LiveServerTestCase(unittest.TestCase):
    def create_app(self):
        """
        Create your Flask app here, with any
        configuration you need.
        """
        raise NotImplementedError

    def setUp(self):
        self.app = self.create_app()
        self._spawn_live_server()
        super(LiveServerTestCase, self).setUp()

    def tearDown(self):
        self._terminate_live_server()

    def get_server_url(self):
        """
        Return the url of the test server
        """
        return 'http://localhost:%s' % self.port

    def _spawn_live_server(self):
        self._process = None
        self.port = self.app.config.get('LIVESERVER_PORT', 5000)

        worker = lambda app, port: app.run(port=port)

        self._process = multiprocessing.Process(
            target=worker, args=(self.app, self.port)
        )

        self._process.start()

        # we must wait the server start listening
        time.sleep(1)

    def _terminate_live_server(self):
        if self._process:
            self._process.terminate()


class JsonRPCTest(LiveServerTestCase):
    def create_app(self):
        return app

    def test_now(self):
        server = ServiceProxy('http://localhost:5000/api')
        s = server.time.now()
        print(s)
        self.assertIn('result', s)

    def test_now1(self):
        server = ServiceProxy('http://localhost:5000/api')
        s = server.time.now()
        print(s)
        self.assertIn('result', s)

    def test_now2(self):
        server = ServiceProxy('http://localhost:5000/api')
        s = server.time.now()
        print(s)
        self.assertIn('result', s)

    def test_now3(self):
        server = ServiceProxy('http://localhost:5000/api')
        s = server.time.now()
        print(s)
        self.assertIn('result', s)

    def test_now4(self):
        server = ServiceProxy('http://localhost:5000/api')
        s = server.time.now()
        print(s)
        self.assertIn('result', s)


if __name__ == '__main__':
    unittest.main()
