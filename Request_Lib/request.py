import requests


def download_file(url, file_name):
    # Send a GET request to the provided URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Open a local file in binary write mode and save the content
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"File '{file_name}' downloaded successfully.")
    else:
        print(f"Failed to download file. Status code: {response.status_code}") #Example usage


if __name__ == "__main__":
	url = 'https://th.bing.com/th/id/R.683f53bffd6b4f7086732a203dbd7204?rik=DXCsbF4Vc6O4lg&riu=http%3a%2f%2f1.bp.blogspot.com%2f-_fvkqH0Yu8I%2fTndklja9_OI%2fAAAAAAAAPGU%2fSdr4QPgK8D4%2fs1600%2fnaruto-shippuden-hd-wallpapers_06.jpg&ehk=M7BuDH6ZN06DasbUkaIdxCeQpy9HrYGTxVWc5pquLKk%3d&risl=&pid=ImgRaw&r=0'
	file_name = 'img.jpg'
	download_file(url, file_name)


