import threading

class MultiThreadedScanner:
    def __init__(self, scanner):
        self.scanner = scanner

    def run_scan(self, target_urls):
        threads = []
        
        for url in target_urls:
            thread = threading.Thread(target=self.scanner.scan_target, args=(url,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
