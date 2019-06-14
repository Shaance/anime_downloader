# ATTENTION: This is only a example of to use a python bind of torrent library in Python for educational purposes.
#            I am not responsible for your download of illegal content or without permission.
#            Please respect the laws license permits of your country.

from qbittorrent import Client


class TorrentClient:

    def __init__(self):
        self.qb = Client('http://127.0.0.1:8081/')
        self.qb.login()

    def get_active_downloads(self):
        return self.qb.torrents(filter='downloading')

    def get_completed_downloads(self):
        return self.qb.torrents(filter='completed')

    def start_torrents(self, torrent_file_list, save_path):
        for file in torrent_file_list:
            self.qb.download_from_file(open(file, 'rb'), savepath=save_path)

    def start_magnets(self, link_list, save_path):
        for link in link_list:
            self.qb.download_from_link(link, savepath=save_path)

    def get_torrent_status(self):
        return self.qb.torrents()

    def get_global_transfer_info(self):
        return self.qb.global_transfer_info
