import cgi
import logging
import os
from datetime import datetime
from os import listdir
from os.path import isfile, join
from typing import List
from urllib.parse import unquote
from urllib.request import urlopen, urlretrieve

from scraper.link_scraper import get_links
from torrent_client import TorrentClient

supported_res = {480, 720, 1080}
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
torrent_client = TorrentClient()


def download_show(mode: str, url: str, res: int, output_directory: str, show_name: str) -> (bool, str):
    valid_mode = mode.lower() == 'magnet' or mode.lower() == 'torrent'
    valid_res = res in supported_res
    output_directory = output_directory.strip()
    valid_output_path = os.access(output_directory, os.W_OK)
    if valid_mode and valid_res and valid_output_path:
        links = get_links(mode, url, res)
        if links:
            logging.info("Beginning download...")
            final_directory = __create_output_directory__(output_directory, show_name)
            if mode == 'torrent':
                __download_links__(links, final_directory)
                __open_torrent_files__(final_directory)
            else:
                torrent_client.start_magnets(links, final_directory)
            return True, "Launched downloads"

        else:
            logging.info("Could not scrap any links :'(")
            return False, "No link could be found for {} on {} mode in {}p resolution".format(url, mode, res)

    else:
        if not valid_mode:
            error_msg = "Mode not supported. Supported modes: {}.".format(['magnet', 'torrent'])
        elif not valid_res:
            error_msg = "Resolution not supported. Supported res: {}p.".format(supported_res)
        else:
            error_msg = "{} does not exist or do not have the write permission.".format(output_directory)

        logging.error(error_msg)
        return False, error_msg


def __create_output_directory__(directory: str, show_name: str) -> str:
    time_str = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    final_directory = os.path.join(directory, time_str + '_' + show_name)
    os.mkdir(final_directory)
    logging.info("Created output directory %s for torrents.", final_directory)
    return final_directory


def __download_links__(urls: List[str], output_directory: str) -> None:
    for url in urls:
        remote_file = urlopen(url)
        metadata = remote_file.info()['Content-Disposition']
        value, params = cgi.parse_header(metadata)
        filename = unquote(params["filename"])
        urlretrieve(url, os.path.join(output_directory, filename))
        logging.info('Downloaded %s', filename)


def __open_torrent_files__(torrent_directory: str) -> None:
    files = [os.path.join(torrent_directory, f) for f in listdir(torrent_directory)
             if isfile(join(torrent_directory, f))]

    files.sort()
    torrent_client.start_torrents(files, torrent_directory)
    # while len(torrent_client.get_active_downloads()) != 0:
    #     logging.info("Still downloading torrents.")
    #     logging.info(torrent_client.get_torrent_status())
    #     logging.info(torrent_client.get_global_transfer_info())
