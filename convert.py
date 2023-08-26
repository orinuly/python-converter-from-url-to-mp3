import os
import shutil

from pytube import YouTube

def url_to_mp4(video_url: str):
    video_file = YouTube(video_url).streams.filter().get_highest_resolution()
    video_file.download()

    mp4_name: str = video_file.default_filename

    shutil.move(mp4_name, 'video')

def url_to_mp3(video_url: str):
    video_file = YouTube(video_url).streams.filter().get_audio_only()
    video_file.download()

    mp4_name: str = video_file.default_filename
    mp3_name: str = mp4_name.replace('.mp4', '.mp3')
    os.rename(mp4_name, mp3_name)

    shutil.move(mp3_name, 'audio')

def main():
    try:
        input_url: str = input('Please enter a URL: ')
        yt = YouTube(input_url)

        while True:
            print('What type of information you want to get?')
            print('1. Title of the video')
            print('2. Author of the video')
            print('3. Thumbnail URL')
            print('4. Download video')
            print('5. Download video as .mp3 file')
            print('To exit from the menu type any other digit')

            choice: int = input()

            if choice == '1':
                print('Title: ', yt.title)
                print('')
            elif choice == '2':
                print('Author: ', yt.author)
                print('')
            elif choice == '3':
                print('Thumbnail: ', yt.thumbnail_url)
                print('')
            elif choice == '4':
                url_to_mp4(input_url)
                print('Finished downloading!')
                print('')
            elif choice == '5':
                url_to_mp3(input_url)
                print('Finished downloading!')
                print('')
            else:
                print('Goodbye!')
                exit()
    except Exception as e:
        print(f'Something went wrong!: {e}')

if __name__ == '__main__':
    main()
