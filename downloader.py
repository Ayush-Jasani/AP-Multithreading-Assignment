import requests

def download_file(url):
    filename = url.split("/")[-1]
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded {filename}")

def main_download():
    import time
    urls = [
        "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        "https://www.learningcontainer.com/wp-content/uploads/2020/04/sample-text-file.txt"
    ]
    start = time.time()
    threads = []
    for url in urls:
        thread = threading.Thread(target=download_file, args=(url,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    end = time.time()
    print("Concurrent download completed in", end - start, "seconds")

if __name__ == '__main__':
    main_merge()
    main_quick()
    main_download()