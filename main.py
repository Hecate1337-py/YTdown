import os
import yt_dlp

# Warna ANSI untuk konsol
HONEY_YELLOW = '\033[38;5;214m'
GREEN = '\033[92m'
RED = '\033[31m'
RESET_COLOR = '\033[0m'

def center_text(text, width):
    """
    Function to center text based on the terminal width.
    """
    lines = text.splitlines()
    return '\n'.join(line.center(width) for line in lines)

def display_banner():
    # Dapatkan lebar terminal
    width = os.get_terminal_size().columns

    # Banner yang diinginkan
    banner = f"""
{GREEN}
$$\\   $$\\                               $$\\               
$$ |  $$ |                              $$ |              
$$ |  $$ | $$$$$$\\   $$$$$$$\\ $$$$$$\\ $$$$$$\\    $$$$$$\\  
          {HONEY_YELLOW}$$$$$$$$ |$$  __$$\\ $$  _____|\\____$$\\_$$  _|  $$  __$$\\ 
$$  __$$ |$$$$$$$$ |$$ /      $$$$$$$ | $$ |    $$$$$$$$ |
$$ |  $$ |$$   ____|$$ |     $$  __$$ | $$ |$$\\ $$   ____|
    {RED}$$ |  $$ |\\$$$$$$$\\ \\$$$$$$$\\$$$$$$$ | \\$$$$  |\\$$$$$$$\\ 
\\__|  \\__| \\_______| \\_______|\\_______|  \\____/  \\_______|
{RESET_COLOR}
    """

    # Center the banner and print it
    print(center_text(banner, width))

# Fungsi untuk mendownload konten YouTube
def download_youtube_content(channel_username, content_type, cookies_file=None):
    # Buat URL channel dari username
    channel_url = f'https://www.youtube.com/{channel_username}'

    # Struktur folder utama dan subfolder berdasarkan jenis konten
    base_folder = 'vid'
    subfolder = os.path.join(base_folder, content_type)

    # Buat subfolder jika belum ada
    if not os.path.exists(subfolder):
        os.makedirs(subfolder)

    
    ydl_opts = {
        'outtmpl': os.path.join(subfolder, '%(title)s.%(ext)s'),
        'format': 'bestvideo[height<=1920][width<=1080]+bestaudio/best',
        'merge_output_format': 'mp4',
        'ffmpeg_location': r'ffmpeg.exe',
    }

    # Filter berdasarkan jenis konten yang dipilih
    if content_type == 'shorts':
        ydl_opts['match_filter'] = yt_dlp.utils.match_filter_func("duration <= 120")
    elif content_type == 'live':
        ydl_opts['match_filter'] = yt_dlp.utils.match_filter_func("is_live")
    elif content_type == 'playlist':
        channel_url += '/playlists'
    elif content_type == 'all':
        # Untuk semua konten, tidak perlu filter khusus
        pass

    # Tambahkan cookies file jika ada pembatasan usia
    if cookies_file:
        ydl_opts['cookies'] = cookies_file

    # Mendownload video berdasarkan opsi yang dipilih
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            print(f"{GREEN}Downloading content ({content_type}) from: {channel_url}{RESET_COLOR}")
            ydl.download([channel_url])
            print(f"{GREEN}All content ({content_type}) has been downloaded to the '{subfolder}' folder.{RESET_COLOR}")
        except yt_dlp.utils.DownloadError as e:
            print(f"{RED}Error: {str(e)}{RESET_COLOR}")

# Menampilkan banner saat program dimulai
display_banner()

# Meminta input pengguna untuk username channel
channel_username = input(f"{HONEY_YELLOW}Enter the YouTube channel username (e.g., @imhecate): {RESET_COLOR}")

# Menampilkan pilihan tipe konten
print(f"{HONEY_YELLOW}Select content type to download:{RESET_COLOR}")
print(f"{GREEN}1. Shorts{RESET_COLOR}")
print(f"{GREEN}2. Live{RESET_COLOR}")
print(f"{GREEN}3. Playlist{RESET_COLOR}")
print(f"{GREEN}4. All (All video content){RESET_COLOR}")
content_choice = input(f"{HONEY_YELLOW}Enter the number (1-4) corresponding to your choice: {RESET_COLOR}")

# Mapping pilihan ke jenis konten
content_map = {
    '1': 'shorts',
    '2': 'live',
    '3': 'playlist',
    '4': 'all'
}

# Validasi input pengguna
if content_choice not in content_map:
    print(f"{RED}Invalid choice. Please run the script again and select a valid option.{RESET_COLOR}")
else:
    content_type = content_map[content_choice]

    # Meminta input pengguna untuk file cookies (jika ada pembatasan usia)
    use_cookies = input(f"{HONEY_YELLOW}Do you have a cookies file for age-restricted videos? (y/n): {RESET_COLOR}").strip().lower()

    if use_cookies == 'y':
        # Secara default, gunakan 'cookies.txt' yang ada di direktori saat ini
        default_cookies_path = os.path.join(os.getcwd(), 'cookies.txt')

        # Meminta path jika pengguna ingin mengubah lokasi cookies.txt, atau gunakan default
        cookies_file = input(f"{HONEY_YELLOW}Enter the path to your cookies file or press Enter to use 'cookies.txt' in current directory: {RESET_COLOR}")
        if not cookies_file:
            cookies_file = default_cookies_path

        # Pastikan file cookies ada sebelum memulai download
        if os.path.exists(cookies_file):
            download_youtube_content(channel_username, content_type, cookies_file)
        else:
            print(f"{RED}Cookies file '{cookies_file}' not found. Please check the path and try again.{RESET_COLOR}")
    else:
        download_youtube_content(channel_username, content_type)
