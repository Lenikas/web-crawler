from threading import Thread


class ThreadWorker(Thread):

    def __init__(self, main_thread, list_download_threads):
        super().__init__()
        self.main_thread = main_thread
        self.list_download_threads = list_download_threads

    def joined_threads(self):
        for thread in self.list_download_threads:
            thread.join()

    def start_threads(self):
        for thread in self.list_download_threads:
            thread.start()